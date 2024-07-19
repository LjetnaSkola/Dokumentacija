
# Napraviti closure funkciju koja za različit ulazni argument 
# kreira funkciju za izračunavanja površina, kruga, kvadrata i 
# pravougaonika. 

def func_povrsina (geom_oblik):
    if (geom_oblik == 'krug'):
        def izracunaj (r):
            return r*r*3.14
        return izracunaj
    else:
        if(geom_oblik == 'kvadrat'):
            def izracunaj(a):
                return a*a
            return izracunaj
        else:
            if(geom_oblik == 'pravougaonik'):
                def izracunaj(a,b):
                    return a*b
                return izracunaj
     
povrsina_kruga = func_povrsina('krug')
povrsina_kvadrata = func_povrsina('kvadrat')
povrsina_pravougaonika = func_povrsina('pravougaonik')

print("Površina kruga sa poluprecnikom 5:", povrsina_kruga(5))
print("Površina kvadrata sa a = 4:", povrsina_kvadrata(4))
print("Površina pravougaonika sa stranicama 3 i 6:", povrsina_pravougaonika(3, 6))
    
