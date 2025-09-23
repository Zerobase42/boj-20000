import hashlib as h

def check_one(i):
    answer=open(f"C:\\Users\\jwoo\\Desktop\\BOJ 20000\\challenge\\challenge{i}.out",'r').read().rstrip()
    mine=open("test.txt",'r').read()

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
        print()
        print(cnt)

check_one(3)