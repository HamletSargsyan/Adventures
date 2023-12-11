# Adventures

[![wakatime](https://wakatime.com/badge/github/HamletSargsyan/Adventures.svg)](https://wakatime.com/badge/github/HamletSargsyan/Adventures) 
![Static Badge](https://img.shields.io/badge/version-2.0.8-blue)
![GitHub (Pre-)Release Date](https://img.shields.io/github/release-date-pre/HamletSargsyan/Adventures?color=blue)
![GitHub all releases](https://img.shields.io/github/downloads/HamletSargsyan/Adventures/total?color=blue)

**Adventures** - это текстовая игра, написанная на языке Python. Игра позволяет игроку исследовать окружающий мир, сражаться с противниками и многое другое.

**Версия**: 2.0.10

## Оглавление

- [Adventures](#adventures)
  - [Оглавление](#оглавление)
  - [Зависимости](#зависимости)
  - [Установка и запуск](#установка-и-запуск)
    - [Установка на ПК](#установка-на-пк)
      - [Windows](#windows)
      - [Linux](#linux)
    - [Установка на телефон](#установка-на-телефон)
  - [Вклад](#вклад)
  - [Автор](#автор)
  - [Лицензия](#лицензия)

## Зависимости


```
inquirer==3.1.3
loguru==0.7.0
Requests==2.31.0
rich==13.6.0
```

## Установка и запуск

Игра работает как на ПК, так и на телефоне.

### Установка на ПК

#### Windows
> Если на вашем ПК нет git'а, то скачайте его с официального сайта
> https://git-scm.com/downloads

```shell
git clone https://github.com/HamletSargsyan/Adventures.git
pip install -r requirements.txt
cd Adventures
python main.py
```

#### Linux
``` shell
sudo apt update && sudo apt install git && git clone https://github.com/HamletSargsyan/Adventures && sudo apt install python && cd Adventures && sudo apt install python-pip && pip install -r requirements.txt && python main.py
```

### Установка на телефон

Чтобы играть на телефоне, вам нужно скачать **Termux**

> Гайд по установке Termux на android и на ios
> https://teletype.in/@artur.kerimov777/LULi6jK5-

После установки приложения выполните следующую команду:

``` shell
pkg update && pkg install git && git clone https://github.com/HamletSargsyan/Adventures && pkg install python && cd Adventures && pkg install python-pip && pip install -r requirements.txt && python main.py
```

После установки игра сама запустится

## Вклад

Если вы хотите внести свой вклад в проект Adventures, вы можете выполнить следующие действия:

1. Сделайте форк репозитория на GitHub.
2. Внесите необходимые изменения в вашем форке.
3. Создайте pull request, чтобы предложить ваши изменения для рассмотрения.

## Автор

Автор проекта Adventurs: [Hamlet Sargsyan](https://github.com/HamletSargsyan/)

Вы можете связаться со мной по электронной почте: hamlets849@gmail.com

## Лицензия

Проект Adventurs распространяется под лицензией **MIT**. Подробную информацию можно найти в файле **LICENSE**.

