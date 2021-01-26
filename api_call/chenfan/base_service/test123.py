import requests

url = "http://14.17.122.160:19081/tasks/complete"

body={
        "taskId":193499,"taskIds":[193499],"orderNo":"vx001002001803747404900732928"
}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIzNjAyMDk4NDEiLCJqdGkiOiLrtIzkoYPjm5jur73guKfgtLXql6jojrfkn43uoJAiLCJpc3MiOiJocmZheC5jYXJsb2FuLmp3dCJ9.3z4hAPO5RpMTRF-HwwfNg1e2fujd_5IoFntlCJLzoUH2vLujoN2sFeiGHkyyjMoPKc94mhY3MTfZ_e4iNXLA4Q'
}

response = requests.post(url=url,headers=headers,json=body)

print(response.text)