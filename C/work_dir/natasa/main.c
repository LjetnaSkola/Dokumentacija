#include "lista.h"
#include <stdio.h>

int main()
{
    CVOR *glava = 0;
    int br;
    
    //dodavanje elemenata
    CVOR *c1 = dodaj_pocetak(&glava, 1), *c2 = dodaj_pocetak(&glava, 2), *c3 = dodaj_kraj(&glava, 3), *c4 = dodaj_iza(c1, 4), *c5 = dodaj_ispred(c1, 5);
    printf("Sadrzaj liste:");
    pisi(glava);
    printf("\n");
    
    //pretrazivanje
    printf("Unesite broj: ");
    scanf("%d", &br);
    printf("Broj %d %spostoji u listi.\n", br, trazi(glava, br) ? "" : "ne ");
    
    //brisanje elemenata
    brisi(c4);
    brisi_iza(c5);
    printf("Sadrzaj liste (nakon brisanja):");
    pisi(glava);
    printf("\n");
    
    //brisanje liste
    brisi_listu(&glava); 
    printf("Sadrzaj liste (prazna):"); 
    pisi(glava); 
    printf("\n");
    
    return 0;
}
