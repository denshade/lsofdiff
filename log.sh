if [ "$#" -ne 1 ]; then
       echo "Usage $0 <pid>"
       exit 1
fi
i=0
while true; do

	lsof -p $1 | rev| cut -d' ' -f1 | rev > logs/$i.log 2> /dev/null      #`date +%y-%m-%d-%H:%M:%S:%N` 2> /dev/null
	sleep 0.5
	echo "."
	let "i=i+1"
done
