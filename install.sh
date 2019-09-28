#!/bin/bash
clear
echo "
__  __ ____    ____  _______   __
|  \/  |  _ \  |  _ \| ____\ \ / /
| |\/| | |_) | | |_) |  _|  \ V /
| |  | |  _ <  |  _ <| |___  | |
|_|  |_|_| \_\ |_| \_\_____| |_|Tools Instaler By +62 .MR REY
  

                                                ";

echo "[✔] Checking directories...";
if [ -d "/usr/share/doc/pencari ip" ] ;
then
echo "[◉] A directory pencari ip was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "/usr/share/doc/pencari ip"
else
 exit
fi
fi

 echo "[✔] Installing ...";
 echo "";
 git clone https://github.com/reyspeed/pencari-ip;
 echo "#!/bin/bash 
 python /usr/share/doc/Crips/crips.py" '${1+"$@"}' > pencari-ip;
 chmod +x pencari-ip;
 sudo cp pencari-ip /usr/bin/;
 rm crips;


if [ -d "/usr/share/doc/pencari ip" ] ;
then
echo "";
echo "[✔]Tool istalled with success![✔]";
echo "";
  echo "[✔]====================================================================[✔]";
  echo "[✔] ✔✔✔  All is done!! You can execute tool by typing pencari ip  !     ✔✔✔ [✔]"; 
  echo "[✔]====================================================================[✔]";
  echo "";
else
  echo "[✘] Installation faid![✘] ";
  exit
fi
