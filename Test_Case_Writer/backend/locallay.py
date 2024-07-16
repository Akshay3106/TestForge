import subprocess

def load_model(model_path):
    """
    Loads and initiates the Ollama model from the given path.

    Args:
        model_path (str): The file path to the Ollama model executable.

    Returns:
        subprocess.Popen: A subprocess object representing the running Ollama model.
    """
    ollama_process = subprocess.Popen([model_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return ollama_process