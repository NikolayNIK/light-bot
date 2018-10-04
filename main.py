from subprocess import call;
import time;

call(["clear"]);
print('''=====light bot=====
<^>v - player.
# - void cell.
O - dark cell (turn all into light to win).
0 - light cell.
''')

HELP = '''1 - move one cell fowrard.
2 - move two cell forward.
L - turn left (counter-clockwise)
R - turn right (clockwise)
C - light the cell.
''';

ORIENTATION_CHARS = ['<', '^', '>', 'v'];
ORIENTATION_INTS = {'<':1, '^':2, '>':3, 'v':4};

ORIENTATION_OFFSET_X = [-1, 0, 1, 0];
ORIENTATION_OFFSET_Y = [0, -1, 0, 1];

#field
#playerX
#playerY
#playerO

level = int(input('Enter a level: '));

def printField(field, playerX, playerY, playerO):
	call(["clear"]);
	print((len(field[0]) + 2) * "#");
	for y in range(0, len(field)):
		row = field[y];
		tmp = '#';
		for x in range(0, len(row)):
			if x == playerX and y == playerY:
				tmp += ORIENTATION_CHARS[playerO - 1];
			else:
				tmp += row[x];
		tmp += '#';
		print(tmp);
	print((len(field[0]) + 2) * "#");

while True:
	try:
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
					playerO = shit;
					playerX = x;
					playerY = y;
					row[x] = ' ';
		
		printField(field, playerX, playerY, playerO);
		print(HELP);
		
		victory = True;
		commands = list(input("Enter commands: "));
		printField(field, playerX, playerY, playerO);
		for command in list(commands):
			time.sleep(1);
			if command == '1':
				playerX += ORIENTATION_OFFSET_X[playerO - 1];
				playerY += ORIENTATION_OFFSET_Y[playerO - 1];
				if (playerX < 0) or (playerY < 0) or (playerY >= len(field)) or (playerX >= len(field[playerY]) or field[playerY][playerX] == '#'):
					victory = False;
					break;
			elif command == '2':
				playerX += 2 * ORIENTATION_OFFSET_X[playerO - 1];
				playerY += 2 * ORIENTATION_OFFSET_Y[playerO - 1];
				if (playerX < 0) or (playerY < 0) or (playerY >= len(field)) or (playerX >= len(field[playerY]) or field[playerY][playerX] == '#'):
					victory = False;
					break;
			elif command == 'C' or command == 'c':
				if field[playerY][playerX] == 'O':
					field[playerY][playerX] = '0';
				else:
					victory = False;
					break;
			elif command == 'L' or command == 'l':
				playerO -= 1;
				if playerO < 1:
					playerO = 4;
			elif command == 'R' or command == 'r':
				playerO += 1;
				if playerO > 4:
					playerO = 1;
			else:
				victory = False;
				print("Wrong command: " + command);
				break;
			
			printField(field, playerX, playerY, playerO);
		
		for row in field:
			for char in row:
				if char == 'O':
					victory = False;
					break;
		
		if victory:
			input("You won! Press enter to continue...");
			level+=1;
		else:
			input("You lost! Press enter to retry...");
	except FileNotFoundError:
		print("No levels left! Congratulations!");
		input("Press enter to continue...");