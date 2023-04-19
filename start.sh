echo "Cloning Repo...."
git clone https://github.com/Techwrdd/linkeasy.in /linkeasy.in
cd /linkeasy.in
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
