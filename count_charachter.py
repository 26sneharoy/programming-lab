def sentence(str):
    count={}

    for i in str:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    return count

print( sentence("grphsss"))