Project Structure: 
clarifi_agent/
├── __init__.py
├── agents/
│   ├── __init__.py
│   ├── chat_interface.py          # simple interface to take user's messages call IntentClassifier and Returns responses 
│   ├── query_runner.py       # SQL query execution
│   └── data_handler.py         # create and delete transacction entries
│   └── intent_clasifier.py         # tells the LLM what class to use
│   └── prompmt_enhancer.py         # improves user prompt for llm understanding
├── api/
│   ├── __init__.py
│   └── endpoints.py          # FastAPI endpoints
├── core/
│   ├── __init__.py
│   ├── config.py            # Configuration settings
│   └── database.py          # SQLAlchemy database connection
├── models/
│   ├── __init__.py
│   └── schemas.py           # Pydantic models
├── main.py                  # FastAPI app entry point
└── final_test.py           # Comprehensive test suite

Database Configuration (core/config.py):
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://user:pass@host:port/db"
    LLM_MODEL: str = "llama3"


LLM Integration Documentation
Overview
This document provides comprehensive documentation for the LLM integration system designed for a financial application. The system processes natural language queries to perform database operations with strong safety measures and user-specific access controls.

1. intent_classifier.py
Class: IntentClassifier
Primary controller that classifies user intents and routes queries to appropriate handlers.

Constructor: __init__(self)
Initializes the LLM model (OllamaLLM)

Creates instances of QueryRunner and DataHandler

Defines enhanced keyword lists for intent classification

Sets up regex patterns for spending/income detection

Method: classify_intent(user_query: str, user_id: int) -> Dict[str, Any]
Purpose: Main entry point for intent classification and routing
Workflow:

Checks for strong spending/income patterns → direct CREATE routing

Uses LLM for primary intent classification

Uses keyword matching as fallback/verification

Resolves conflicts between LLM and keyword results

Routes to appropriate handler

Returns structured classification result

Method: _is_spending_or_income_query(user_query: str) -> bool
Purpose: Detects if a query indicates financial transactions (spending/income)
Detection Methods:

Regex patterns for spending (spent $X, paid $Y, etc.)

Regex patterns for income (earned $X, received $Y, etc.)

Dollar amount detection with context

Statement vs question analysis

Method: _llm_classify_intent(user_query: str) -> Dict[str, Any]
Purpose: Uses LLM to classify intent with structured JSON output
Output Format: {"intent": "VIEW|CREATE|UPDATE|DELETE", "confidence": float, "reason": str}
Error Handling: Returns default VIEW intent with low confidence on failure

Method: _keyword_classify_intent(user_query: str) -> str
Purpose: Keyword-based intent classification as fallback mechanism
Hierarchy:

Spending/income patterns → CREATE

Delete keywords → DELETE

Update keywords → UPDATE (with "set up" exception)

Insert keywords → CREATE (with "add up" exception)

View keywords → VIEW

Dollar amounts → CREATE (unless question about amounts)

Method: _resolve_intent_conflict(llm_result, keyword_intent) -> str
Purpose: Resolves conflicts between LLM and keyword classifications
Rules:

LLM confidence < 0.4 → trust keywords

LLM confidence ≥ 0.8 → trust LLM

Medium confidence: special handling for spending queries with dollar amounts

Method: _route_to_handler(user_query, user_id, intent) -> Dict[str, Any]
Purpose: Routes query to appropriate handler based on intent
Routing Logic:

CREATE → data_handler.process_natural_language_create()

UPDATE → data_handler.process_natural_language_update()

DELETE → _handle_delete_intent()

VIEW → query_runner.process_natural_language_query()

Method: _prepare_create_query(user_query: str) -> str
Purpose: Prepares CREATE queries with appropriate action verbs
Enhancements:

Adds "log" prefix for spending queries

Adds "record" prefix for income queries

Adds "add" prefix for other CREATE queries

Method: _handle_delete_intent(user_query, user_id) -> Dict[str, Any]
Purpose: Handles DELETE intent with confirmation flow
Features: Routes to data_handler's delete processor with confirmation requirements

Method: classify_and_respond(user_query, user_id) -> str
Purpose: Simplified method for direct response generation
Returns: Human-readable response string based on classification result

