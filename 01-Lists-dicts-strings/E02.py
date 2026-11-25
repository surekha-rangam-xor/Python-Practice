def clean_name(raw):
    for name in raw:
        cleaned=" ".join(name.split()).title()
        words=cleaned.split(" ")
        intials=".".join(word[0] for word in words)+"."
        print(f"{cleaned!r} -> {intials}")
    
    
        

clean_name( ["  aNNa   maRIA  smith ", "o'brien   john", "MARY-JANE watson", "li   wei"])


