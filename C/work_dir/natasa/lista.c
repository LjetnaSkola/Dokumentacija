#include "lista.h"
#include <stdio.h>
#include <stdlib.h>

CVOR* dodaj_pocetak(CVOR **pglava, int podatak)
{
    CVOR *novi = (CVOR *)malloc(sizeof(CVOR));
    novi->podatak = podatak;
    novi->sljedeci = *pglava;
    *pglava = novi;
    return novi;
}

CVOR* dodaj_kraj(CVOR **pglava, int podatak)
{
    CVOR *p, *novi = (CVOR *)malloc(sizeof(CVOR));
    novi->podatak = podatak;
    novi->sljedeci = 0;
    if (*pglava == 0)
		*pglava = novi;
    else
    {
        for (p = *pglava; p->sljedeci; p = p->sljedeci);
        p->sljedeci = novi;
    }
    return novi;
}

CVOR* dodaj_iza(CVOR *cvor, int podatak)
{
    CVOR *novi = (CVOR *)malloc(sizeof(CVOR));
    novi->podatak = podatak;

    novi->sljedeci = cvor->sljedeci;
    cvor->sljedeci = novi;

    return novi;
}

CVOR* dodaj_ispred(CVOR *cvor, int podatak)
{
    CVOR *novi = (CVOR *)malloc(sizeof(CVOR));

    novi->podatak = cvor->podatak;
    novi->sljedeci = cvor->sljedeci;

    cvor->podatak = podatak;
    cvor->sljedeci = novi;

    return cvor;
}

CVOR* trazi(CVOR *glava, int podatak)
{
    while (glava && glava->podatak != podatak)
        glava = glava->sljedeci;
    return glava;
}

int brisi_iza(CVOR *cvor)
{
    CVOR *p = cvor->sljedeci;
    if (p == 0)
        return 0;

    cvor->sljedeci = p->sljedeci;
    free(p);
    return 1;
}

int brisi(CVOR *cvor)
{
    CVOR *p = cvor->sljedeci;
    if (p == 0)
        return 0;

    cvor->podatak = p->podatak;
    cvor->sljedeci = p->sljedeci;
    free(p);
    return 1;
}

void brisi_listu(CVOR **pglava)
{
    while (*pglava)
    {
        CVOR *p = (*pglava)->sljedeci;
        free(*pglava);
        *pglava = p;
    }
}

void pisi(CVOR *glava)
{
    while (glava)
	{
        printf(" %d", glava->podatak);
        glava = glava->sljedeci;
    }
}