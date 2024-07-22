

echo "Enter a non-negative number N: "
read N

if (( N < 0 )); then
    echo "Error. N < 0."
else
factorial=1

for (( i=1; i<=N; i++ ))
do
    factorial=$((factorial * i))
done

echo "Factorial of $N is: $factorial."
fi
