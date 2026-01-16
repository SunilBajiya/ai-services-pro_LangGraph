def approval_node(state):
    if state['validated']:
        state['approved'] = True
    else:
        state['approved'] = False




# state['data'] ={
#     "customer_id":"c123",
#     "amount": 50000,
#     "status": "PENDING"
#     "validation": True
#     "approved": True
# }