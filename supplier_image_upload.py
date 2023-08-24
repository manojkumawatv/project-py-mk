#!/usr/bin/env python3
import requests
import glob
path="./supplier-data/images/"
url="http://localhost/upload/"
print("Uploading...")
for f in glob.glob(path+"*.jpeg"):
  with open(f,'rb') as file_obj:
    r=requests.post(url, files={'file': file_obj})
