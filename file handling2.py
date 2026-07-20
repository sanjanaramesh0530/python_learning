with open("name.txt","w+")as f:
    f.write("mango,orange,apple,fig,strawberry")
    f.seek(0)
    print(f.read())
