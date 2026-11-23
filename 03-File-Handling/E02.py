from pathlib import Path
 
def write_squares(path, n):
    path = Path(path)
 
    path.parent.mkdir(parents=True, exist_ok=True)
 
    with open(path, "w", encoding="utf-8") as f:
        for i in range(1, n + 1):
            f.write(f"{i} squared is {i * i}\n")
 
    return n
 
 
file_path = Path("03-File-Handling/output/squares.txt")
 
count = write_squares(file_path, 8)
 
print(f"Lines written: {count}")
 
content = file_path.read_text(encoding="utf-8")
 
print(content, end="")