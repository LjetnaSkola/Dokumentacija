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
