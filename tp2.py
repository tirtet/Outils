
import subprocess
import os, sys, stat

# Creation d'un fichier
file = open("test.txt", "w")
file.write("Ceci est un fichier test")
file.close()
# Donne des droits au fichier, ici read pour tout le monde, et read/write pour owner

os.chmod("test.txt", stat.S_IROTH )
os.chmod("test.txt", stat.S_IRWXU )


# lestcutre des droits du fichier
filename = "test.txt"
mask = oct(os.stat(filename).st_mode)[-3:]
print("les droits du fichier:", mask)


