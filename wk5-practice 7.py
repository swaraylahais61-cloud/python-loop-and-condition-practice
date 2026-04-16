#Palindrome Check (NO reverse built-in)

word = "katak"
is_palindrome = True

for i in range(len(word)):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")