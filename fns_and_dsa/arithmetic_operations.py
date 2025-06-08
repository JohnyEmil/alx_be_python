def perform_operation(num1, num2, operation):
  num1 = float(num1)
  num2 = float(num2)
  operation = str(operation)
  match operation:
    case "add":
      return num1+num2
    case "subtract":
      return num1-num2
    case 'multiply':
      return num1*num2
    case 'divide':
      if num2 == 0 :
        return "division by zero not allowed"
      else:
        return num1/num2
    case _:
        raise ValueError(f"Invalid operation: {operation}")
  
  
    

