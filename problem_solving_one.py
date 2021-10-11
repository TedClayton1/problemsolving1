# input data hello from user
# print out in reverse


# greeting = input("Please say hello: ")
# stringlength=len(greeting)
# slicedString=greeting[stringlength::-1]
# print(slicedString)

#input data string from user
# Print out the first letter of each word as capital with a space in between 

# conversation = input("What are you doing today and please respond in lowercase letters? ")
# result = conversation.title()

# print(result)

#input data string 
# and then compress that string

new_string = ""
string = "aaaaaaaaabbbbbbcccccccccccddddddeeeeeeeeeeeeeeeeeeeeffffffffffffffffffggggggggggggggg"
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count = count + 1
    else:
        new_string += string[i] + str(count)
        count = 1
new_string +=  string[i+1] + str(count)
print(new_string)

#word, phrase or sequence that reads the same forward as backward i.e madam(palindrome)
#write code that takes user input and checks to see if is a palindrome and reports the result

palindrome_checker = input("Please provide a word, phrase or sequence  ")
if(palindrome_checker==palindrome_checker[::-1]):
    print("This word is indeed a palindrome! Read it and weep or rejoice :)")
else:
    print("This for darn sure isn't a palindrome! Please try again ")



