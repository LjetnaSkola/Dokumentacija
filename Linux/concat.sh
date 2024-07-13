    # Checks the number of arguments
    # -ne (not equal)
    # $# is special variable in Bash which stores a number of arguments
    if [ "$#" -ne 1 ]; then         # if number of args is not 1
        echo "Usage: $0 <naziv_datoteke>"
        exit 1
    fi

    # File name as an argument
    datoteka=$1

    # Checks the existance of the file
    if [ ! -f "$datoteka" ]; then
        echo "File '$datoteka' doesnt exist."
        exit 1
    fi

    countries=()

    echo "Sadržaj datoteke '$datoteka':"
    while IFS= read -r country
    do
        countries+=("$country")
    done < "$datoteka"
    
    concatenated_countries=("${countries[@]}" "${countries[@]}" "${countries[@]}")
    
    echo "${concatenated_countries[@]}"
