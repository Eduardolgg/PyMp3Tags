# PyMp3Tags
Add tags to mp3 by getting the track number and song name from the file name.

***Usage: PyMp3Tags.py [options] songs_dir***

##Options:
* -a artist
* -l album name
* -y year
* -g genre. View mp3info man for more info.

##Considerations:
 * The track number and song name is extracted from the file name.
 * File name format: 00_Song_Title.mp3

   * 00: Is a track number and can be one or more digits.

   * Song_title: It is the name of the song and will delete the characters - and _ will be replaced by white space and the title converted to camel case.
 * This script needs mp3info to work properly.
