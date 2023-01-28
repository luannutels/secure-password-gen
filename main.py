SECURE = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('I','|'),('C','('),('E','ε'),('r','®'),('n','ⁿ'),('8','∞'),('B','ß'),('b','ß'))
def secure(password):
  '''Secure Password Function'''
  for x,y in SECURE:
    password = password.replace(x,y)
  return password
if __name__ == "__main__":
  password = input("Enter Your Password:- \n")
  password = secure(password)
  print(f"Your Password is {password}")