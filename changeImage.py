#!/usr/bin/env python3
from PIL import Image
#import subprocess
import glob
print("Changing images...")
path="./supplier-data/images"
size=(600,400)
for file in glob.glob(path+"/*.tiff"):
  img=Image.open(file)
  x, f, e=file.split(".")
  img.resize(size).convert("RGB").save("/home/student-00-bf54473ca934"+f+".jpeg")
  print(f)
