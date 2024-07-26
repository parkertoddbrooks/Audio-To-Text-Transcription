import os
import sys
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv
import anthropic

# Load environment variables from .env file
load_dotenv()

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.google_api_free import process_audio
from src.google_api import process_audio as process_audio_paid

console = Console()

SUPPORTED_FORMATS = ['.mp3', '.wav', '.m4a', '.aac', '.flac', '.ogg', '.wma', '.aiff', '.aif', '.amr']

# Get the API key from the environment variable
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Initialize the Anthropic client
client = None
if CLAUDE_API_KEY:
    try:
        client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)
    except ImportError:
        console.print("Warning: anthropic library not installed. Claude post-processing will not be available.", style="bold yellow")
else:
    console.print("Warning: CLAUDE_API_KEY not set in .env file. Claude post-processing will not be available.", style="bold yellow")

def get_user_input(prompt, options):
    while True:
        console.print(prompt)
        for option in options:
            console.print(option)
        choice = console.input("Enter your choice: ").strip().lower()
        for option in options:
            if choice == option.split('.')[0] or choice == option.split()[-1].lower():
                return option.split('.')[0]
        console.print("Invalid choice. Please try again.", style="bold red")

def save_transcription(transcription, file_path, is_markdown=False):
    try:
        extension = '.md' if is_markdown else '.txt'
        base_path = file_path
        counter = 1
        while os.path.exists(file_path + extension):
            file_path = f"{base_path}-{counter:02d}"
            counter += 1

        full_path = file_path + extension
        with open(full_path, "w") as f:
            if is_markdown:
                f.write(f"# Audio Transcription\n\n{transcription}\n")
            else:
                f.write(transcription)
        console.print(f"Transcription saved to {full_path}", style="bold green")
        return full_path
    except Exception as e:
        console.print(f"ERROR: Failed to save transcription - {str(e)}", style="bold red")
        return None

def post_process_with_claude(file_path):
    if not client:
        console.print("Claude post-processing is not available. Please check your API key and anthropic library installation.", style="bold red")
        return

    console.print("Post-processing with Claude Opus 3...")
    
    # Read the original file
    with open(file_path, 'r') as f:
        original_text = f.read()
    
    console.print(f"Original text length: {len(original_text)} characters")
    
    # Split the text into smaller chunks
    chunk_size = 4000
    chunks = [original_text[i:i+chunk_size] for i in range(0, len(original_text), chunk_size)]
    
    console.print(f"Number of chunks: {len(chunks)}")
    
    processed_chunks = []
    
    try:
        for i, chunk in enumerate(chunks):
            console.print(f"Processing chunk {i+1} of {len(chunks)}...")
            console.print(f"Chunk size: {len(chunk)} characters")
            
            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                messages=[
                    {
                        "role": "user",
                        "content": f"""Please reformat the following part of a transcript to improve readability. 
                        Separate ideas into paragraphs, similar to a script or chat format. 
                        Do not change the content or add any interpretations. 
                        If the chunk starts or ends mid-sentence, keep it as is.
                        Preserve all original content, including names and technical terms.

                        {chunk}

                        Reformatted transcript part:"""
                    }
                ]
            )
            
            processed_chunk = message.content[0].text
            processed_chunks.append(processed_chunk)
            console.print(f"Processed chunk size: {len(processed_chunk)} characters")
        
        # Combine processed chunks
        processed_text = "\n\n".join(processed_chunks)
        
        console.print(f"Total processed text length: {len(processed_text)} characters")
        
        # Save the processed text to a new file
        processed_file_path = f"{os.path.splitext(file_path)[0]}_processed{os.path.splitext(file_path)[1]}"
        with open(processed_file_path, 'w') as f:
            f.write(processed_text)
        
        console.print(f"Processed transcription saved to {processed_file_path}", style="bold green")
    except Exception as e:
        console.print(f"Error processing with Claude: {str(e)}", style="bold red")

def process_text_file(file_path):
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        
        word_count = len(text.split())
        console.print(f"Text file loaded. Word count: {word_count}")
        
        return {
            "transcription": text,
            "word_count": word_count,
            "duration": None,
            "confidence": None
        }
    except Exception as e:
        console.print(f"Error reading text file: {str(e)}", style="bold red")
        return None

def main():
    while True:
        console.print(Panel("Welcome to the Audio-To-Text Transcription Tool!", title="Welcome", style="bold green"))
        choice = get_user_input("Choose an option:", [
            "1. Free version (limited to short audio clips)",
            "2. Paid version (supports longer audio files, requires Google Cloud API key)",
            "3. Process existing text file",
            "4. Exit"
        ])
        
        if choice == '4':
            console.print(Panel("Thank you for using Audio-To-Text. Goodbye!", title="Goodbye", style="bold green"))
            break

        if choice in ['1', '2']:
            audio_file = console.input("[bold yellow]Path to audio file:[/bold yellow] ")
            if not os.path.exists(audio_file):
                console.print(Panel(f"Error: File '{audio_file}' not found.", title="Error", style="bold red"))
                continue

            file_extension = os.path.splitext(audio_file)[1].lower()
            if file_extension not in SUPPORTED_FORMATS:
                console.print(Panel(f"Error: Unsupported file format. Supported formats are: {', '.join(SUPPORTED_FORMATS)}", title="Error", style="bold red"))
                continue

            console.print(Panel("Processing audio file...", style="cyan"))
            
            if choice == "1":
                result = process_audio(audio_file)
            else:
                result = process_audio_paid(audio_file)
        elif choice == '3':
            text_file = console.input("[bold yellow]Path to text file:[/bold yellow] ")
            if not os.path.exists(text_file):
                console.print(Panel(f"Error: File '{text_file}' not found.", title="Error", style="bold red"))
                continue

            result = process_text_file(text_file)

        if result:
            console.print(Panel.fit(
                f"[bold]Word count:[/bold] {result['word_count']}\n"
                f"[bold]Audio duration:[/bold] {result['duration']:.2f} seconds\n" if result['duration'] else ""
                f"[bold]Confidence:[/bold] {result['confidence']:.2f}" if result['confidence'] else "",
                title="Processing Result",
                border_style="green"
            ))

            save_choice = get_user_input("Do you want to save the text?", ["1. Yes", "2. No"])
            
            if save_choice == "1":
                save_dir = console.input("[bold yellow]Enter the directory to save the file:[/bold yellow] ").strip()
                if not os.path.exists(save_dir):
                    console.print(f"Directory '{save_dir}' does not exist. Creating it.")
                    os.makedirs(save_dir)
                
                file_format = get_user_input("Choose file format:", ["1. Text", "2. Markdown"])
                is_markdown = file_format == "2"
                
                file_name = os.path.splitext(os.path.basename(audio_file if 'audio_file' in locals() else text_file))[0]
                save_path = os.path.join(save_dir, file_name)
                saved_file_path = save_transcription(result['transcription'], save_path, is_markdown)
                
                if saved_file_path and client:
                    post_process_choice = get_user_input("Do you want the text to be post-processed by Claude Opus 3?", ["1. Yes", "2. No"])
                    if post_process_choice == "1":
                        post_process_with_claude(saved_file_path)
            else:
                console.print("Text not saved.")
        else:
            console.print(Panel("Processing failed.", title="Error", style="bold red"))

        if console.input("[bold yellow]Press Enter to continue or type 'exit' to quit:[/bold yellow] ").lower() == 'exit':
            console.print(Panel("Thank you for using Audio-To-Text. Goodbye!", title="Goodbye", style="bold green"))
            break

if __name__ == "__main__":
    main()