#ifndef LISTA_H
#define LISTA_H

typedef struct cvor
{
    int podatak;
    struct cvor *sljedeci;
} CVOR;

CVOR* dodaj_pocetak(CVOR **pglava, int podatak);
CVOR* dodaj_kraj(CVOR **pglava, int podatak);
CVOR* dodaj_iza(CVOR *cvor, int podatak);
CVOR* dodaj_ispred(CVOR *cvor, int podatak);

CVOR* trazi(CVOR *glava, int podatak);

int brisi_iza(CVOR *cvor);
int brisi(CVOR *cvor);
void brisi_listu(CVOR **pglava);

void pisi(CVOR *glava);

#endif
