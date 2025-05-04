"""
Orignal Author: DevTechBytes
https://www.youtube.com/@DevTechBytes
"""

class Config:
    PAGE_TITLE = "Streamlit Ollama Chatbot"

    OLLAMA_MODELS = ('qwen3:4b', 'qwen3:0.6b', 'qwen3:1.7b', 'qwen3:8b')

    SYSTEM_PROMPT = f"""You are a helpful chatbot that has access to the following 
                    open-source models {OLLAMA_MODELS}.
                    You can can answer questions for users on any topic."""
    