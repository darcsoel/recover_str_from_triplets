def recover_secret(triplets):
    recovered = [i for l in triplets for i in l]
    unique = []

    for char in recovered:
        if char not in unique:
            unique.append(char)

    for _ in range(2):
        for list_ in triplets:
            if unique.index(list_[1]) > unique.index(list_[2]):
                unique.remove(list_[1])
                unique.insert(unique.index(list_[2]), list_[1])
            if unique.index(list_[0]) > unique.index(list_[1]):
                unique.remove(list_[0])
                unique.insert(unique.index(list_[1]), list_[0])

    return "".join(unique)
