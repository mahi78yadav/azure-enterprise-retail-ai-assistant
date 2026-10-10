
import streamlit as st
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Microsoft Foundry configuration
ENDPOINT = "https://gmahi-78-3687-resource.services.ai.azure.com/api/projects/gmahi-78-3687"
AGENT_NAME = "retail-ai-assistant-mahi2026"

st.set_page_config(
    page_title="Enterprise Retail AI Assistant",
    page_icon="🛍️",
    layout="centered",
)

st.title("🛍️ Enterprise Retail AI Assistant")
st.caption("Ask questions about retail products, returns, warranties, and customer support.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Ask your retail question...")

if user_message:
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Searching the retail knowledge base..."):
                credential = DefaultAzureCredential()
                project_client = AIProjectClient(
                    endpoint=ENDPOINT,
                    credential=credential,
                    allow_preview=True,
                )

                openai_client = project_client.get_openai_client(
                    agent_name=AGENT_NAME
                )
                conversation = openai_client.conversations.create()

                response = openai_client.responses.create(
                    conversation=conversation.id,
                    input=[{"role": "user", "content": user_message}],
                )

                answer = response.output_text or (
                    "I could not generate an answer. Please try again."
                )
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

        except Exception as error:
            st.error(
                "Unable to contact Microsoft Foundry. "
                "Please check your Azure login, permissions, and configuration."
            )
            st.caption(f"Technical details: {error}")
