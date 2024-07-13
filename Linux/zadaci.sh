1. Write a Bash script which accepts (name) as input and displays the greeting "Welcome (name)"

	echo "Enter name (name) :" 
	read name

	echo "Greeting message :"
	echo "Welcome $name"


2. Your task is to use for loops to display only odd natural numbers from A to B.

	echo "Enter variable A (A) :"
	read A
	echo "Enter variable B (B) :"
	read B
	
    echo "Odd numbers from $A to $B are:"
    for (( i=A; i<=B; i++ ))
    do
      if (( i % 2 != 0 ))
      then
        echo $i
      fi
    done	


3. Write a shell script that accepts a number greater than 3, lets say N. The script prints the Fibonacci sequence with N numbers in the sequence.

    echo "Enter a number greater than 3 (N) :"
    read N
    
    if [ $N -lt 4 ]; then
        echo "Number must be greater than 3!"
        exit 1
    fi
    
    function fibonacci {
    
        local num=$1
        a=0
        b=1
    
        echo "Fibonacci array of $num numbers:"
        
        for (( i=0; i<num; i++ ))
        do
            echo -n "$a "
            fn=$((a + b))
            a=$b
            b=$fn
        done
        echo
    }

    fibonacci $N


4. Write a shell script that accepts a non-negative number and shows its factorial as output.

    echo "Enter a non-negative number (N) :"
    read N
    
    if [ $N -lt 0 ]; then
        echo "Number must be equal or greater than 0"
        exit 1
    fi
    
    function factorial {
    
        local num=$1
        local result=1
        
        while([ $num -gt 1 ]); do
            
            result=$((result * num))
            ((num--))
        done
        
        echo "$N! = $result"
    } 
    
    factorial $N


5. Given M lines of input, print the Nth character from each line as a new line of output. It is guaranteed that each of the M lines of input will have a Nth character.

    echo "Enter number of input lines (M) :"
    read M
    
    array=()
    
    while [ $M -gt 0 ]; do
        echo "Unesite element : "
        read element
        array+=("$element")
        ((M--))
    done
    
    echo "Printing array elements : "
    for element in "${array[@]}"
    do
        echo "$element"
    done
    
    echo "Enter number (N) :"
    read N
    
    function character_extraction {
        local line=$1
        echo "${line:N-1:1}"
    }
    
    echo "Printing Nth elemnt of each array element : "
    for element in "${array[@]}"
    do
        character_extraction "$element"
    done
    
    
6. Display the first 5 lines of an input file.

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

    # First 5 lines of file
    echo "First 5 lines of file '$datoteka':"
    head -n 5 "$datoteka"


7. Print file in reverse order

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
    
    tac "$datoteka"


8. Display the last 4 characters of an input file.

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
    
    tail -c 4 "$datoteka"
    
    
9. Given a list of countries, each on a new line, your task is to read them into an array. Then, concatenate the array with itself (twice) - so that you have a total of three repetitions of the original array - and then display the entire concatenated array, with a space between each of the countries names.
Input:
Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
NorthKorea
Norway
OUTPUT:
Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway

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

10. Given a text file, which will be piped to your command through STDIN, use grep to display all those lines which contain any of the following words in them:
the
that
then
those
The search should not be sensitive to case. Display only those lines of an input file, which contain the required words

    grep -i -e 'the' -e 'that' -e 'then' -e 'those'

