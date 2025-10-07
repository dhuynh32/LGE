import unittest
from src.main import call_model, echo_node, AgentState

class TestAgentFunctions(unittest.TestCase):
    def test_call_model_hello(self):
        state = {"messages": ["hello"]}
        result = call_model(state)
        self.assertIn("Agent remembers: hello -> Hello, world!", result["messages"][-1])

    def test_call_model_ping(self):
        state = {"messages": ["ping"]}
        result = call_model(state)
        self.assertEqual(result["messages"][-1], "pong")

    def test_echo_node(self):
        state = {"messages": ["test"]}
        result = echo_node(state)
        self.assertEqual(result["messages"][-1], "Echo: test")

    def test_empty_state(self):
        state = {"messages": []}
        result = call_model(state)
        self.assertIn("Agent remembers:  -> Hello, world!", result["messages"][-1])
        result2 = echo_node(state)
        self.assertEqual(result2["messages"][-1], "Echo: ")

if __name__ == "__main__":
    unittest.main()
