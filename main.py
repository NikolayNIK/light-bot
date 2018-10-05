from subprocess import call;
from time import sleep;
from os import system;

# Clears console.
def clear():
	try:
		call("clear");
	except:
		system("cls");

clear();
print('''=====light bot=====
<^>v - player.
# - void cell.
O - dark cell (turn all into light to win).
0 - light cell.
''')

HELP = '''1 - move one cell fowrard.
2 - move two cells forward.
L - turn left (counter-clockwise).
R - turn right (clockwise).
C - light the cell.
''';

ORIENTATION_CHARS = ['<', '^', '>', 'v'];
ORIENTATION_INTS = {'<':1, '^':2, '>':3, 'v':4};

ORIENTATION_OFFSET_X = [-1, 0, 1, 0];
ORIENTATION_OFFSET_Y = [0, -1, 0, 1];

level = int(input('Enter a level: '));

# Clears console and prints field with borders.
def printField(field, playerX, playerY, playerO):
	clear();
	print((len(field[0]) + 2) * "#");
	for y in range(0, len(field)):
		row = field[y];
		tmp = '#';
		for x in range(0, len(row)):
			if x == playerX and y == playerY:
				tmp += ORIENTATION_CHARS[playerO];
			else:
				tmp += row[x];
		tmp += '#';
		print(tmp);
	print((len(field[len(field) - 1]) + 2) * "#");

try:
	while True:
		# Read level from file.
		file = open(str(level) + ".txt", "r");
		field = file.readlines();
		file.close();
		
		playerX = None;
		playerY = None;
		playerO = None;

		# Turn field into a field and find player position and orientation.
		for y in range(0, len(field)):
			row = list(field[y]);
			row.pop();
			
			field[y] = row;
			for x in range(0, len(row)):
				char = row[x];
				shit = ORIENTATION_INTS.get(char);
				if shit:
					playerO = shit - 1;
					playerX = x;
					playerY = y;
					row[x] = ' ';
					break; # Can't break upper one. Darn python.
		
		printField(field, playerX, playerY, playerO);
		print(HELP);
		
		victory = True;
		commands = list(input("Enter commands: "));
		printField(field, playerX, playerY, playerO);
		
		# Execute commands one by one.
		for command in list(commands):
			sleep(1);
			if command == '1':
				playerX += ORIENTATION_OFFSET_X[playerO];
				playerY += ORIENTATION_OFFSET_Y[playerO];
				if (playerX < 0) or (playerY < 0) or (playerY >= len(field)) or (playerX >= len(field[playerY]) or field[playerY][playerX] == '#'):
					victory = False;
					break;
			elif command == '2':
				playerX += 2 * ORIENTATION_OFFSET_X[playerO];
				playerY += 2 * ORIENTATION_OFFSET_Y[playerO];
				if (playerX < 0) or (playerY < 0) or (playerY >= len(field)) or (playerX >= len(field[playerY]) or field[playerY][playerX] == '#'):
					victory = False;
					break;
			elif command == 'C' or command == 'c' or command == 'с' or command == 'С':
				if field[playerY][playerX] == 'O':
					field[playerY][playerX] = '0';
				else:
					victory = False;
					break;
			elif command == 'L' or command == 'l' or command == 'д' or command == 'Д':
				playerO -= 1;
				if playerO < 0:
					playerO = 3;
			elif command == 'R' or command == 'r' or command == 'к' or command == 'К':
				playerO += 1;
				if playerO > 3:
					playerO = 0;
			else:
				victory = False;
				print("Wrong command: " + command);
				break;
			
			printField(field, playerX, playerY, playerO);
		
		for row in field:
			for char in row:
				if char == 'O':
					victory = False;
					break; # Can't break upper one. Darn python.
		
		if victory:
			input("You won! Press enter to continue...");
			level+=1;
		else:
			input("You lost! Press enter to retry...");
except FileNotFoundError:
	print("No levels left! Congratulations!");
	input("Press enter to continue...");