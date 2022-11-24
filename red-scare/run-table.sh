declare -a arr=("data/rusty-1-5757.txt" "data/wall-p-10000.txt" "data/common-2-5757.txt" "data/gnm-5000-7500-1.txt" "data/grid-50-2.txt" "data/increase-n500-3.txt" "data/ski-level5-3.txt" "data/smallworld-50-1.txt" "data/wall-n-10000.txt" "data/wall-z-10000.txt")
for file in "${arr[@]}"
do
  echo "$file"
  python main.py < "$file"
done