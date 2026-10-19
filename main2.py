Certamente! Ecco il codice completo e pulito per il file setup.py (senza spazi invisibili o problemi di indentazione), pronto per essere utilizzato nel tuo progetto Python:

Python
from setuptools import setup, find_packages
import re
import subprocess


def derive_version() -> str:
    version = ''
    try:
        with open('discord/__init__.py', 'r', encoding='utf-8') as f:
            version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
    except Exception:
        pass

    if not version:
        raise RuntimeError('version is not set or discord/__init__.py not found')

    if version.endswith(('a', 'b', 'rc')):
        # Aggiunge un identificatore basato sul conteggio dei commit e sull'hash di Git
        try:
            p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            if out:
                version += out.decode('utf-8').strip()
            
            p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()
            if out:
                version += '+g' + out.decode('utf-8').strip()
        except Exception:
            pass

    return version


setup(
    name='tuo-nome-pacchetto', # Sostituisci con il nome del tuo pacchetto
    version=derive_version(),
    packages=find_packages(),
    install_requires=[
        # Aggiungi qui le dipendenze del tuo progetto, ad esempio:
        # 'aiohttp>=3.8.0',
    ],
    python_requires='>=3.8',
)