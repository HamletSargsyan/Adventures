import os
import requests
import zipfile
import io
import shutil
import subprocess

from utils import alert, clear, prompt

from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
import inquirer

from config import game

console = Console()

GITHUB_REPO = "Adventures"
REPO_URL = "https://api.github.com/repos/HamletSargsyan/Adventures"
RELEASES_URL = f"{REPO_URL}/releases/latest"


def download_latest_release():
    clear()
    # Запрашиваем информацию о последнем релизе
    response = requests.get(RELEASES_URL)

    if response.status_code != 200:
        alert(
            f"Не удалось получить информацию о релизе. Код состояния: {response.status_code}",
            "error",
        )
        return

    latest_release = response.json()
    release_tag = latest_release["tag_name"].replace("v", "")
    download_url = (
        f"https://github.com/HamletSargsyan/Adventures/archive/v{release_tag}.zip"
    )

    # Отправляем GET-запрос на скачивание
    response = requests.get(download_url)

    if response.status_code != 200:
        alert(
            f"Не удалось скачать архив. Код состояния: {response.status_code}",
            "error",
            enter=False,
        )
        return

    alert(f"Начало скачивания архива из релиза {release_tag}", "success", enter=False)
    # Создаем объект ZipFile из полученных данных
    with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
        # Распаковываем архив в текущей директории, используя extractall
        zip_file.extractall()

    # Получаем список всех файлов и папок в распакованной директории
    extracted_files = os.listdir(f"{GITHUB_REPO}-{release_tag}")

    # Перемещаем файлы и папки из распакованной директории в текущую
    for item in extracted_files:
        item_path = os.path.join(f"{GITHUB_REPO}-{release_tag}", item)
        target_path = os.path.join(os.getcwd(), item)

        if os.path.exists(target_path):
            if os.path.isfile(target_path):
                os.remove(target_path)
            else:
                shutil.rmtree(target_path)

        os.rename(item_path, target_path)

    # Удаляем пустую распакованную директорию
    os.rmdir(f"{GITHUB_REPO}-{release_tag}")

    alert(f"Архив из релиза {release_tag} успешно скачан.", "success", enter=False)

    # После успешного скачивания и распаковки, запускаем main.py
    main_script = "main.py"
    if os.path.exists(main_script):
        try:
            alert(f"Установка зависимостей.", "success", enter=False)

            if os.name == "nt":
                subprocess.run(["pip", "install", "-r", "requirements.txt"])
            else:
                subprocess.run(["pip3", "install", "-r", "requirements.txt"])

            alert(f"Зависимости успешно скачены.", "success", enter=False)
            alert(f"Запуск игры.", "success", enter=False)

            if os.name == "nt":
                subprocess.run(["python", main_script])
            else:
                subprocess.run(["python3", main_script])
        except Exception:
            alert(
                "Не удалось запустить игру автоматичесый, пожалуйста введите команду для его запуска для ващей системы",
                level="error",
            )
            alert("Выход из игры", enter=False)
            exit()
    else:
        alert(f"Файл {main_script} не найден.", "error", enter=False)


@game.on("check_update")
def check_update():
    try:
        response = requests.get(RELEASES_URL)

        clear()

        if response.status_code == 200:
            latest_release = response.json()
            tag_name = latest_release["tag_name"]

            # Парсим версии и сравниваем их
            latest_version = tag_name.strip("v")
            current_version = game.config.version.value.strip("v")

            print(
                Panel(
                    Markdown(latest_release["body"]),
                    title=f"[bright_white]Описание версии {tag_name}[/bright_white]",
                )
            )

            # https://github.com/HamletSargsyan/Adventures/issues/13
            if latest_version != current_version:
                alert(f"Новый релиз доступен: {tag_name}", "success", enter=False)

                questions = [
                    inquirer.List(
                        "choice",
                        message="Выберите опцию:",
                        choices=[
                            ("Назад", "1"),
                            ("Обновить", "2"),
                        ],
                    ),
                ]

                choice = prompt(questions)

                if choice == "1":
                    game.trigger("start")
                elif choice == "2":
                    download_latest_release()
            else:
                alert("", enter=True)
        else:
            alert("Не удалось получить информацию о релизе.", "error")
    except Exception as e:
        alert(f"Не удалось получить информацию о релизе. Причина: {e}", "error")
