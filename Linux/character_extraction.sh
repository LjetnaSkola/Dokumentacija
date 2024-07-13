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
