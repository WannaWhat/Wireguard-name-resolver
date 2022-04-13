#!/usr/bin/python3
import subprocess
import sys
import os

PEER_SECTION_NAME = "[Peer]"
PUBKEY_PARAM_NAME = "PublicKey"
INTERFACE_WG_SHOW_NAME = "interface:"
PEER_WG_SHOW_NAME = "peer:"


class Colors(object):
    Color_Off = '\033[0m'
    Black = '\033[0;30m'
    Red = '\033[0;31m'
    Green = '\033[0;32m'
    Yellow = '\033[0;33m'
    Blue = '\033[0;34m'
    Purple = '\033[0;35m'
    Cyan = '\033[0;36m'
    White = '\033[0;37m'
    IYellow = '\033[0;93m'
    IGreen = '\033[0;92m'


def get_config_file(interface: str) -> (bool, str):
    config_path = os.path.join("/etc/wireguard", f"{interface}.conf")
    if not os.path.exists(config_path):
        return False, "File doesnt not exists"
    try:
        with open(config_path, "r") as file:
            config_file_text = file.read()
    except Exception as e:
        return False, e
    return True, config_file_text


def get_param_value(key: str, delimiter: str, source: str) -> str or bool:
    if key not in source:
        return False
    return delimiter.join(source.split(delimiter)[1:]).replace(" ", "")


def create_peers_asocial(config_file_text: str) -> {}:
    peer_name = None
    out_asocial = {}
    for _r in config_file_text.split("\n"):
        peer_name_swp = get_param_value(PEER_SECTION_NAME, "#", _r)
        if peer_name_swp:
            peer_name = peer_name_swp
            continue
        if peer_name is not None:
            pubkey = get_param_value(PUBKEY_PARAM_NAME, "=", _r)
            if pubkey:
                out_asocial[pubkey] = peer_name
                peer_name = None
    return out_asocial


def main(interface: str = None):
    request_list = ["wg", "show"]
    if interface is not None:
        request_list.append(interface)
    try:
        output = subprocess.check_output(request_list)
    except Exception as e:
        print("Can't execute command wg. Check is wireguard installed into your system")
        print(f"Error: {e}")
        sys.exit(-1)
    output = output.decode()
    output = output.split("\n")
    errors = []
    peers_asocial = {}
    for _r in output:
        interface_swp = get_param_value(INTERFACE_WG_SHOW_NAME, ":", _r)
        if interface_swp:
            status_flag, config_file_text = get_config_file(interface_swp)
            print(f"{Colors.IGreen}{INTERFACE_WG_SHOW_NAME[0:-1]}{Colors.White}:{Colors.Green} {interface_swp}{Colors.Color_Off}")
            if not status_flag:
                errors.append(config_file_text)
                continue
            peers_asocial = create_peers_asocial(config_file_text)
            continue
        else:
            peer_swp = get_param_value(PEER_WG_SHOW_NAME, ":", _r)
            if peer_swp:
                if peer_swp in peers_asocial:
                    print(f"{Colors.IYellow}{PEER_WG_SHOW_NAME[0:-1]}{Colors.White}:{Colors.Yellow} {peers_asocial[peer_swp]} "
                          f"-{PEER_WG_SHOW_NAME.join(_r.split(PEER_WG_SHOW_NAME)[1:])}{Colors.Color_Off}")
                continue
        print(_r)
    print(Colors.Color_Off)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        interface = sys.argv[1]
    else:
        interface = None
    main(interface=interface)
