def validation_node(state):
    data = state['data']

    if data['amount'] < 100000: 
        state['validated'] = True

    else:
        state['validated'] = False



# state['data'] ={
#     "customer_id":"c123",
#     "amount": 50000,  
#     "status": "PENDING"
#     "validation": True
# }