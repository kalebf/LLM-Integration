# query_runner.py
import sys
from httpcore import ConnectionPool
import psycopg2
from psycopg2 import connect, pool
from langchain_ollama import OllamaLLM
from langchain.agents import tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file
print("Loading SQL Agent")

# Database connection parameters from environment variables
db_params = {
    "database": "postgres",
    "user": "postgres",
    "password": "kalebf6201",
    "host": "127.0.0.1",
    "port": "5432"
}

# Initialize connection pool
mydb = psycopg2.connect(**db_params)
#Test connection
"""print(mydb)
mydb.close()
"""



# Get table info
def get_table_info(connect):
  cur = connect.cursor()
  cur.execute("""
    SELECT table_name, column_name
    FROM information_schema.columns
    WHERE table_schema = %s
""", ( "public", ))

  # Organize columns by table
  table = {}
  for table_name, column_name in cur.fetchall():
      if table_name not in table:
        table[table_name] = []
      table[table_name].append(column_name)
    # Format table info
  table_info = "\n".join([f"{table_name}: {', '.join(columns)}" for table_name, columns in table.items()])
  #close connection
  cur.close()
  return table_info


# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3")

# Custom prompt template
def create_prompt(table_info: str, user_query: str, previous_error:str) -> str:
  return f"""
    You are an expert SQL Query Generator.
    Database Schema: {table_info}
    Important Rules: 
    1. Always verify column names before using them
    2. Use the most appropriate tables for the query

    Generate a SQL query for the following question: 
    {user_query}
    Only return the SQL query, nothing else.
    """
# Function to generate and execute SQL query
def write_sql_query(user_query: str,mydb = mydb, max_retries = 3) -> str:
    table_info = get_table_info(mydb)
    previous_errors = ''
    retries = 0
    while retries < max_retries:
      try: 
        # Create the prompt with table info and user query
        prompt = create_prompt(table_info, user_query, previous_errors)
        # Generate SQL query using the LLM
        sql_query = llm.invoke(prompt).strip()
        print (f"Generated SQL Query: {sql_query}")

        #Execute the query to verify it works
        with mydb.cursor() as cursor:
          cursor.execute(sql_query)
          results = cursor.fetchall()
          for row in results:
            print(row)
          return results
      # Catch SQL errors and retry  
      except Exception as e:
        previous_errors = f"\nThe previous query had an error: {str(e)}. Please correct it."
        retries += 1
        print(f"Retrying... ({retries}/{max_retries})")
        
      # If all retries are exhausted, return an error message
      except Exception as e:
        print(f"Failed to generate a valid SQL query after {max_retries} attempts.")
        return "Error: Unable to generate a valid SQL query."

def main():
  if len(sys.argv) <2:
    print("Please provide a question. Usage query_runner.py <question here>'")
    sys.exit(1)
  #Get question from command line
  question = sys.argv[1]
  print(f"User question: {question}")
  write_sql_query({"question":question}, mydb=mydb)

if __name__ == "__main__":
  test_question = input(str("Enter your question or type exit to exit: "))
  while test_question != "exit":  
    print(f"Testing with prompt: {test_question}\n")
    results = write_sql_query(test_question, mydb=mydb)

    print("\nFinal Results:")
    if isinstance(results, list):
        if not results:
            print("Query executed but returned no results.")
        else:
            for row in results:
                print(row)
    else:
        print(results)
    test_question = input(str("Enter your question or type exit to exit: "))
  else :
    print("Exiting program.")
