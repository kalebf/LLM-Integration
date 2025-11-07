import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Now import from your package
    from agents.llm_agent import LLMAgent
    
    def test_agent():
        print("Initializing LLM Agent...")
        try:
            agent = LLMAgent()
            print("LLM Agent initialized successfully!")
            
            # Test with a simple query
            test_query = "Show me all categories"
            print(f"\nTesting: '{test_query}'")
            
            result = agent.process_message(test_query, user_id=1)
            print(f"Response: {result['response']}")
            if result['visualization_data']:
                print("Visualization data available")
            else:
                print("No visualization data")
                
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
    
    if __name__ == "__main__":
        test_agent()

except ImportError as e:
    print(f"Import error: {e}")
    print("\nCurrent directory:", os.getcwd())
    print("Contents:", [f for f in os.listdir('.') if os.path.isdir(f) or f.endswith('.py')])