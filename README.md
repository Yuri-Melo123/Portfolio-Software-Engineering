# Sistema de Gerenciamento Ágil de Tarefas

## Sobre o Projeto Original
Sistema de controle de estoque desenvolvido em Python com interface gráfica usando Tkinter e banco de dados SQLite. O sistema permite autenticação de usuários, controle de permissões por perfil (admin/comum), cadastro, atualização e visualização de produtos com alerta de quantidade mínima.

## Objetivo do Projeto Atual
Desenvolver um sistema básico para gerenciamento de tarefas que permita visualizar, priorizar e monitorar o progresso das atividades de uma equipe ágil.

## Metodologia Utilizada
Utilizamos a metodologia **Kanban** com as colunas:
- A Fazer
- Em Progresso
- Concluído

## Funcionalidades
- Autenticação de usuários com criptografia de senha (SHA256)
- Controle de sessão com perfis (Administrador e Comum)
- Cadastro de produtos com controle de quantidade mínima
- Atualização de estoque
- Visualização com destaque de produtos abaixo do mínimo
- Cadastro de novos usuários (somente admin)
- Gerenciamento de um quadro Kanban

## Tecnologias Utilizadas
- Python 3
- Tkinter
- SQLite3
- hashlib (para criptografia de senha)

## Como Executar
1. Instale o Python: https://www.python.org/
2. Execute o `main.py`
3. Crie um usuário administrador manualmente no banco de dados 
    (O Banco de dados presente neste repositório já possui um Usuário Administrador cadastrado - Login: admin / Senha: admin123)

## Estrutura
```
Aplicação/
├── docs/
│   └── fluxograma.pdf
├── src/
│   ├── app.py
│   ├── menu.py
│   ├── kanban.py
│   ├── kanban_gui.py
│   ├── utils.py
|   └── main.py
├── tests/
│   └── test_app.py
├── banco_de_dados.db (gerado automaticamente)
├── README.md
├── README.txt (Apresentação do controle de estoque)
└── requirements.txt
```

## Fluxograma
Veja o funcionamento no arquivo `fluxograma.pdf`.
=======
## Instruções de Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd Portfolio-Software-Engineering
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Justificativa para Mudança de Escopo
Durante o projeto, decidiu-se adicionar um campo de prioridade nas tarefas, para permitir uma melhor ordenação e foco em entregas críticas. A alteração foi refletida no código, testes e Kanban.

## Aprendizados
- Prática com interfaces Tkinter
- Conexão e manipulação de banco de dados SQLite
- Segurança com hash de senha
- Estruturação de projeto para entrega acadêmica e repositório GitHub

Desenvolvido por Yuri de Oliveira Melo
