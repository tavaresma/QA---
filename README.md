# Controle de Qualidade — QA na Prática

## Teste Unitário — Validação de CPF (Jest)

```javascript
function validarCPF(cpf) {
  return /^\d{11}$/.test(cpf); // Verifica se tem exatamente 11 dígitos
}

test('CPF válido com 11 números', () => {
  expect(validarCPF('12345678901')).toBe(true);
});

test('CPF inválido com letras', () => {
  expect(validarCPF('abc12345678')).toBe(false);
});

test('CPF inválido com menos de 11 dígitos', () => {
  expect(validarCPF('12345678')).toBe(false);
});
```

---

##  Teste de Integração — Autenticação + E-mail

```javascript
function autenticar(email, senha) {
  return email === 'teste@teste.com' && senha === '123456';
}

function enviarEmailRecuperacao(email) {
  return email.includes('@') ? 'E-mail enviado' : 'E-mail inválido';
}

test('Usuário válido pode recuperar a senha', () => {
  const email = 'teste@teste.com';
  const senha = '123456';

  if (autenticar(email, senha)) {
    const resultado = enviarEmailRecuperacao(email);
    expect(resultado).toBe('E-mail enviado');
  }
});
```

---

##  Teste de Interface com Cypress

```javascript
// cypress/e2e/login.cy.js
describe('Teste de Login', () => {
  it('Deve fazer login com credenciais válidas', () => {
    cy.visit('http://localhost:3000/login');
    cy.get('#email').type('usuario@email.com');
    cy.get('#senha').type('senhaSegura123');
    cy.get('button[type=submit]').click();

    // Verifica se redireciona para o dashboard
    cy.url().should('include', '/dashboard');
  });
});
```

---

## Teste de Regressão — Cálculo de Desconto

```javascript
function calcularTotal(valor, desconto) {
  return valor - desconto;
}

test('Cálculo do total com desconto', () => {
  expect(calcularTotal(100, 10)).toBe(90);
});
```

---

### Observações
- Os testes unitários foram escritos com **Jest**.
- O teste de automação de interface foi feito com **Cypress**.
- Todos os testes simulam situações reais de um sistema simples de login e compra.

