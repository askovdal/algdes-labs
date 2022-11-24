echo '' > results.txt
echo "file\tA\tF\tM\tN\tS" >> results.txt
for file in data/*
do
  echo "$file"
  echo -n "$file\t" >> out.txt
  python main.py < "$file" >> results.txt
done