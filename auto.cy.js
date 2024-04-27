/// <reference types="cypress" />

describe('Form Submission', () => {
    it('should fill and submit the form', () => {
      cy.visit('https://raghavarora09.github.io/selenium-basic/')
  
      cy.get('#name').should('be.visible').type('John Doe').wait(500)
      cy.get('#address').should('be.visible').type('111 lane 2, New delhi, India').wait(500)
      cy.get('#subscribe').should('be.visible').check().wait(500)
  
      cy.get('input[name="gender"]').should('be.visible').then(($radioButtons) => {
        cy.wrap($radioButtons)
          .filter((index, radio) => radio.value === 'male')
          .check()
          .wait(500)
      })
  
      cy.get('#country').should('be.visible').then(($dropdown) => {
        cy.wrap($dropdown).select('India').wait(500)
      })
  
      cy.get('button[type="submit"]').should('be.visible').click().wait(500)
  
      cy.on('window:alert', (text) => {
        expect(text).to.exist
        console.log(text)
      })
    })
  })    
