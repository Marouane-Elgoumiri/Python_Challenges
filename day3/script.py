text = input("Please enter a text: ")

a = input("Enter Letter 1: ")
b = input("Enter Letter 2: ")
c = input("Enter Letter 3: ")


L=(text.split())
print ("******************I************************")
print(f"\nLetter {a} appears:{text.count(a)} times")
print(f"Letter {b} appears:{text.count(b)} times")
print(f"Letter {c} appears:{text.count(c)} times")
print ("******************II************************")
print(f"\nThere are {len(L)} words in your text")
print ("******************III***********************")
print(f"\nThe first letter is {text[0]} and end with {text[-1]}")
print ("******************IV***********************")
L.reverse()
inverted_text= ' '.join(L)
print(f"\nInverted text: {inverted_text}")
print ("******************IV***********************")
y = input("Looking for a word? answer with yes or no ")
if(y=="yes"):
    word= input("Enter the word: ")
    if (word in text):
         print(f"Yep it does exist")
    else: print("Sorry nope")
elif(y=="no"):
     print("bye")
     exit(0)