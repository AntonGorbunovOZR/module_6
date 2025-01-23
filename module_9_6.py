def all_variants(text):
    l = len(text)
    for i in range(l):
        yield text[i]

    for i in range(2, l + 1):
        for n in range(l - i + 1):
            k = n + i
            yield text[n:k]

a = all_variants("abc")
for k in a:
    print(k)