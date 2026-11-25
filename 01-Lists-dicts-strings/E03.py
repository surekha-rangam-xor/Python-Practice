def mask_card(number):
    number = str(number)
    return "*" * (len(number) - 4) + number[-4:]
 
 
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(words[::-1])
 
 
def middle(text):
    n = len(text)
    start = (n - 1) // 2
    end = n // 2 + 1
    return text[start:end]
 
 
def every_other(text):
    return text[::2]
 
 
# Driver code
print(mask_card("4111111111111111"))
 
print(reverse_words("learning python is fun"))
 
print(middle("python"), middle("slicing"))
 
print(every_other("abcdefghij"))
 
print("Programming"[::-1])