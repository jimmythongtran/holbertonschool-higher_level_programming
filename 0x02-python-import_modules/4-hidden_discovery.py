#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    size = len(dir(hidden_4))
    for a in range(0, size):
        if dir(hidden_4)[a][0:2] != "__":
            print(dir(hidden_4)[a])
