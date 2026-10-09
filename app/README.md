# Retail AI Assistant — Python Application

This folder contains the Python client for the Enterprise Retail AI Assistant built with Microsoft Foundry.

## Features

- Connects to the existing Microsoft Foundry project.
- Invokes the `retail-ai-assistant-mahi2026` agent.
- Uses Microsoft Entra ID authentication through `DefaultAzureCredential`.
- Supports grounded retail product and policy questions through the connected knowledge base.

## Prerequisites

- Python 3.10 or later
- Azure CLI authentication or another supported Microsoft Entra ID credential
- Access to the configured Microsoft Foundry project and agent

## Install dependencies

From this folder, run:

```bash
python -m pip install -r requirements.txt
```

## Authenticate

Sign in to Azure CLI in your local development environment:

```bash
az login
```

Ensure your signed-in identity has the required permissions to access the Foundry project.

## Run

```bash
python run_agent.py
```

The script connects to the configured Foundry agent and prints its response.

## Security

Do not commit credentials, API keys, tokens, or secrets to source control.
