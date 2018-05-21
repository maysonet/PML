
import pickle


filename = "datae.PML"
try:
    with open(filename, 'rb') as input:
        proj = pickle.load(input)
        print(proj.name)
        
except FileNotFoundError:
        print("problem ocurred")
