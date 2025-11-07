from agents.llm_agent import LLMAgent
from core.database import SessionLocal
from sqlalchemy import text

def test_complete_pipeline():
    print("Testing Complete Agent Pipeline...")
    
    # Test 1: Database connection
    print("\n1. Testing database connection...")
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT COUNT(*) FROM categories"))
        count = result.fetchone()[0]
        print(f"Database connected, found {count} categories")
        db.close()
    except Exception as e:
        print(f"Database test failed: {e}")
        return
    
    # Test 2: LLM Agent initialization
    print("\n2. Testing LLM Agent...")
    try:
        agent = LLMAgent()
        print("LLM Agent initialized")
    except Exception as e:
        print(f"LLM Agent failed: {e}")
        return
    
    # Test 3: Sample queries
    print("\n3. Testing sample queries...")
    test_queries = [
        "Show me all categories",
        "What are my recent transactions?",
        "Show my spending by category"
    ]
    
    for query in test_queries:
        print(f"   Testing: '{query}'")
        try:
            result = agent.process_message(query, user_id=1)
            print(f"Response length: {len(result['response'])} chars")
            print(f"Preview: {result['response'][:100]}...")
            if result.get('visualization_data'):
                print("Visualization data generated")
            else:
                print("No visualization data (normal for some queries)")
        except Exception as e:
            print(f"Query failed: {e}")
            import traceback
            traceback.print_exc()
    
    print("\nAll tests completed!")

if __name__ == "__main__":
    test_complete_pipeline()