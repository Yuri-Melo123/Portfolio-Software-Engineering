# Sistema de Gerenciamento Ágil de Tarefas

## Objetivo
Desenvolver um sistema básico para gerenciamento de tarefas que permita visualizar, priorizar e monitorar o progresso das atividades de uma equipe ágil.

## Escopo
O sistema implementa um CRUD de tarefas com campos como título, descrição, prioridade e status. Além disso, incorpora controle de qualidade com testes automatizados e simulação de mudança de escopo.

## Metodologia Utilizada
Utilizamos a metodologia **Kanban**, aplicada diretamente na aba **Projects** do GitHub com as colunas:
- A Fazer
- Em Progresso
- Concluído

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

3. Execute a aplicação:
   ```bash
   python app.py
   ```

4. Para executar os testes:
   ```bash
   pytest
   ```

## Justificativa para Mudança de Escopo
Durante o projeto, decidiu-se adicionar um campo de prioridade nas tarefas, com a justificativa de permitir melhor ordenação e foco em entregas críticas. A alteração foi refletida no código, testes e Kanban.
