given_string = "fhbfhlfdwbbwvhwiugowuiwwm"

# ----------------- CORE Python ----------------------
# new_dict = {}
# for c in given_string:
#     if c not in new_dict:
#         new_dict[c]=1
#     else:
#         new_dict[c]+=1

# print(new_dict)

from collections import defaultdict

new_dict = defaultdict(int) #by default it gives value = 0 for every character in given_string
# new_dict = defaultdict(lambda:2)

for c in given_string :
    new_dict[c]+= 1

print(new_dict)
