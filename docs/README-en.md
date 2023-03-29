<img src="docs\src\PassGenAPI-GIF.gif" alt="PassGenAPI">

# :globe_with_meridians: **PassGenAPI**
   :globe_with_meridians:**PassGenAPI** is a fun and useful tool to generate passwords that are strong:lock::muscle: and safe for you and your users!:man_technologist: With our API, you can easily create **random passwords** with various lengths and levels of complexity and **hashes**. Choose from special characters, uppercase and lowercase letters, numbers and soon much more to customize your password! Furthermore, you can easily integrate our API with other tools to make your application even more secure and reliable. So why use easy to guess passwords when you can have strong and secure passwords with PassGenAPI? 💂🏼‍♂️

<div align="center" alt="contacts">
   <a href="https://github.com/Nicolas-albu/PassGenAPI/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/ Nicolas-albu/PassGenAPI?style=for-the-badge" target="_blank"></a>
   <img src="https://img.shields.io/badge/version-1.1.10-blue?style=for-the-badge" target="_blank">
</div>

##

   #### :earth_americas: **Documentation language:**
   PassGenAPI documentation is available in English and Portuguese. To choose the desired language, just click on the next language. All code examples, instructions, and explanations will be available in your chosen language to make the API easier to understand and use.

   **USA** [**English**](docs/README-en.md)

   **BRA** [**Portuguese**](README.md)

