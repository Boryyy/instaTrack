# instaTrack - Instagram followers/following tracker

A simple script that will track your instagram account who you are following and they are not following back , who unfollowed you , and who added you.

Tested only with 200-500-800 followers , so if u have any question you can ask me about it , report an issue.


# Setup
1) Install the dependencies. Run this command in the command line:

* `cd C:/path/to/directory/with/program/`
* `pip3 install -r requirements.txt`

If you are using windows and this command is not working try :

* `py -m pip install -r requirements.txt`


2) You will need an bot account , or use your own account , but i suggest to use a bot account , then add the account you want to track.

3) Adding the bot account in the python code.

You have to edit the code and put your bot/account you want to track.

* `USERNAME = ''` you have to put username of your bot account.
* `PASSWORD = ''` you have to put password of your bot account.
* `usr = ('')` put the account you want to track.

If you think the program is taking too long scanning your followers , you can lower the seconds at:
* `user_input = ('700')` , i have 500 followers so i put it at 700 , you can test your own.

Run the program.
* `python3 instaTrack.py`

# Disclaimer

* Dont forget to edit the seconds i mention before at [Setup](https://github.com/Boryyy/instaTrack#setup) , it will improve the script and you can get the track faster.

