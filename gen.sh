cat notes.txt | tr '\t' ' ' | sed 's/  / /g' |sed 's/\/[^ ]*//g' |sed 's/#/s/' | awk '{print "sox -n -r 22025 -c 1 -b16 " $1 ".wav synth 15 sin " $2 " fade 0.01 0 15" }' > run.sh

