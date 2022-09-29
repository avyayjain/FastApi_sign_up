import json
import requests


def upload_to_google_drive(file):
    print(file)
    headers = {
        "Authorization": "Bearer ya29.A0ARrdaM9MJrex2srvdXI6mn5JK580rEh2o9l-INLduAbXrhGqQZs6dFSQAQ2iyg47e7ns8LilNYLq"
                         "-myYxfjaGzzep-OVPQXLRqzM7ND4FQAR-Vd1xwbQX6EhzV6im1pesfsdr1JMCQYO5QvpyqIVkwmyUd9j"}
    para = {
        "name": file.file,
    }
    typei = json.dumps(para["name"])
    print(typei)
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(file, "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files.files
    )
    print(r.text)

#upload_to_google_drive("test.jpg")