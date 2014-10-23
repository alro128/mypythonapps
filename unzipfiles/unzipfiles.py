import zipfile
import os

basedir = "C:\\Python\\workspace_python\\downloads\\"
  
flist = os.listdir(basedir)

for f in flist:
 if f.endswith(".zip"):
  print f
  z = zipfile.ZipFile(basedir+f)
  z.extractall(basedir)
