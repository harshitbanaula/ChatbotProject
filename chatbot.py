import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()
genai_api_key = os.getenv("GENAI_API_KEY")

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Fetch the title
        title = soup.title.string if soup.title else 'No Title'
        
        # Fetch paragraphs
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        
        # Fetch additional data
        images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]
        links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs]
        headings = {
            'h1': [h.get_text() for h in soup.find_all('h1')],
            'h2': [h.get_text() for h in soup.find_all('h2')],
            'h3': [h.get_text() for h in soup.find_all('h3')]
        }
        
        if not paragraphs:
            raise ValueError("No paragraphs found on the page.")
        
        return title, paragraphs, images, links, headings
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None, None, None, None, None
    except ValueError as e:
        print(e)
        return None, None, None, None, None

def process_data(title, paragraphs, images, links, headings):
    context = f"Title: {title}\n\n"
    context += "\n".join(paragraphs[:5])  # Limit to first 5 paragraphs for brevity
    context += "\n\nImages Found:\n" + "\n".join(images[:3])  # Limit to first 3 images
    context += "\n\nLinks Found:\n" + "\n".join(links[:3])  # Limit to first 3 links
    context += "\n\nHeadings:\n"
    for heading_tag, heading_list in headings.items():
        context += f"{heading_tag.upper()}:\n" + "\n".join(heading_list[:2]) + "\n"  # Limit to first 2 headings of each type
    
    return context

def chat_with_gpt(prompt):
    try:
        genai.configure(api_key=genai_api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        print(response.text)
        return response.text
    except Exception as e:
        print(f"Error communicating with the ChatGPT API: {e}")
        return "I'm sorry, I couldn't process that request."

def main():
    url = input("Enter the website URL: ")
    title, paragraphs, images, links, headings = fetch_website_content(url)
    
    if title and paragraphs:
        context = process_data(title, paragraphs, images, links, headings)
        print("\nWebsite Content Fetched Successfully!\n")
        
        command_history = []
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting the chatbot. Goodbye!")
                break
            elif user_input.lower() == 'help':
                print("Commands:\n - Type your question to interact with the chatbot.\n - Type 'exit' or 'quit' to end the conversation.\n - Type 'history' to see previous commands.")
                continue
            elif user_input.lower() == 'history':
                print("Command History:")
                for command in command_history:
                    print(f" - {command}")
                continue
            
            command_history.append(user_input)
            prompt = f"{context}\n:User   {user_input}\nChatbot:"
            response = chat_with_gpt(prompt)
            print(f"Chatbot: {response}")
            
            # Rate limiting: wait for 1 second before the next API call
            time.sleep(1)

if __name__ == "__main__":
    main()

