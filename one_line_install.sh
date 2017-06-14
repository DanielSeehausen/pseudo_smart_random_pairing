if command -v python3 > /dev/null 2>&1; then
  echo true
else
  brew install python3
fi

git clone git@github.com:DanielSeehausen/pseudo_smart_random_pairing.git
chmod +x pseudo_smart_random_pairing/smart_assign.py
echo "alias get_pairs='python3 $PWD/pseudo_smart_random_pairing/smart_assign.py'" >> ~/.bash_profile
source ~/.bash_profile
