user1 = {
  'name': 'Sorna',
  'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fxn):
  def wrap(*args, **kwargs):
    if args[0]["valid"]:
        return fxn(*args, **kwargs)
    else:
        return print("invalid user")

  return wrap

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

