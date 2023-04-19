import os 

deb_pkg_path = "make.deb"

os.system("dpkg -x %s ." % deb_pkg_path)

files = os.listdir('.')

for f in files:
    print(f)
