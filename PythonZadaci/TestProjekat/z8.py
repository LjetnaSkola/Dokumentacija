def foo(string, delim):
    substrs = string.split(delim)
    return substrs
def main():
    s1 = "ovo.je.test"
    print(f"{foo(s1,'.')}")
    
if __name__ == "__main__":
    main()
