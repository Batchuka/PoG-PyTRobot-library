from setuptools import setup, find_packages

setup(
    name='minha_biblioteca',
    version='1.0.0',
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Uma descrição breve da sua biblioteca',
    long_description='Uma descrição mais detalhada da sua biblioteca', # Pode ser um arquivo README.md
    long_description_content_type='text/markdown',  # Indica o tipo do conteúdo da long_description
    url='',  # URL do repositório da biblioteca
    packages=find_packages(),  # Encontra automaticamente todos os pacotes Python do projeto
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
