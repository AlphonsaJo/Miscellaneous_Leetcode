#GFG Lambda Functions for Revision
# Lambda function to convert a string to upper case
str = "test"
upper = lambda string : string.upper()
print(upper(str))

#List Comprehension
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
    print(item())
    
# if-else loop
max = lambda a, b : a if (a > b) else b
print(max(1,5))

#Return second largest of a sublist
sortList = lambda x: (sorted(i) for i in x)
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

#filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

#Filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
