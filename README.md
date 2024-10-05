# Hi-low Finance
Hi-low Finance App é uma aplicação web desenvolvida em Django com o objetivo de gerenciar o fluxo de caixa e gerar relatórios financeiros detalhados para empresas ou usuários individuais. A aplicação inclui funcionalidades de gestão contábil, relatórios customizáveis e cadastro de usuários, visando facilitar a análise e visualização de dados financeiros.

## Funcionalidades
- Gestão de Fluxo de Caixa: Tela dedicada para gerenciar entradas e saídas de caixa, permitindo o acompanhamento financeiro em tempo real.
- Relatórios Financeiros: Geração de relatórios personalizados sobre a situação financeira, como balanço patrimonial, DRE (Demonstrativo de Resultados do Exercício), entre outros.
- Cadastro de Usuários: Sistema de autenticação e gerenciamento de usuários com permissões definidas para acesso aos diferentes módulos da aplicação.
- Dashboard: Visualização gráfica das finanças em tempo real, permitindo uma análise simplificada de entradas, saídas e saldo disponível.

## Tecnologias Utilizadas
- Backend: Django 4.2 (Python)
- Frontend: HTML, CSS, Bootstrap
- Banco de Dados: sqlite(dev/teste) | PostgreSQL (produção)
- Visualizações de Dados: Plotly para gráficos interativos nos relatórios financeiros
- Autenticação: Sistema de autenticação nativo do Django com permissões de acesso
- Hospedagem: Configurado para rodar em qualquer ambiente com suporte a Docker ou Heroku

## Pré-requisitos
Para rodar o projeto localmente, você precisará ter instalado:

Python 3.8 ou superior
Django 4.2
PostgreSQL
Git (para clonar o repositório)
Pipenv ou Virtualenv (para gerenciamento do ambiente virtual)

## Uso
- Autenticação: Acesse com o superusuário que foi criado. Adicione usuários no menu de configurações (Settings > Cadastro de Usuários).
- Gestão de Fluxo de Caixa: Navegue até a tela de gestão de fluxo de caixa para adicionar, editar e excluir transações financeiras.
- Relatórios: Acesse os relatórios financeiros a partir do menu "Relatórios Financeiros" e selecione o tipo de relatório que deseja visualizar (DRE, balanço, etc.).

## Contribuições
Sinta-se à vontade para contribuir com o projeto através de pull requests. Antes de contribuir, por favor, crie uma nova issue detalhando a proposta ou problema.