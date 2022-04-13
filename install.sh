#!/usr/bin/bash
cp src/wg-resolver.py /usr/local/bin/wg-resolver
chmod +x /usr/local/bin/wg-resolver
chmod +x uninstall
echo "wg-name-resolver Installed!"
echo "You can try it with command: $ wg-resolver"
