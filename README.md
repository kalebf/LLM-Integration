# LLM-Integration
Part of a Budgeting app where the LLM  assists the user with different needs of budgeting and information.  

## Before starting, ensure you have the following installed on your system:
Docker Desktop
 (for running Metabase and PostgreSQL containers)
Visual Studio Code
 (for running commands and editing files)
Python 3.10+
 (optional for testing DB connections, but we used it)
psycopg2 library for Python (for PostgreSQL connections)

## Step 1: Start Metabase in Docker

# Run this command inside VS Code terminal (PowerShell or Command Prompt works too):
docker run -d -p 3000:3000 --name metabase metabase/metabase
-d runs container in background
-p 3000:3000 maps Metabase’s port 3000 to your local port 3000
--name metabase names the container metabase
After this, Metabase will appear in Docker Desktop under Containers.

## Step 2: Start PostgreSQL in Docker
# Now let’s run a PostgreSQL container:
docker run --name some-postgres -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres

Explanation:
--name some-postgres → container name is some-postgres
-e POSTGRES_PASSWORD=secret → sets default password to secret
-p 5432:5432 → exposes PostgreSQL on your local machine at port 5432
-d postgres → runs in background using official postgres image
PostgreSQL is now running on localhost:5432 with:
user: postgres
password: secret

## Step 3: Verify Database Connection with Python
Inside VS Code terminal, install psycopg2:
pip install psycopg2
Create a test file test_connection.py in your project folder:
import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="secret",
        host="localhost",
        port="5432"
    )
    print("Connected successfully to PostgreSQL!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)

Run it:
python test_connection.py
If successful, you’ll see: "Connected successfully to PostgreSQL!"

## Step 4: Open Metabase in Browser
Now, go to: http://localhost:3000
This will open the Metabase setup wizard.
Create an Admin account (username, email, password).
Choose Connect to your database.
Enter PostgreSQL credentials:
Host: localhost
Port: 5432
Database name: postgres
Username: postgres
Password: secret
Click Next.
If all is correct, Metabase will connect to PostgreSQL and show the dashboard.

What You Have Now:
Metabase running at http://localhost:3000
PostgreSQL running locally with a test database
Python test confirmed DB connection
Metabase connected to PostgreSQL and ready for queries


Now you can create "Questions" Inside Metabase and save it to the dashboard that will be used by the LLM to display to the user. 


