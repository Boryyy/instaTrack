# instaTrack - Instagram followers tracker.

A simple script that will track your instagram followers , if anyone removes you or add you , and then a bot account will print it into your dm account. It has cookie support , the script will make you login only once. ( You need two accounts , the main account that has the followers , and an bot account.)

Tested with 500 followers and it takes like less than a minute , if you have more followers will take longer.


# Setup
1) Install the dependencies. Run this command in the command line:

* `cd C:/path/to/directory/with/program/instaTrackDM`
* `pip3 install -r requirements.txt`

If you are using windows and this command is not working try :

* `py -m pip install -r requirements.txt`


2) You will need two accounts , the main account of the followers that you want to track and one bot account.

3) Adding the main account and the bot account.

You have to edit the code and put your main account then the bot account you want to track.

* `USERNAME = ''` you have to put username of your main account.
* `PASSWORD = ''` you have to put password of your main account.

* `SUSERNAME = ''` you have to put username of your bot account.
* `SPASSWORD = ''` you have to put password of your bot account.

If you think the program is taking too long scanning your followers , you can lower the seconds at:
* `time.sleep(2) line 100` If you want it as fast as posible remove the whole row , or try (1).

Run the program.
* `python instaTrackDM.py`

# 24/7 Support

* If you want to run this script 24/7 like i do , it will send you daily message at decent time of the day (you choose), report an issue or add me on discord bory#8037