Function: get_intent_classifier() -> IntentClassifier
Purpose: Singleton factory function for IntentClassifier

2. query_runner.py
Class: QueryRunner
Handles natural language to SQL conversion and query execution with LLM-optimized views.

Constructor: __init__(self)
Initializes LLM model

Creates PromptEnhancer instance

Initializes conversation context storage

Method: execute_query(query: str) -> Dict[str, Any]
Purpose: Executes SQL queries with proper transaction management
Features:

Automatic commit for non-SELECT queries

Automatic rollback on error

Returns structured results with column names and data

Handles both SELECT and DML operations

Method: _get_schema_info() -> str
Purpose: Generates LLM-friendly database schema information
Focus: LLM-optimized views only (tables prefixed with llm_)
Includes:

View names and columns

Specific usage instructions

Critical financial view documentation

Response rules and filtering examples

Method: process_natural_language_query(user_query: str, user_id: int) -> Tuple[str, str]
Purpose: Main entry point for VIEW intent processing
Two-stage Approach:

SQL Generation: Converts natural language to SQL using LLM

Answer Extraction: Extracts and formats answer from query results
Includes: User access validation for business subusers

Method: _check_user_llm_access(user_id: int) -> Dict[str, Any]
Purpose: Validates user permissions for LLM access
Rules:

Business subusers (role_id=2) → No LLM access

All other roles → Access granted
Returns: Structured access check result

Method: _generate_sql_query(enhanced_query, schema_info, user_id) -> str
Purpose: Generates SQL queries with strict safety rules
Key Rules:

Uses LLM-optimized views only

Automatically filters by user_id

Specific view selection based on query type

Critical financial query patterns predefined

Method: _extract_and_format_answer(original_query, enhanced_query, raw_data, sql_query) -> str
Purpose: Extracts human-readable answers from query results
Features:

Uses LLM to interpret data in context

Removes template artifacts

Follows strict rules against data fabrication

Falls back to direct formatting if LLM fails

Method: _clean_template_artifacts(response: str) -> str
Purpose: Removes LLM template remnants from responses
Patterns Removed: $[amount], [name], INSERT_AMOUNT, etc.

Method: _create_direct_response(raw_data, original_query) -> str
Purpose: Creates direct responses without LLM when possible
Logic:

Extracts money amounts directly

Handles name/list responses

Provides simple context-based formatting

Method: _clean_sql_response(sql_response: str) -> str
Purpose: Extracts clean SQL from LLM responses
Handles:

Markdown code blocks

Explanatory text

Multiple SQL statements

Method: execute_query_with_params(query: str, params: Dict) -> Dict[str, Any]
Purpose: Executes parameterized queries to prevent SQL injection
Features: Proper transaction management with parameters

3. data_handler.py
Class: DataHandler
Handles CREATE, UPDATE, and DELETE operations with safety measures.

Constant: ALLOWED_USER_MOD_TABLES
Defines tables users can modify via natural language

Currently only: ['transactions']

Constructor: __init__(self)
Initializes LLM model

Creates QueryRunner instance

Initializes pending deletes storage

Method: process_natural_language_create(enhanced_query, original_user_query, user_id) -> Dict[str, Any]
Purpose: Processes CREATE intent for transaction/budget/goal creation
Key Features:

Converts natural language to INSERT statements

Enforces schema rules (no id/created_at columns)

Validates table permissions

Executes SQL and returns results

Expense amounts are negative, income are positive

Method: process_natural_language_update(enhanced_query, original_user_query, user_id) -> Dict[str, Any]
Purpose: Processes UPDATE intent (reserved for future expansion)
Current Implementation: Basic SQL generation with user_id safety check

Method: process_natural_language_delete(enhanced_query, original_user_query, user_id, session_id='') -> Dict[str, Any]
Purpose: Processes DELETE intent with confirmation flow
Safety Features:

Only allows transactions table deletions

Requires user_id constraint

Generates preview of what will be deleted

Creates pending delete with confirmation ID

Returns confirmation request instead of immediate execution

Method: confirm_delete(user_id, confirmation_id, confirm=True, session_id='') -> Dict[str, Any]
Purpose: Executes or cancels pending delete operations
Workflow:

