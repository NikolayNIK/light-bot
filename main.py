from subprocess import call

#playerX
#playerY
#playerO
#field

# Characters
CHARS_CELL = ['1','2','3','4','5']
CHARS_CELL_DARK = ['a','b','c','d','e']
CHARS_CELL_LIGHT = ['A','B','C','D','E']
CHAR_PLAYER = '@'

# Orientation contants
ORIENTATION_NONE = 0;
ORIENTATION_UP = 1;
ORIENTATION_RIGHT = 2;
ORIENTATION_BOTTOM = 3;
ORIENTATION_LEFT = 4;
ORIENTATION = {

HELP = """
0 - to light the cell you're standing on.
1 - to move forward in the direction you looking to.
"""

# prints "UI" and lets user enter a commands.
def update():
	call(["clear"]);
	print((len(field[0]) + 1) * "#");
	for row in field:
		tmp = '#';
		for char in row:
			if char != '\n':
				tmp += char;
		tmp += '#';
		print(tmp);
	print((len(field[0]) + 1) * "#");
	
	# print help
	print(HELP);
	commands = list(input("Enter commands: "));
	
	

# Read level from file.
file = open("level.txt", "r");
lines = file.readlines();
file.close();

playerX = int(lines[0]);
playerY = int(lines[1]);
playerO = int(lines[2]);


# Search for player and its orientation.
for y in range(0, len(field)):
	row = field[y];
	for x in range(0, len(row)):
		char = row[x];
		if char == 

update();