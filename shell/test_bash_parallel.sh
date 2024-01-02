for i in {1..10}
do
    sleep 3s && echo "$i done" &
done
wait
