# /repos/{owner}/{repo}/pulls
# This is an axample project to fetch pull requests of an particular repository from GitHub !!
import requests

#it is same like opening this URL on browser
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

all_details = response.json()

for i in range(len(all_details)):
     print(all_details[i]["user"]["login"])



