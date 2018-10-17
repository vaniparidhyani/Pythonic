#!/usr/bin/python


import sys
import boto3
import pprint
import json

input = sys.argv[1]
value = sys.argv[2]

dynamodb = boto3.resource('dynamodb','ap-south-1')
table = dynamodb.Table('qlik')
#print(table.creation_date_time)

def post(msg,table):
  table.put_item(
   Item={
        'count': msg,
    }
)
  return "Message submitted: "+ msg

def get_all(msg,table):
  response = table.scan()
  items = response['Items']
  print json.dumps(items)
#  pp = pprint.PrettyPrinter(indent=4)
#  pp.pprint(json.dumps(items))

def get_specific(msg,table):
  response = table.get_item(
    Key={
        'count': msg,
    }
)
  item = response['Item']
  rev = msg[::-1]
  if ( rev == msg ):
    return msg +" is pallindrome"
  else:
    return msg +" is not pallindrome"

def delete(msg,table):
  table.delete_item(
   Key={
        'count': msg,
    }
)
  return "Deleted Item: "+ msg

if "post" in input:
  print post(value,table)
if "get_all" in input:
  get_all(value,table)
if "get_specific" in input:
  print get_specific(value,table)
if "delete" in input:
  print delete(value,table)
