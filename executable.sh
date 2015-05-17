
python script.py
for file in /Users/UMBC/MedicalJournals/PDFs/*.pdf
do
 # do something on "$file"
 #cat "$file" >> /var/www/cdn.example.com/cache/large.css
 newfile=${file:32}
 path=/Users/UMBC/MedicalJournals/Texts/
 extension=.txt
 outfile=$path$newfile$extension
 echo $outfile
 python pdf2txt.py "$file" >> $outfile
done