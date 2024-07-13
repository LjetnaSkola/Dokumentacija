    # Provjeravanje broja argumenata
    # -ne (not equal)
    # $# is special variable in Bash which stores a number of arguments
    if [ "$#" -ne 1 ]; then         # if number of args is not 1
        echo "Upotreba: $0 <naziv_datoteke>"
        exit 1
    fi

    # Prihvatanje naziva datoteke kao argumenta
    datoteka=$1

    # Provjeravanje da li datoteka postoji
    if [ ! -f "$datoteka" ]; then
        echo "Datoteka '$datoteka' ne postoji."
        exit 1
    fi

    # Ispis prvih 5 linija datoteke
    echo "Prvih 5 linija iz datoteke '$datoteka':"
    head -n 5 "$datoteka"
