#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    """
    YOUR CODE HERE
    """
    if length == 1:
        return None
    # for i in weights:
    #     for x in range(length):
    #         print(x,i)
    #         hash_table_insert(ht,x,i)
    
    for x in range(length):
        # print(x,weights[x])
        hash_table_insert(ht,x, weights[x])


    s = []

    for i in range(length):
        temp = limit - hash_table_retrieve(ht, i)
        # print(temp)
        # print(weights[i])
        if temp in weights:
            s.append(i)
    
    s.sort(reverse = True)
    return s
            # for j in range(length):
            #     if weights[j] == temp and temp != None: 
            #         if j not in s:
            #             s.append(j)

     
        
            


    
    
    # return None


# def print_answer(answer):
#     if answer is None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))
# weights_2 = [4, 4]
# print(get_indices_of_item_weights(weights_2, 2, 8))