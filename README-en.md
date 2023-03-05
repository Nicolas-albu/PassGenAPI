
<img src="docs\OpenGenAPI-GIF.gif" alt="OpenGenAPI">

# :globe_with_meridians: **PassGenAPI** 
  The :globe_with_meridians:**PassGenAPI** is a fun and useful tool to generate passwords that are strong:lock::muscle: and safe for you and your users!:man_technologist: With our API, you can easily create random passwords with various lengths and levels of complexity. Choose from special characters, uppercase and lowercase letters, numbers and soon much more to customize your password! Furthermore, you can easily integrate our API with other tools to make your application even more secure and reliable. So why use easy to guess passwords when you can have strong and secure passwords with PassGenAPI? 💂🏼‍♂️

  Currently, PassGenAPI is at version **1.0.0**.

  #### :earth_americas: **Documentation language:**
  PassGenAPI documentation is available in English and Portuguese. To choose the desired language, just click on the next language. All code examples, instructions, and explanations will be available in your chosen language to make the API easier to understand and use.

  **USA** [**English**](README-en.md)

  **BRA** [**Português**](README.md)

## :computer: **How to use**

To use **PassGenAPI**, you must send an HTTP POST request to the endpoint "**https://pass-gen-api.vercel.app/password_definitions**". The API accepts the following parameters:

**password_length**: defines the length of the password. The default value is 12. <br>
**number_of_passwords**: defines the number of passwords that will be generated. The default value is 1. <br>
**type_of_characters**: defines the type of characters that will be used to generate the password. <br>The available options are **lowercase**, **uppercase**, **digits** and **symbols**. The default value is all character types.

### **Example usage in Python with requests:**

```console
$ pip install requests
```

```python
import json
import requests

# Defines the API endpoint
endpoint = "https://pass-gen-api.vercel.app/password_definitions"

# Defines the data that will be sent in JSON format
password_data = {
    "password_length": 10,
    "number_of_passwords": 3,
    "type_of_characters": ["digits", "lowercase", "symbols"]
}

# Convert data to JSON format
json_password_data = json.dumps(password_data)

# Send the POST request to the API endpoint with the data in JSON
response = requests.post(url=endpoint, data=json_password_data)

# Displays the API response
print(response.json()['password'])

```

### **Example usage in Python with urllib:**

```python
import urllib.request
import json

# Defines the API endpoint
endpoint = "https://pass-gen-api.vercel.app/password_definitions"

# Defines the data that will be sent in JSON format
password_data = {
    "password_length": 10,
    "number_of_passwords": 3,
    "type_of_characters": ["digits", "lowercase", "symbols"]
}

# Convert data to JSON format
json_password_data = json.dumps(password_data).encode("utf8")

# Creates a POST request with the data in JSON
request = urllib.request.Request(url=endpoint, data=json_password_data)

# Sends the POST request to the API endpoint
response = urllib.request.urlopen(request)

# Reads the API response and decodes it from JSON format
response_data = json.loads(response.read().decode('utf8'))

# Displays the API response
print(response_data.json()['password'])

```

## :man_technologist: **Installation**

To use PassGenAPI locally, follow the steps below:

1. **Clone the repository in your local environment:**
    ```console
    $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
    ```

2. **Create a virtual environment with the appropriate command for your operating system:**
    * **Windows:**
        ```console
        $ py -m venv environment_name
        ```
    * **Linux/macOS:**
        ```console
        $ python3 -m venv environment_name
        ```

3. **Activate the virtual environment:**
    * **Windows:**
        ```console
        $ environment_name\Scripts\activate
        ```
    * **Linux/macOS:**
        ```console
        $ source environment_name/bin/activate
        ```

4. **Install the dependencies with the following command:**
    ```console
    $ pip install -r requirements.txt
    ```

## :pushpin: **About PassGenAPI**
:globe_with_meridians:**PassGenAPI** was developed with a focus on high performance, using the **FastAPI**:zap: web framework. With the use of FastAPI, the API offers significantly superior performance compared to other similar tools, ensuring an agile and efficient user experience. FastAPI is known for its efficiency and ease of use, allowing PassGenAPI to be developed more quickly and scalably. In addition, FastAPI provides features such as automatic documentation and type validation, making creating and maintaining the API easier and less error-prone:heavy_check_mark:.

Furthermore, PassGenAPI has been tested with **Pytest** to ensure code and application quality. Automated testing was an important part of the software development process as it helped to identify problems early.

Additionally, we are always working on new implementations to provide even more customizable options for password generation. So, keep an eye out for future updates to PassGenAPI to gain access to new features and make your application even more secure and reliable! :lock:

Currently, PassGenAPI is at version **1.0.0**.

## :rotating_light: **License**

PassGenAPI is under the **Apache-2.0 license**, which means you can use, modify and distribute the API source code for personal and commercial purposes. However, you must include the copyright notice with your distribution and ensure that the same license applies to your modifications. The Apache-2.0 license also includes a disclaimer of warranties and a limitation of liability, so make sure you read it carefully before using PassGenAPI in your project.