# Coding Challenge | Crossmint | Internship
This repository contains my solution for a coding challenge as part of Crossmint's Internship program.

## Project Structure

```plaintext
crossmint-challenge/
├── 📁src
│ ├── main.py
│ ├── api_interactions.py   # API interactions
│ ├── astral_objects.py     # Definition of astral objects using subclasses
│ ├── utils.py     			# Util functions for development
├── 📁docs
│ ├── 📁build
│ │ ├── 📁html				# HTML documentation files ✨
│ │ │ ├── (HTML documentation files)
│ └── (...)
├── .env.template           # Template for environment variables
├── requirements.txt        # Python package dependencies
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository and install the required packages:
	```bash
	git clone https://github.com/jandrana/crossmint-challenge && cd crossmint-challenge && pip install -r requirements.txt
	```

2. Configure environment variables
	- Copy the `.env.template` to a new `.env` file
		```bash
		cp .env.template .env
		```
	- Edit and fill the `.env` file with the correct values

## Running Instructions

To run the application:
```bash
python src/main.py
```

## Documentation

This project uses Sphinx to generate documentation from the Google-style docstrings added in the code.

### View Documentation

If you want to view the documentation, open the [`index.html`](docs/build/html) file in your browser.

### Updating the Documentation

To update/create the documentation, run the following command in the project's root directory:

```bash
cd docs && sphinx-apidoc -o source ../src && make html
```

This command builds the HTML documentation from the docstrings added in the application  

## Challenge Approach

During this section you can find a detailed explanation of the approach and steps taken in order to solve Crossmint's Internship Challenge

### 1. Preparation, analysis and planning of approach

#### 1.1 Analysis and understanding of the problem

<ul>
<details>
<summary><b>Click here to see the steps taken!</b></summary>

- Thorough understanding of the challenge, its requirements and the evaluation criteria.
- Reading and understanding of the provided Megaverse API Documentation while quickly refreshing my knowledge on REST APIs
- Considered different ways of approaching the problem and thought of potential Python packages dependencies.
- Break down of the problem into small tasks to make it easier to solve.

</details>
</ul>

#### 1.2  Environment set up and creation of the GitHub Repo

<ul>
<details>
<summary><b>Project Structure Details</b></summary>

Designed a basic structure for the project to ensure that the project is: modular, scalable, mantainable and easy to understand:
```plaintext
crossmint-challenge/
├── 📁src					# Folder with source code files
│ └── *.py
├── requirements.txt        # To fill during development with package dependencies
├── .gitignore				# Basic .gitignore for temporary/cache/private files
└── README.md
```

</details>

<details>
<summary><b>Packages and source files pseudo-code</b></summary>

- Intalled and added to `requirements.txt` basic needed Python packages like `requests` for API interactions and `python-dotenv` for environment variables.
- Created source files with pseudo-code depending on their code functionality
	1. `main.py` as main entry point of the program
	2. `api_interactions.py` for code regarding API interactions.
	3. `astral_objects.py` for defining the astral objects of the megaverse

</details>

</ul>

### 2. Development for Phase 1

#### 2.1 Progressed with `api_interactions.py`

<ul>
<details>
<summary><b>1. Handling private information needed for interacting with the API</b></summary>

I considered some information needed for interacting with the API to be **private** (my candidate ID and the API base URL). 

**Implementing a solution for this:**

This situation lead me to store this information in 2 environment variables located in a new ignored `.env` file in the root directory of the repository.

Implemented a new function `get_env_variable` for retrieving the value of both variables stored in the `.env` file. 
- New package needed: `python-dotenv` (added to `requirements.txt`).
- Implemented **error handling** for inexistent or empty variables in `.env` file.

</details>

<details>
<summary><b>2. Creation of the API Client.</b></summary>

Implemented a new `ApiClient` class with the goal of handling interactions with the megaverse API. Steps taken:
- Implementation of the `__init__` method using the `candidate_id` and `base_url` of the API.
- Implementation of the `get_goal_map` method for retrieving my current goal map and validating that the interaction with the API worked as expected with the given `candidate_id` and url.
- Implementation of the `create_polyanet` method
- Implementation of the `_post` helper method

</details>
</ul>

#### 2.2 Testing progress made in `main.py`

<ul>
<details>
<summary><b>Details of new <code>main.py</code></b></summary>

Created `main` function for testing the functionality of `api_interactions.py` by:
- Retrieving `candidate_id` and `base_url` values using the `get_env_variable` function
- Created `api_client` variable and assigned it to the initilization of `ApiClient` with `candidate_id` and `base_url`.
- Retrieved `goal_map` value using the method `get_goal_map` from `api_client`

After finishing this step I figured it would be a good idea to implement a new helper method in the `ApiClient` for handling potential API errors. See implementation in: [2.5 Handling API Errors](#25-handling-api-errors-api_interactionspy)

</details>
</ul>

#### 2.3 Progressed with `astral_objects.py`

<ul>
<details>
<summary><b>Created parent class <code>AstralObject</code></b></summary>

- Implemented `__init__` method using `row` and `column` attributes that indicate an object's position
- Implemented `create` abstract method for ensuring that every child class of `AstralObject` implements a `create` method. If it's doesn't, it raises a NotImplementedError.

</details>

<details>
<summary><b>Defined child classes for <code>AstralObject</code> representing each megaverse objects</b></summary>

- `Polyanet`: Implemented `create` method, which uses `api_client.create_polyanet` and the object's position for creating the desired object.
- `Soloon` and `Cometh` sketched for now, since they were not needed yet

</details>
</ul>


#### 2.4 Progressed with `main.py`

Updated `main.py` for evaluating the progress made until now by incorporating the functions and classes developed.

<ul>
<details>
<summary><b>1. Created new function <code>create_megaverse</code></b></summary>

**Note:** Function located in `main.py` due to its importance and direct relationship with the `main`

Functionality: 
- Parses the given `goal_map` and creates a list `megaverse_objects` based on the retrieved information. Each element of the list contains an astral object class with its position (e.g. "Polyanet(row, column)").
- Iterates `megaverse_objects` and creates each object using the `create` method of such object class using the variable `api_client` as argument.
- At the end, it returns the `megaverse_objects` list. This return simply facilitates the usage of util functions like `print_megaverse` for development and debugging uses.

</details>

<details>
<summary><b>2. Updated <code>main</code> to incorporate the new <code>create_megaverse</code></b></summary>

Integrating this new function in the `main` allowed me to integrate all the functions and classes developed for completing my first megaverse!

</details>
</ul>

 #### 2.5 Handling API Errors `api_interactions.py`

<details>
<summary><b>Details of the new implementation for error handling</b></summary>

 Even though the first phase was successfully finished, before moving to the second phase I prioritized the implementation of a clean and comprehensive error handler regarding API exceptions. This way I could get rid of repetitive handling of exceptions found in various methods. 
 
 Steps taken to achieve this:
 1. Created new `_handle_error` helper method inside the `ApiClient` class.
 2. Added different messages depending on multiple types of request exceptions. This way I made sure of handling diverse HTTP and connection errors, timeouts and other unexpected errors.
 3. For improving the error handling output, I added an extra argument `re_raise=False`. If re_raise is `True`, after printing the specific error message of an exception, the caught exception is re raised and outputs the Traceback of the exception. It is `False` by default in order to simplify the output of the error. It can be easily changed to `True` if futher detail of the Exception is needed.
 4. Finally, I updated the other methods so that they manage exceptions using this new  `_handle_error` helper method.

This step required further testing of the program when encountering diverse types of errors.

</details>

### 3. Development for Phase 2

#### 3.1 Finished functionality of `api_interactions.py` (`ApiClient` Class)

<ul>
<details>
<summary><b>Implemented <code>create_soloon</code> and <code>create_cometh</code> methods</b></summary>

Implemented both of these new methods to the `ApiClient` Class with their respective url.

Both methods are very similar to the `create_polyanet` but they include an extra key in their data dictionary (`color` for soloons and `direction` for comeths).

</details>

<details>
<summary><b>Implemented exponential backoff logic to the <code>_post</code> method</b></summary>

Implemented exponential backoff retry logic when receiving exceptions regarding "Too Many Request for URL". Regarding any other exceptions, it uses the `_handle_error` helper method.

**Note:** The retry method is performed as long as the indicated exception occurs less than 5 times in a row.

</details>
</ul>

#### 3.2 Finished functionality of `astral_objects.py`

<details>
<summary><b>Finished the missing child classes of <code>AstralObject</code>: <code>Soloon</code> and <code>Cometh</code></b></summary>

Both are very similar to the `Polyanet` subclass with some extra things to take into account.
 - Both of these child classes include an `__init__` method that inherits the `row` and `column` attributes from their parent class `AstralObject` and contain an extra attribute that is specific to each class.
	- `Soloon`'s specific attribute is `color` 
	- `Cometh`'s specific attribute is `direction`
 - Implemented `create` method to both new child classes, which uses `api_client.create_[object_name]` (where [object name] is soloon or cometh) providing as arguments the object's inherited and specific attributes (`row`, `column` and `color`/`direction`).

</details>

#### 3.3 Finished functionality of `main.py`

Finally, I will provide a much more detailed explanation of how I managed to finish the second phase of the challenge by updating `create_megaverse`. By making the function able to successfully interpret the objects present in the `goal_map`. 

<details>
<summary><b>Click here for Details! | Updated <code>create_megaverse</code></b></summary><br>

It is important to understand that in order to create a `Soloon` or `Cometh` we need not only the `row` and `column` attributes for knowing that object's position but we also need to know its specific attributes. For `Soloon` objects we need its `color` and, for `Cometh` objects we need its `direction`.

To achieve this, I updated the `goal_map` parsing to also look for values ending with the word `SOLOON` and `COMETH`. If it finds a value with such characteristics, it retrieves the object's specific attribute (`color`/`direction`) from the object's name. 
 

**EXAMPLE: Detailed functionality explanation:**

Let me explain the map parsing functionality with an example where `[goal_map : ["BLUE_SOLOON", ...]]`:

- **What us mortal should interpret:** `goal_map` says that there should be a **Blue Soloon** at the first `row` and `column` of our map.

- **REMINDER**: Attributes needed for creating a **Soloon** are: _row, column and **color**._

**How does `create_megavese` interpret this?**
 - During the map parsing, at the first column and row of the map we find the value `"BLUE_SOLOON"`, which ends with the word SOLOON. 
 
 	Great! Now I know I have to create a new `Soloon` at `row=0` and `column=0`
 - Current missing information for creating a `Soloon`: desired value for the `color` attribute.

 - To find out the `color` of the `Soloon`, the function uses the following line of code: 
	```py
	color = value.split('_')[0].lower()
	```
	Let's break down in a _"code-like"_ format what this line does following the same example: 
	```py
	# Reminder: in this example, value = "BLUE_SOLOON"
	# 1. Splits into two `"BLUE_SOLOON"` with `"_"` as delimiter --> ["BLUE", "SOLOON"]
		"BLUE_SOLOON".split('_') = ["BLUE", "SOLOON"]
	# 2. Retrieves the 1st value of the splitted string
		[BLUE, SOLOON][0] = "BLUE"
	# 3. Converts to lowercase the retrieved value
		"BLUE".lower() = "blue": 
	# 4. Assigns the converted value ("blue") to the missing attribute (color)
		color = "blue"
