	# Prompt the user to enter values of A and B
	echo "Enter the starting number (A):"
	read A

	echo "Enter the ending number (B):"
	read B

	# Loop through the numbers from A to B
	for (( num=A; num<=B; num++ )); do
		if (( num % 2 != 0 )); then
			echo $num
		fi
	done