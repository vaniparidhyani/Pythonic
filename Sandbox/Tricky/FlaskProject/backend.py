#!/usr/bin/python

import pwd, os

msg = "All Good!"
def MainFunction(inputs):
  if ValidateInputs(inputs):
    ExecuteOperation(inputs)
 
  return msg

def ValidateInputs(input):
  #Check for empty inputs
  for v in input.values():
    if not v :
      global msg
      msg = "Enter values for all the fields"
      return False
      
  #Check if user exists
  try:
    pswd = pwd.getpwnam(input['Username'])
    if input['Op'] == 'Create':
      msg = "User already exists. Can not create this user. Please go back and choose wisely this time!"
      return False
  except:
    return True

def ExecuteOperation(input):
  if input['Op'] == 'Create':
    os.system('useradd -d '+input['Home']+' -s '+input['Shell']+' '+input['Username'])
