import requests
print(requests.__version__)
#// https://pypi.org/project/requests/
r = requests.get("http://google.com/")
print(r.status_code)
# https://stackoverflow.com/questions/14120502/how-to-download-and-write-a-file-from-github-using-requests 
r = requests.get("https://raw.githubusercontent.com/j-Saggu/Lab1/main/lab1.py")
print(r.status_code)

