def arithmetic_arranger(problems, show_answers=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  formatted_problems = []

  for problem in problems:
      parts = problem.split()
      if parts[1] != "+" and parts[1] != "-":
        return "Error: Operator must be '+' or '-'."
      operand1, operator, operand2 = parts
      if not operand1.isdigit() or not operand2.isdigit():
          return "Error: Numbers must only contain digits."
      if len(operand1) > 4 or len(operand2) > 4:
          return "Error: Numbers cannot be more than four digits."
      max_length = max(len(operand1), len(operand2))
      top_line = operand1.rjust(max_length + 2)
      bottom_line = operator + operand2.rjust(max_length + 1)
      dash_line = "-" * (max_length + 2)

      formatted_problem = [top_line, bottom_line, dash_line]

      if show_answers:
          answer = str(eval(problem)).rjust(max_length + 2)
          formatted_problem.append(answer)
      formatted_problems.append(formatted_problem)
  arranged_problems = ["    ".join(parts) for parts in zip(*formatted_problems)]

  return "\n".join(arranged_problems)


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problems_with_answers = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

print(arithmetic_arranger(problems))
print(arithmetic_arranger(problems_with_answers, True))
