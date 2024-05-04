from datetime import datetime

class Validation:
  def __init__(self) -> None:
    pass

  @staticmethod
  def getInt(message, min, max):
    check = True
    while check:
      try:
        _input = int(input(message))
        if _input >= min and _input <= max:
          check = False
        else:
          print("Please input number in range: ", min , " and ", max)
      except:
        print("Invalid Input")
    return _input
  
  @staticmethod
  def getFloat(message, min, max):
    check = True
    while check:
      try:
        _input = float(input(message))
        if _input >= min and _input <= max:
          check = False
        else:
          print("Please input number in range: ", min , " and ", max)
      except:
        print("Invalid Input")
    return _input
  
  @staticmethod
  def is_date_format(s):
        format = "%d-%m-%Y"
        try:
            datetime.strptime(s, format)
            return True
        except ValueError:
            return False
  
  @staticmethod
  def getBirth():
    status = True
    while status:
      birth = input("Enter your date of birth (dd-mm-YYYY): ")
      if Validation.is_date_format(birth):
        status = False
        return birth
      else:
        print("Invalid date format!!!")