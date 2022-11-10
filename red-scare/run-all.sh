echo '' > out.txt
for file in data/*
do
  echo "$file"
  echo "$file" >> out.txt
  python main.py < "$file" >> out.txt
done