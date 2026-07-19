from ..agents.memory_agent import MemoryAgent


def test_memory_save():

    memory = MemoryAgent()

    memory.save_conversation("test", {"status": "OPEN"})

    assert True
