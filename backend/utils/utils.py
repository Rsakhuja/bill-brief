import os

def directory_exist(file):
    file_name = file.filename
    print(f"\n Processing file: {file_name} \n")
    pdf_storage_directory = f"llm_implementation/data/{file_name}"
    if not os.path.exists(pdf_storage_directory): # If it doesn't, we create the directory
        print(f"\nCreating directory at :::{pdf_storage_directory}::: to store pdf \n")
        os.makedirs(pdf_storage_directory)
    file_path = os.path.join(pdf_storage_directory, file_name)
    if os.path.exists(file_path):
        print(f"\n {file_name} already exists at {file_path} \n")
        return True
    else:
        print(f"\nNew File ::: {file_name} being saved at {file_path} \n")
        file.save(file_path)
        return False
    
def split_text_for_threads(file_name, llm_response, max_length=280):
    """
    Splits a long text into smaller parts suitable for a Twitter thread.

    Args:
    - text (str): The text to split into threads.
    - max_length (int): Maximum length of each thread part (default is 280 characters, Twitter's current limit).

    Returns:
    - list of str: List of texts, each representing a part of the thread.
    """
    threads = []

    bill_introduction = f"This analysis of 📄 BILL : {file_name} 📄 \n"
    text = bill_introduction +  llm_response['summary'] + ' ✅ ' + llm_response['benefits'] + ' ⚠️ ' + llm_response['concerns']  
    words = text.split()
    current_part = ""

    for word in words:
        if len(current_part) + len(word) + 1 <= max_length-10:
            if current_part:
                current_part += " "
            current_part += word
        else:
            threads.append(current_part+'...')
            current_part = word

    if current_part:
        threads.append(current_part)

    print(f"\n\n\nThis is what the threads looks like :::: {threads} \n\n\n")

    return threads