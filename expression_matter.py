def expression_matter(a, b, c):
    # highest achievable result
    return max((a+b) *c, a*(b+c),a*b*c,a+b*c,a+b+c)

print(expression_matter(1,2,3))