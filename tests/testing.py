import silky
from silky import iteration
from silky import train as tr

#iteration.run_ferret()
while (True):
    if (iteration.run_ferret_forest() < 5):
        print("Success! Model can solve the forest game in under 5 attempts!")
        break
