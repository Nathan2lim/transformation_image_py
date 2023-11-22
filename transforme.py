from PIL import Image
import json

nomFichier = "imagemystere2.json"

def chargerImg(nomFichier) : 
    chargable = open(nomFichier)
    charger = json.load(chargable)
    return charger

def imageClassique(): 
    
    file = chargerImg(nomFichier)

    data = file['pixels']
    hauteur = len(data)
    largeur = len(data[0])

    print(hauteur)
    print(largeur)

    monImage = Image.new('RGB', (largeur, hauteur))

    for y in range(hauteur):
        for x in range(largeur):
            picol= data[y][x]
            monImage.putpixel((x, y), tuple(picol))
    
    monImage.show()



file = chargerImg(nomFichier)

data = file['pixels']
hauteur = len(data)
largeur = len(data[0])

print(hauteur)
print(largeur)

# Créez une nouvelle image avec une taille augmentée (par exemple, doublez la taille)
nouvelle_largeur = largeur * 2
nouvelle_hauteur = hauteur * 2

monImage = Image.new('RGB', (nouvelle_largeur, nouvelle_hauteur))

# Remplissez la nouvelle image avec les pixels de l'image d'origine
for y in range(hauteur):
    for x in range(largeur):
        pixel_value = data[y][x]
        monImage.putpixel((x * 2, y * 2), pixel_value)
        monImage.putpixel((x * 2 + 1, y * 2), pixel_value)
        monImage.putpixel((x * 2, y * 2 + 1), pixel_value)
        monImage.putpixel((x * 2 + 1, y * 2 + 1), pixel_value)

monImage.show()


