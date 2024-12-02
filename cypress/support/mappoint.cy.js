describe('Teste de Acesso ao Admin e Registro de Mappoint', () => {
    const baseUrl = 'http://127.0.0.1:8000'; // URL base da aplicação.
  
  
    it('Deve acessar o painel de administração, realizar login e registrar dados de mappoint', () => {
      // Realizar o login no painel de administração com o super usuário
      cy.visit(`${baseUrl}/admin/login/`); // Acessar a página de login do admin
  
  
      // Preencher os campos de login
      cy.get('#id_username').type('admin'); // Nome de usuário do admin
      cy.get('#id_password').type('admin'); // Senha do admin
      cy.get('.submit-row > input').click(); // Clicar no botão de login
  
  
      // Esperar até o painel de administração ser carregado
      cy.get('.dashboard').should('be.visible'); // Espera por um elemento visível na página de administração
  
  
      // Acessar o painel de mappoint
      cy.get('.model-mappoint > th > a', { timeout: 10000 }).click(); // Clicar no link para acessar o mappoint
      cy.url().should('include', '/admin/network/mappoint/'); // Verifica se a URL contém a parte correta
  
  
      // Preencher o formulário de mappoint
      cy.get('li > .addlink').click(); // Clicar no botão de adicionar novo mappoint
  
  
      // Preencher os campos
      cy.get('#id_name').type('Nome do Mappoint'); // Preencher nome
      cy.get('#id_description').type('Descrição do Mappoint'); // Preencher descrição
      cy.get('#id_latitude').type('40.712776'); // Preencher latitude
      cy.get('#id_longitude').type('-74.005974'); // Preencher longitude
  
  
      // Finalizar o registro
      cy.get('.default').click(); // Clicar no botão de salvar
  
  
      // Verificar se o mappoint foi registrado corretamente
      cy.url().should('include', '/admin/network/mappoint/'); // Verificar se está na lista de mappoints
      cy.contains('Nome do Mappoint').should('be.visible'); // Verificar se o nome do mappoint aparece na lista
    });
  });
  
  