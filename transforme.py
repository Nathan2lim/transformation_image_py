

# fait en sorte que je puisse lire un fichier 
def read_file(path):
    file = open(path, "r") 
    return file


print(read_file('./imagemystere.json'))