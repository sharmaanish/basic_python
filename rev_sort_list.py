list_a = [1,2,3,1,5,6]

left = 0
right = len(list_a) - 1

while left < right:
    list_a[left] , list_a[right] = list_a[right] , list_a[left]
    left += 1
    right -= 1

print(list_a)