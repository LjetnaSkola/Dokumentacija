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
