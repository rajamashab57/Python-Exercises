from typing import Tuple

# my_tuple : Tuple[int]  = (1,2,3,4,5,6)

# print(my_tuple*3)


# single_tuple  : tuple = (1)
# double_tuple : Tuple[int] = (1,2)

# mutliple_tuple : Tuple[int]  = (1,2,3)

# mixed_tuple : Tuple[int,float,str] = (3,3.12, "Hello")


# # print(mixed_tuple[0])
# print(double_tuple.__len__())

# # Exercise 4: Iterating Through a Tuple
# # Use a for loop to iterate through a tuple and print each element.

# # my_tuple : Tuple[int] = (1,2,3,4,5)

# # for i in my_tuple:
# #     print(i)

# find_index = mixed_tuple.index("Hello")
# print(find_index)


# nested_tuples : Tuple[int] = (1,(1,2,3),3,4 , (1,2,3))

# print(nested_tuples[0])
# print(nested_tuples[1])
# print(nested_tuples[3])
# print(nested_tuples[4])


# converting_list : Tuple[int] = (1,2,3,4)


# my_list = list(converting_list)
# print(my_list)


# list_tupel : list[int] = [1,2,3,4]

# # converting = Tuple[list_tupel]

# print(tuple(list_tupel))

# packing and unpacking tuples 


# my_tuples : Tuple[str,int,str] = ("Mashab", 24 , "Businessman")

# name , age , profession = my_tuples

# print(my_tuples)


# nested tuples

# nested_tuples : Tuple[Tuple[int,int],Tuple[int,int]] = ((12,13),(10,13))

# print(nested_tuples.count(0))


# =================================




nested_tuples : Tuple[int,int,int ,int ] = [1,2,3,4]

print(nested_tuples.__add__(1))