import requests
from prettytable import PrettyTable

GITLAB_TOKEN = "glpat-ZeX3SbdQBsaW5v2rdJsA"

def get_pipelines():
    url = "http://gitlab.example.com/api/v4/projects/4/pipelines"
    headers = {'Authorization': 'Bearer ' + GITLAB_TOKEN}
    response = requests.get(url,headers=headers)
    return response.status_code, response.json()

if __name__ == '__main__':
    status_code, pipelines = get_pipelines()
    print("status code is " + str(status_code))
    table = PrettyTable()
    table.field_names = ["Pipeline ID", "Pipeline Status", "Pipeline Ref", "Pipeline Source"]
    for pipeline in pipelines:
        table.add_row([pipeline['id'], pipeline['status'], pipeline['ref'], pipeline['source']])
    print(table)