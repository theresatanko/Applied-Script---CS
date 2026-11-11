#!/bin/bash
# Detta RECON script samlar in systeminformation om Linux-Miljöer.
# Kan användas för följande attacker:
# TODO: [Skriv möjliga attacker]
# Author: Frans Schartau
# Last Update: 2026-11-11


MSG() {
    local color="${1:-}"
    shift || true
    local msg="$*"

    case "${color^^}" in
        R|RED)    printf '\033[31m%s\033[0m\n' "$msg" ;;
        G|GREEN)  printf '\033[32m%s\033[0m\n' "$msg" ;;
        Y|YELLOW) printf '\033[33m%s\033[0m\n' "$msg" ;;
        B|BLUE)   printf '\033[34m%s\033[0m\n' "$msg" ;;
        C|CYAN)   printf '\033[36m%s\033[0m\n' "$msg" ;;
        *)        printf '%s %s\n' "$color" "$msg" ;;
    esac
}

# MSG "FÄRG" "MEDELANDE"
# Till exempel:
# MSG "G"  "===ABC==="
# För att skriva I GRÖNT.

MSG "G" "Välkommen till detta RECON script som samlar in systeminformation om Linux-Miljöer"

MSG "G" "===SYSTEMINFO==="
uname -a

MSG "G" "===AKTUELL ANVÄNDARE==="
echo $USER

MSG "G" "===ANVÄNDARE MED SHELL==="
grep "sh$" /etc/passwd

MSG "G" "===NÄTVERK==="
ip a | grep inet


MSG "G"  "===OPENSSL DIGESTS==="
# lists digest algorithms
openssl list -digest-algorithms | awk '/^  [A-Z0-9]/ {print $1}' | grep -vE "RSA-|NULL|MD4|MD5|SHA1" | tr -d ' ' | sort -u


MSG "R"  "=========MAIN SYSTEM INFO========="
MSG "G"  "===DATE & TIME==="
date
timedatectl


MSG "G"  "===OS INFO==="
uname --all; printf "\n"
cat /etc/{os-*,issue} 2>/dev/null
MSG "G"  "===STORAGE==="
lsblk
MSG "G"  "===CPU & MEM==="
lscpu | grep "Model name"
lsmem | grep "Total online memory"
MSG "G"  "===HARDWARE BUS==="
lsusb
lspci | grep -iE "vpu|npu|intel"

MSG "R"  "=========FÄRDIG========="
