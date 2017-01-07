#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    size = len(dir(hidden_4))
    for a in range(0, size):
        if dir(hidden_4)[a][0:2] != "__":
            print(dir(hidden_4)[a])
#    for a in dir(hidden_4):
#        if dir(hidden_4)[a][0:2] != "__":
#            print(dir(hidden_4)[a])
