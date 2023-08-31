from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import streamlit as st

# Load Environment Variables
load_dotenv()

#Initialize Database
# from.uri( this is where you would change the database, to either a local or remote database. )
# If remote, use the .env file to add your remote access key.
db = SQLDatabase.from_uri("sqlite:///assets/chinook.db")

#Initializing Language Model
llmn = OpenAI(temperature=0)
db_chain = SQLDatabaseChain(llm=llmn, database=db)

# Streamlit App
st.title("AI Interface for SQL Databases")
st.markdown("This is a ficticious internal company database ( [chinook DB](https://github.com/lerocha/chinook-database) )" +
            " that allows employees an easy method of data retreival through natural language.")
st.markdown("[Visual Representation](https://docs.yugabyte.com/images/sample-data/chinook/chinook-er-diagram.png)")
st.markdown("[Source Code](https://github.com/delfortrie/)")

# Sample Questions
question_bank = [
    'What does the company produce?',
    'How many products do we offer?',
    'What is the average unit price for our products?',
    'Which customers have the most invoices, and what is their contact information?',
    'Which employees have upcoming birthdays?',
    ]

# Loop through questions, add to markdown
st.markdown("## Sample Questions")
for i in question_bank:
    st.markdown("- " + i)

# Chatbot
prompt = st.chat_input()
answer = db_chain.run(prompt)

# Only run if there is a prompt
if prompt:
    st.chat_message("User").write(prompt)
    st.chat_message("AI").write(answer)