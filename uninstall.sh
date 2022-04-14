#!/usr/bin/bash
rm /usr/local/bin/wg-resolver 2>/dev/null
if [ $? -eq 1 ]
then
  echo -e "\e[31m[+] wg-name-resolver already uninstalled from your system\e[0m"
  exit 0
fi
echo -e "\e[32m[+] wg-name-resolver uninstalled\e[0m"