from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import BaseMessage, SystemMessage , ToolMessage , HumanMessage , AIMessage
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

load_dotenv()

document_content =""

class AgentState(TypedDict):
    messages:Annotated[Sequence[BaseMessage], add_messages]
    
@tool
def update(content:str) -> str:
    """Upadate the document with new content"""
    global document_content
    document_content += "\n" + content
    return f"Document updated. Current content:\n{document_content}"

@tool
def save(filename:str) -> str:
    """Save the document to a file
    
    Args: filename name for the text file
    """
    if not filename.endswith(".txt"):
        filename += ".txt"
   
    try:
        with open(filename, "w") as f:
            f.write(document_content)
            print(f"Document saved to {filename}")
        return f"Document saved to {filename}"
    
    except Exception as e:
        return f"Error saving document: {str(e)}" 

tools = [update, save]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash").bind_tools(tools)
 
 
def our_agent(state: AgentState) -> AgentState:
    system_prompt = SystemMessage(content=f"""
    You are Drafter, a helpful writing assistant. You are going to help the user update and modify documents.
    
    - If the user wants to update or modify content, use the 'update' tool with the complete updated content.
    - If the user wants to save and finish, you need to use the 'save' tool.
    - Make sure to always show the current document state after modifications.
    
    The current document content is:{document_content}
    """)
    
    if not state["messages"]:
        user_input = " i am ready to help you draft your document. What would you like to do?"
        user_message = HumanMessage(content=user_input)
        
    else:
        user_input = input("\n what could like to with the doucuent?")
        user_message = HumanMessage(content=user_input)
    all_messages = [system_prompt] + list(state["messages"]) + [user_message]
    
    response = model.invoke(all_messages)
    
    print(f"\n🤖 AI: {response.content}")
    if hasattr(response, "tool_calls") and response.tool_calls:
        print(f"🔧 USING TOOLS: {[tc['name'] for tc in response.tool_calls]}")

    return {"messages": list(state["messages"]) + [user_message, response]}
