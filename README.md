<img src="docs\src\PassGenAPI-GIF.gif" alt="PassGenAPI">


# :globe_with_meridians: **PassGenAPI** 
  A :globe_with_meridians:**PassGenAPI** é uma ferramenta divertida e útil para gerar senhas fortes:lock::muscle: e seguras para você e seus usuários!:man_technologist: Com a nossa API, você pode facilmente criar **senhas aleatórias** com vários comprimentos e níveis de complexidade e **hashes**. Escolha entre caracteres especiais, letras maiúsculas e minúsculas, números e em breve muito mais para personalizar a sua senha! Além disso, você pode integrar facilmente a nossa API com outras ferramentas para tornar a sua aplicação ainda mais segura e confiável. Então, por que usar senhas fáceis de adivinhar quando você pode ter senhas fortes e seguras com a PassGenAPI? 💂🏼‍♂️

<div align="center" alt="contatos">
  <a href="https://github.com/Nicolas-albu/PassGenAPI/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/Nicolas-albu/PassGenAPI?style=for-the-badge" target="_blank"></a>
  <img src="https://img.shields.io/badge/version-1.1.10-blue?style=for-the-badge" target="_blank">
</div>

##

  #### :earth_americas: **Idioma da documentação:**
  A documentação da PassGenAPI está disponível em inglês e português. Para escolher o idioma desejado, basta clicar no idioma seguinte. Todos os exemplos de código, instruções e explicações estarão disponíveis no idioma escolhido para facilitar a compreensão e utilização da API.

  **USA** [**English**](docs/README-en.md)

  **BRA** [**Português**](README.md)

