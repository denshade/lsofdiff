LINE=""
for file in $(ls logs/*.log);
do
     LINE="$LINE,$file"
done
echo $LINE
for line in $(cat logs/*.log | sort -u); do

 LINE="$line"
 for file in $(ls logs/*.log); 
 do
	
	LINE="${LINE},$(cat $file | grep $line| wc -l)"
 done
 echo $LINE
done
