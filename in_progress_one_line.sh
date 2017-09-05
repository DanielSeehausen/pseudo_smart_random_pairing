"...looking for Python3"
if command -v python3 > /dev/null 2>&1; then
  echo "Python3 already installed"
else
  brew install python3
  echo "Python3 installed"
fi

git clone git@github.com:DanielSeehausen/pseudo_smart_random_pairing.git
sudo chmod +x ./pseudo_smart_random_pairing/smart_assign.py
sudo touch /usr/bin/get_pairs
sudo chmod +x /usr/bin/get_pairs
sudo echo "python3 $PWD/pseudo_smart_random_pairing/smart_assign.py" >> /usr/bin/get_pairs
