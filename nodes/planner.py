from llm.gemini_client import get_gemini_llm

def planner_node(state):
    try:
        llm = get_gemini_llm()
        prompt = f"""Break this business request into workflow steps:{state['client_request']}"""
        response = llm.generate_content(prompt)
        if not response or not response.text:
            state['plan'] = ['Default step']
        else:
            state['plan'] = response.text.split("\n")

    except Exception as e:
        state['plan'] =['planning failed']
        state['error'] = str(e)
    
    return state