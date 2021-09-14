import random

# generating random floating points between [0,1)
random_float=random.random()
print(random_float)

# generating random integer points between [0,10]
random_integer=random.randint(1,10)
print(random_integer)

# ----------------------------
# -- Exercise --
random_decimal_integer=random.uniform(0,5)
print(random_decimal_integer)

# another way to print decimals between 0 and 5
random_float=random.random()
print(random_float*5)

# applications: dice, coin toss, video games etc. 

# Calculate love score
love_score=random.randint(1,100)
print(love_score)
