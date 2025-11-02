# Notes for Claude

## Environment Setup

- Use `uv pip install` instead of regular pip for package installation
- For local development installation: `uv pip install -e .`

## Common Commands

Use `tinbox --help` to see all available options. A few useful commands:

- `tinbox --to es document.pdf` — translate a PDF to Spanish
- `tinbox --from zh --to en document.docx` — translate a Word document from Chinese to English
- `tinbox --model lmstudio:local-model --to es document.pdf` — translate using a local LM Studio model

## Using LM Studio (Local Models)

LM Studio allows you to run LLMs locally on your Mac without API calls. To use LM Studio with tinbox:

1. Download and install [LM Studio](https://lmstudio.ai/)
2. Load a model in LM Studio (e.g., Mistral 7B, Llama 2, etc.)
3. Start the local server in LM Studio (default: `http://localhost:1234`)
4. Use tinbox with `--model lmstudio:model-name` where `model-name` matches the model loaded in LM Studio

### Example:
```bash
tinbox --model lmstudio:mistral-7b --to es document.pdf
```

### Configuration:
- Default LM Studio endpoint: `http://localhost:1234/v1`
- To use a custom endpoint, set the environment variable: `export LMSTUDIO_API_BASE=http://your-custom-url:port/v1`
- LM Studio models use smaller token limits (2048 vs 4096) to accommodate local model constraints
- No API costs - runs entirely on your local machine

### Notes:
- Local models may be slower than cloud APIs depending on your hardware
- Smaller models may produce lower quality translations than GPT-4 or Claude
- Make sure the LM Studio server is running before using tinbox

## Project-Specific Information

- Pillow is required for image processing in the PDF processor and LiteLLM translator
