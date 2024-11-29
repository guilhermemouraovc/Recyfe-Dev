![Imagem do WhatsApp de 2024-10-17 à(s) 00 07 14_7e13165b](https://github.com/user-attachments/assets/bbc79c7a-d803-460e-b62f-8a1ea2923d88)

## Descrição

Recyfe é um aplicativo desenvolvido com o objetivo de incentivar a reciclagem e o consumo consciente através de práticas sustentáveis. O sistema permite que os usuários acumulem créditos por suas ações sustentáveis, que podem ser trocados por recompensas. Além disso, oferece uma plataforma de compra de produtos feitos a partir de materiais reciclados e facilita a doação e a reciclagem de itens têxteis.

Este projeto foi criado como parte da disciplina de Projetos 2 na CESAR School - turma 2024.2.
 
## Tecnologias

- **Framework de Desenvolvimento**: Django - Framework web em Python para o back-end.
- **Interface**: HTML/CSS/JavaScript - Para a interface do usuário.
- **Banco de dados**: Sqlite/PostgreSQL - Para armazenar informações.
- **Hospedagem**: Azure - O produto final será hospedado na plataforma Azure.

## Ferramentas

- **Prototipação**: Figma - Utilizado para criar e validar protótipos de design da interface do usuário.
- **Gestão de Projetos**: Jira - Ferramenta para o planejamento e acompanhamento das tarefas do projeto.
- **Comunicação e Reuniões**: Discord/WhatsApp - Plataformas utilizadas para reuniões e comunicação da equipe.

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

## Equipe

- [Guilherme Mourão](https://github.com/guilhermemouraovc) - gmvc@cesar.school
- [Henrique Figueiredo](https://github.com/fthenri) - hft@cesar.school
- [Jeronimo Rossi](https://github.com/Jeraross) - jbr2@cesar.school
- [Luis Guilherme](https://github.com/luisgxlauria) - lgals@cesar.school
- [Joao Lucas](https://github.com/JRobalinho) - jlvrf@cesar.school
- [Caio Ferreira](https://github.com/CaioLira18) - cflo@cesar.school

## Site

- [Site - Azure](https://recyfe.azurewebsites.net/)


<details>
<summary><h2>SR1</h2></summary>

- [Screecast do Protótipo Lo-fi](https://www.youtube.com/watch?v=FWHbXnmOCmE)

- [Screecast do Site](https://youtu.be/bEzvsAhCzDU)

- [Site - Azure](https://recyfe.azurewebsites.net/)

- [Analise_de_Viabilidade_Programacao_em_Par_Projeto_Django.pdf](https://github.com/user-attachments/files/17388785/Analise_de_Viabilidade_Programacao_em_Par_Projeto_Django.pdf)

- **Print Product Backlog**

![Captura de tela 2024-10-16 001422](https://github.com/user-attachments/assets/85b3fbb5-fec5-48c2-86d3-9d452925157d)

- **Print Issues/Bug Tracker**

![Captura de tela 2024-10-16 001519](https://github.com/user-attachments/assets/1bce1d27-25c7-48f8-ab5f-7672a40192b8)

- **Print Diagrama de Atividades do Projeto**

![image](https://github.com/user-attachments/assets/b5ff5f6b-c16d-4836-bc7e-2cefa89e0790)

- **6 Historias de Usuário Bem Definidas / 2 Historias Implementadas**

1. **Visualização do Feed** - **Implementada**

História: Como usuário, quero acessar uma página inicial clara e visualmente atraente, onde posso visualizar posts de outros usuários.

Cenários de Validação:

Cenário 1: Acesso e uso da página inicial com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a página inicial,
Então eu devo ser capaz de ver uma interface clara e atraente,
E eu devo poder postar minhas próprias práticas,
E visualizar dicas sobre reutilização de resíduos têxteis.

Cenário 2: Tentativa de login sem credenciais corretas

Dado que eu não tenha inserido minhas credenciais corretamente,
Quando eu tentar fazer login no sistema,
Então uma mensagem de erro "Credenciais inválidas" deve aparecer,
E o acesso ao sistema deve ser negado.

Cenário 3: Acesso ao Feed com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar o Feed,
Então eu devo ser capaz de visualizar posts de outros usuários,
E receber informações sobre sustentabilidade dos administradores.

Cenário 4: Falha ao acessar o Feed

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E houver uma falha no carregamento do Feed,
Então uma mensagem de erro "Erro ao carregar o Feed, tente novamente mais tarde" deve aparecer.

Cenário 5: Tentativa de postar sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

2. **Postagem de Práticas Sustentáveis** - **Implementada**

História: Como usuário, quero postar minhas próprias práticas sobre sustentabilidade na página inicial.

Cenários de Validação:

Cenário 1: Postagem de prática sustentável com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E tentar postar uma prática sustentável,
Então o post deve ser criado com sucesso e aparecer no Feed.

Cenário 2: Tentativa de postar sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

3. **Navegação de Produtos**

História: Como usuário, quero poder visualizar detalhes completos dos produtos. Desejo ver a imagem do produto, sua descrição e o tipo de material reutilizado.

Cenários de Validação:

Cenário 1: Visualização dos detalhes do produto com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a página de um produto,
Então eu devo ser capaz de ver uma imagem clara do produto,
E eu devo poder visualizar a descrição completa,
E o tipo de material reutilizado no produto.

Cenário 2: Tentativa de login sem credenciais corretas

Dado que eu não tenha inserido minhas credenciais corretamente,
Quando eu tentar fazer login no sistema,
Então uma mensagem de erro "Credenciais inválidas" deve aparecer,
E o acesso ao sistema deve ser negado.

Cenário 3: Falha ao carregar a página de detalhes do produto

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E houver uma falha ao carregar os detalhes do produto,
Então uma mensagem de erro "Erro ao carregar os detalhes do produto, tente novamente mais tarde" deve aparecer.

Cenário 4: Tentativa de visualizar detalhes sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a página de detalhes de um produto,
Então uma mensagem "Você precisa estar logado para visualizar os detalhes do produto" deve aparecer.

4. **Localização de Pontos de Doação e Vendas**

História: Como administrador, quero disponibilizar no aplicativo, por meio de GPS, a localização dos pontos de doação e das lojas que vendem produtos reutilizados.

Cenários de Validação:

Cenário 1: Cadastramento de novos pontos de doação ou lojas com sucesso

Dado que eu tenha um perfil de administrador,
Quando eu fizer login no sistema,
E acessar a função de cadastramento de novos pontos de doação ou lojas,
E inserir as informações requeridas,
Então o novo ponto de doação ou loja deve ser cadastrado com sucesso,
E as informações devem aparecer no mapa disponível para os usuários.

Cenário 2: Tentativa de cadastrar novos pontos de doação sem permissão

Dado que eu tenha um perfil de usuário sem permissões de administrador,
Quando eu tentar acessar a função de cadastramento de novos pontos de doação ou lojas,
Então uma mensagem de "Permissão negada" deve aparecer,
E o sistema deve impedir o cadastramento.

Cenário 3: Visualização de locais no mapa com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a função de mapa,
Então eu devo ser capaz de visualizar as localizações dos pontos de doação e lojas próximos a mim,
Baseado na minha localização GPS.

Cenário 4: Visualização de informações detalhadas sobre um local

Dado que eu esteja visualizando o mapa,
Quando eu selecionar um ponto de doação ou loja,
Então as informações detalhadas (como horário de funcionamento e serviços oferecidos) devem ser exibidas para mim.

Cenário 5: Falha ao visualizar o mapa por problemas de GPS

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a função de mapa,
E houver problemas com o GPS ou sinal de localização,
Então uma mensagem "Falha ao carregar a localização, verifique suas configurações de GPS" deve aparecer.

Cenário 6: Tentativa de visualizar mapa sem permissão

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a função de mapa,
Então uma mensagem "Você precisa estar logado para visualizar o mapa de pontos de doação e lojas" deve aparecer.

5. **Sistema de Pontuação e Recompensas**

História: Como usuário, quero acessar uma aba de recompensas, onde posso visualizar os créditos acumulados por minhas ações sustentáveis e escolher diferentes tipos de recompensas.

Cenários de Validação:

Cenário 1: Visualização de créditos acumulados com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a aba de recompensas,
Então eu devo ser capaz de visualizar meu saldo de créditos acumulados,
E ver as opções de recompensas disponíveis na plataforma.

Cenário 2: Tentativa de visualizar recompensas sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a aba de recompensas,
Então uma mensagem "Você precisa estar logado para acessar suas recompensas" deve aparecer.

Cenário 3: Troca de créditos por recompensas com sucesso

Dado que eu tenha créditos suficientes,
Quando eu acessar a aba de recompensas,
E escolher uma recompensa,
Então eu devo ser capaz de trocar meus créditos pela recompensa escolhida,
E uma confirmação da troca deve aparecer.

Cenário 4: Notificação de novas recompensas

Dado que eu tenha acumulado créditos suficientes para desbloquear novas recompensas,
Quando eu acessar a aba de recompensas,
Então eu devo ser notificado de que novas recompensas estão disponíveis para troca.

Cenário 5: Tentativa de trocar créditos insuficientes

Dado que eu tenha um perfil de usuário registrado,
Quando eu acessar a aba de recompensas,
E tentar trocar créditos por uma recompensa sem ter créditos suficientes,
Então uma mensagem "Créditos insuficientes para esta recompensa" deve aparecer.

6. **Catalogação de Créditos e Opções de Envio**

História: Como usuário, desejo acessar uma seção onde posso ver informações sobre opções de envio de residuos texteis para reuso e catalogação de créditos por resíduo enviado.

Cenários de Validação:

Cenário 1: Acesso à seção de reciclagem com sucesso

Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a seção de doação ou reciclagem,
Então eu devo ser capaz de visualizar as opções de envio ou entrega para reuso de itens têxteis.

Cenário 2: Tentativa de acessar a seção de reciclagem sem estar logado

Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a seção de doação ou reciclagem,
Então uma mensagem "Você precisa estar logado para acessar essa seção" deve aparecer,
E o sistema deve bloquear o acesso.

Cenário 3: Acompanhamento de créditos recebidos com sucesso

Dado que eu tenha enviado itens para reciclagem,
Quando eu acessar meu perfil ou a seção de reciclagem,
Então eu devo poder visualizar o histórico de itens enviados,
E ver os créditos recebidos por cada item reciclado.

Cenário 4: Notificação de créditos insuficientes para acompanhamento

Dado que eu tenha enviado itens para reciclagem,
Quando eu acessar meu saldo de créditos,
E não houver crédito suficiente catalogado,
Então uma mensagem "Nenhum crédito disponível para os itens reciclados" deve aparecer.
</details>


<details>
<summary><h2>SR2</h2></summary>

## Links Relevantes:

- [Projeto no Jira](https://cesar-team-pkcqpghh.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog?selectedIssue=SCRUM-5)
- [Protótipo de Média Fidelidade no Figma](https://www.figma.com/design/r7UbvzWSKmMyssPNiVZ9aN/Prot%C3%B3tipo-m%C3%A9dia-fidelidade?node-id=3-16&node-type=canvas&t=Hs3Z2o3N54AUvip7-0)
- [Screencast do Protótipo de Média Fidelidade](https://youtu.be/sY4a9ruACbE)
- [Screencast da Execução dos Testes](https://www.youtube.com/watch?v=vvllLXazW7E)

## Deployment das histórias produzidas:

- [Projeto na Azure](https://recyfe.azurewebsites.net/)
- [Screencast da Azure](https://youtu.be/sajPkyRTAzU)

## 10 Histórias de Usuário Bem Definidas:

1. **Visualização do Feed**
2. **Postagem de Práticas Sustentáveis**
3. **Curtir e Comentar Postagens de Outros Usuários**
4. **Favoritar Postagens de Outros Usuários**
5. **Visualização de Detalhes do Produto**
6. **Receber Notificação Automática ao Se Interessar por um Produto**
7. **Cadastramento de Novos Pontos de Doação**
8. **Visualização de Locais no Mapa**
9. **Sistema de Pontuação e Recompensas**
10. **Transferência de Créditos**

### História 1: Visualização do Feed

**Como usuário registrado, quero acessar uma página inicial clara e visualmente atraente, para visualizar posts de outros usuários.**

**Sketch:**
- **Tela Inicial (Feed):**
- Barra de navegação lateral.
- Seção principal com posts de outros usuários.
- Botão para criar postagens de práticas sustentáveis.
- Dicas sobre reutilização de resíduos têxteis ao lado.

**Storyboard:**
- Usuário faz login: Usuário insere suas credenciais e entra no sistema.
- Acesso ao Feed: O usuário é redirecionado para a página inicial, onde visualiza postagens de outros usuários.
- Visualização de Posts: O usuário navega pela página e vê dicas de sustentabilidade fornecidas por administradores e visualiza posts de outros usuários.

**Cenários de Validação:**
- **Cenário 1: Acesso e uso da página inicial com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar a página inicial,
Então eu devo ser capaz de ver uma interface clara e atraente,
E eu devo poder postar minhas próprias práticas,
E visualizar dicas sobre reutilização de resíduos têxteis.
- **Cenário 2: Tentativa de login sem credenciais corretas:**
Dado que eu não tenha inserido minhas credenciais corretamente,
Quando eu tentar fazer login no sistema,
Então uma mensagem de erro "Credenciais inválidas" deve aparecer,
E o acesso ao sistema deve ser negado.
- **Cenário 3: Acesso ao Feed com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E acessar o Feed,
Então eu devo ser capaz de visualizar posts de outros usuários,
E receber informações sobre sustentabilidade dos administradores.
- **Cenário 4: Falha ao acessar o Feed:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E houver uma falha no carregamento do Feed,
Então uma mensagem de erro "Erro ao carregar o Feed, tente novamente mais tarde" deve aparecer.
- **Cenário 5: Tentativa de postar sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

### História 2: Postagem de Práticas Sustentáveis

**Como usuário registrado, quero postar minhas próprias práticas sobre sustentabilidade na página inicial, para compartilhar ações sustentáveis com outros usuários.**

**Sketch:**
- **Página de Criação de Post:**
- Formulário para inserção de título e descrição.
- Botão para anexar imagens ou vídeos.
- Botão de publicação ao final do formulário.
- Opção de adicionar tags relacionadas à prática sustentável.

**Storyboard:**
- Usuário faz login: O usuário entra no sistema inserindo suas credenciais.
- Acesso ao Feed: O usuário é redirecionado para a página inicial, onde visualiza o botão "Criar Post".
- Criação de Post: O usuário clica no botão, preenche os detalhes da prática sustentável e anexa imagens ou vídeos relevantes.
- Postagem Concluída: O usuário confirma a postagem, que aparece no feed de outros usuários.

**Cenários de Validação:**
- **Cenário 1: Postagem de prática sustentável com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu fizer login no sistema,
E tentar postar uma prática sustentável,
Então o post deve ser criado com sucesso e aparecer no Feed.
- **Cenário 2: Tentativa de postar sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar postar uma prática sustentável,
Então uma mensagem "Você precisa estar logado para postar" deve aparecer.

### História 3: Curtir e Comentar Postagens de Outros Usuários

**Como usuário registrado, quero poder curtir e comentar postagens de outros usuários, para interagir com o conteúdo e expressar minha opinião ou interesse.**

**Sketch:**
- **Feed de Postagens:**
- Cada postagem tem um ícone de "curtir" e um campo para adicionar comentários.
- Exibição de contador de curtidas e comentários em cada postagem.
- Seção de comentários que exibe respostas de outros usuários.

**Storyboard:**
- Usuário faz login: O usuário insere suas credenciais e acessa o feed de postagens.
- Curtir Postagem: O usuário clica no ícone de "curtir" em uma postagem para registrar seu interesse. O contador de curtidas é atualizado.
- Comentar Postagem: O usuário escreve um comentário no campo apropriado abaixo da postagem e clica em "enviar". O comentário é adicionado à seção de comentários da postagem.
- Visualizar Comentários: O usuário pode ver comentários feitos por outros usuários e responder diretamente.

**Cenários de Validação:**
- **Cenário 1: Curtir postagem com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu clicar no ícone de "curtir" em uma postagem,
Então o contador de curtidas deve ser atualizado corretamente e refletir meu interesse.
- **Cenário 2: Comentar postagem com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu adicionar um comentário e clicar em "enviar",
Então o comentário deve aparecer imediatamente na seção de comentários da postagem.
- **Cenário 3: Visualização de curtidas e comentários com sucesso:**
Dado que eu esteja visualizando o feed de postagens,
Quando houver curtidas e comentários na postagem,
Então o número de curtidas e os comentários devem ser exibidos corretamente.
- **Cenário 4: Tentativa de curtir ou comentar sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar curtir ou comentar em uma postagem,
Então uma mensagem "Você precisa estar logado para curtir ou comentar postagens" deve aparecer.

### História 4: Favoritar Postagens de Outros Usuários

**Como usuário registrado, quero poder favoritar postagens de outros usuários, para salvar conteúdos interessantes e acessá-los facilmente depois.**

**Sketch:**
- **Feed de Postagens:**
- Cada postagem tem um ícone de "favoritar" ao lado.
- Botão para acessar a aba de postagens favoritas no perfil do usuário.

**Storyboard:**
- Usuário faz login: O usuário insere suas credenciais e acessa o feed de postagens.
- Favoritar Postagem: O usuário clica no ícone de "favoritar" em uma postagem que deseja salvar.
- Acesso às Postagens Favoritas: O usuário navega até seu perfil e acessa a aba de postagens favoritas, onde visualiza as postagens que favoritou.

**Cenários de Validação:**
- **Cenário 1: Favoritar postagem com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu clicar no ícone de "favoritar" em uma postagem,
Então ela deve ser salva na minha lista de favoritos.
- **Cenário 2: Visualização de postagens favoritas com sucesso:**
Dado que eu esteja logado,
Quando eu acessar minha aba de postagens favoritas,
Então eu devo ser capaz de visualizar os posts que favoritei.
- **Cenário 3: Tentativa de favoritar sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar favoritar uma postagem,
Então uma mensagem "Você precisa estar logado para favoritar postagens" deve aparecer.

### História 5: Visualização de Detalhes do Produto

**Como usuário registrado, quero visualizar as informações completas de um produto, para tomar decisões conscientes sobre compras sustentáveis.**

**Sketch:**
- **Tela com Lista de Produtos:**
- Produtos listados com imagem e nome.
- Botão "Ver Detalhes" em cada produto que dará informações do produto.

**Storyboard:**
Usuário faz login: O usuário insere suas credenciais e acessa a lista de produtos.
Visualização das Informações: O usuário visualiza a imagem, descrição e informações sobre o material reutilizado.

**Cenários de Validação:**
- **Cenário 1: Visualização dos detalhes do produto com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu clicar em "Ver Detalhes" de um produto,
Então eu devo ser capaz de ver as informações completas do produto.
- **Cenário 2: Falha ao carregar a página de detalhes do produto:**
Dado que eu tenha um perfil de usuário registrado,
Quando houver uma falha no carregamento da página de detalhes do produto,
Então uma mensagem "Erro ao carregar detalhes do produto, tente novamente mais tarde" deve aparecer.
- **Cenário 3: Tentativa de visualizar detalhes sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar visualizar detalhes de um produto,
Então uma mensagem "Você precisa estar logado para visualizar detalhes do produto" deve aparecer.

### História 6: Receber Notificação Automática ao Se Interessar por um Produto

**Como usuário registrado, quero receber uma mensagem automática via e-mail, para ser notificado quando demonstrar interesse em um produto.**

**Sketch:**
- **Página de Detalhes do Produto:**
- Botão “Receber notificação” sobre o produto.

**Storyboard:**
- Usuário faz login: O usuário insere suas credenciais e entra no sistema.
- Acesso à Página de Detalhes do Produto: O usuário navega até a página de detalhes de um produto de interesse.
- Solicitação de Notificação: O usuário clica no botão "Receber notificação" e escolhe o método de recebimento (WhatsApp ou e-mail).
- Confirmação de Notificação: O sistema envia uma mensagem automática com informações do produto escolhido.

**Cenários de Validação:**
- **Cenário 1: Envio de mensagem automática com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu clicar em "Receber notificação",
Então eu devo receber uma mensagem automática com informações sobre o produto escolhido no método selecionado.
- **Cenário 2: Tentativa de usar a função sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar usar a função de "Receber notificação",
Então uma mensagem "Você precisa estar logado para usar essa função" deve aparecer.
- **Cenário 3: Confirmação de método de notificação:**
Dado que eu tenha escolhido um método de notificação,
Quando eu confirmar a solicitação,
Então uma mensagem de confirmação com o método escolhido deve ser exibida.

### História 7: Cadastramento de Novos Pontos de Doação

**Como administrador, quero cadastrar novos pontos de doação e lojas, para mantê-los atualizados no sistema.**

**Sketch:**
- **Interface Administrativa:**
- Botão "Cadastrar Ponto".
- Formulário para inserção de nome e endereço.
- Botão "Confirmar Cadastro".

**Storyboard:**
- Administrador faz login: O administrador insere suas credenciais.
- Acesso ao Menu de Cadastramento: O administrador navega até a seção de "Cadastrar Ponto".
- Inserção de Detalhes: O administrador preenche o formulário com informações do ponto de doação.
- Cadastro Concluído: O administrador confirma o cadastro, que aparece no mapa.

**Cenários de Validação:**
- **Cenário 1: Cadastramento de novos pontos de doação ou lojas com sucesso:**
Dado que eu seja um administrador autenticado,
Quando eu preencher o formulário com as informações do ponto de doação ou loja e clicar em "Confirmar Cadastro",
Então o ponto de doação ou loja deve ser adicionado com sucesso no sistema e aparecer no mapa.
- **Cenário 2: Tentativa de cadastrar sem permissão de administrador:**
Dado que eu não tenha permissões de administrador,
Quando eu tentar acessar a função de cadastramento de novos pontos de doação ou lojas,
Então o sistema deve bloquear o acesso e exibir a mensagem "Permissão negada. Apenas administradores podem cadastrar novos pontos."

### História 8: Visualização de Locais no Mapa

**Como usuário registrado, quero ver os pontos de doação e lojas no mapa, para localizar rapidamente o mais próximo de mim.**

**Sketch:**
- **Tela de Mapa:**
- Mapa interativo com ícones indicando pontos de doação e lojas.
- Opção de filtro para selecionar o tipo de local (loja, ponto de doação).
- Ao clicar em um ponto, exibe informações detalhadas (endereço, horário, serviços oferecidos).

**Storyboard:**
- Usuário faz login: O usuário insere suas credenciais e acessa o sistema.
- Acesso ao Mapa: O usuário navega até a seção de mapa para visualizar os pontos.
- Interação com o Mapa: O usuário utiliza os filtros para selecionar tipos de locais de interesse (ponto de doação ou loja).
- Visualização de Detalhes: Ao clicar em um ponto no mapa, o usuário vê informações detalhadas, como endereço e horários de funcionamento.

**Cenários de Validação:**
- **Cenário 1: Visualização de locais no mapa com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu acessar a seção de mapa,
Então os pontos de doação e lojas devem ser exibidos corretamente no mapa interativo.
- **Cenário 2: Falha ao visualizar o mapa por problemas de GPS:**
Dado que eu tenha um perfil de usuário registrado,
Quando houver um problema com o GPS ou serviço de localização,
Então uma mensagem de erro "Erro ao carregar o mapa" deve aparecer.
- **Cenário 3: Tentativa de visualizar o mapa sem estar logado:**
Dado que eu não esteja logado no sistema,
Quando eu tentar acessar a seção de mapa,
Então uma mensagem "Você precisa estar logado para acessar o mapa" deve aparecer.

### História 9: Sistema de Pontuação e Recompensas

**Como usuário registrado, quero visualizar meus créditos acumulados e trocá-los por recompensas, para me beneficiar por ações sustentáveis.**

**Sketch:**
- **Tela de Recompensas:**
- Exibição do saldo de créditos acumulados.
- Lista de recompensas disponíveis, com imagem, descrição e valor em créditos.
- Botão para trocar créditos por uma recompensa específica.
- Tela de confirmação de troca realizada.

**Storyboard:**
- Usuário faz login: O usuário insere suas credenciais e entra no sistema.
- Acesso à Aba de Recompensas: O usuário navega até a seção de recompensas, onde visualiza seu saldo de créditos acumulados.
- Seleção de Recompensa: O usuário escolhe uma recompensa disponível e confirma a troca.
- Confirmação: O sistema confirma a troca e atualiza o saldo de créditos.

**Cenários de Validação:**
- **Cenário 1: Visualização de créditos acumulados com sucesso:**
Dado que eu tenha um perfil de usuário registrado,
Quando eu acessar a aba de recompensas,
Então meu saldo de créditos acumulados deve ser exibido corretamente.
- **Cenário 2: Troca de créditos por recompensas com sucesso:**
Dado que eu tenha créditos suficientes,
Quando eu selecionar uma recompensa e confirmar a troca,
Então a recompensa deve ser liberada com sucesso e meu saldo de créditos atualizado automaticamente.
- **Cenário 3: Tentativa de trocar créditos insuficientes:**
Dado que eu não tenha créditos suficientes,
Quando eu tentar trocar créditos por uma recompensa,
Então uma mensagem de erro "Créditos insuficientes para esta recompensa" deve aparecer.

### História 10: Transferência de Créditos

**Como administrador do sistema, quero transferir créditos entre contas de usuários, para facilitar trocas de produtos para doação pelos créditos.**

**Sketch:**
- **Painel de Administração:**
- Área específica para gerenciamento de créditos com campo de busca para selecionar usuários.
- Seção para definir o valor de créditos a ser transferido.
- Botão de confirmação da transferência.
- Histórico de transferências realizado pelo administrador.

**Storyboard:**
- Administrador faz login: O administrador insere suas credenciais e acessa o painel de administração.
- Busca de Usuário: O administrador usa a função de busca para localizar a conta do usuário que irá receber ou enviar créditos.
- Inserção de Créditos: O administrador define a quantidade de créditos a ser transferida entre as contas dos usuários.
- Confirmação da Transferência: O administrador clica em "Transferir" e a operação é realizada. Uma mensagem de confirmação é exibida, e o histórico da operação é atualizado.
- Verificação do Histórico: O administrador pode acessar o histórico de transferências realizadas, verificando valores, data e usuários envolvidos.

**Cenários de Validação:**
- **Cenário 1: Transferência de créditos com sucesso:**
Dado que eu seja um administrador autenticado,
Quando eu selecionar um usuário e definir um valor de crédito para transferir,
Então a transferência de créditos deve ser realizada com sucesso, e os saldos dos usuários envolvidos devem ser atualizados corretamente.
- **Cenário 2: Verificação de transferência no histórico:**
Dado que eu tenha realizado uma transferência de créditos,
Quando eu acessar o histórico de transferências,
Então os detalhes da operação devem ser exibidos corretamente, incluindo usuários envolvidos, valor transferido e data.
- **Cenário 3: Tentativa de transferir créditos sem ser administrador:**
Dado que eu não tenha permissões de administrador,
Quando eu tentar acessar a função de transferência de créditos,
Então o sistema deve bloquear o acesso e exibir a mensagem "Permissão negada. Apenas administradores podem realizar transferências de créditos."

## Instruções de acesso ao projeto:


### Página Inicial
Ao acessar o **Recyfe**, você visualizará a **home**, onde estão listados todos os posts da comunidade. Esses posts podem ser curtidos, comentados e adicionados aos seus favoritos, mas para realizar qualquer ação, é necessário estar logado.

### Menu Lateral
O **Recyfe** possui duas abas laterais que organizam suas funcionalidades:

### Aba Lateral Esquerda
- **Home**: Página principal, com posts da comunidade.
- **Perfil**: Permite visualizar suas postagens e editar informações pessoais.
- **Mapa**: Mostra os pontos de doação e lojas cadastrados pelo administrador. Clique nos marcadores para visualizar mais detalhes sobre cada ponto.
- **E-commerce**: Exibe os produtos disponíveis para compra. Você pode adicionar itens ao carrinho e finalizar a compra via WhatsApp com um vendedor. Após a compra, um e-mail de confirmação será enviado.
- **Recompensas**: Lista recompensas que podem ser trocadas por créditos. Esses créditos são acumulados ao doar resíduos têxteis nos pontos de doação e são gerenciados pelo administrador.
- **Criar Post**: Permite criar novas postagens com texto e, opcionalmente, adicionar imagens. Clique em "Postar" para publicar.
- **Admin**: Direciona para o painel de administração (Django Admin), onde administradores podem:
  - Gerenciar créditos dos usuários.
  - Adicionar produtos.
  - Cadastrar pontos no mapa.
  - Inserir novas recompensas.

### Aba Lateral Direita
- **Favoritos**: Lista todos os posts que você marcou como favoritos.
- **Meus Resgates**: Mostra as recompensas que você já resgatou.
- **Log Out**: Permite sair da conta e retornar à home como visitante.

### Funcionalidades Detalhadas
1. **Perfil**: No perfil, é possível editar informações pessoais e acessar as postagens feitas por você.
2. **Mapa**: Navegue pelos pontos de doação e lojas cadastrados. Clique nos marcadores para ver informações específicas sobre cada local.
3. **E-commerce**: Compre produtos adicionando-os ao carrinho. Finalize a compra diretamente pelo WhatsApp com um vendedor. Após o processo, um e-mail confirmará a transação.
4. **Recompensas**: Resgate recompensas disponíveis com os créditos que você acumulou ao doar resíduos.
5. **Administração**: Ao acessar o painel administrativo como administrador, você terá controle sobre:
   - Créditos dos usuários.
   - Produtos disponíveis no e-commerce.
   - Pontos exibidos no mapa.
   - Recompensas para resgate.

### Acesso
- É possível navegar pela home e visualizar posts sem estar logado.
- Para interagir com posts, criar conteúdo ou acessar funcionalidades adicionais, é necessário realizar login ou cadastro.
- O login ou cadastro pode ser acessado na **aba lateral esquerda**.

## Diagrama de atividades do sistema:

![Sem título](https://github.com/user-attachments/assets/b581b8ce-a5d5-4872-bdc9-029d17f72362)

## Issues/bug tracker:

- Issues Abertas:

![Captura de tela 2024-11-28 174116](https://github.com/user-attachments/assets/c44f1470-932f-4d0d-8cb3-dab81c9c1e49)

![Captura de tela 2024-11-28 174230](https://github.com/user-attachments/assets/6c1b0275-6385-4b11-8777-5c14190ee8ea)

- Issues Fechadas:

![Captura de tela 2024-11-28 223008](https://github.com/user-attachments/assets/1cdbeec5-07b1-441f-95e6-238db0859e45)
 
![Captura de tela 2024-11-28 223035](https://github.com/user-attachments/assets/d4fb0aac-1710-4220-9461-75de77829327)

## Print dos quadros da Sprints/Backlog:

![Captura de tela 2024-10-28 142443](https://github.com/user-attachments/assets/d7b6c565-2ce1-4bf0-b3d5-ac42b9a769d0)

![Captura de tela 2024-10-28 141316](https://github.com/user-attachments/assets/09edba1f-386d-4662-9c29-2a1c717e6fc1)

## Programacao em Par:

Na segunda etapa (SR2) do projeto **Recyfe**, focamos na implementação de funcionalidades estratégicas alinhadas às histórias de usuário definidas, testes automatizados e integração contínua. A equipe foi organizada em pares e trios, com responsabilidades específicas. Abaixo, destacamos as experiências e resultados obtidos durante a programação em par, enfatizando os benefícios e desafios enfrentados.

---

### Par 01 – Luís Guilherme e João Lucas Robalinho (Front-end)
**Responsabilidades:**  
- Implementação de funcionalidades do Feed (visualização de postagens, curtidas, comentários e criação de novos posts).  

**Destaques:**  
- Integração contínua permitiu detectar erros de design e lógica precocemente.  
- Interface final foi limpa, funcional e alinhada às histórias definidas.  

**Aprendizados:**  
- Revisões conjuntas ao final de cada sessão foram cruciais para a qualidade do código.  
- Apesar das dificuldades iniciais na adaptação ao ritmo da programação em par, os resultados superaram as expectativas.

---

### Par 02 – Henrique e Guilherme Mourão (Sistema de Créditos e Testes Automatizados)
**Responsabilidades:**  
- Implementação do sistema de créditos (gerenciamento de recompensas por práticas sustentáveis).  
- Criação de testes automatizados e pipeline de integração contínua (CI/CD).  

**Destaques:**  
- A troca de conhecimentos técnicos foi um diferencial.  
- Henrique liderou a definição da arquitetura, enquanto Guilherme Mourão integrou a pipeline automatizada.  

**Aprendizados:**  
- Suporte mútuo foi determinante para solucionar problemas de integração durante o deploy.  

---

### Par 03 – Caio Lira e Jerônimo (Localização Geográfica e e-Commerce)
**Responsabilidades:**  
- Desenvolvimento da visualização de pontos de doação no mapa.  
- Implementação da funcionalidade de e-commerce.  

**Destaques:**  
- Feedbacks regulares entre os membros garantiram uma conexão coesa entre as funcionalidades.  
- A localização geográfica exigiu ajustes em tempo real para melhorar a precisão dos marcadores.  

**Aprendizados:**  
- Comunicação frequente foi vital para alinhar o design do mapa aos requisitos do e-commerce.  
- Revisões conjuntas garantiram qualidade e integração entre os módulos.

---

### Conclusões
A programação em par foi essencial para o sucesso da segunda etapa do projeto **Recyfe**. Apesar de não ser aplicada integralmente em todos os momentos, a abordagem colaborativa proporcionou maior qualidade no código, redução de inconsistências e troca contínua de conhecimento entre os membros.

</details>
