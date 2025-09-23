import hashlib as h

def check_one(i):
    answer=open(f"challenge/challenge{i}.out",'r').read().rstrip()
    try:
        mine=open(f"output/20000_out{i}.txt").read().rstrip()
    except:
        print(f"{i}.txt is don't open because it don't have.\n{h.sha256(answer.encode()).hexdigest()}\n")
        return

    print("mine: ",h.sha256(mine.encode()).hexdigest())
    print("answ: ",h.sha256(answer.encode()).hexdigest())
    print(f"len mine:{len(mine)}\n len answ:{len(answer)}")
    
    if answer==mine:
        print("correct!!")
        return
    else:
        print("incorrect.")
        answer_enter=answer.split('\n')
        mine_enter=mine.split('\n')
        cnt=0
        for a,b in zip(answer,mine):
            if a!=b:
                print(cnt, a, b)
            cnt+=1

def check_all():
    for i in range(10):
        check_one(i)

n=input()
if n.isdigit():
    check_one(int(n))
else:
    check_all()