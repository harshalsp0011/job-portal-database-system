import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL Credentials 
db_username = "postgres"
db_password = "121201"
db_host = "localhost"
db_port = "5432"
db_name = "job_db"

# Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

# Function to run queries
def run_query(query):
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)
    return df

# Streamlit UI 

st.set_page_config(page_title="Job Portal Dashboard", layout="wide")

st.title("Job Portal Database System")

# Custom SQL Query Section
st.markdown("---")
st.subheader("Run Your Own SQL Query")
custom_query = st.text_area("Enter SQL Query:", height=150)

if st.button("Execute Custom SQL"):
    try:
        df = run_query(custom_query)
        st.success("Custom query executed successfully!")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")
