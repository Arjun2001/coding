def suseq(arr, index, subs):
    if index == len(arr):
        if len(subs) == 0:
            return
        print(subs)
    else:
        suseq(arr, index+1, subs+[arr[index]])
        suseq(arr, index+1, subs)

a = [1,2,3]
suseq(a,0,[])
