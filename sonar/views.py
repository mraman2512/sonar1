from django.shortcuts import render

# Create your views here.
import requests
from django.conf import settings

# def fetch_code_from_gitlab(project_id):
#     headers = {'Private-Token': settings.GITLAB_TOKEN}
#     url = f'{settings.GITLAB_URL}/api/v4/projects/39818435/repository/files'
#     response = requests.get(url, headers=headers)

#     if response.status_code != 200:
#         raise Exception('Failed to fetch code from GitLab')

#     return response.json()


# def scan_code(project_id):
#     headers = {'Content-Type': 'application/json'}
#     data = {'project': project_id}
#     url = f'{settings.SONARQUBE_URL}/api/ce/submit'
#     response = requests.post(url, headers=headers, json=data)

#     if response.status_code != 200:
#         raise Exception('Failed to scan code with SonarQube')

#     return response.json()


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class fetch_report(APIView):
    def post(self, request):
        data = request.data
        project_id = data['project_id']
        

    def get(self, request,project_id):

        headers = {'Content-Type': 'application/json'}
        # url = f'{settings.SONARQUBE_URL}/api/measures/component?component={project_id}&metricKeys=ncloc,duplicated_lines_density,violations'
        # url = "http://localhost:9000/api/issues/search?projectKey=orgn&p=1&ps=500&status=TO_REVIEW&onlyMine=false&sinceLeakPeriod=false"
        url = f'{settings.SONARQUBE_URL}/api/issues/search?projectKey={project_id}&p=1&ps=500&status=TO_REVIEW&onlyMine=false&sinceLeakPeriod=false'
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception('Failed to fetch report from SonarQube')

        return response.json()
