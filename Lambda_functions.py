# Lambda function to convert a string to upper case
str = "test"
upper = lambda string : string.upper()
print(upper(str))

#List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())
