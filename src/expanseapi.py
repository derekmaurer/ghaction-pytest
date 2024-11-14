import requests
import json
from datetime import datetime, timedelta

def expanseget(exticket,extoken,exinstance):
    url = 'https://'+exinstance+'.desire2learn.com/api/operations/getChangeTicketDetails?TicketName='+exticket
    headers = {'Content-Type':'application/json','x-access-token':extoken}
    response = requests.get(url, headers=headers)
    return response

def expnewchange(firstname,lastname,department,username,extoken,exinstance):
    now = datetime.utcnow()

    ChangeStart     = now
    ChangeRequested = now + timedelta(hours=2)
    ChangeEnd       = now + timedelta(hours=2)

    HistoricalSuccess           = "Standard Change"
    WorstCaseImpact             = "P4"
    PlannedStartDate            = ChangeStart.strftime("%Y-%m-%d %H:%M:%S")
    PlannedEndDate              = ChangeEnd.strftime("%Y-%m-%d %H:%M:%S")
    CompletionDueDate           = ChangeEnd.strftime("%Y-%m-%d %H:%M:%S")
    CreatedByUser               = "operationsautomation"
    AssignmentGroup             = "Cloud-Platform"
    AssignedTo                  = "operationsautomation"
    BusinessJustification       = "As per user request"
    ShortDescription            = "068 - Platform - RHU AD User Creation "+username
    Description                 = "068 - Platform - RHU - AD User Creation:"+username+", RHU.int.d2l Domain where the new user will be created, "+department+" User department, "+firstname+" User First Name, "+lastname+" User Last Name, "+username+" Account name"
    ExpectedMinutesToComplete   = 120
    ExpectedMinutesOfDowntime   = 0
    ImplementationPlan          = "https://d2lmail.sharepoint.com/:w:/r/sites/Saas/SaaSCM/sops/Documents/068%20-%20Platform%20-%20AD%20User%20Administration.docx?d=wd25abc52420441659c948065cf6b801b&csf=1&web=1&e=xWt2on"
    ValidationPlan              = "https://d2lmail.sharepoint.com/:w:/r/sites/Saas/SaaSCM/sops/Documents/068%20-%20Platform%20-%20AD%20User%20Administration.docx?d=wd25abc52420441659c948065cf6b801b&csf=1&web=1&e=xWt2on"
    RollbackPlan                = "https://d2lmail.sharepoint.com/:w:/r/sites/Saas/SaaSCM/sops/Documents/068%20-%20Platform%20-%20AD%20User%20Administration.docx?d=wd25abc52420441659c948065cf6b801b&csf=1&web=1&e=xWt2on"
    TestingPlan                 = "https://d2lmail.sharepoint.com/:w:/r/sites/Saas/SaaSCM/sops/Documents/068%20-%20Platform%20-%20AD%20User%20Administration.docx?d=wd25abc52420441659c948065cf6b801b&csf=1&web=1&e=xWt2on"
    SecurityPolicyReview        = "1"

    jsonbody = expformatjsonbody(HistoricalSuccess,WorstCaseImpact,PlannedStartDate,PlannedEndDate,CompletionDueDate,CreatedByUser,AssignmentGroup,AssignedTo,BusinessJustification,ShortDescription,Description,ExpectedMinutesToComplete,ExpectedMinutesOfDowntime,ImplementationPlan,ValidationPlan,RollbackPlan,TestingPlan,SecurityPolicyReview)
    print (jsonbody)

    url = 'https://'+exinstance+'.desire2learn.com/api/operations/createChange'
    headers = {'Content-Type':'application/json','x-access-token':extoken}
    response = requests.post(url, headers=headers, data=jsonbody)
    return (response)

def expupdatechange(exticket,status,extoken,exinstance):
    if status == 'pending':
        url = 'https://'+exinstance+'.desire2learn.com/api/operations/setChangePendingApproval?TicketName='+exticket+'&UpdatedByUser=operationsautomation'
        headers = {'Content-Type':'application/json','x-access-token':extoken}
        response = requests.get(url, headers=headers)
        return (response) 
    if status == 'inprogress':
        url = 'https://'+exinstance+'.desire2learn.com/api/operations/setChangeInProgress?TicketName='+exticket+'&UpdatedByUser=operationsautomation'
        headers = {'Content-Type':'application/json','x-access-token':extoken}
        response = requests.get(url, headers=headers)
        return (response)
    if status == 'complete':
        url = 'https://'+exinstance+'.desire2learn.com/api/operations/setChangeCompletedSuccessfully?TicketName='+exticket+'&MinutesOfDowntime=0&UpdatedByUser=operationsautomation'
        headers = {'Content-Type':'application/json','x-access-token':extoken}
        response = requests.get(url, headers=headers)
        return (response)
    if status == 'cancelled':
        url = 'https://'+exinstance+'.desire2learn.com/api/operations/setChangeCancelled?TicketName='+exticket+'&UpdatedByUser=operationsautomation'
        headers = {'Content-Type':'application/json','x-access-token':extoken}
        response = requests.get(url, headers=headers)
        return (response)

def expformatjsonbody(HistoricalSuccess,WorstCaseImpact,PlannedStartDate,PlannedEndDate,CompletionDueDate,CreatedByUser,AssignmentGroup,AssignedTo,BusinessJustification,ShortDescription,Description,ExpectedMinutesToComplete,ExpectedMinutesOfDowntime,ImplementationPlan,ValidationPlan,RollbackPlan,TestingPlan,SecurityPolicyReview):
    jsonbody = {
        'HistoricalSuccess':HistoricalSuccess,
        'WorstCaseImpact':WorstCaseImpact,
        'PlannedStartDate':PlannedStartDate,
        'PlannedEndDate':PlannedEndDate,
        'CompletionDueDate':CompletionDueDate,
        'CreatedByUser':CreatedByUser,
        'AssignmentGroup':AssignmentGroup,
        'AssignedTo':AssignedTo,
        'BusinessJustification':BusinessJustification,
        'ShortDescription':ShortDescription,
        'short_description':ShortDescription,
        'Description':Description,
        'ExpectedMinutesToComplete':ExpectedMinutesToComplete,
        'ExpectedMinutesOfDowntime':ExpectedMinutesOfDowntime,
        'ImplementationPlan':ImplementationPlan,
        'ValidationPlan':ValidationPlan,
        'RollbackPlan':RollbackPlan,
        'TestingPlan':TestingPlan,
        'SecurityPolicyReview':SecurityPolicyReview
    }

    jsonbody = json.dumps(jsonbody)
    return (jsonbody)