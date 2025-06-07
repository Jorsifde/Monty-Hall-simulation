import random

def monty_hall_simulation(runs):
    wins = 0
    losses = 0

    for i in range(runs):
        
        car = random.randint(0, 2)
        
        choice = random.randint(0, 2)
        
        possible_doors = [i for i in range(3) if i != choice and i != car]
        opened = random.choice(possible_doors)
        
        switch_choice = [i for i in range(3) if i != choice and i != opened][0]
       
        if switch_choice == car:
            wins += 1
        else:
            losses += 1

    print(f"Anzahl Durchläufe: {runs}")
    print(f"Gewonnen (mit Wechseln): {wins} ({wins/runs:.2%})")
    print(f"Verloren (mit Wechseln): {losses} ({losses/runs:.2%})")


try:
    runs = int(input("Wie viele Durchläufe sollen simuliert werden? "))
    monty_hall_simulation(runs)
except ValueError:
        print("Bitte eine gültige Zahl eingeben.")
