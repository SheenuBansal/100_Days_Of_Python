# Check Given Number Is Prime Number or Not:
def prime_checker(number):
    count=0
    divisors=[]
    for i in range(1,number+1):
        if number%i==0 :
            count+=1
            divisors.append(i)
    
    if count==2:
        print("It's a Prime Number.")
    else:
        print("It's not a Prime Number")
    print(f"And it's divisors are {divisors}")



n = int(input("Check this number: "))
prime_checker(number=n)


# -------------------------------------------------------------------------- #
#                             Another way:
# -------------------------------------------------------------------------- #



# def prime_checker(number):
#     is_Prime= True
    
#     for i in range(2,number):
#         if number%i==0 :
#             is_Prime=False 
#             break

#     if is_Prime==True:
#         print("It's a Prime Number.")
#     else:
#         print("It's not a Prime Number")


# n = int(input("Check this number: "))
# prime_checker(number=n)





