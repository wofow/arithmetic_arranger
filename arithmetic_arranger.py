def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dashes = ""
    answer_line = ""

    for problem in problems:
        operands, operator = parse_problem(problem)

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not operands[0].isdigit() or not operands[1].isdigit():
            return "Error: Numbers must only contain digits."

        if len(operands[0]) > 4 or len(operands[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(operands[0]), len(operands[1])) + 2
        first_line += f"{operands[0]:>{width}}    "
        second_line += f"{operator} {operands[1]:>{width - 2}}    "
        dashes += '-' * width + "    "

        if show_answers:
            answer = eval(problem)
            answer_line += f"{answer:>{width}}    "

    arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}"

    if show_answers:
        arranged_problems += f"\n{answer_line.rstrip()}"

    return arranged_problems


def parse_problem(problem):
    problem = problem.split()
    operands = [problem[0], problem[2]]
    operator = problem[1]
    return operands, operator
