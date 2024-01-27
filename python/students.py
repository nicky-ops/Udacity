names =  input("Enter names seperated by commas: ").split(',')
assignments =  input("Enter the number of assignments seperated by commas: ").split(',')
grades =  input("Enter grades seperated by commas: ").split(',')

## message string to be used for each student
## HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

## write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name in names:
	for assignment in assignments:
		for grade in grades:
			print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
