# {{cookiecutter.library_name}}

Este é um pacote criado a partir do Cookiecutter PyTRobot Library, projetado para fornecer uma estrutura base para acelerar o desenvolvimento dos módulos de reúso deste framework.

## Instalação

Você pode instalar o pacote usando o seguinte comando:

```bash
pip install {{cookiecutter.library_name}}
```

# Uso

O pacote deve ser importado como qualquer outro e precisa ser configurado. No arquivo package_config.py, é implementada a classe {{class_name}}, responsável por implementar os métodos e propriedades de configuração e interface desse pacote. Sinta-se a vontade para preencher as informações necessárias da forma que quiser — o framework PyTRobot oferece o método [load_config](), que automaticamente preenche todas as configurações de um pacote baseado no arquivo *.properties*, explore essa lógica para mais detalhes.


# Adicionando Novos Módulos

Se você deseja adicionar novos módulos ou funcionalidades ao pacote, é uma prática recomendada importar as classes e funções relevantes no arquivo __init__.py do pacote. Isso tornará as classes e funções mais acessíveis quando os usuários importarem o pacote.

Por exemplo, no arquivo __init__.py:

```
from .nome_do_pacote import NomeDaClasse
from .outro_modulo import OutraClasse

# ... outras importações ...
```

