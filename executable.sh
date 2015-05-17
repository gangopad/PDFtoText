
python script.py
counter=0
for file in /Users/gangopad/DownloadJournals/PDFs/*.pdf
do
 # do something on "$file"
 #cat "$file" >> /var/www/cdn.example.com/cache/large.css
 newfile=${file:32}
 #path=/Users/UMBC/MedicalJournals/Texts/
 path=/Users/gangopad/DownloadJournals/Texts
 extension=.txt
 #outfile=$path$newfile$extension
 outfile=file$counter$extension
 echo $outfile
 python pdf2txt.py "$file" >> $outfile
 counter=$((counter+1))
done