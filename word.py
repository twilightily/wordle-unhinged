import random
l=['bark','meow','disk', 'lost', 'word', 'poem', 'fact', 'girl', 'town', 'love', 'dirt', 'rant', 'news', 'bird', 'army', 'milk','lily', 'node', 'shot', 'heat', 'race', 'debt', 'fade', 'bean', 'meal', 'pour', 'fire', 'hang', 'cage', 'take', 'pack', 'wake', 'trip', 'half', 'crop', 'pace', 'rung', 'dorm', 'grow', 'tidy','plot']
n=random.randint(0,len(l))
t=4
w=l[n]
found='f'
lw=list(w)
while t>=0:
    wro=0
    rig=[]
    x=input("guess!:")
    if len(x)!=4:
        print("letter can only be 4 letters,you will lose a chance")
    lx=list(x)
    if x==w:
        print("you guessed it!")
        found='t'
        break
    else:
        for i in lx:
            if i in lw:
                if lx.index(i)==lw.index(i) and i not in l:
                    rig.append(i)
                else:
                    wro+=1
        print("right letter wrong place:",wro)
        print("right letter right place:",rig)
        print("you have {} chances left".format(t))
        t-=1
if found=='f':
    print("the word was:",w)


