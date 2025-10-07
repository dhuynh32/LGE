from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

def call_model(state: AgentState):
    messages = state['messages']
    if messages:
        last_message = messages[-1]
    else:
        last_message = ""
    if last_message.lower() == "ping":
        response = "pong"
    else:
        response = f"Agent remembers: {last_message} -> Hello, world!"
    return {"messages": messages + [response]}

def echo_node(state: AgentState):
    messages = state['messages']
    if messages:
        last_message = messages[-1]
    else:
        last_message = ""
    response = f"Echo: {last_message}"
    return {"messages": messages + [response]}

from langgraph.graph import StateGraph

def print_workflow_structure():
    print("\nWorkflow Structure:")
    print("  [agent] <--- user input (default)")
    print("      |\n      +--> [echo] <--- user input starts with 'echo '")
    print("      |\n      +--> [agent] (after echo)")
    print("  [agent] is both entry and finish point.")

def main():
    workflow = StateGraph(AgentState)
    workflow.add_node("agent", call_model)
    workflow.add_node("echo", echo_node)
    workflow.set_entry_point("agent")
    workflow.set_finish_point("agent")
    app = workflow.compile()

    print("Welcome to the LangGraph CLI! Type 'exit' to quit.")
    print_workflow_structure()
    state = {"messages": []}
    turn = 1
    while True:
        user_input = input(f"You ({turn}): ")
        if user_input.strip().lower() == "exit":
            print("Exiting chat. Conversation history:")
            for idx, msg in enumerate(state['messages']):
                print(f"{idx+1}: {msg}")
            break
        # Add user message to state
        state['messages'].append(user_input)
        # Decide which node to use
        if user_input.lower().startswith("echo "):
            print("[LOG] Routing to node: echo")
            state = app.invoke(state, node="echo")
        else:
            print("[LOG] Routing to node: agent")
            state = app.invoke(state, node="agent")
        print(f"[LOG] State after node: {state['messages']}")
        print(f"Agent: {state['messages'][-1]}")
        turn += 1
if __name__ == "__main__":
    main()
