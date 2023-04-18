# Initialize your list and read in the value of "n" followed by "n" lines of commands where
# each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    n = int(input())
    l = []
    for _ in range(n):
        s = input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)
