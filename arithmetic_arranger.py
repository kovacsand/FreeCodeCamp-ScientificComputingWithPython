import regex

def arithmetic_arranger(problems, show = False):
  arranged_problems = ''
  
  if (len(problems) > 5):
        return 'Error: Too many problems.'
  
  seperatedList = []
  for problem in problems:
      seperatedList.append(problem.split())

  #SITUATIONS THAT SHOULD RETURN AN ERROR
  for problem in seperatedList:
      if (problem[1] != '+' and problem[1] != '-'):
          return 'Error: Operator must be \'+\' or \'-\'.'
      if not (regex.match('^[0-9]*$', problem[0] + problem[2])):
          return 'Error: Numbers must only contain digits.'
      if (len(problem[0]) > 4 or len(problem[2]) > 4):
          return 'Error: Numbers cannot be more than four digits.'


  #DETERMINING LENGTH OF DASH OF LINES
  lengths = []
  for problem in seperatedList:
      lengths.append(len(max(problem, key = len)) + 2)

  #SOLVING THE PROBLEMS
  solutions = []
  for problem in seperatedList:
      if (problem[1] == '+'):
          solutions.append(int(problem[0]) + int(problem[2]))
      else:
          solutions.append(int(problem[0]) - int(problem[2]))      
    
  #PRINT FIRST LINE
  for i in range(len(seperatedList)):
      for j in range(lengths[i] - len(seperatedList[i][0])):
          arranged_problems += (' ')
      arranged_problems += (seperatedList[i][0])
      if (i < len(seperatedList) - 1):
          arranged_problems += ('    ')
  arranged_problems += ('\n')


  #PRINT SECOND LINE
  for i in range(len(seperatedList)):
      arranged_problems += (seperatedList[i][1])
      for j in range(lengths[i] - 1 - len(seperatedList[i][2])):
        arranged_problems += (' ')
      arranged_problems += (seperatedList[i][2])
      if (i < len(seperatedList) - 1):
          arranged_problems += ('    ')
  arranged_problems += ('\n')


  #PRINT THIRD LINE
  for i in range(len(seperatedList)):
    for j in range(lengths[i]):
      arranged_problems += ('-')
    if (i < len(seperatedList) - 1):
          arranged_problems += ('    ')


  #PRINT FOURTH LINE
  if (show):
      arranged_problems += ('\n')
      for i in range (len(solutions)):
          for j in range(lengths[i] - len(str(solutions[i]))):
              arranged_problems += (' ')
          arranged_problems += (str(solutions[i]))
          if (i < len(solutions) - 1):
              arranged_problems += ('    ')
            
  print(arranged_problems)
  return arranged_problems