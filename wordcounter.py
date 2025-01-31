# name = "Ironman"


# def word_counter (a):
#     word_counter = {}
#     temp = []
#     for i in name:
#         if i in temp:
#             continue
#         else:    
#             # print(i,name.count(i))
#             temp.append(i)
#             word_counter[i] = name.count(i)          # 'Dhananjay'-->print(i)-->'D'-->type-->str
#     return word_counter

# print(word_counter(name))

        

## simple alternate method 

def word_counter (s):
    word_counter = {}       # no need to check whether the character occurs previously or not 
    for char in s:          # because in dictionary the keys will automatically update i.e no duplication of keys 
        word_counter[char] = s.count(char)
    return word_counter

print(word_counter("Dhananjay"))