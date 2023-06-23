

def palindromes():
    word = input("Введите слово-палиндром: ")
    if word==word[::-1]:
        return True
    return False
print(palindromes())
