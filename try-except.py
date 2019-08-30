def ask_num():

  while True:
    try:
      num = int(input("Enter a number: "))
      print(f'Thank you, your number squared is: {num ** 2}' )
      break
    
    except:
      print("An error occured! Please try again!")
      continue
    
    finally:
      print("Executed successfully!")

ask_num()
