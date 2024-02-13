#!/bin/bash

if [ ! -x $(which curl) ]; then
    echo -e "\e[31mcurl не найден, пожалуйста установите и попробуйте снова\e[0m"
    exit 1
fi


release_info=$(curl -s https://api.github.com/repos/HamletSargsyan/Adventures/releases/latest)

archive_url=$(echo "$release_info" | grep '"tarball_url":' | sed -E 's/.*"([^"]+)".*/\1/')

tag_name=$(echo "$release_info" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

curl -LJO "$archive_url"

tar -zxvf HamletSargsyan-Adventures-*.tar.gz
rm HamletSargsyan-Adventures-*.tar.gz

install_dir=$(pwd)/$(echo HamletSargsyan-Adventures-*)

mv $install_dir Adventures
install_dir=$(pwd)/Adventures

cd $install_dir

pip_command=""

if command -v pip3 &>/dev/null; then
    pip_command="pip3"
elif command -v pip &>/dev/null; then
    pip_command="pip"
else
    echo -e "\e[31mpip не найден, пожалуйста установите и попробуйте снова\e[0m"
    exit 1
fi

if eval "$pip_command  install -r requirements.txt --no-python-version-warning --disable-pip-version-check --break-system-packages"; then
    echo
else
    echo -e "\e[31mНе удалось скачать зависимости\e[0m"
    exit 1
fi

clear -x

echo
echo
echo -e "\e[95m   ###    ########  ##     ## ######## ##    ## ######## ##     ## ########  ########  ######  \e[0m"
echo -e "\e[95m  ## ##   ##     ## ##     ## ##       ###   ##    ##    ##     ## ##     ## ##       ##    ## \e[0m"
echo -e "\e[95m ##   ##  ##     ## ##     ## ##       ####  ##    ##    ##     ## ##     ## ##       ##       \e[0m"
echo -e "\e[95m##     ## ##     ## ##     ## ######   ## ## ##    ##    ##     ## ########  ######    ######  \e[0m"
echo -e "\e[95m######### ##     ##  ##   ##  ##       ##  ####    ##    ##     ## ##   ##   ##             ## \e[0m"
echo -e "\e[95m##     ## ##     ##   ## ##   ##       ##   ###    ##    ##     ## ##    ##  ##       ##    ## \e[0m"
echo -e "\e[95m##     ## ########     ###    ######## ##    ##    ##     #######  ##     ## ########  ######  \e[0m"
echo
echo
echo -e "\e[32mAdventures версии $tag_name успешно установлен и распакован в $install_dir\e[0m"
echo
echo 

echo -n "Хотите запустить игру? [Y/n]: "
read -r answer
answer=${answer:-Y}
if [[ $answer =~ ^[Yy]$ ]]; then
    python_command=""
    if command -v python3 &>/dev/null; then
        python_command="python3"
    elif command -v python &>/dev/null; then
        python_command="python"
    else
        echo "\e[31mpython не найден, пожалуйста установите и попробуйте снова\e[0m"
        exit 1
    fi

    eval "$python_command $install_dir/main.py"
else
    exit 0
fi
