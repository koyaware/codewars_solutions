def same_case(a, b):
    # your code here
    if not str(a).isalpha() or not str(b).isalpha():
        return -1
    elif a.isupper() and b.isupper():
        return 1
    elif a.islower() and b.islower():
        return 1
    return 0

print(same_case("a","g"))