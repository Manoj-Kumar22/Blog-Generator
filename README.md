# Blog Generator

An AI-powered blog generator using LangGraph and Groq LLM.

## Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd BlogGenerator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
cp .env.example .env
```

4. Edit `.env` file and add your API keys:

- Get your Groq API key from: https://console.groq.com/
- Get your LangChain API key from: https://smith.langchain.com/

5. Run the application:

```bash
python app.py
```

## API Usage

Send POST requests to `/blogs` with:

```json
{
  "topic": "Your blog topic",
  "language": "french" // optional
}
```

## Environment Variables Required

- `GROQ_API_KEY`: Your Groq API key for LLM access
- `LANGCHAIN_API_KEY`: Your LangChain API key for tracing
- `LANGCHAIN_PROJECT`: Project name for LangChain tracing