## :page_with_curl: Sumário da Documentação
- [:thinking: **Para o que posso utilizar a PassGenAPI?**](#para-o-que-posso-utilizar-a-passgenapi)
- [:computer: **Como usar**](#computer-como-usar)
- [:man_technologist: **Instalação**](#man_technologist-instalação)
- [:pushpin: **Sobre a PassGenAPI**](#pushpin-sobre-a-passgenapi)
- [:rotating_light: **Licença**](#rotating_light-licença)

## :thinking: **Para o que posso utilizar a PassGenAPI?**

| **Funcionalidades** | **Descrição** |
| :---: | --- |
| **password** | geração de senhas personalizadas com vários comprimentos, quantidade de senhas e caracteres específicos como símbolos, lowercase, uppercase e digitos |
| **hash** | geração de hashes de diversos tipos, como MD5, SHA-1, SHA-2 e SHA-3

## :computer: **Como usar**

Você pode usar a PassGenAPI para 

<details>
<summary> <b>:point_right:geração de senhas aleatórias</b> </summary>

Enviar uma solicitação HTTP POST para o endpoint "**https://passgenapi.onrender.com/password**". A API aceita os seguintes parâmetros:

|    Parâmetros   | Tipo | Descrição  | Opções | Valor Padrão |
|      :---:      | :---:  |    ---     |  ---   |    :---:     |
| **password_length** | **int** | define o comprimento da senha | | 12 | 
| **number_of_passwords** | **int** | define o número de senhas que serão geradas | | 1 |
| **types_of_characters** | **str** \| **list[str]** | define o tipo de caracteres que serão utilizados para gerar a senha | **lowercase**, **uppercase**, **digits** e **symbols** | todos os tipos de caracteres |

<!--[Quer ver um exemplo da utilização destes parâmetros?](#com-requests)-->

<details>
<summary> <b>:point_right:Quer ver um exemplo da utilização destes parâmetros?</b> </summary>

```python
import json
import requests

# Define o endpoint da API
endpoint = "https://passgenapi.onrender.com/password"

# Define os dados que serão enviados no formato JSON
password_data = {
    "password_length": 10,
    "number_of_passwords": 3,
    "type_of_characters": ["digits", "lowercase"]
}

# Converte os dados para o formato JSON
json_password_data = json.dumps(password_data)

# Envia a requisição POST para o endpoint da API com os dados em JSON
response = requests.post(url=endpoint, data=json_password_data)

# Exibe a resposta da API
print(response.json()['password'])
```
</details>

</details>

<details>
<summary><b>:point_right:geração de hashes</b></summary>

Enviar uma solicitação HTTP POST para o endpoint "**https://passgenapi.onrender.com/hash**". A API aceita os seguintes parâmetros:

|    Parâmetros        | Tipo    | Descrição  | Opções |
|      :---:           | :---:   |    ---     | :---:  |
| **data_for_encrypt** | **str** | define o dado que será criptografado |
| **hash_type**        | **str** | define o tipo de hash que será utilizado | **sha1**, **sha224**, **sha256**, **sha384**, **sha3-256** e **md5** |

</details>


<details>
<summary> <b>:point_right:Exemplo de requisições</b> </summary>

### **Com requests:**

```console
$ pip install requests
```

```python
import json
import requests

# Define o endpoint da API
endpoint = "https://passgenapi.onrender.com/password"

# Define os dados que serão enviados no formato JSON
password_data = {
    "password_length": 10,
    "number_of_passwords": 3,
    "type_of_characters": ["digits", "lowercase", "symbols"]
}

# Converte os dados para o formato JSON
json_password_data = json.dumps(password_data)

# Envia a requisição POST para o endpoint da API com os dados em JSON
response = requests.post(url=endpoint, data=json_password_data)

# Exibe a resposta da API
print(response.json()['password'])

```
</details>


## :man_technologist: **Instalação**

<details>
<summary> <b>:point_right:Utilizar na máquina local</b> </summary>

Para utilizar a PassGenAPI localmente, siga os passos abaixo:

1. **Clone o repositório em seu ambiente local:**
    ```console
    $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
    ```

2. **Entre no repositório clonado:**
    ```console
    $ cd PassGenAPI
    ```

3. **Crie um ambiente virtual com o comando apropriado para o seu sistema operacional:**
    * **Windows:**
        ```console
        $ py -m venv nome_do_ambiente
        ```
    * **Linux/macOS:**
        ```console
        $ python3 -m venv nome_do_ambiente
        ```

4. **Ative o ambiente virtual:**
    * **Windows:**
        ```console
        (nome_do_ambiente)$ nome_do_ambiente\Scripts\activate
        ```
    * **Linux/macOS:**
        ```console
        (nome_do_ambiente)$ source nome_do_ambiente/bin/activate
        ```

5. **Instale as dependências com o seguinte comando:**
    ```console
    (nome_do_ambiente)$ pip install -r requirements.txt
    ```

6. **Na raiz do projeto PassGenAPI, execute o seguinte comando:**
    ```console
    (nome_do_ambiente)$ uvicorn passgenapi.main:app --host localhost --port 8000
    ```

    Esse comando faz com que rode o servidor no host local da sua máquina na porta 8000.

    :warning: **Observação:** você pode mudar o host e a porta apenas alterando os argumentos de `--host` e `--port`

</details>


<details>
<summary> <b>:point_right:Utilizar em um contâiner Docker</b> </summary>

1. **Clone o repositório em seu ambiente local:**
    ```console
    $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
    ```

2. **Entre no repositório clonado:**
    ```console
    $ cd PassGenAPI
    ```

3. **Crie uma imagem da PassGenAPI:**
    ```console
    $ docker image build -t image_passgenapi .
    ```

4. **Crie um container pela imagem recém-gerada:**
    ```console
    $ docker run -d --name container_passgenapi -p 80:80 image_passgenapi
    ```

</details>


## :rocket: **Versões**
### **v1.1.10**
A :globe_with_meridians:**PassGenAPI** versão 1.1.10 trouxe as seguintes melhorias:
- [x] Melhoria no encapsulamento dos métodos da classe PasswordGenerator
- [x] Adição de geração de hashes: HashGenerator
- [x] Melhoria nos testes unitários
- [x] Refatoração da classe PasswordGenerator
- [x] Melhoria na perfomance da memória
- [x] Implantação da API um contâiner Docker
- [x] Migração da Vercel para Render

### **v1.1.4**
A :globe_with_meridians:**PassGenAPI** versão 1.1.4 foi a primeira versão a entrar em produção na Vercel, sem contâiner Docker, apenas com FastAPI e Pytest:
- [x] Criação da classe de geração de senhas: PasswordGenerator
- [x] Deploy na Vercel

## :pushpin: **Sobre a PassGenAPI**
A :globe_with_meridians:**PassGenAPI** foi desenvolvida com um foco em alto desempenho, utilizando o framework web **FastAPI**:zap:. Com a utilização do FastAPI, a API oferece uma performance significativamente superior em relação a outras ferramentas similares, garantindo uma experiência ágil e eficiente ao usuário. O FastAPI é conhecido por sua eficiência e facilidade de uso, permitindo que a PassGenAPI seja desenvolvida de forma mais rápida e escalável. Além disso, o FastAPI fornece recursos como documentação automática e validação de tipos, tornando a criação e manutenção da API mais fácil e menos propensa a erros :heavy_check_mark:.

Além disso, a PassGenAPI foi testada com **Pytest** para garantir a qualidade do código e da aplicação. Os testes automatizados foram uma parte importante do processo de desenvolvimento de software, pois ajudaram a identificar problemas precocemente.

Além disso, estamos sempre trabalhando em novas implementações para oferecer ainda mais opções personalizáveis para a geração de senhas, como a recente implementação do Docker. Então, fique de olho nas atualizações futuras da PassGenAPI para ter acesso a novas funcionalidades e tornar a sua aplicação ainda mais segura e confiável! :lock:

<img src="https://img.shields.io/badge/version-1.1.10-blue?style=for-the-badge" target="_blank">

## :rotating_light: **Licença**

A PassGenAPI está sob a licença **Apache-2.0 license**, o que significa que você pode usar, modificar e distribuir o código-fonte da API para fins pessoais e comerciais. No entanto, você deve incluir a nota de direito autoral na sua distribuição e garantir que a mesma licença seja aplicada às suas modificações. A licença Apache-2.0 também inclui uma renúncia de garantias e uma limitação de responsabilidade, portanto, certifique-se de lê-la cuidadosamente antes de usar a PassGenAPI em seu projeto.

<a href="https://github.com/Nicolas-albu/PassGenAPI/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/Nicolas-albu/PassGenAPI?style=for-the-badge" target="_blank"></a>
