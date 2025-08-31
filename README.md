# Website Content Scraper and Chatbot

This Python project scrapes content from a given website and interacts with the user using the fetched content. It uses **BeautifulSoup** for web scraping and **Google Generative AI** for generating responses to user queries based on the website content. It fetches additional data like images, links, and headings, which are passed to the chatbot model for more interactive conversations.

## Features

- **Web Scraping**: Extracts the following data from the website:
  - Title of the website
  - Paragraphs (first 5 paragraphs for brevity)
  - Images (first 3 images)
  - Links (first 3 links)
  - Headings (first 2 headings from `h1`, `h2`, `h3`)
  
- **Chatbot**: Interacts with the user by generating responses based on the scraped content using Google Generative AI (`gemini-1.5-flash` model).

- **Command History**: Keeps a history of the user commands for reference.

- **Rate Limiting**: A delay is implemented to ensure that API calls are made at a reasonable rate (1 second between requests).

## Requirements

### Software Requirements:
- Python 3.x

### Libraries:
- **requests** (for making HTTP requests)
- **beautifulsoup4** (for web scraping)
- **google-generativeai** (for interacting with Google Generative AI)
- **python-dotenv** (for environment variable management)

### Installation:

1. **Create a Virtual Environment**:
   - It's recommended to use a virtual environment for this project. To create one, run the following command in your project directory:
   
     ```bash
     python -m venv venv
     ```

2. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   - Once the virtual environment is activated, install the required libraries from `requirements.txt`:
   
     ```bash
     pip install -r requirements.txt
     ```

4. **Create a `.env` File**:
   - Create a `.env` file in the root directory of the project to store your **GENAI_API_KEY**.
   - Add your Google Generative AI API key to the `.env` file:
   
     ```plaintext
     GENAI_API_KEY=your_api_key_here
     ```

5. **Run the Script**:
   - After setting up the `.env` file and installing dependencies, run the script:
   
        ```bash
     python chatbot.py
     ```

## How It Works

1. **Scraping Website Content**:
   - The program sends an HTTP GET request to the given URL.
   - It extracts the following data from the page:
     - The title of the webpage
     - The first 5 paragraphs of text
     - URLs of the first 3 images
     - The first 3 links on the page
     - The first 2 headings of types `h1`, `h2`, `h3`
   
2. **Processing the Data**:
   - The scraped content is formatted into a context string that will be used for interaction with the chatbot.
   
3. **Chatbot Interaction**:
   - The user can ask questions based on the scraped content. The chatbot generates responses based on the available context, utilizing the Google Generative AI model.
   - It uses the `gemini-1.5-flash` model to process the prompt and return an answer.

4. **Command History**:
   - Every user input is stored in the command history, and users can view previous commands by typing `history`.

## Commands

- **exit** or **quit**: Exit the chatbot.
- **help**: Display a list of available commands.
- **history**: Display the history of commands entered by the user.

## Example Usage

Enter the website URL: https://example.com
Website Content Fetched Successfully!

You: What is this website about?
Chatbot: This website is about example content. It provides an overview of various topics.
