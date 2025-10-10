#General Budgeting Overview Functions
def get_monthly_budget_summary(user_id: int, month: str) -> dict:
    """
    Return remaining money to spend per category for the given month.
    Returns: {'groceries': float, 'entertainment': float, ...}
    """

def get_monthly_income_vs_spending(user_id: int, month: str) -> dict:
    """
    Compare monthly income to total spending.
    Returns: {'income': float, 'total_spent': float, 'difference': float}
    """

def get_essential_vs_nonessential_percentage(user_id: int, month: str) -> dict:
    """
    Calculate what percentage of income goes to essential vs non-essential expenses.
    Returns: {'essential_pct': float, 'nonessential_pct': float}
    """

#Spending and Expense Tracking
def get_total_spent_comparison(user_id: int, month: str, comparison_month: str) -> dict:
    """
    Compare total spending for two months.
    Returns: {'current_month': float, 'comparison_month': float, 'difference': float}
    """

def get_top_spending_categories(user_id: int, month: str, top_n: int = 5) -> dict:
    """
    Identify categories consuming most of the budget.
    Returns: {'category1': float, 'category2': float, ...}
    """

def get_recurring_subscriptions(user_id: int) -> list:
    """
    Return all recurring charges (subscriptions) for the user.
    Returns: [{'name': str, 'amount': float, 'frequency': str}, ...]
    """

def check_budget_exceedances(user_id: int, month: str) -> dict:
    """
    Check if any category exceeds allocated budget.
    Returns: {'category': float_over_budget, ...}
    """
#Savings and Goals
def get_savings_progress(user_id: int) -> dict:
    """
    Return current saved amount for all goals.
    Returns: {'goal_name': {'target': float, 'saved': float, 'progress_pct': float}, ...}
    """

def calculate_required_monthly_savings(user_id: int, goal_name: str) -> float:
    """
    Suggest how much to save each month to meet a goal by its target date.
    Returns: float
    """

def suggest_savings_allocation(user_id: int, short_term_pct: float, long_term_pct: float) -> dict:
    """
    Suggest allocation between short-term and long-term savings.
    Returns: {'short_term': float, 'long_term': float}
    """
#Deptt Management
def get_debt_summary(user_id: int) -> dict:
    """
    Return balances, interest rates, and monthly payments for all debts.
    Returns: {'debt_name': {'balance': float, 'interest_rate': float, 'monthly_payment': float}, ...}
    """

def get_debt_repayment_schedule(user_id: int) -> dict:
    """
    Return repayment schedule and interest for all debts.
    Returns: {'debt_name': [{'month': int, 'payment': float, 'interest': float, 'principal': float}, ...]}
    """

def suggest_optimal_repayment_strategy(user_id: int) -> dict:
    """
    Suggest best repayment strategy (e.g., snowball or avalanche).
    Returns: {'strategy': str, 'estimated_savings': float}
    """

def calculate_interest_savings_highest_interest_first(user_id: int) -> float:
    """
    Estimate money saved by paying high-interest debt first.
    Returns: float
    """

#Trends and Insights (Analysis)
def get_spending_trends(user_id: int, months: list) -> dict:
    """
    Return spending trends over specified months.
    Returns: {'month1': total_spent, 'month2': total_spent, ...}
    """

def identify_spending_patterns(user_id: int, months: list) -> dict:
    """
    Highlight recurring patterns or areas to improve.
    Returns: {'pattern_name': description, ...}
    """

def get_discretionary_spending_progress(user_id: int, months: list) -> dict:
    """
    Track reduction in discretionary spending over time.
    Returns: {'month1': float, 'month2': float, ...}
    """
def suggest_budget_adjustments(user_id: int, month: str) -> dict:
    """
    Suggest budget adjustments based on past spending and income.
    Returns: {'category': suggested_amount, ...}
    """

#Cash Flow and Future Projections
def project_future_budget(user_id: int, months_ahead: int) -> dict:
    """
    Estimate budget for next N months based on current income and expenses.
    Returns: {'month1': {'income': float, 'expenses': float, 'balance': float}, ...}
    """

def get_projected_cash_flow(user_id: int, period: str) -> dict:
    """
    Return expected cash inflow and outflow for next month/quarter.
    Returns: {'inflow': float, 'outflow': float, 'net': float}
    """

def identify_upcoming_large_expenses(user_id: int, months_ahead: int) -> list:
    """
    Detect any planned or recurring large expenses.
    Returns: [{'name': str, 'amount': float, 'due_date': str}, ...]
    """

def simulate_budget_adjustment(user_id: int, category: str, reduction_pct: float) -> dict:
    """
    Estimate impact of reducing spending in a category by a percentage.
    Returns: {'new_expense': float, 'new_balance': float}
    """
#Tax and Financial Planning
def estimate_tax_setaside(user_id: int, year: int) -> float:
    """
    Estimate how much money to set aside for taxes this year.
    Returns: float
    """

def simulate_income_change(user_id: int, new_income: float) -> dict:
    """
    Simulate impact of a raise or bonus on budget and savings.
    Returns: {'new_budget': dict, 'new_savings_suggestions': dict}
    """

def check_retirement_goal_progress(user_id: int) -> dict:
    """
    Track progress toward retirement savings goals.
    Returns: {'401k': float, 'IRA': float, 'target': float, 'progress_pct': float}
    """

def suggest_savings_reallocation(user_id: int, short_term_pct: float, long_term_pct: float) -> dict:
    """
    Recommend reallocating between short-term and long-term investments.
    Returns: {'short_term': float, 'long_term': float}
    """
#Alerts (Optional)
def set_budget_alert(user_id: int, category: str, threshold: float) -> None:
    """
    Create alert when user is about to exceed a budget in a category.
    """

def generate_weekly_financial_summary(user_id: int) -> str:
    """
    Return a weekly summary of spending, income, and savings.
    """

def generate_monthly_financial_summary(user_id: int) -> str:
    """
    Return a monthly summary of spending, income, and savings.
    """
#Budget Adjustments
def suggest_budget_cuts(user_id: int) -> dict:
    """
    Recommend areas to cut back to save money.
    Returns: {'category': suggested_reduction_amount, ...}
    """

def adjust_budget_for_income_drop(user_id: int, new_income: float) -> dict:
    """
    Suggest how to adjust expenses to stay on track if income temporarily drops.
    Returns: {'category': new_budget_amount, ...}
    """

def create_custom_budget(user_id: int, project_name: str, total_amount: float, categories: dict) -> dict:
    """
    Create a custom budget for a project or event.
    categories: {'category_name': allocated_amount, ...}
    Returns: {'project_name': str, 'categories': dict}
    """
