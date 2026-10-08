# azure-enterprise-retail-ai-assistant
Enterprise Retail AI Assistant using Azure AI, RAG, Azure AI Search, Microsoft Foundry, and AI Agents

# Enterprise Retail AI Assistant

An enterprise-style AI assistant built on Microsoft Azure using Generative AI, Retrieval-Augmented Generation (RAG), Azure AI Search, Microsoft Foundry, and AI Agents.

## Business Scenario

The Retail AI Assistant helps users find and understand information from enterprise retail documents and data.

Example questions:

- What is the return policy for laptops?
- Which products are suitable for a student under ₹50,000?
- What are the warranty terms for a product?
- Find relevant products and explain why they are suitable.

## Architecture

```text
Retail Documents / Data
          |
          v
   Azure Data Lake
          |
          v
  Document Processing
          |
          v
     Azure AI Search
   Keyword + Vector Search
          |
          v
   Retrieval-Augmented
      Generation (RAG)
          |
          v
    Microsoft Foundry
        LLM
          |
          v
      AI Agent
          |
          v
   Retail AI Assistant
