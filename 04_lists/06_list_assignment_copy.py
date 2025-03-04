"""
List assignment and list copy
- There is one list in the memory and two pointers to it
- If you really want to make a copy th pythonic way is to use the slice syntax
- It creates a shallow copy.
"""


def main():
    x = ['apple', 'bob', 'cat', 'drone']
    y = x
    x[0] = 'qqrq'
    print(x)            # ['qqrq', 'bob', 'cat', 'drone']
    print(y)            # ['qqrq', 'bob', 'cat', 'drone']
    print(id(x))        # 2217735008960
    print(id(y))        # 2217735008960

if __name__ == '__main__':
    main()
