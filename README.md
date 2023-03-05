
<img src="docs\OpenGenAPI-GIF.gif" alt="OpenGenAPI">

# :globe_with_meridians: **PassGenAPI**
  A :globe_with_meridians:**PassGenAPI** é uma ferramenta divertida e útil para gerar senhas fortes:lock::muscle: e seguras para você e seus usuários!:man_technologist: Com a nossa API, você pode facilmente criar senhas aleatórias com vários comprimentos e níveis de complexidade. Escolha entre caracteres especiais, letras maiúsculas e minúsculas, números e em breve muito mais para personalizar a sua senha! Além disso, você pode integrar facilmente a nossa API com outras ferramentas para tornar a sua aplicação ainda mais segura e confiável. Então, por que usar senhas fáceis de adivinhar quando você pode ter senhas fortes e seguras com a PassGenAPI? 💂🏼‍♂️


## **Como usar**

Para utilizar a **PassGenAPI**, você deve enviar uma solicitação HTTP POST para o endpoint "**https://pass-gen-api.vercel.app/password_definitions**". A API aceita os seguintes parâmetros:

**password_length**: define o comprimento da senha. O valor padrão é 12. <br>
**number_of_passwords**: define o número de senhas que serão geradas. O valor padrão é 1. <br>
**type_of_characters**: define o tipo de caracteres que serão utilizados para gerar a senha. <br>As opções disponíveis são **lowercase**, **uppercase**, **digits** e **symbols**. O valor padrão é todos os tipos de caracteres.

### **Exemplo de uso em Python com requests**

```console
$ pip install requests
```

```python
import json
import requests

# Define o endpoint da API
endpoint = "https://pass-gen-api.vercel.app/password_definitions"

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

### **Exemplo de uso em Python com urllib**

```python
import urllib.request
import json

# Define o endpoint da API
endpoint = "https://pass-gen-api.vercel.app/password_definitions"

# Define os dados que serão enviados no formato JSON
password_data = {
    "password_length": 10,
    "number_of_passwords": 3,
    "type_of_characters": ["digits", "lowercase", "symbols"]
}

# Converte os dados para o formato JSON
json_password_data = json.dumps(password_data).encode("utf8")

# Cria uma solicitação POST com os dados em JSON
request = urllib.request.Request(url=endpoint, data=json_password_data)

# Envia a solicitação POST para o endpoint da API
response = urllib.request.urlopen(request)

# Lê a resposta da API e a decodifica do formato JSON
response_data = json.loads(response.read().decode('utf8'))

# Exibe a resposta da API
print(response_data.json()['password'])

```


## **Instalação**

Para utilizar a PassGenAPI localmente, siga os passos abaixo:

1. **Clone o repositório em seu ambiente local:**
    ```console
    $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
    ```

2. **Crie um ambiente virtual com o comando apropriado para o seu sistema operacional:**
    * **Windows:**
        ```console
        $ py -m venv nome_do_ambiente
        ```
    * **Linux/macOS:**
        ```console
        $ python3 -m venv nome_do_ambiente
        ```

3. **Ative o ambiente virtual:**
    * **Windows:**
        ```console
        $ nome_do_ambiente\Scripts\activate
        ```
    * **Linux/macOS:**
        ```console
        $ source nome_do_ambiente/bin/activate
        ```

4. **Instale as dependências com o seguinte comando:**
    ```console
    $ pip install -r requirements.txt
    ```
