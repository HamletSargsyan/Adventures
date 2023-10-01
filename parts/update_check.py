import requests
from variables import version
from utils import alert, clear

from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown

console = Console()

repository_url = 'https://api.github.com/repos/HamletSargsyan/Adventures/releases/latest'

def check_update():
    try:
        response = requests.get(repository_url)

        clear()

        if response.status_code == 200:
            latest_release = response.json()
            tag_name = latest_release['tag_name']

            # Парсим версии и сравниваем их
            latest_version = tag_name.strip('v')
            current_version = version.strip('v')

            if latest_version > current_version:
                release_url = latest_release['html_url']
                alert(f'Новый релиз доступен: {tag_name}', 'success', enter=False)
                alert(f'Ссылка на скачивание: {release_url}', enter=False)
            else:
                alert('У вас актуальная версия', 'success', enter=False)
            print(Panel(Markdown(latest_release['body']), title="[bright_white]Описание версии[/bright_white]"))
            alert('', enter=True)
        else:
            alert('Не удалось получить информацию о релизе.', 'error')
    except:
        alert('Не удалось получить информацию о релизе.', 'error')
