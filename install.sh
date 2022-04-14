#!/usr/bin/bash
echo ""
echo -e "\e[34mStart installation script\e[0m"
echo ""
if [ -x /usr/bin/python3 ]
then
  echo -e "\e[32m[+] Python3 already installed in your system\e[0m"
else
  echo -e "\e[41m[-] Python3 not installed in your system"
  echo -e "[-] Use command: \e[1m$ apt install python3\e[21m for install"
  exit -1
fi

if [ -x /usr/bin/wg ]
then
  echo -e "\e[32m[+] Wireguard already installed in your system\e[0m"
else
  echo -e "\e[41m[-] Wireguard not installed in your system"
  echo -e "[-] Use command: \e[1m$ apt install wireguard\e[0m for install"
  exit -1
fi

cp src/wg-resolver.py /usr/local/bin/wg-resolver
chmod +x /usr/local/bin/wg-resolver
chmod +x uninstall.sh
echo -e "\e[32m[+] wg-name-resolver installed!\e[0m"
echo ""
echo "You can try it with command: $ wg-resolver"
echo ""
