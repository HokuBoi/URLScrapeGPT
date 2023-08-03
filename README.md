# URL Text Scraper

This project is a simple Flask application that takes a URL as input, scrapes the text from the webpage, and generates a summary using the OpenAI GPT-3.5 Turbo model.

## Setup

Before running the application, you need to set up your OpenAI API key as an environment variable. This key is used by the application to interact with the OpenAI API.

To do this, you can set the `OPENAI_API_KEY` environment variable in your terminal session. Here's how to do it on Unix-like systems:

```bash
export OPENAI_API_KEY='your-api-key-here'
```

Replace `your-api-key-here` with your actual OpenAI API key.

On Windows, you can use the `set` command:

```cmd
set OPENAI_API_KEY=your-api-key-here
```

Remember, these commands only set the environment variable for the current terminal session. If you close the terminal or start a new session, you'll need to set the variable again.

## How to run

First, clone this repository to your local machine:

```bash
git clone https://github.com/HokuBoi/URLScrapeGPT.git
cd URLScrapeGPT
```

Next, install the project's dependencies. This project uses Poetry, so you can do this by running:

```bash
poetry install
```

Next, activate the virtual environment:

```bash
poetry shell
```

Then, you can start the Flask application by running:

```bash
python main.py
```

The application should now be running at `localhost:81`.

## How to use

To use the application, navigate to `localhost:81` in your web browser. Enter a URL in the input field and click "Submit". The application will scrape the text from the webpage and display a summary.

---

Remember to replace `your-api-key-here` with your actual OpenAI API key. Also, please keep your API key safe and do not share it with others.
