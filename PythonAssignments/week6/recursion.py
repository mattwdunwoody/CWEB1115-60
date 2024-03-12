# recursion

# palindrome
# neveroddoreven

def isPalindrome(word):
    word = word.replace(" ", "")
    return f"Is {word} a palindrome? {word == word[::-1]}"
print(isPalindrome("never odd or even"))

# towers of hanoi
def printMove(source, to):
    print('Move from', source, 'to', to)

def Towers(n, source, to, spare):
    if n == 1:
        printMove(source, to)
    elif n != 1:
        Towers(n-1, source, spare, to)
        printMove(source, to)
        Towers(n-1, spare, to, source)

Towers(10, 'A', 'C', 'B')