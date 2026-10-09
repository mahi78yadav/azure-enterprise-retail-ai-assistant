
import json

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from product_tool import get_product_details

endpoint = "https://gmahi-78-3687-resource.services.ai.azure.com/api/projects/gmahi-78-3687"

tools = [
    {
        "type": "function",
        "name": "get_product_details",
        "description": "Find retail products under a maximum price for a given purpose.",
        "parameters": {
            "type": "object",
            "properties": {
                "max_price": {
                    "type": "integer",
                    "description": "Maximum price in INR"
                },
                "purpose": {
                    "type": "string",
                    "description": "Intended use, such as student or business"
                }
            },
            "required": ["max_price", "purpose"],
            "additionalProperties": False
        },
        "strict": True
    }
]


def run_product_tool(arguments):
    args = json.loads(arguments) if isinstance(arguments, str) else arguments
    products = get_product_details(
        max_price=args["max_price"],
        purpose=args["purpose"]
    )
    return json.dumps(products, ensure_ascii=False)


with (
    DefaultAzureCredential() as credential,
    AIProjectClient(
        endpoint=endpoint,
        credential=credential,
        allow_preview=True
    ) as project_client
):
    # Use the project OpenAI client directly, not the existing agent endpoint.
    openai_client = project_client.get_openai_client()

    question = input("Ask your retail assistant: ")

    response = openai_client.responses.create(
        model="gpt-4.1-mini",
        input=question,
        tools=tools,
        tool_choice="required"
    )

    while True:
        function_calls = [
            item for item in response.output
            if item.type == "function_call"
        ]

        if not function_calls:
            break
            
        print("Function calls detected:", len(function_calls))

        tool_outputs = []

        for call in function_calls:
            if call.name == "get_product_details":
                result = run_product_tool(call.arguments)
                print("Product tool result:", result)
            else:
                result = json.dumps({"error": "Unknown tool"})

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": call.call_id,
                "output": result
            })

        response = openai_client.responses.create(
            model="gpt-4.1-mini",
            previous_response_id=response.id,
            input=tool_outputs,
            tools=tools,
            tool_choice="auto"
        )

    print("\nAssistant response:")
    print(response.output_text)

