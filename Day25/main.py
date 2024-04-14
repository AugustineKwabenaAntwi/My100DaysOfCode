nums = [1,2,3,4,5,6,7,8,9,10]
'''my_list = []
for n in nums:
    my_list.append(n)
print(my_list)'''    

## list comprehension
my_list=[n for n in nums]
print(my_list)

'''my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
print(my_list)'''

my_list=[n for n in nums if n%2==0 ]
print(my_list)

# i want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
my_list = []

'''for letter in 'abcd':
    for num in range(4):
        my_list.append((letter,num))
print(my_list)        '''

my_list = [(letter,num) for letter in 'abcd' for num in range(4) ]
print(my_list)

names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman', 'Superman','Spiderman','Wolverine','Deadpool']

my_dict = {name:hero for (name,hero) in zip(names,heros) if name != 'Peter'}
print(my_dict)