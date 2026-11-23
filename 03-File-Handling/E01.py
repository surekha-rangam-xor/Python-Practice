def file_stats(path):
 
    lines = 0
    words = 0
    characters = 0
    blank = 0
 
    with open(path, "r", encoding="utf-8") as f:
 
        for line in f:
            lines += 1
 
            content = line.rstrip("\r\n")
 
    
            words += len(content.split())
 
    
            characters += len(content)
 
    
            if content.strip() == "":
                blank += 1
 
    return {
        "lines": lines,
        "words": words,
        "characters": characters,
        "blank": blank
    }
 
 

path = "D:\\My_Space\\Python-Practice\\03\\notes.txt"

 

with open(path, "r", encoding="utf-8") as f:
 
    for line_number, line in enumerate(f, start=1):
 
        if line_number > 5:
            break
 
        print(f"{line_number:3}: {line.rstrip('\r\n')}")
 
 

result = file_stats(path)
 
print("Lines:", result["lines"])
print("Words:", result["words"])
print("Characters:", result["characters"])
print("Blank lines:", result["blank"])