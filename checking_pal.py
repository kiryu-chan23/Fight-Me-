

def check_for_palindromes(theList):
    palindromes = [] #Initialize an empty list to store palindrome words


    for word in theList:
        # check if the word is the same forwards and backwords
        if word == word[::-1]:
            palindromes.append(word) # add palindrome to the list
    return palindromes # return the list of  palindromes

theList = ["level", "hello", "world", "madam", "python"]
print(check_for_palindromes(theList))