def ant(t):
    gs = ['']; i = 0
    for s in t:
        if s == '':
            i += 1
            gs.append('')
        else:
            gs[i] += s
    return gs
