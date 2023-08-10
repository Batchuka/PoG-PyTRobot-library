#  Faça sua biblioteca para o PyTRobot

Este é um template para iniciar rapidamente bibliotecas gerais de python, mas voltado para o PyTRObot, usando o Cookiecutter.

## Como Usar

1. Certifique-se de ter o Cookiecutter instalado:

```
pip install cookiecutter
```

2. Clone este repositório:

```
cookiecutter https://github.com/Batchuka/PoG-PyTRobot-library.git
```

3. O cookiecutter irá pedir nome do pacote 'library_name' e o nome da classe principal, 'class_name'. Dê o nome ao pacote e a classe principal, que deve ser usada para implementar as configurações e interface do pacote. Após isso, seu nome, email e versão do pacote.


4. Seu novo projeto será criado no diretório especificado.


5. Após implementado o pacote, implemente também os testes unitários que serão utilizados pelo *tox* no pipeline de publicação.


6. Após implementados os testes, você pode configurar o *tox* para publicar o pacote em seu repositório de preferência.

## Contribuição

Se você encontrar algum problema ou tiver sugestões para melhorias, fique à vontade para abrir uma issue ou enviar um pull request!
