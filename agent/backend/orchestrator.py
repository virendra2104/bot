from agent.academy_agents import knowledge_agent, web_agent
from tutor.llm_tutor import llm_tutor_agent
from flows.registration import handle_registration
from memory.state_manager import AgentState
from flows.intent_detector import detect_intent

# Global state
state = AgentState()

async def run_agent(message: str) -> str:
    """
    Main orchestrator function to handle messages
    """

    # Step 0: Check if registration is ongoing
    if state.get("intent") == "registration":
        return handle_registration(message, state)

    # Step 1: Detect intent
    intent = detect_intent(message)
    if intent == "registration":
        return handle_registration(message, state)

    # Step 2: Internal knowledge agent
    answer = await knowledge_agent(message)
    if answer != "NOT_FOUND":
        return answer

    # Step 3: Web agent
    web_answer = await web_agent(message)
    if web_answer != "NOT_FOUND":
        return web_answer

    # Step 4: LLM fallback
    return await llm_tutor_agent(message)
