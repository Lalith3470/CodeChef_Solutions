for _ in range(int(input())):
    n=int(input())
    st=input()
    st1=input()
    cnt1=st.count("1")
    cnt2=st1.count("1")
    if cnt1==cnt2:
        print("YES")
    else:
        print("NO")
