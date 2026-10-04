import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

db_uri = os.getenv("SQL_SERVER_URI")
db = SQLDatabase.from_uri(db_uri)

llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest",
    temperature=0,
)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
model_with_tools = llm.bind_tools(tools)

SYSTEM_PROMPT = """You are an agent designed to interact with a Microsoft SQL Server database.
Given an input question, create a syntactically correct T-SQL query, run it, and look at the results.
Always limit your query to at most 5 results using TOP unless specified otherwise.
Never run any DML statements (INSERT, UPDATE, DELETE, DROP)."""

def call_model(state: MessagesState):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = model_with_tools.invoke(messages)
    return {"messages": [response]}

builder = StateGraph(MessagesState)

builder.add_node("agent", call_model)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

app = builder.compile()

if __name__ == "__main__":
    test_question = "What are the top 3 selling tracks in Chinook?"
    print(f"\nQuestion: {test_question}\n" + "-" * 40)

    events = app.stream(
        {"messages": [HumanMessage(content=test_question)]},
        stream_mode="values"
    )
    for event in events:
        event["messages"][-1].pretty_print()