def scale(w=200,h=200):
    rev=False
    if h>w:
       w,h=reversed((w,h))
       rev=True
    W,H=round(min(200,w)),round(min(200,w)*(h/w))
    if rev:
      W,H=reversed((W,H))

    return W,H

if __name__ == "__main__":
    w,h=[int(x) for x in input('res: ').split(',')]
    print(scale(w,h))