## :page_with_curl: Documentation Summary
- [:thinking: **What can I use PassGenAPI for?**](#what-can-I-use-passgenapi-for)
- [:computer: **How to use**](#computer-how-to-use)
- [:man_technologist: **Installation**](#man_technologist-installation)
- [:pushpin: **About PassGenAPI**](#pushpin-about-passgenapi)
- [:rotating_light: **License**](#rotating_light-license)

## :thinking: **What can I use PassGenAPI for?**

| **Features** | **Description** |
| :---: | --- |
| **password** | generation of personalized passwords with various lengths, number of passwords and specific characters such as symbols, lowercase, uppercase and digits |
| **hash** | generation of hashes of different types, such as MD5, SHA-1, SHA-2 and SHA-3

## :computer: **How to use**

You can use the PassGenAPI to

<details>
<summary> <b>:point_right:generating random passwords</b> </summary>

Send an HTTP POST request to the "**https://passgenapi.onrender.com/password**" endpoint. The API accepts the following parameters:

| Parameters | Type | Description | Options | Default Value |
| :---: | :---: | --- | --- | :---: |
| **password_length** | **int** | sets password length | | 12 |
| **number_of_passwords** | **int** | defines the number of passwords to be generated | | 1 |
| **types_of_characters** | **str** \| **list[str]** | defines the type of characters that will be used to generate the password | **lowercase**, **uppercase**, **digits** and **symbols** | all types of characters |

<!--[Want to see an example of using these parameters?](#com-requests)-->

<details>
<summary> <b>:point_right:Do you want to see an example of using these parameters?</b> </summary>

```python
import json
import requests

# Set the API endpoint
endpoint = "https://passgenapi.onrender.com/password"

# Define the data that will be sent in JSON format
password_data = {
     "password_length": 10,
     "number_of_passwords": 3,
     "type_of_characters": ["digits", "lowercase"]
}

# Convert data to JSON format
json_password_data = json.dumps(password_data)

# Send the POST request to the API endpoint with the data in JSON
response = requests.post(url=endpoint, data=json_password_data)

# Display the API response
print(response.json()['password'])
```
</details>

</details>

<details>
<summary><b>:point_right:hash generation</b></summary>

Send an HTTP POST request to the "**https://passgenapi.onrender.com/hash**" endpoint. The API accepts the following parameters:

| Parameters | Type | Description | Options |
| :---: | :---: | --- | :---: |
| **data_for_encrypt** | **str** | defines the data that will be encrypted |
| **hash_type** | **str** | defines the type of hash to be used | **sha1**, **sha224**, **sha256**, **sha384**, **sha3-256** and **md5** |

</details>


<details>
<summary> <b>:point_right:Example requests</b> </summary>

### **With requests:**

```console
$ pip install requests
```

```python
import json
import requests

# Set the API endpoint
endpoint = "https://passgenapi.onrender.com/password"

# Define the data that will be sent in JSON format
password_data = {
     "password_length": 10,
     "number_of_passwords": 3,
     "type_of_characters": ["digits", "lowercase", "symbols"]
}

# Convert data to JSON format
json_password_data = json.dumps(password_data)

# Send the POST request to the API endpoint with the data in JSON
response = requests.post(url=endpoint, data=json_password_data)

# Display the API response
print(response.json()['password'])

```
</details>


## :man_technologist: **Installation**

<details>
<summary> <b>:point_right:Use on local machine</b> </summary>

To use PassGenAPI locally, follow the steps below:

1. **Clone the repository in your local environment:**
     ```console
     $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
     ```

2. **Enter the cloned repository:**
     ```console
     $ cd PassGenAPI
     ```

3. **Create a virtual environment with the appropriate command for your operating system:**
     * **Windows:**
         ```console
         $ py -m venv environment_name
         ```
     * **Linux/macOS:**
         ```console
         $ python3 -m venv environment_name
         ```

4. **Activate the virtual environment:**
     * **Windows:**
         ```console
         (environment_name)$ environment_name\Scripts\activate
         ```
     * **Linux/macOS:**
         ```console
         (environment_name)$ source environment_name/bin/activate
         ```

5. **Install the dependencies with the following command:**
     ```console
     (environment_name)$ pip install -r requirements.txt
     ```

6. **In the root of the PassGenAPI project, run the following command:**
     ```console
     (environment_name)$ uvicorn passgenapi.main:app --host localhost --port 8000
     ```

     :point_right:This command makes the server run on your machine's localhost on port 8000.

     :warning: **Note:** you can change the host and port just by changing the arguments of `--host` and `--port`

</details>


<details>
<summary> <b>:point_right:Use in a Docker container</b> </summary>

1. **Clone the repository in your local environment:**
     ```console
     $ git clone https://github.com/Nicolas-albu/PassGenAPI.git
     ```

2. **Enter the cloned repository:**
     ```console
     $ cd PassGenAPI
     ```

3. **Create a PassGenAPI image:**
     ```console
     $ docker image build -t image_passgenapi .
     ```

4. **Create a container for the newly generated image:**
     ```console
     $ docker run -d --name container_passgenapi -p 80:80 image_passgenapi
     ```

</details>


## :rocket: **Versions**
### **v1.1.10**
The :globe_with_meridians:**PassGenAPI** version 1.1.10 brought the following improvements:
- [x] Improved encapsulation of PasswordGenerator class methods
- [x] Added hash generation: HashGenerator
- [x] Improved unit testing
- [x] PasswordGenerator class refactoring
- [x] Memory performance improvement
- [x] API Deployment in a Docker Container
- [x] Migration from Vercel to Render

### **v1.1.4**
The :globe_with_meridians:**PassGenAPI** version 1.1.4 was the first version to go into production at Vercel, without a Docker container, only with FastAPI and Pytest:
- [x] Creation of password generation class: PasswordGenerator
- [x] Deploy at Vercel

## :pushpin: **About PassGenAPI**
:globe_with_meridians:**PassGenAPI** was developed with a focus on high performance, using the **FastAPI**:zap: web framework. With the use of FastAPI, the API offers significantly superior performance compared to other similar tools, ensuring an agile and efficient user experience. FastAPI is known for its efficiency and ease of use, allowing PassGenAPI to be developed more quickly and scalably. In addition, FastAPI provides features such as automatic documentation and type validation, making creating and maintaining the API easier and less error-prone:heavy_check_mark:.

Furthermore, PassGenAPI has been tested with **Pytest** to ensure code and application quality. Automated testing was an important part of the software development process as it helped to identify problems early.

Additionally, we are always working on new implementations to provide even more customizable options for password generation. So, keep an eye out for future updates to PassGenAPI to gain access to new features and make your application even more secure and reliable! :lock:

<img src="https://img.shields.io/badge/version-1.1.10-blue?style=for-the-badge" target="_blank">

## :rotating_light: **License**

PassGenAPI is under the **Apache-2.0 license**, which means you can use, modify and distribute the API source code for personal and commercial purposes. However, you must include the copyright notice with your distribution and ensure that the same license applies to your modifications. The Apache-2.0 license also includes a disclaimer of warranties and a limitation of liability, so make sure you read it carefully before using PassGenAPI in your project.

<a href="https://github.com/Nicolas-albu/PassGenAPI/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/Nicolas-albu/PassGenAPI?style=for-the-badge" target="_blank"></a>