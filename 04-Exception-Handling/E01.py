def divide_line(line):
 
    parts = line.split()
 
    try:
        if len(parts) != 2:
            raise ValueError
 
        a = float(parts[0])
        b = float(parts[1])
 
        result = a / b
 
    except ZeroDivisionError:
        return "Cannot divide by zero"
 
    except ValueError:
        return "Invalid input: expected two numbers"
 
    else:
        return f"{a:g} / {b:g} = {result:g}"
 
 
inputs = []
 
print("Enter inputs (press Enter on an empty line to finish):")
 
while True:
    line = input()
 
    if not line.strip():
        break
 
    inputs.append(line)
 
 
print("\nOutputs:")
 
for line in inputs:
    print(divide_line(line))