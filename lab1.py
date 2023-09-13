import requests
print(requests.__version__)
#// https://pypi.org/project/requests/
r = requests.get("http://google.com/")
r.status_code
