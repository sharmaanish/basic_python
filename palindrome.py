expected_str = str(input("enter the pallindrome"))

left =  0

right = len(expected_str) - 1
result =   'it is'
while left < right:
    if expected_str[left] != expected_str[right]:
        result = "its not palindorme"
        break

    left += 1
    right -= 1


print(result)