</details>

### Personal improvements:

Truth is, as much as I love learning and solving challenges, I also love giving some personal enhancements to the project's I develop. Which is why I took the freedom of making the following improvements.

#### Added `.env.template` file to repository

Since I considered some needed variables to be private (my candidate ID and the metaverse api base URL), I preferred to store this information in environment variables at the `.env` file (which of course I added to the .gitignore).

Since the `.env` file is not present in this public repository, I created a new `.env.template` which serves as an example of what the `.env` should look like. Naturally, this new file needs to be renamed and edited filling the values of each variable. See the [Setup](#setup) Section for an easy setup.

#### Added Docstrings

If you have seen my [GitHub](https://github.com/jandrana), you should have noticed by now that I **love** making clean and documented code for others to see and understand. Following this practice has helped countless times, it daily helps me when mentoring other 42 students by making it much easier for everyone to understand a code that they didn't develop. But it has specially helped me when developing collaborative projects. 

This project couldn't be less! So I decided to implement Docstrings (following [Google's Style Guide](https://android.googlesource.com/platform/external/google-styleguide/+/refs/tags/android-s-beta-2/pyguide.md#3_8_3-functions-and-methods)) to all the functions and classes present in the `src/` folder of this repository.

#### Generated `docs/` using Sphinx

After doing some research regarding the usage of Docstrings for documenting code I found an amazing Python package: **Sphinx**

**Sphinx** is a documentation generator that easily generates documentation for your project!

It retrieves all of your Docstrings present in your source code and with a few configurations, it generates multiple `.html` files containing your project documentation.

You can see the generated documentation if you open in your browser the `.html` files present at [docs/build/html](docs/build/html).

Note: In order to be able to see the html files (in their proper format), make sure to clone this repository and open the **downloaded** files in your browser.


#### Utils functions

During the development of the project I created a couple of helper functions made to "see" what was happening inside the program. After finishing the project I thought the best option was to move them to the `utils/` folder, since they are not actively useful for the program to work but they are very useful for developing/debugging cases.

During the project I also created a `test/` folder, making use of the `pytest` python package. Truth is, it is my first experience using this package and I just wanted to play around and learn about it, which is why I deleted such folder from this `main` branch of the repo. BUT! If you are very very curious about it, you can take a look to the `test` branch of this repo and see it!

#### Project's README 

Finally, I culminated the project by creating this README—_because a finished project seems too empty without it_

I love making README's for a project's presentation which is why I do it in _~~all~~ most_ of my repos—_I'm getting there 💫_
 
Anyways, In this README, as you have seen, I added some important and basic information regarding this project. Since I was already working on this, I wanted to add what was going to be a _"small"_ section regarding my Challenge Experience and Approach. I know, it definitely ended up being bigger than "small" but I am sure it served well its purpose.

## 📬 Contact me

I'm always happy to talk about experiences and share thoughts with anyone interested in coding, so please feel free to contact me! 

- Github: [@jandrana](https://github.com/jandrana)
- Mail: yo@anaalejandra.com
