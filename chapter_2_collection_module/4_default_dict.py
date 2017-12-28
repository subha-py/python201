from collections import defaultdict

sentence = 'The red for jumped over the fence and ran to the zoo for food'
words = sentence.split(' ')


# simplified this code using default dict
# reg_dict = {}
# for word in words:
#     if word in reg_dict:
#         reg_dict[word]+=1
#     else:
#         reg_dict[word]=1
# print(reg_dict)

d=defaultdict(int)
for word in words:
    d[word]+=1

print(d)