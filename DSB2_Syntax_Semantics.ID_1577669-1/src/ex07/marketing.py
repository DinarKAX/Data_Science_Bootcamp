import sys

def f_call_center(clients, recipients):#Клиенты, которые не видели сообщение
    clients_set = set(clients)
    recipients_set = set(recipients)
    return list(clients_set - recipients_set)

def f_potential_clients(participants, clients):#Участники, которые не являются клиентами
    participants_set = set(participants)
    clients_set = set(clients)
    return list(participants_set - clients_set)

def f_loyalty_program(clients, participants):#клиенты, которые не участвовали в мероприятии
    participants_set = set(participants)
    clients_set = set(clients)
    return list(clients_set - participants_set)

def main():
    if len(sys.argv) != 2:
        raise ValueError("Wrong count arguments!")
    
    list_f = ["call_center", "potential_clients", "loyalty_program"]
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
                'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
                'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org',
                    'jessica@gmail.com', 'elon@paypal.com', 'pinkman@yo.org',
                    'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if sys.argv[1] == list_f[0]:
        result = f_call_center(clients, recipients)
    elif sys.argv[1] == list_f[1]:
        result = f_potential_clients(participants, clients)
    elif sys.argv[1] == list_f[2]:
        result = f_loyalty_program(clients, participants)
    else:
        raise ValueError("Wrong task name")
    
    for email in result:
        print(email)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(type(err).__name__, err, sep=': ')