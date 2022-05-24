# Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).

def sublist(lis):
    sub = []
    lis = (num for num in lis) 
    n = next(lis, 5)  
    while n != 5:
        sub.append(n)
        n = next(lis, 5)  
    return sub

lis = [1,2,3,4,5,6,7,8,9]
print(sublist(lis))


# Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. 
# What is returned is a list of all of the numbers up until it reaches 7.

def check_nums(lis):
    lis = (num for num in lis)
    lis2 = []
    num = next(lis, 7)
    while num != 7:
        lis2.append(num)
        num = next(lis,7)
    return lis2
lis = [1,2,4,6,7,9]
print(check_nums(lis))

# Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. 
# The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).

def sublist(lis):
    lis = (value for value in lis)
    sub = []
    value = next(lis, "STOP")
    while value != "STOP":
        sub.append(value)
        value = next(lis, "STOP")
    return sub
lis = ["Here", "is", "the", "word", "STOP"]
print(sublist(lis))



# Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”.
# The function should return the new list.

def stop_at_z(lis):
    lis = (value for value in lis)
    sub = []
    value = next(lis, "z")
    while value != "z":
        sub.append(value)
        value = next(lis, "z")
    return sub
lis = ["Here", "is", "the", "word", "z"]
print(stop_at_z(lis))



# Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. 
# Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0
sum2 = 0
i = 0
lst = [65, 78, 21, 33]

for x in lst:
    sum1 += x
print(sum1)

while i < len(lst):
    sum2 += lst[i]
    i += 1    
print(sum2)


# Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’.
# What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are 
# returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing


def beginning(lis):
    lis = (value for value in lis)
    value = next(lis, "bye")
    sub = []
    while value != "bye":
        sub.append(value)
        value = next(lis,"bye")
    final_lis = []
    if len(sub)>=10:
        for i in range(0,10):
            final_lis.append(sub[i])
        return final_lis
    else:
        return sub
lis = ['a','b','c','d','e','f','t','y','s','z','u','bye']
print(beginning(lis))
