str_ob = 'amazon'

list_str= list(str_ob)

left = 0
right = len(list_str) - 1 

while left < right:
    list_str[left], list_str[right] = list_str[right], list_str[left]

    left += 1
    right -= 1

joined_str = "".join(list_str)
print(joined_str)