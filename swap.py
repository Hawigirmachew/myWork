def swap_case(s):
    line=""
    for x in s:
        if x == x.upper():
           line+= x.lower()
        else:
            line+= x.upper()
    return line
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)