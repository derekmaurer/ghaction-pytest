import boto3
import json
import datetime

def dateconvert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def getaccesstoken(ssm_name,region):
    client = boto3.client('ssm', region_name=region)
    response = client.get_parameter(Name=ssm_name, WithDecryption=True)
    token = json.loads(json.loads(json.dumps(response, sort_keys=True, indent=4, default=dateconvert))["Parameter"]["Value"])
    accesstoken = token[0]["accessToken"]
    return(accesstoken)