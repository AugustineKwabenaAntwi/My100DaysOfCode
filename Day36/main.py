def binary_search(list,element):
    middle = 0
    start = 0
    end = len(list)-1
    step = 0

    while (start <=end):
        print(f"Steps:{step} list: {str(list[start:end +  1])}")

        step +=1
        middle = (start + end)//2 

        if list[middle] == element :
            return middle
        elif list[middle] < element :
            start = middle + 1
        else:
            end = middle -1 ##take the item directly to the left of the midpoint that means getting rid of the mid
    return False        


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12

binary_search(my_list,target)