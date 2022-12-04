class Saiyan:

    race = 'Saiyan'
        #latest transformation #source of power
    def __init__(self, l_trns, src_pwr):

        self.l_trns = l_trns
        self.src_pwr = src_pwr
 
Goku = Saiyan("Mastered Ultra Instinct", "Angel")
Vegeta = Saiyan("Ultra Ego", "God of Destruction")
Gohan = Saiyan("Beast Form", "Half-Human Bloodline")
 

print('Goku is a', Goku.race)
print('Latest Transformation: ', Goku.l_trns)
print('Source of Power: ', Goku.src_pwr)
 

print('\nVegeta is a', Vegeta.race)
print('Latest Transformation: ', Vegeta.l_trns)
print('Source of Power: ', Vegeta.src_pwr)

print('\nGohan is a', Gohan.race)
print('Latest Transformation: ', Gohan.l_trns)
print('Source of Power: ', Gohan.src_pwr)
