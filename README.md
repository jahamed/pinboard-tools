This parses my "wikipedia" tagged bookmarks from Pinboard and outputs them to a backup file.

Usage:

Create "credentials.py" and paste your Pinboard login information :
login = {
	'token' : 'INSERT PINBOARD API TOKEN HERE'
}

pip install -r requirements.txt

python wikipedia_backup.py