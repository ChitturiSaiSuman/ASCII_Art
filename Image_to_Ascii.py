# Converts Images to ASCII Art

from PIL import Image
from numpy import array
from os import listdir

def convert_to_matrix(file:str, empty: str, filled:str) -> None:
	image = Image.open("Letters/" + file, "r")
	width, height = image.size
	values = list(image.getdata())
	for i in range(len(values)):
		values[i] = list(values[i])
	
	values = list(values)
	l = []
	temp = [values[0]]
	for i in range(1, len(values)):
		if i % width == 0:
			l.append(temp)
			temp = []
		temp.append(values[i])
	l.append(temp)
	file_name = list(map(str, file.split(".")))[0]
	with open("Letters/" + file_name + ".txt", "w") as text_file:
		for s in l:
			text_file.write(''.join([empty if 255 not in s[i] else filled for i in range(len(s))])+'\n')



# Main Function to handle input and
# call Other utility functions

def main():
	# Change empty and filled to other characters
	# to produce different ASCII Arts
	empty, filled = '-', '#'
	for file in sorted(listdir("Letters")):
		if ".png" in file:
			convert_to_matrix(file, empty, filled)


# Call Main Function
if __name__ == '__main__':
	main()