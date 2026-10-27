#Binary Search

# numbers = [89, 120, 150, 160, 180, 189, 201]
# min = (0 + 6) // 2
# print(min)

# Binary search loop
# numbers = [89, 120, 150, 160, 180, 189, 201]
# while low <= high:
#    mid = (low + high) // 2

#    if numbers[mid] < target:
#        print("Number found")
#        return
#    elif numbers[mid] == target:
#        print("Number found at index: ",mid, "with value: ",target)
#        return
#   else:
#        high = mid - 1

# Complete Example

numbers = [89, 120, 150, 160, 180, 189, 201]
print("Numbers in the list:", numbers)

target = int(input("Enter the number to search: "))
low = 0
high = len(numbers) - 1

while low <= high:
        mid = (low + high) // 2


        if numbers[mid] == target:
                print("Number found at index:",mid, "with value:",target)
                break
        elif numbers[mid] < target:
                low = mid + 1
        else:
                high = mid - 1
else:
        print("Number not found")






