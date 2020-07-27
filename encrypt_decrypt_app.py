import random
letter = ["a", "b" , "c", "d", "e",
          "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o",
          "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]

character = list(input("Enter a 26 character code of your choice that you want for encryption or decryption: ")) 

#space_key = list(input("Enter a 4 character code for spaces in your sentence:"))

#  def check_key():
#    for n in space_key:
#      if n == character[1,2,3,4] :
#        print("Enter a different code")
#        check_key()
#      else:
#        startup()
key_code = {key:value for key, value in zip(letter, character)}

reverse_dict = {key:value for key, value in zip(character, letter)}

#key_code[" "] = random.choice(space_key)
#reverse_dict[" "] = random.choice(space_key)

codedlist= []

reverselist=[]

def startup():
  prompt1 = input("Would you like to encrypt or decode?(e or d)")
  if prompt1.lower() == "e":
    encodetext()
  elif prompt1.lower() =="d":
    reverse()
    
def encodetext():
  statement = str(input("Enter the statement to be encrypted:").lower())
  for i in statement:#s
    updated_list = codedlist.append(key_code.get(i))
  encryptedstring=""
  for element in codedlist:
    encryptedstring += element 
  print(encryptedstring)
  #f = open(r"#enter a path on your computer", "a", encoding="utf-8")
  #f.write(encryptedstring)
  #f.write("\n")
  #f.close

def reverse():
  statement2 = str(input("Enter the statement to be decrypted:").lower())
  for i in statement2:
    updated_list = reverselist.append(reverse_dict.get(i))
  decryptedstring=""
  for element in reverselist:
    decryptedstring += element 
  print(decryptedstring)
  #f = open(r"enter you path location", "a", encoding="utf-8")
  #f.write(decryptedstring)
  #f.close

startup()