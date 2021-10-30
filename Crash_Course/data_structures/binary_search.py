

def binary_search(list1, value):
    found = False
    if len(list1) == 0:
        found = False 
    if len(list1) == 1 and value == list1[0]:
        found = True

    if len(list1) > 1:
        while found:
        # sort the list
            sorted_list = list1.sort()
            
            # find the middle value
            middle_value = (sorted_list[0] + sorted_list[len(sorted_list) - 1])/2
            print("Middle value", middle_value)
            if value == middle_value:
                found = True
            elif value > middle_value:
                new_list = sorted_list[middle_value + 1:]
                mid_val = (new_list[0] + new_list[len(new_list) - 1])/2
                if mid_val == value:
                    found = True
            elif value < middle_value:
                new_list = sorted_list[0: middle_value]
                mid_val = (new_list[0] + new_list[len(new_list) - 1])/2
                if mid_val == value:
                    found = True
    # return found
a = [2, 4]
result = binary_search(a, 2)
print(result)
