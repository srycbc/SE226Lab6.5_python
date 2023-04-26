print("***QUESTION 1***")

def createList(list1,list2):
    list3=[]

    for x in list2:
        if x in list1 and x not in list3:
            list3.append(x)
    return list3

list1 = [5,7,8,6,1,2]
list2 = [9,7,6,2,3,4,1]
list3 = createList(list1,list2)
print(list3)

print()
print("***QUESTION 2***")

def createPalindrome(stringWords):
    palindorme = []
    for y in stringWords:
        if y == y[::-1]:
            palindorme.append(y)
    return palindorme

stringWords = ["seray","course","python","level","mom","software","bob"]
palindorme = createPalindrome(stringWords)
print(palindorme)

print()
print("***QUESTION 3***")

def findPrime(numbers):
    primeNumbers = []
    prime = [True] * (max(numbers)+1)
    prime[0] = False
    prime[1] = False

    for a in numbers:
        if prime[a]:
            primeNumbers.append(a)
            for b in range(a*2, max(numbers)+1,a):
                prime[b] = False
    return primeNumbers

numbers = [1,2,3,4,5,6,7,8]
primeNumbers = findPrime(numbers)
print(primeNumbers)

print()
print("***QUESTION 4***")

def anagrams(word, word_list):
    sortWord = sorted(word.lower().replace(" "," "))
    anagramList = []

    for w in word_list:
        sWord = sorted(w.lower().replace(" "," "))
        if sortWord == sWord:
            anagramList.append(w)
    return anagramList

word = "below"
word_list = ["elbow", "wolbe", "computer", "seray"]
anagramList = anagrams(word,word_list)
print(anagramList)
