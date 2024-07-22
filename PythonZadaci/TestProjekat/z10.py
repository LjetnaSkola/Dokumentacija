def povrsina(tip: str):
    if(tip == "krug"):
        def pov_kr(r):
            return r*r*3.14
        return pov_kr 
        
    elif(tip == "kvadrat"):
        def pov_kv(a):
            return a*a
        return pov_kv

    elif(tip == "pravougaonik"):
        def pov_prav(a,b):
            return a*b
        return pov_prav


def main():
    tip = "krug"
    r = 1
    pov = povrsina(tip)
    print(f"P Kruga: {pov(r)}")
    
    tip = "kvadrat"
    a = 3
    pov = povrsina(tip)
    print(f"P Kvadrata: {pov(a)}")
    
    tip = "pravougaonik"
    a = 4
    b = 5
    pov = povrsina(tip)
    print(f"P pravougaonika: {pov(a, b)}")


if __name__ == "__main__":
    main()
