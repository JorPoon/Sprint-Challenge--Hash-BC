#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    """
    YOUR CODE HERE
    """
    i = 1
    for i in range(length):
        # print(i)
        # print(tickets[i].source, tickets[i].destination)
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
    
    # print(hashtable.storage)
    src = "NONE"
    x = 0
    # print(hash_table_retrieve(hashtable, src))
    while x < length:
        x = x + 1
        route.append(hash_table_retrieve(hashtable,src))
        src = hash_table_retrieve(hashtable,src)
   
    #     src = hash_table_retrieve(hashtable,src)
        


    #     while x.key == src:
    #         route.append(x.value)
    #         src = x.value
        # if x is not None:
        #     print(x.key)
        #     if x.key == src:
        #         route.append(x.value)
        #         src = x.value
    
    print(route)
        # print(hashtable.storage[src])
    #     route.append(hash_table_retrieve(hashtable, src))
    #     src = hash_table_retrieve(hashtable, src)
    # print(route)
        
        


    return route

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4,ticket_5,ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]
print(reconstruct_trip(tickets, 10))
