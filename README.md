# LLM-Integration
Part of a Budgeting app where the LLM  assists the user with different needs of budgeting and information.  

## 1. SQL AI Agent Access using Python, LangChain, and Ollama: 
Video: "Mastering AI-Powered SQL Querying: Build a Smart MySQL Agent with Python, LangChain, and Ollama".
Source: https://www.youtube.com/watch?v=g9MrxC64yF8
Goal: Install Ollama and a local LLM, then use it with LangChain.
[0:00]: Introductions and overview of the project.
[1:30]: Installation and Setup. Install Ollama and use it to pull the necessary local models. This is a critical first step.
[4:15]: LangChain and Database Connection. Learn how to use LangChain's SQL Database Toolkit to connect to a database.
[6:00]: Running Queries. The video walks through how the LLM generates SQL queries and executes them against the database.
[10:00]: Bringing it all together. The video demonstrates the full agent in action.  

## 1. AI Graphing using:
Video: "Build a Plotly AI Agent for Creating Visualizations".
Source: YouTube.
Goal: Learn how to use an LLM to generate Plotly code.
[2:30]: Initial Setup. The video demonstrates the basic Python setup for generating visualizations.
[4:15]: The plotly.express function. The presenter explains how the LLM calls plotly.express functions to create charts.
[7:00]: Graph Generation. The video shows the agent taking a user prompt and returning the appropriate Plotly figure. 

## 3.Combining the agent and Plotly functionality
This requires manually combining the code from the two types of tutorials.
Retrieve database data: Run the database-focused agent code from Part 1 to get the data you want to visualize.
Generate Plotly code: Use the agent to generate Python code for the Plotly graph. Instead of generating the SQL query, the prompt will instruct the agent to generate the Plotly code from the retrieved data.
Execute the code: The agent uses its code execution tool to run the generated Plotly code and produce the graph. 

Installations
ollama: For running the local LLM.
langchain: The agent framework.
langchain-experimental: For the Python REPL tool.
langchain-community: For connecting to the database.
plotly: The plotting library.
pandas: For data manipulation.
sqlalchemy: The database toolkit dependency. 

Set up Ollama: Download and install Ollama, then pull your desired LLM (e.g., ollama pull llama3).
Install Python libraries: Use pip to install all the required packages.
Define the tools: Create the SQLDatabaseToolkit and the PythonREPLTool for your agent.
Create the agent: Use create_react_agent to build the agent and equip it with the necessary tools.
Craft the prompts: Write a prompt that guides the agent through the process:
Phase 1: Generate and execute a SQL query to retrieve data.
Phase 2: Use the retrieved data to generate and execute Python code for the Plotly visualization.
Execute the workflow: Run the agent with your natural language request, and it will perform both steps to deliver your graph.
