import tkinter as tk

def convertBin() :
    octet = valeur.get()
    octetBinaire = list(map(int, octet))
    octetBinaireResultat = octetBinaire[0] * 128 + octetBinaire[1] * 64 + octetBinaire[2] * 32 + octetBinaire[3] * 16 + octetBinaire[4] * 8 + octetBinaire[5] * 4 + octetBinaire[6] * 2 + octetBinaire[7] * 1
    
    resultatLabel.config(text=f"Le résultat en binaire est de : {octetBinaireResultat}")

def convertHex() :
    octet = valeur.get()
    octetBinaire = list(map(int, octet))

    nombreBinaire1 = octetBinaire[0] * 8 + octetBinaire[1] * 4 + octetBinaire[2] * 2 + octetBinaire[3] * 1
    nombreBinaire2 = octetBinaire[4] * 8 + octetBinaire[5] * 4 + octetBinaire[6] * 2 + octetBinaire[7] * 1
    calcul = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    octetHexaResultat = calcul[nombreBinaire1] + calcul[nombreBinaire2]

    resultatLabel.config(text=f"Le résultat en hexadécimale est de : {octetHexaResultat}")
    
def replaceButton() : 
    buttonConvert.destroy() # destroy the button

    buttonHex = tk.Button(root, text="Hexadécimale", command=convertHex)
    buttonHex.pack()

    buttonBin = tk.Button(root, text="Binaire", command= convertBin)
    buttonBin.pack()


root=tk.Tk()

root.title("Convertisseur")
root.geometry("500x800")
root.minsize(360, 480)
root.maxsize(800, 1080)
# root.iconbitmap("")
root.config(background="#1C1919")

labelTitle = tk.Label(root, text="Convertisseur hexadécimale, décimale et binaire", font=("Courrier", 13, "bold"), bg='#1C1919', fg="#FFFFFF", pady=40)
labelTitle.pack()

valeur = tk.Entry(root)
valeur.pack()

buttonConvert = tk.Button(root, text="Convertir", command=replaceButton)
buttonConvert.pack()

resultatLabel = tk.Label(root, text="", bg="#1C1919", fg="#FFFFFF")
resultatLabel.pack()

root.mainloop()
