def compress(str1):
    compressed = ""
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed += str1[i - 1] + str(count)
            else:
                compressed += str1[i - 1]
            count = 1
    if count > 1:
        compressed += str1[-1] + str(count)
    else:
        compressed += str1[-1]
    return compressed


str1 = str(input("Give a string to compress:\n"))
comp = compress(str1)
original_lenght = len(str1)
compressed_lengeth = len(comp)
ratio = round(compressed_lengeth / original_lenght, 2)
print(f"Compressed string: {comp}")
print(f"Compressing ratio {ratio}")

