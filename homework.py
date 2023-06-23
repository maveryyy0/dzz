

def palindromes():
    word = input("Введите палиндром: ")
    if word==word[::-1]:
        return True
    return False
print(palindromes())
