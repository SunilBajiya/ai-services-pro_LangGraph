def delivery_node(state):
    if state['approved']:
        state['result'] =" Workflow complete sucessfully"
    else:
        state['result'] = "Workflow rejected during approval"

    return state