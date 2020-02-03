# Create a Local File Using .write() method

inner_planets = open('inner_planets.txt', 'w')
inner_planets.write("Mercury\nVenus\nEarth\nMars")
inner_planets.close()

inner_planets = open('inner_planets.txt', 'r')
print(inner_planets.read())
inner_planets.close()
