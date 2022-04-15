
cd logs
for i in $(seq 1 13); do 
diff $i.log $((i +1)).log; 
done
