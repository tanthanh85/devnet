import requests

GITLAB_TOKEN = "glpat-ZeX3SbdQBsaW5v2rdJsA"

def get_projects():
    url = "http://gitlab.example.com/api/v4/projects"
    headers = {'Authorization': 'Bearer ' + GITLAB_TOKEN}
    response = requests.get(url,headers=headers)
    return response.status_code, response.json()

if __name__ == '__main__':
    status_code, projects = get_projects()
    print("status code is " + str(status_code))
    for project in projects:
        print(str(project['id']) + " " + project['name'])

