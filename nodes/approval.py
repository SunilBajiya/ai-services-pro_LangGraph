def approval_node(state):
    if state['validated']:
        state['approved'] = True
    else:
        state['approved'] = False
    return state


