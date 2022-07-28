def rev_str(s):
    if len(s) == 1:
        return s
    return rev_str(s[int(len(s)/2):]) + rev_str(s[:int(len(s)/2)])

if __name__ == "__main__":
    print(rev_str("Hello"))