# query_runner.py

def execute_budget_query(user_id: int, intent: str, parameters: dict, db_connection) -> dict:
    """
    Main entry point for executing a user's query.
    Steps:
      1. Map intent to the correct budgeting function.
      2. Retrieve necessary data from the database.
      3. Call the budgeting function with the parameters.
    Returns a dictionary with:
      {
        'data': dict,         # structured results for visualization or summary
        'summary': str        # human-readable summary for chatbot
      }
    """
    ...

def retrieve_user_data(user_id: int, categories: list = None, months: list = None, db_connection=None) -> dict:
    """
    Retrieve user financial data from PostgreSQL.
    Returns structured dictionary for the budgeting functions.
    """

def map_intent_to_function(intent: str) -> callable:
    """
    Map the LLM intent to the corresponding budgeting function.
    Example mapping:
      'get_budget_summary' -> get_monthly_budget_summary
      'simulate_debt_scenario' -> simulate_debt_scenarios
    Returns a function reference.
    """

def prepare_parameters(intent: str, extracted_params: dict, user_data: dict) -> dict:
    """
    Ensure the parameters from the LLM match the required budgeting function inputs.
    """
