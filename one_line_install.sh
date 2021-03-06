
CHECK='\033[0;32m\xE2\x9C\x94\033[0m'

echo -e "\n...looking for Python3..."
if command -v python3 > /dev/null 2>&1; then
  echo -e "\t...already installed ${CHECK}\n"
else
  echo -e "\t...missing -- installing now"
  (brew install python3 && echo -e "\t...done ${CHECK}") || echo -e "\t...Python3 installation failed! Is brew missing? Is it installed but not in your path?\n"
fi

echo "...cloning repo"
git clone git@github.com:DanielSeehausen/pseudo_smart_random_pairing.git && echo -e "\t...done ${CHECK}"
echo -e "\n...making script executable"
sudo chmod +x ./pseudo_smart_random_pairing/smart_assign.py && echo -e "\t...done ${CHECK}"
echo -e "\n...adding get_pairs to path via symlink in /usr/local/bin/"
(sudo ln -s $PWD/pseudo_smart_random_pairing/smart_assign.py /usr/local/bin/get_pairs && echo -e "\t...done ${CHECK}") || echo -e "\t...something went wrong -- does the file already exist?"
echo -e "\n...reloading path"
source ~/.bash_profile && echo -e "\t...done ${CHECK}"

echo -e "\n*************************************************************************\nThe command 'get_pairs' may now be run from the terminal.\nMake sure to update the pseudo_smart_random_pairing/students.py file first!\n*************************************************************************"
