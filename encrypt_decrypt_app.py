#Version 1.0
import sys
import smtplib
letter = ["a", "b" , "c", "d", "e",
          "f", "g", "h", "i", "j",
          "k", "l", "m", "n", "o",
          "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]

character = list(input("Enter a 26 character code of your choice that you want for encryption or decryption: ")) 

if len(character) < 26:
  print("Insufficient characters")
  sys.exit
  
elif len(character) > 26:
  print("excess characters")
  sys.exit

key_code = {key:value for key, value in zip(letter, character)}

reverse_dict = {key:value for key, value in zip(character, letter)}

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
  for i in statement:
    updated_list = codedlist.append(key_code.get(i))
  encryptedstring= ""
  for element in codedlist:
    encryptedstring += element 
  print(encryptedstring)
  email = input("do you want to email? y/n: ").lower()
  if email == "y":
    gmail_user = '#'
    gmail_password = '#'
    server = smtplib.SMTP('smtp.gmail.com', ###)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(gmail_user, gmail_password)
    subject= 'TEXT'
    body = encryptedstring + "###"+ "#### "
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
      'your email',
      'their email',
      msg
    )
    print('The message has been sent!')
  elif email == "n":
    sys.exit
                          
def reverse():
  statement2 = str(input("Enter the statement to be decrypted:").lower())
  for i in statement2:
    updated_list = reverselist.append(reverse_dict.get(i))
  decryptedstring=""
  for element in reverselist:
    decryptedstring += element 
  print(decryptedstring)

startup()
