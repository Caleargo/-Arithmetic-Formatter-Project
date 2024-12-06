def arithmetic_arranger(problems, show_answers=False):
    

    # Validation Process
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for problem in problems:
        parts = problem.split()
        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not parts[0].isdigit() or not parts[2].isdigit():
            return 'Error: Numbers must only contain digits.'
    
    # Parse the problems
    parsed_problems = []
    for problem in problems:
        parts = problem.split()
        operand1 = parts[0]
        operator = parts[1]
        operand2 = parts[2]
        width = max(len(operand1), len(operand2)) + 2

        parsed_problems.append((operand1, operator, operand2, width))

    #Declare the lines in the code

    first_line = ""
    second_line = ""
    third_line = ""
    answer_line = ""

    #Build each part for the Output

    for idx, (operand1, operator, operand2, width) in enumerate(parsed_problems):

        if idx > 0:
            first_line += "    "
            second_line += "    "
            third_line += "    "
            answer_line += "    "
        
        #Format each part
        first_line += operand1.rjust(width)
        second_line += operator + " " + operand2.rjust(width - 2)
        third_line += "-" * width

        #Calculate all lines

        if show_answers:
            if operator == "+":
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            answer_line += answer.rjust(width)

        #Concatenate all lines
        if show_answers:
            arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + answer_line
        else:
            arranged_problems = first_line + "\n" + second_line + "\n" + third_line
        
    return arranged_problems

# Example calls to the function 
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))