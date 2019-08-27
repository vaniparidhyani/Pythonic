#/usr/bin/python


import json
import requests
import os
import shutil

inventory_directory = "/apps/scripts/ssh_key_rotation/inventory"

if not os.path.exists(inventory_directory):
  os.makedirs(inventory_directory)


requests.packages.urllib3.disable_warnings()

projects = '{"projects": [{"name": "partnerPortal","landscape": ["dev03", "dev04"],"apptype": ["author", "publish", "webserver"]},{"name": "acom","landscape": ["dev04", "qa04"],"apptype": ["author", "publish"]}]}'

projects = json.loads(projects)

for project in projects['projects']:
  shutil.rmtree(inventory_directory+"/"+project['name'])
  for landscape in project['landscape']:
    for apptype in project['apptype']:
      url = "https://wcms-hostdb.com/cgi-bin/appservers.py?project="+project['name']+"&landscape="+landscape+"&apptype="+apptype
      resp = requests.get(url, verify=False)
      json_resp = resp.json()
      if len(json_resp) > 0:
        dir = inventory_directory+"/"+project['name']+"/"+landscape
        if not os.path.exists(dir):
          os.makedirs(dir)
        open(dir+"/"+apptype, 'w').close()
        f=open(dir+"/"+apptype, "a+")
        for host in json_resp:
          host = json.dumps(host).strip('["').strip('"]')
          f.write("%s\n" % host)
        f.close()
