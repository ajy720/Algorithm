h, m = map(int, input().split())

tot = h*60+m-45

if tot<0:
    tot=tot+1440

print(tot//60, tot%60)