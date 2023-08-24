#! /usr/bin/env python3
import os
import requests
import glob

url="http://localhost/fruits/"
path="./supplier-data/descriptions/"
print("Uploading descriptions...")
for file in os.listdir(path):
  with open(path+file, 'r') as f:
   field=f.read().split("\n")
   f,e=file.split(".")
#testing   print("name: "+field[0]+"\nweight: "+field[1]+"\ndescription: "+field[2]+"\nimage_name: "+f+".jpeg")
   w,u=field[1].split()
   dict={"name":field[0], "weight":w, "description":field[2],"image_name":f+".jpeg"}
   r=requests.post(url, data=dict)
   print("satus code: "+r.status_code)
