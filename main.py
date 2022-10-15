def str_count(strng, letter):
    # Your code here ;
    if len(letter) >= 1:
        a = strng.count(letter)
    return a

print(str_count("Hello", "o"))