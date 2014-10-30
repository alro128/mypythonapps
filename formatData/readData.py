# Forma data

basedir = "/Users/alro/dev/elasticsearch/"
i = basedir+"data_books.txt"

c = 0
n = 0
b = []

f = open(i)
for l in f:
 c+=1
 b.append(str(l)) 
 if c==8:
  c=0 
  n+=1
  t = "\"title\": \"{0}\", \"author\": \"{1}\", \"cover\": \"{2}\", \"comments\": {3}, \"currency\": \"{4}\", \"pricenew\": {5}, \"priceused\": {6}".format(b[0],b[1],b[2],b[3],b[4],b[5],b[6])
  print "{ " + t.replace('\r', '').replace('\n', '') + "}"
  b = []

f.close()
