
echo "Enter number of lines M:"
read M
echo "N is "
read N
while read line
do
    echo "${line:$N-1:1}"
done
