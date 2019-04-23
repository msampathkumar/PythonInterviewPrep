def merge_data(data):
    ret = [data[0]]
    for set1 in data[1:]:
        for i in range(len(ret)):
            if set1.intersection(ret[i]):
                ret[i] = set1.union(ret[i])
    return ret



def main(countries, data):
    data = [(max(_), min(_)) for _ in data]
    data.sort()
    left_countries = set(range(countries))
    #


if __name__ == '__main__':
    # main(counries=5, data=[[2, 3]])
    main(counries=5, data=[[0, 1], [0, 4]])
