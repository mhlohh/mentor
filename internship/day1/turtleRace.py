import turtle

WIDTH, HEIGHT = 800,800
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
MIN_RACER = 2
MAX_RACER = 10

def get_number_of_racers():
    racer = 0
    while True:
        racer = input("Enter the number of racers (2-10): ")
        if racer.isdigit():
            racer = int(racer)
            if MIN_RACER <= racer <= MAX_RACER:
                break
            else:
                print(f"Ther number of racer should be between ({MIN_RACER} - {MAX_RACER})")
        else:
            print(f"Input not a numeric... Try Again!")
    return racer
            
racers = get_number_of_racers()
print(racers)