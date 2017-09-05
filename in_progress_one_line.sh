"...looking for Python3"
if command -v python3 > /dev/null 2>&1; then
  echo "Python3 already installed"
else
  brew install python3
  echo "Python3 installed"
fi

"...cloning repo"
git clone git@github.com:DanielSeehausen/pseudo_smart_random_pairing.git
"...making script executable"
sudo chmod +x ./pseudo_smart_random_pairing/smart_assign.py
"...adding get_pairs to path via symlink in /usr/bin/"
sudo ln -s $PWD/pseudo_smart_random_pairing/smart_assign.py /usr/bin/get_pairss
