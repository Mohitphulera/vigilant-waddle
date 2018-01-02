file = open("Dict.txt", "r") 
word = str(input("Type your word for spell checking: "))
word = word.lower() 
success = False
i = 1
for line in file:
    if word == line.strip(): 
	        print("Your word is spelt correctly!")
	        success = True
	        break
if success == False: 
    print("The word is spelt wrong")
