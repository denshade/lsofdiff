if [ "$#" -ne 2 ]; then
       echo "Usage $0 <pid> <sleeptime>"
       exit 1
fi
echo "recording: control C to stop."
mkdir -p logs
rm logs/*.log
i=0
while true; do
	lsof -p $1 -Fn > logs/$i.log 2> /dev/null      #`date +%y-%m-%d-%H:%M:%S:%N` 2> /dev/null
	sleep $2
	echo -n "."
	let "i=i+1"
done
