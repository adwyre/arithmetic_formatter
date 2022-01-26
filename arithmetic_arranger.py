def arithmetic_arranger(problems,answers=False):
  #check number of problems
  if len(problems) >5:
    return("Error: Too many problems.")
    exit()
  line1=""
  line2=""
  line3=""
  line4=""
  digits= ['0','1','2','3','4','5','6','7','8','9']

  for problem in problems:
    #parse text
    problemPieces = problem.split()
    num1 = problemPieces[0]
    operator1 = problemPieces[1]
    num2 = problemPieces[2]

    def checkDigits(number):
      for i in number:
        if i not in digits:
          return False
      return True

    #check operators
    if (operator1 == '-' or operator1 == '+'):
      #check if only digits   
      if (checkDigits(num1) == False or checkDigits(num2) == False):
        print(checkDigits(num1), checkDigits(num2))
        return ("Error: Numbers must only contain digits.")
        #check number of digits
      if (len(num1) > 4 or len(num2) > 4):
        return("Error: Numbers cannot be more than four digits.")
        exit()
      #format problems
      maxLength = max(len(num1), len(num2))
      totLength = maxLength+2
      #1
      line1 += (((totLength-len(num1))*' ') + num1 + '    ')
      
      #2
      line2 += (operator1 + ((maxLength-len(num2)+1)*' ') + num2 + '    ')
      
      #3
      line3+= ((totLength * '-') + '    ')

      #4
      if operator1 == '+':
        num3= str(int(num1) + int(num2))
      else:
        num3= str(int(num1) - int(num2))
      line4+= (((totLength-len(num3))*' ') + num3 + '    ')
      
    else:
      return("Error: Operator must be '+' or '-'.")
      exit()
  
  #final lines
  arranged_problems = line1.rstrip() + '\n' + line2.rstrip() + '\n' + line3.rstrip()

  #print answers
  if answers:
    arranged_problems += '\n' + line4.rstrip()

  return arranged_problems