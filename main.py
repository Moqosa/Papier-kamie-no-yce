from random import choice #Pobiera lista lub krotkę i losuje jeden losowy element

while True:
    
    wybor_gracza = input("Wybierz papier/kamien/nożyce:")
    
    wybor_komputera = ['papier', 'kamien', 'nożyce']
    
    losowanie_komputera = choice(wybor_komputera)
    
    komputer_points = int(0)
    gracz_points = int()
    
    if losowanie_komputera == wybor_gracza:
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Mamy remis")
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    
    elif losowanie_komputera == 'papier' and  wybor_gracza == 'nożyce':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Gratulacje wygrałeś z komputerem")
        gracz_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    
 
    elif losowanie_komputera == 'papier' and wybor_gracza == 'kamień':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Przykro mi ale przegrałeś :(")
        komputer_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    

    elif losowanie_komputera == 'kamien' and wybor_gracza == 'papier':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Gratulacje wygrałeś z komputerem")
        gracz_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    

    elif losowanie_komputera == 'kamien' and wybor_gracza == 'nożyce':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Przykro mi ale przegrałeś :(")
        komputer_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    

    elif losowanie_komputera == 'nożyce' and wybor_gracza == 'papier':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Przykro mi ale przegrałeś :(")
        komputer_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  
    
    elif losowanie_komputera == 'nożyce' and wybor_gracza == 'kamień':
        print(f"Komputer wylosował: {losowanie_komputera}")
        print("Gratulacje wygrałeś z komputerem")
        gracz_points += 1
        wybor = input("\nCzy chcesz kontynuować dalje grę (tak/nie):")
        if wybor == 'nie':
            break
        else:
            continue  

print(f"Wynik komputera to {komputer_points} \nWynik gracza to {gracz_points}")
