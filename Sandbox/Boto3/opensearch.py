from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

sts_client = boto3.client('sts')
#client = boto3.client('opensearch')


host = "vpc-cmc-search-qa-nklhlxkkftwqqq7jqgt4maequ4.us-west-2.es.amazonaws.com"
host = "vpc-cmc-test-e2ihw5opel55zggwcn2mchqif4.us-west-2.es.amazonaws.com"

region = "us-west-2"

service = 'es'


#assumed_role_object=sts_client.assume_role(RoleArn="arn:aws:iam::375532340732:role/CMC-Services-NonProd-NonProdOpensearchIAMRole-TC8NSHR7YKIJ",RoleSessionName="AssumeRoleSession1")
#print(assumed_role_object)
#credentials=assumed_role_object['Credentials']



credentials = boto3.Session().get_credentials()
print(credentials)

#awsauth = AWS4Auth(credentials['AccessKeyId'],credentials['SecretAccessKey'] , region, service, credentials['SessionToken'])
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)


search = OpenSearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

print(search)
document = {
    "title": "Moneyball",
    "director": "Bennett Miller",
    "year": "2011"
}

#search.index(index="movies", doc_type="_doc", id="5", body=document)

print(search.get(index="movies", doc_type="_doc", id="5"))
