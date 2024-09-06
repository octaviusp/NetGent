import unittest
from netgent.core.state import State
from netgent.core.agent import Agent

class TestState(unittest.TestCase):
    def test_state_update(self):
        state = State({"a": 1})
        state.update({"b": 2})
        self.assertEqual(state.data, {"a": 1, "b": 2})

class MockAgent(Agent):
    def invoke(self, state: State) -> State:
        state.update({"processed": True})
        return state

class TestAgent(unittest.TestCase):
    def test_agent_invoke(self):
        agent = MockAgent()
        initial_state = State({"input": "test"})
        result_state = agent.invoke(initial_state)
        self.assertTrue(result_state.get("processed"))

if __name__ == '__main__':
    unittest.main()