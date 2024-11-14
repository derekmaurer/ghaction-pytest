import boto3
import json

def getssmparam(ssm_name):
    session = boto3.Session()
    ssm = session.client('ssm')
    parameter = ssm.get_parameter(Name=ssm_name, WithDecryption=True)
    parameter = json.loads(parameter['Parameter']['Value'])
    return(parameter)
