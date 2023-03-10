
<img src="docs\OpenGenAPI-GIF.gif" alt="OpenGenAPI">

# :globe_with_meridians: **PassGenAPI** 
  A :globe_with_meridians:**PassGenAPI** é uma ferramenta divertida e útil para gerar senhas fortes:lock::muscle: e seguras para você e seus usuários!:man_technologist: Com a nossa API, você pode facilmente criar senhas aleatórias com vários comprimentos e níveis de complexidade. Escolha entre caracteres especiais, letras maiúsculas e minúsculas, números e em breve muito mais para personalizar a sua senha! Além disso, você pode integrar facilmente a nossa API com outras ferramentas para tornar a sua aplicação ainda mais segura e confiável. Então, por que usar senhas fáceis de adivinhar quando você pode ter senhas fortes e seguras com a PassGenAPI? 💂🏼‍♂️

## :computer: **Como usar**

Para utilizar a **PassGenAPI**, você deve enviar uma solicitação HTTP POST para o endpoint "**https://pass-gen-api.vercel.app/password_definitions**". A API aceita os seguintes parâmetros:

**password_length**: define o comprimento da senha. O valor padrão é 12. <br>
**number_of_passwords**: define o número de senhas que serão geradas. O valor padrão é 1. <br>
**type_of_characters**: define o tipo de caracteres que serão utilizados para gerar a senha. <br>As opções disponíveis são **lowercase**, **uppercase**, **digits** e **symbols**. O valor padrão é todos os tipos de caracteres.

## :hammer_and_wrench: Implementações de Criptografias

### **Hashes**
- [X] MD5
- [X] SHA-1
- [X] SHA-2
- [X] SHA-3

### **Chave Simétrica**
- [ ] DES (Data Encryption Standard)
- [ ] 3DES (Triple Data Encryption Standard)
- [ ] AES (Advanced Encryption Standard)


### **Chave Assimétrica**
- [ ] RSA
- [ ] Diffie-Hellman
- [ ] ECC (Elliptic Curve Cryptography)

## :rotating_light: **Licença**

A PassGenAPI está sob a licença **Apache-2.0 license**, o que significa que você pode usar, modificar e distribuir o código-fonte da API para fins pessoais e comerciais. No entanto, você deve incluir a nota de direito autoral na sua distribuição e garantir que a mesma licença seja aplicada às suas modificações. A licença Apache-2.0 também inclui uma renúncia de garantias e uma limitação de responsabilidade, portanto, certifique-se de lê-la cuidadosamente antes de usar a PassGenAPI em seu projeto.