def foo(list_in):
    list_out = []
    for t in list_in:
        s = t[0]
        m = t[0]
        idx = 0
        n = 0
        for k in t[1:]:
            n += 1
            s += k
            if k > m:
                m = k
                idx = n
        list_out.append((s, m, idx))
    return list_out
