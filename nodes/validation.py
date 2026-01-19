def validation_node(state):
    data = state['data']

    if data['amount'] < 100000: 
        state['validated'] = True

    else:
        state['validated'] = False
    return state