Validates confirmation ID exists

If confirm=False → cancels pending delete

If confirm=True → executes delete SQL

Returns execution results

Cleans up pending delete record

Method: _preview_delete(sql_query, user_id) -> Dict[str, Any]
Purpose: Shows what will be deleted before execution
Implementation: Converts DELETE to SELECT, counts records, shows samples

Method: _cleanup_old_pending_deletes(max_age_minutes=10)
Purpose: Cleans up expired pending deletes
Default: Deletes older than 10 minutes

Method: list_pending_deletes(user_id) -> Dict[str, Any]
Purpose: Lists all pending delete operations for a user
Returns: Structured list with confirmation IDs and preview info

Method: cancel_all_pending_deletes(user_id) -> Dict[str, Any]
Purpose: Cancels all pending deletes for a user
Use Case: Session cleanup or user request

Method: log_interaction(user_id, original_prompt, response)
Purpose: Logs LLM interactions to database
Table: llmlogs (auto-incrementing id, user_id, prompt, response)

4. prompt_enhancer.py
Class: PromptEnhancer
Enhances natural language queries for better SQL generation.

Constructor: __init__(self)
Initializes LLM model

Method: enhance_query(user_query: str, schema_info: str) -> str
Purpose: Improves query specificity for SQL generation
Enhancements:

Maps vague terms to exact database category names

Adds category_kind filters when relevant

References appropriate LLM-optimized views

Makes queries more precise for accurate data retrieval

5. chat_interface.py
Class: ChatInterface
Main chatbot interface that orchestrates the entire LLM integration system.

Constructor: __init__(self)
Creates IntentClassifier instance

Initializes optional conversation history storage

Method: process_message(user_id: int, message: str, session_id=None) -> Dict[str, Any]
Purpose: Main chatbot entry point
Workflow:

Classifies intent using IntentClassifier

Routes to appropriate handler

Extracts response text

(Optional) Updates conversation history

Returns structured response with metadata

Method: _update_history(user_id, session_id, user_message, bot_response)
Purpose: Maintains conversation history (optional feature)
Storage: In-memory dictionary with message limit (20 messages)
Format: List of message objects with role, content, and timestamp

Database Schema Notes
LLM-Optimized Views
The system uses specially created views for LLM queries:

llm_user_profile: User personal/business info

llm_business_hierarchy: User relationships

llm_transaction_summary: Most important for spending questions

llm_financial_overview: Financial summaries

llm_budget_overview: Budget planning data

Critical Column Notes
amount: Negative for expenses, positive for income

absolute_amount: Always positive

created_at: Actual transaction date

month: Summary month in overview views

Security & Safety Features
User Isolation: All queries automatically filter by user_id

Table Restrictions: Users can only modify allowed tables

DELETE Confirmation: Two-step process with preview

SQL Injection Protection: Parameterized queries

Access Control: Business subusers denied LLM access

Transaction Safety: Automatic commit/rollback

Integration Points for Backend Team
Primary Entry Points
ChatInterface.process_message() - Main chatbot interface

IntentClassifier.classify_intent() - Direct intent classification

QueryRunner.process_natural_language_query() - View operations only

Required Initialization
python
from agents.chat_interface import ChatInterface

chat_bot = ChatInterface()
response = chat_bot.process_message(user_id=123, message="How much did I spend this month?")
Environment Requirements
settings.LLM_MODEL configured in core.config

Database connection pool via core.database.get_db()

LLM model accessible via langchain_ollama.OllamaLLM

Error Handling
All methods return structured dictionaries with:

status: COMPLETE, ERROR, CONFIRM_REQUIRED, etc.

message: Human-readable status

sql: Generated SQL (for debugging)

Additional context-specific fields

Current Focus & Future Expansion
Currently Implemented
Transaction creation (spending/income)

Transaction deletion (with confirmation)

Information viewing (expenses, income, budgets, user info)

User access control

Safety measures for destructive operations

Reserved for Future Expansion
UPDATE operations (stubbed for implementation)

Additional table modifications

Enhanced conversation context

More complex query patterns

Advanced budget/goal management



