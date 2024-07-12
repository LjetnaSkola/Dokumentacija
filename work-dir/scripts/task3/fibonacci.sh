
echo "N: "
read N

i=0
j=1

if (( N <= 3 )); then
    echo "Error. N <= 3."
else
    echo "Fibonacci sequence up to $N numbers:"
    
    echo -n "$i "
    echo -n "$j "
    
    for (( k=2; k<N; k++ )); do
        fn=$((i + j))
        echo -n "$fn "
        i=$j
        j=$fn
    done
    
    echo   
fi
