
echo "A: "
read A
echo "B: "
read B

if((A > B)); then
	echo "Error"
fi

for((i = A; i <= B; i++)); do
	if((i%2 != 0)); then
		echo $i
	fi
done