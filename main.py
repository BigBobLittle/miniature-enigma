import utils
import prompts
from transformers import pipeline, RagTokenizer, RagTokenForGeneration, BartForConditionalGeneration, BartTokenizer




def write_properly(input_text):
    """Enhances both grammar and style of the input message."""
    prompt = prompts.WRITE_PROPERLY_PROMPT + input_text

    response = utils.generate_response(prompt)
    return response



def write_the_same_grammar_fixed(input_text):
    """Corrects only the grammatical errors in the input message."""
    prompt = prompts.WRITE_SAME_GRAMMAR_FIXED_PROMPT + input_text

    response = utils.generate_response(prompt)
    return response

def summarize(input_text):
    """Provides a concise summary of the input message."""
        # Load the pre-trained model and tokenizer
    model_name = "sshleifer/distilbart-cnn-12-6"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    # Define the summarization pipeline
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

    # Print the summarized text
    summary = summarizer(input_text, max_length=50, min_length=30, do_sample=False)
    return summary[0]['summary_text']
    

def summarize_text(input_text, max_length=512, context_length=1024):
    # Initialize the RAG tokenizer
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")

    # Initialize the RAG model
    rag_model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")

    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=context_length, truncation=True)

    # Generate summary using RAG model
    summarized_output = rag_model.generate(**inputs, max_length=max_length, min_length=max_length//2)

    # Decode the summary
    summarized_text = tokenizer.decode(summarized_output[0], skip_special_tokens=True)
    
    return summarized_text




# Main program 
if __name__ == "__main__":
    print("Welcome to the English Improvement Agent!")
    print("1. Write properly (grammar and style)")
    print("2. Write the same, grammar fixed")
    print("3. Summarize")
    choice = input("Enter your choice (1-3): ")

    input_text = input("Enter your text: ")

    if choice == "1":
        result = write_properly(input_text)
    elif choice == "2":
        result = write_the_same_grammar_fixed(input_text)
    elif choice == "3":
        result = summarize(input_text)
        
    else:
        print("Invalid choice. Please try again.")
        exit()

    print("\nResult:")
    print(result)
    exit()