# Artificial Intelligence SQL Interface

# Startup 
1. Clone the repository by running `git clone 
2. I recommend setting up a virtual environment for this project (optional).
a. Run `python3 -m venv environment_name` in the root directory of the project.
b. Activate the virtual environment by running `source path/to/environment_name/bin/activate` . (Linux & Mac)
3. Install the project dependencies by running `pip install -r path/to/requirements.txt` .
4. Open the .environment file and add your OpenAI API key to the `OPEN_API_KEY` variable.
5. Rename the .environment file to .env
6. Run the application by running `streamlit app.py`

## Notes
a. You can obtain your API key by signing up for an account at https://openai.com/
b. I recommend placing a soft and hard limit on your billing, requests are not "cheap".

# Future Features
I plan on maintaining this repository and adding utilities to this program.

1. Upload a document on the fly (held in memory) and make requests on said document.
    a. These might include: PDF, CSV, JSON, etc.
2. Input a URL and make requests about the link provided ( news article, blog, etc. )
