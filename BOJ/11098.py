for _ in ' '*int(input()):
    cost = 0
    name = ''
    for i in ' '*int(input()):
        mCost, mName = input().split()
        mCost = int(mCost)
        if cost < mCost:
            cost = mCost
            name = mName

    print(name)
