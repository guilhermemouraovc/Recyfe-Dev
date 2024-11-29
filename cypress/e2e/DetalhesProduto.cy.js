describe('Testes de Visualização de Detalhes do Produto', () => {
  
    // Cenário 1: Visualização dos detalhes do produto com sucesso
    it('Deve permitir a visualização dos detalhes do produto com sucesso', () => {
      // Acessar a página de login
      cy.visit('http://127.0.0.1:8000/login') // Substitua pela URL de login
      cy.get('input[name="username"]').type('Soca fofinho') // Nome de usuário
      cy.get('input[name="password"]').type('SUA_SENHA') // Senha
      cy.get('button[type="submit"]').contains('Log in').click() // Submeter o login
  
      // Verificar se o login foi bem-sucedido
      cy.url().should('include', '/posts') // O usuário deve ser redirecionado para a página de posts
  
      // Verificar se a lista de produtos está visível
      cy.get('.product-list').should('be.visible') // Substitua pela classe correta da lista de produtos
  
      // Clicar no botão "Ver Detalhes" de um produto específico
      cy.get('.product-card') // Substitua pela classe de cada produto
        .first()
        .find('button')
        .contains('Ver Detalhes')
        .click()
  
      // Verificar se as informações detalhadas do produto são exibidas
      cy.url().should('include', '/produto') // Substitua pela URL correta da página de detalhes
      cy.get('.product-details').should('be.visible') // Verifica se as informações do produto são exibidas
    })
  
    // Cenário 2: Falha ao carregar a página de detalhes do produto (sem login)
    it('Deve exibir uma mensagem de erro quando tentar visualizar os detalhes sem estar logado', () => {
      // Acessar diretamente a página de detalhes do produto sem estar logado
      cy.visit('http://127.0.0.1:8000/produto/some-product-slug') // Substitua pela URL de detalhes do produto com slug
  
      // Verificar se o usuário foi redirecionado para a página de login
      cy.url().should('include', '/login')
  
      // Verificar se a mensagem de erro aparece
      cy.contains('Você precisa estar logado para visualizar detalhes do produto').should('be.visible')
    })
  
    // Cenário 3: Tentar visualizar detalhes do produto sem estar logado (falha ao tentar acessar a página diretamente)
    it('Deve exibir uma mensagem informando que o login é necessário', () => {
      // Tentar acessar diretamente a página de detalhes de um produto
      cy.visit('http://127.0.0.1:8000/produto/some-product-slug') // Substitua pela URL de detalhes com slug
  
      // Verificar se a mensagem de login aparece
      cy.contains('Você precisa estar logado para visualizar os detalhes do produto').should('be.visible')
    })
  })
  