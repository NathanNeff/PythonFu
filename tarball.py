import tarfile
import os

maxSize = 200
i = 0
curSize = 0

dir_to_tar = 'dummydata'

s = tarfile.open('tarfile' + str(i) + '.tgz', mode='w:gz')
for f in os.listdir(dir_to_tar):
    full_path = dir_to_tar + "/" + f
    s.add(full_path)
    curSize = curSize + os.path.getsize(full_path)
    if curSize >= maxSize:
        print "Finished writing %s" % s.name
        s.close()
        i = i + 1
        s = tarfile.open('tarfile' + str(i) + '.tgz', mode='w:gz')
        curSize = 0
        print "Opening new tar file: %s" % s.name
s.close()

