function yougrab() {
if [[ $# -lt 2 || $# -gt 3 ]]
then
	echo "Correct usage:
yougrab <url> <name> for mp3 conversion
yougrab <url> <name> vid to keep video"
else
	if [ $# -eq 2 ]
	then
		echo "Hacking..."
		youtube-dl $1 -o $2_raw
		echo "Hack complete... Beginning conversion"
		vlc -I dummy $2_raw --sout='#transcode{acodec=mp3,vcodec=dummy}:standard{access=file,mux=raw,dst="'$2'.mp3"}' vlc://quit
		mv $2.mp3 ~/Music/
		echo "Mp3 conversion complete"
		rm $2_raw
	else
		echo "Hacking..."
		youtube-dl $1 -o $2
		mv $2 ~/Videos/
		echo "Hack complete"
	fi
fi
}	
