from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import re
from sqlalchemy import create_engine, text
import os
import json

# Load env variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


def ChatGoogleGen(question: str):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)
    # Load DB credentials
    db_user = "DB_NAME"
    db_password = "db_password"
    db_name = "atliq_tshirts"
    cloud_sql_connection_name = os.getenv("CLOUD_SQL_CONNECTION_NAME")  

    # Build Unix socket-based connection URI for Cloud SQL
    db_uri = f"mysql+pymysql://{db_user}:{db_password}@/{db_name}?unix_socket=/cloudsql/{cloud_sql_connection_name}"

    print("🔍 DB URI:", db_uri)
    
    # LangChain-compatible DB object
    db = SQLDatabase.from_uri(db_uri, include_tables=["t_shirts"], sample_rows_in_table_info=3)

    # SQLAlchemy engine to execute the final query
    engine = create_engine(db_uri)

    prompt = '''
    You are an SQL expert.
    This is the schema of the database: {schema}
    Your task is to generate the SQL query required to get the answer for this question: {question}
    Your output should be in JSON FORMAT with the below key:
     - sql_query: <your sql query here>

    DO NOT INCLUDE THE ```json``` TAGS.
    '''

    formatted_prompt = prompt.format(schema=db.table_info, question=question)
    response = llm.invoke(formatted_prompt)

    #print("\nRaw LLM response:\n", response.content)

    # Try to parse JSON directly
    match = re.search(r"```json\s*({.*?})\s*```", response.content, re.DOTALL)
    if not match:
        return ""

    json_str = match.group(1)

    # Step 2: Parse JSON and extract the SQL query
    try:
        data = json.loads(json_str)
        query = data.get("sql_query", "").strip()
    except json.JSONDecodeError:
        query = ""

    # Execute the query
    query = text(query)
    # print(query)

    with engine.connect() as conn:
        result = conn.execute(query)
        rows = result.fetchall()
        print("Manual SQL Result:", rows)
        prompt_2 = '''
        Generate a human like answer for the following question: {question} using the following answer: {rows}
        '''
        output = llm.invoke(prompt_2.format(question=question, rows=rows))
        return output.content

