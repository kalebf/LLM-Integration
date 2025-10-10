# llm_agent.py

def parse_user_message(user_input: str) -> dict:
    """
    Use the LLM to interpret the user's message.
    Returns a dictionary with:
      {
        'intent': str,           # e.g., 'get_budget_summary', 'simulate_debt_scenario'
        'parameters': dict       # e.g., {'month': '2025-10', 'category': 'groceries'}
      }
    """
    ...

def request_clarification(parsed_intent: dict) -> str:
    """
    If parameters are missing or unclear, generate a follow-up question for the user.
    Returns a string question.
    """
    ...

def route_request(parsed_intent: dict) -> dict:
    """
    Route the request to the query_runner or visualizer based on intent type.
    Returns the agent's response.
    """
    ...

def generate_chatbot_response(agent_output: dict) -> str:
    """
    Convert the agent output into human-readable text for the chatbot.
    Returns a string summary or answer.
    """
    ...
