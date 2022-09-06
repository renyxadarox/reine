p = "HereLiesJohnRenie"
t = """
eineRnhoJsJohnRenie
ineRnhoJsesJohnReni
neRnhoJseiesJohnRen
eRnhoJseiLiesJohnRe
RnhoJseiLeLiesJohnR
nhoJseiLereLiesJohn
hoJseiLerereLiesJoh
oJseiLereHereLiesJo
hoJseiLerereLiesJoh
nhoJseiLereLiesJohn
RnhoJseiLeLiesJohnR
eRnhoJseiLiesJohnRe
neRnhoJseiesJohnRen
ineRnhoJsesJohnReni
eineRnhoJsJohnRenie
"""

m = [[*w] for w in [s for s in t.split('\n')][1:-1]]
s = 0


def calc_renie(r, c, l, w):
    global s
    if l == len(p):
        s += 1
        print(s, ":", w)
    else:
        if c > 0 and m[r][c-1] == p[l]:
            calc_renie(r, c - 1, l + 1, w + "←")
        if r > 0 and m[r-1][c] == p[l]:
            calc_renie(r - 1, c, l + 1, w + "↑")
        if c < len(m[r])-1 and m[r][c + 1] == p[l]:
            calc_renie(r, c + 1, l + 1, w + "→")
        if r < len(m)-1 and m[r + 1][c] == p[l]:
            calc_renie(r + 1, c, l + 1, w + "↓")


calc_renie(7, 9, 1, "")
print(f"{s=}")
