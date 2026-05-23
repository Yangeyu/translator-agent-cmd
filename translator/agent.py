"""AI agent functionality for Y-Translator CLI"""

from agno.agent import Agent
from agno.models.dashscope import DashScope
from .config import Config

class TranslatorAgent:
    """Translator AI Agent wrapper"""
    
    def __init__(self, config: Config):
        """Initialize the agent with configuration"""
        self.config = config
        self.model = DashScope(
            id=config.model,
            api_key=config.api_key,
            base_url=config.api_base,
        )
        
        self.agent = Agent(
            instructions=[
                "You are only a translator",
                "You only translate user input to English, when user input is Chinese",
                "You only translate user input to Chinese, when user input is English",
                "You don't answer any questions",
                "Please translate following user input"
            ],
            model=self.model,
            stream=True,
            debug_mode=config.debug,
        )
    
    def process_query(self, query: str, stream: bool = True) -> None:
        """Process a single query and print the response"""
        if not query.strip():
            return
            
        self.agent.print_response(query, stream=stream)
    
    def translate(self, query: str) -> str:
        """Translate text and return the result as a string"""
        response = self.agent.run(query, stream=False)
        return response.content
