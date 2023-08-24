#!/usr/bin/env python3
from PIL import Image
import glob
print("Changing images...")
path="./supplier-data/images"
size=(600,400)
for file in glob.glob(path+"/*.tiff"):
  img=Image.open(file)
  x, f, e=file.split(".")
  print(f)
  img.resize(size).convert("RGB").save("."+f+".jpeg")
  print(f)
