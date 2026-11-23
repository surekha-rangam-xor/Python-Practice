from pathlib import Path
 
 
def parse_readings(lines):
    values = []
    bad = []
 
    for line_number, line in enumerate(lines, start=1):
        text = line.strip()
 
        try:
            number = float(text)
            values.append(number)
 
        except ValueError:
            bad.append((line_number, text))
 
    return values, bad
 
 
path = Path("D:\\My_Space\\Python-Practice\\04-Exception-Handling\\data\\readings.txt")
 
lines = path.read_text(encoding="utf-8").splitlines()
 
values, bad = parse_readings(lines)
 
print("Lines:", len(lines))
print("Valid:", len(values))
 
print("Invalid lines:", [line_number for line_number, text in bad])
 
for line_number, text in bad:
    print(f"  line {line_number}: {text!r}")
 
if values:
    average = sum(values) / len(values)
 
    print(f"Average: {average:.2f}")
    print(f"Min: {min(values)}  Max: {max(values)}")
else:
    print("No valid readings found.")