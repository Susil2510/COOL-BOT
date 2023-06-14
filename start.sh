if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Susil2510/COOL-BOT.git /COOL-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /COOL-BOT
fi
cd /COOL-BOT
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
