


echo "Enter countries (one per line, end with Ctrl+D):"
countries=()
 while read country
 do
   countries+=("$country")
 done

concatenated="${countries[@]} ${countries[@]} ${countries[@]}"
echo "Concatenated array with three repetitions:"
echo $concatenated
