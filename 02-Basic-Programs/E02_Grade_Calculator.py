def grade(scores):
    l=[]
    for token in scores:
        if token.isdigit():
            score=int(token)
            if 0<= score <=100:
                l.append(score)
                if score >=90:
                    print(f"{score}:A")
                elif score>=80 and score<=89:
                    print(f"{score}:B")
                elif score>=70 and score<=79:
                    print(f"{score}:C")
                elif score>=60 and score<=69:
                    print(f"{score}:D")
                elif score<60:
                    print(f"{score}:F")
        else:
            print(f"{token}:Invalid")
    if l:
        print(f"Average of valid scores:{sum(l)/len(l):.1f}")
    else:
        print("No Valid Scores")



data=input("enter the scores separated by spaces:") 
scores=data.split()
grade(scores)