alien_o = {'x_position':0,'y_position':25,'speed':'medium'}

if alien_o['speed'] == 'slow':
	x_increament = 1
elif alien_o['speed'] == 'medium':
	x_increament =2
else:
	x_increament = 3

alien_o['x_position'] += x_increament

print(f"The alien's new position is {str(alien_o['x_position'])}")