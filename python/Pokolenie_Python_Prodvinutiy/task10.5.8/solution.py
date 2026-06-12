clients = {}

def bank(operation, user_id, amount=0):
    global clients

    match operation:
        case 'top up':
            clients[user_id] = clients.get(user_id, 0) + amount
        case 'withdraw':
            clients[user_id] = clients.get(user_id, 0) - amount
        case 'pay':
            clients[user_id] = clients.get(user_id, 0) - amount
        case 'show balance':
            if user_id in clients:
                print(clients[user_id])
            else:
                print(0)