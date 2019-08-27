import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--hostname", help="enter the hostname you need to remove")
args = parser.parse_args()
host = args.hostname
password = ''
master_hostname="or1010050158190.com"
servicelist = []






def getServices(hostname):
        getServiceslist = []
        url="https://"+master_hostname+":5665/v1/objects/services?attrs=name&attrs=package&filter=host.name==%22"+hostname+"%22"
        print url
        r = requests.get(url, auth=('root', password), verify=False)
        print r.status_code
        out = r.json()
        for serv in out["results"]:
                if serv["attrs"]["package"] == "_api":
                        getServiceslist.append(serv["name"])
        return getServiceslist







def delServices(hostname,listofservices):
        for servicename in listofservices:
                url="https://"+master_hostname+":5665/v1/objects/services/"+servicename+"?cascade=1"
                print url
                headers= {'Accept': 'application/json'}
                r = requests.delete(url, auth=('root', password), verify=False, headers=headers)
                print r.status_code








def delPackage(hostname):
        url="https://"+master_hostname+":5665/v1/config/packages/"+hostname+"?cascade=1"
        print url
        headers= {'Accept': 'application/json'}
        r = requests.delete(url, auth=('root', password), verify=False, headers=headers)
        print r.status_code












servicelist = getServices(host)
print servicelist
print "####################################################"
delServices(host,servicelist)
servicelist = getServices(host)




if servicelist:
        print "It seems all Services are not deleted"
        print servicelist
        print "Deleting services once again"
        delServices(host,servicelist)
else:
        print ""




if servicelist:
        print "Not able to delete all the services for this node. Please retry or contact Admin "
else:
        print "All services related to node deleted, removing the node from Icinga now  . . "
        #delPackage(host)
