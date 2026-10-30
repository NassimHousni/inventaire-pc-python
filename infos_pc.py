import platform
import psutil
from datetime import datetime


print("\n=== ÉTAT DE MON PC ===\n")
print("System:", platform.system())
print("version:", platform.version())
print("Nom du pc:", platform.node())
print("Architecture:", platform.machine())
print("Processor:", platform.processor())

###Variable pour stocker la date et l'heure du rapport
date_rapport = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Date du rapport :", date_rapport)

print()
####Calcul de l'espace disque utilisé en pourcentage et affiche le pourcentage d'utilisation du disque C:
disque_utilise = psutil.disk_usage("C:/").percent
print("Utilisation du disque C:", disque_utilise, "%")

###Calcul de la RAM totale en Gio
ram_octets = psutil.virtual_memory().total
ram_gio = ram_octets / (1024 ** 3)
print("Ram totale :", round(ram_gio, 1), "Gio")

####Calcul de la RAM utilisée en pourcentage
ram_utilisee = psutil.virtual_memory().percent
print("Ram utilisee: ", ram_utilisee, "%")

####Calcul de l'espace disque total en Gio et donne Avertissement si l'espace disque est presque plein
if disque_utilise > 90:
    print("Attention, le disque C: est presque plein !")
else:
    print("Disque C: : utilisation normale")

###Calcul de l'espace disque total en Gio et donne Avertissement si la RAMest presque plein
if ram_utilisee > 80:
    print("Attention, la RAM est presque pleine !")
else:
    print("RAM : utilisation normale")

###utilisation de la fonction open() pour créer un fichier texte et écrire les informations dans le fichier
nom_fichier = "rapport_pc.txt"
with open(nom_fichier, "w", encoding="utf-8") as fichier:
    fichier.write("=== ÉTAT DE MON PC ===\n")
    fichier.write("Date du rapport : " + date_rapport + "\n")
    fichier.write("System: " + platform.system() + "\n")
    fichier.write("version: " + platform.version() + "\n")
    fichier.write("Nom du pc: " + platform.node() + "\n")
    fichier.write("Architecture: " + platform.machine() + "\n")
    fichier.write("Processor: " + platform.processor() + "\n")
    fichier.write("Utilisation du disque C: " + str(disque_utilise) + "%\n")
    fichier.write("Ram totale : " + str(round(ram_gio, 1)) + " Gio\n")
    fichier.write("Ram utilisee: " + str(ram_utilisee) + "%\n")
    if disque_utilise > 90:
        fichier.write("Attention : le disque C: est presque plein !\n")
    if ram_utilisee > 80:
        fichier.write("Attention : la RAM est presque pleine !\n")
