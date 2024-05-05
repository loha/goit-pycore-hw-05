from validations import isOnlyChars, isPhone, is_valid_uuid

def body_parser(func):
  def inner(*args):
    try:
      cmd, *payload = args[0].split(" ")

      return func(cmd.lower(), payload)
    except ValueError:
      print("Give me name and phone please.")

  return inner

def add_user_validation(func):
  def inner(*args, **kwargs):
    try:
      payload = args[0]

      if not isOnlyChars(payload[0]):
        raise ValueError
      
      if not isPhone(payload[1]):
        raise ValueError
          
      return func(*args, **kwargs)
    except ValueError:
      print("Give me valid name(only chars) and phone(start with +380) please.")

  return inner

def edit_user_by_id_validation(func):
  def inner(*args, **kwargs):
    try:
      payload = args[0]

      if not is_valid_uuid(payload[0]):
        raise ValueError
      
      if not isOnlyChars(payload[1]):
        raise ValueError
      
      if not isPhone(payload[2]):
        raise ValueError

      return func(*args, **kwargs)
    except ValueError:
      print("Give me valid user id(should be UUID) and new name(only chars) and phone(start with +380) please.")

  return inner

def get_phone_validation(func):
  def inner(*args, **kwargs):
    try:
      payload = args[0]

      if not isOnlyChars(payload[0]):
        raise ValueError

      return func(*args, **kwargs)
    except ValueError:
      print("Give me valid  name(only chars).")

  return inner
