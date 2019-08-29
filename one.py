# one.py

print('hello')

# __name__ -> built in variable
# gets assigned the string "__main__" in the background
# if we run current file directly python will assign
# if __name__ == "__main__":


def func():
  print('FUNC() IN ONE.PY')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
  print('ONE.PY is being run directly!')
else:
  print('ONE.PY has been imported!')