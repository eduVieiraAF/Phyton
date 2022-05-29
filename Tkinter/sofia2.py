from ast import Break

while True:
    nome = input("Digite um nome: ").upper()
    
    if nome == "SOFIA":
        print("Linda do papai!")
    
    elif nome == "EDUARDO":
        print("Papai bobinho...")
    
    elif nome == "CAMILA":
        print("HELLOOOOOOOOOOOO!")
    
    elif nome == "YUKARI":        
        print("Nome em Joãoponeis")
    
    elif nome == "BYE":
        break
    
    else:
        print("Não conheço esse.")
    
    print()