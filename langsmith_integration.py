# langsmith_integration.py
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.tracers import LangChainTracer
from langsmith import Client

class LangSmithLLM:
    def __init__(self, openai_api_key: str, langsmith_api_key: str):
        self.openai_api_key = openai_api_key
        self.langsmith_api_key = langsmith_api_key
        self.client = Client(api_key=langsmith_api_key)
        self.tracer = LangChainTracer(project_name="Mi Proyecto", client=self.client)
        self.chat_model = ChatOpenAI(openai_api_key=openai_api_key)

    def generate_response(self, prompt: str) -> str:
        response = self.chat_model.predict(prompt, callbacks=[self.tracer])
        return response

    def handle_faq(self, question: str) -> str:
        faq_responses = {
            "What are your business hours?": "Our business hours are from 9 AM to 5 PM, Monday to Friday.",
            "How can I track my order?": "You can track your order using the tracking number provided in your confirmation email.",
            "What is your return policy?": "Our return policy allows returns within 30 days of purchase. Please visit our return policy page for more details.",
            # Add more FAQs as needed
        }
        return faq_responses.get(question, "I'm sorry, I don't have an answer to that question.")

    def generate_product_info(self, product_name: str) -> str:
        product_info = {
            "Product A": "Product A is a high-quality item with excellent features...",
            "Product B": "Product B is known for its durability and performance...",
            # Add more product info as needed
        }
        return product_info.get(product_name, "I'm sorry, I don't have information about that product.")
