# Artificial Intelligence SQL Interface
A ficticious internal company database that employees can query via natural language.
- Replace the database with your own and you have an incredibly powerful open-source tool at your disposal.

# Startup 
1. Clone the repository by running `git clone https://github.com/delfortrie/langchain_sql.git`
2. I recommend setting up a virtual environment for this project ( step 3 & 4 )
3. Run `python3 -m venv environment_name` in the root directory of the project
4. Activate the virtual environment in Linux or Mac by running `source path/to/environment_name/bin/activate` 
5. Install the project dependencies by running `pip install -r path/to/requirements.txt`
6. Open the .environment file and add your OpenAI API key to the `OPEN_API_KEY` variable
7. Rename the `.environment` file to `.env`
8. Run the application with `streamlit run app.py` in the terminal

## Notes
- You can obtain your API key by signing up for an account at https://openai.com/.
-  I recommend placing a soft and hard limit on your billing, requests are not "cheap".

# Future Features
1. Upload a document on the fly ( held in memory ) and make requests on said document.
- These might include: PDF, CSV, JSON, etc.
2. Input a URL and make requests about the link provided ( news article, blog, etc. )
