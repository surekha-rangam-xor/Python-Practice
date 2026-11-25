from pathlib import Path
 
 
def append_entry(path, text):
    with open(path, "a", encoding="utf-8") as file:
        file.write(text + "\n")
 
 
def count_lines(path):
    path = Path(path)
 
    if not path.exists():
        return 0
 
    with open(path, "r", encoding="utf-8") as file:
        return sum(1 for line in file)
 
 
path = Path("output/journal.txt")
 
if path.exists():
    path.unlink()
 
print("Lines before:", count_lines(path))
 
entries = [
    "Started the course",
    "Finished file exercises",
    "Reviewed CSV handling"
]
 
for entry in entries:
    append_entry(path, entry)
 
print("Lines after first run:", count_lines(path))
 
append_entry(path, "Added one more entry")
 
print("Lines after append:", count_lines(path))
 
with open(path, "r", encoding="utf-8") as file:
    print(file.read(), end="")