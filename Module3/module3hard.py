def calculate_structure_sum(element):
    s = 0
    for i in element:
        if isinstance(i, list):
            s += sum(i)
        elif isinstance(i, dict):
            a = sum(i.values())
            b = len(i.keys())
            s += a + b
        elif isinstance(i, tuple):
            for k in i:
                if isinstance(k, int):
                    s += k
                elif isinstance(k, dict):
                    a = sum(k.values())
                    b = 0
                    for j in k.keys():
                        b += len(j)
                    s += a + b
                elif isinstance(k, list):
                    for j in k:
                        if isinstance(j, set):
                            for v in j:
                                if isinstance(v, tuple):
                                    for m in v:
                                        if isinstance(m, int):
                                            s += m
                                        elif isinstance(m, str):
                                            s += len(m)
                                        elif isinstance(m, tuple):
                                            for u in m:
                                                if isinstance(u, str):
                                                    s += len(u)
                                                elif isinstance(u, int):
                                                    s += u
        elif isinstance(i, str):
            s += len(i)
    return s


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
