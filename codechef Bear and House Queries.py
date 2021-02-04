def xaxis(st, en, h):
    while st <= en:
        mid = st + (en-st)//2
        print('?',mid,h,flush=True)
        ans = input()
        if ans == 'YES':
            result = mid
            st = mid + 1
        else:
            en = mid - 1
    return result

def yaxis (st, en):
    while st <= en:
        mid = st + (en-st)//2
        print('?','0',mid,flush=True)
        ans = input()
        if ans == 'YES':
            result = mid
            st = mid + 1
        else:
            en = mid - 1
    return result
L = xaxis(0, 1000, 0)
L *= 2
Y = xaxis(0, 1000, L)
Y *= 2
T = yaxis(L, 1000)
final = (L*L)+(Y*(T-L)//2)
print('!',final)
