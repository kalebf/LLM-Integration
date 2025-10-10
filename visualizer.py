# visualizer_agent.py

def create_visualization(data: dict, intent: str, plot_type: str = None) -> dict:
    """
    Create a visualization based on the intent and data.
    Returns:
      {
        'plot_object': object,    # Plotly figure or Dash component
        'summary': str            # Human-readable description of the visualization
      }
    """

def determine_plot_type(intent: str) -> str:
    """
    Decide the most appropriate plot type based on the user’s intent.
    Examples:
      'get_spending_trends' -> 'line'
      'get_top_spending_categories' -> 'bar'
      'get_essential_vs_nonessential_percentage' -> 'pie'
    """

def format_plot_for_chatbot(plot_object) -> str:
    """
    Generate a human-readable summary of the visualization for the chatbot.
    Example:
      "Here’s your spending trend over the last 6 months."
    """
