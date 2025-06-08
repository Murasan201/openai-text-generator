# openai-text-generator

A simple Python utility that uses OpenAI’s GPT-4 ChatCompletion API to generate text based on user-provided prompts.

## Features

- Uses environment variable `OPENAI_API_KEY` to authenticate.
- Sends prompts to GPT-4 and prints the generated responses.
- Includes debug output for API responses.

## Installation

1. Ensure Python 3.7+ is installed.
2. Install dependencies:
   ```bash
   pip install --upgrade openai
   ```
3. (Optional) Add local scripts to your PATH:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   ```

## Usage

Set your API key and run the script (replace `YOUR_API_KEY_HERE` with your actual API key):

```bash
export OPENAI_API_KEY="YOUR_API_KEY_HERE"  
python3 generate_text.py
```

You can also pass the key inline:

```bash
OPENAI_API_KEY="YOUR_API_KEY_HERE" python3 generate_text.py
```

## Author

Murasan  
Homepage: [https://murasan-net.com/](https://murasan-net.com/)

## Repository

[https://github.com/Murasan201/openai-text-generator](https://github.com/Murasan201/openai-text-generator)

## License

See [LICENSE](LICENSE) for details.
