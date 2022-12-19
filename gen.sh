cat notes.txt | tr '\t' ' ' | sed 's/  / /g' |sed 's/\/[^ ]*//g' |sed 's/#/s/' | awk '{print "sox -n -r 11025 -c 1 -b8 " $1 ".wav synth 5 sin " $2 " fade 0.01 0 5" }' > run.sh

