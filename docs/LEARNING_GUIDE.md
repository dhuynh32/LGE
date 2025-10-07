# LangGraph Essentials: Documentation & Learning Guide

## Overview
This project demonstrates core LangGraph concepts through a stepwise, hands-on learning approach. It covers agent creation, state management, CLI interaction, multi-node workflows, conditional routing, and workflow visualization.

## Project Structure
- `src/main.py`: Main agent logic, CLI, state management, multi-node workflow, logging, and visualization.
- `requirements.txt`: Python dependencies (LangGraph, LangChain, etc.).
- `.taskmaster/tasks/tasks.json`: Task tracking and project management.
- `README.md`: Project introduction and setup instructions.

## LangGraph Concepts Demonstrated
### 1. Agent Creation
- How to initialize a LangGraph agent.
- Basic prompt/response loop.

### 2. State Management
- Using LangGraph's state to persist conversation context.
- Passing and updating state between nodes.

### 3. CLI Interface
- Interactive command-line chat with the agent.
- Educational logging to show state and workflow changes.

### 4. Multi-Node Workflow
- Building a graph with multiple nodes (e.g., agent, echo, router).
- Implementing conditional routing and node selection.

### 5. Visualization & Debugging
- Printing workflow structure and node execution order.
- Enhanced logging for learning and debugging.

## Example Scenarios
- Simple "Hello World" interaction.
- Stateful conversation with memory.
- Conditional routing based on user input.

## Extending the Implementation
- Add new nodes for more complex workflows.
- Integrate external APIs or tools.
- Expand CLI for advanced user interaction.

## Learning Guide
1. **Read through `src/main.py` and follow the comments.**
2. **Run the CLI and experiment with different inputs.**
3. **Modify the workflow graph to add or change nodes.**
4. **Use the logging and visualization to understand agent decisions.**
5. **Refer to LangGraph and LangChain documentation for deeper learning.**

---

For questions or contributions, see the repository at https://github.com/dhuynh32/LGE
