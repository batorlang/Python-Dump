def compress(str1):
    unique=[]
    uniquecount=[]
    compressed=""

    for i in str1:
        if i not in unique:
            unique.append(i)

    for i in range(len(unique)):
        count = 0
        for j in str1:
            if j == unique[i]:
                count += 1
        uniquecount.append(count)

    for i in range(len(uniquecount)):
        if uniquecount[i] > 1:
            compressed += unique[i] + str(uniquecount[i])
        else:
            compressed += unique[i]
    

    return compressed
    

str1 = input("Give a string to compress:\n")
compressedd = compress(str1)
originalstrnr = len(str1)
compressedstrnr = len(compress(str1))
ratio = compressedstrnr / originalstrnr
print(f"Compressed string: {compressedd}")
print(f"Compressing ratio {round(ratio, 2)}")
