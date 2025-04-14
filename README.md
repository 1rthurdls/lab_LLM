#  AI Chat with Pygame (Gemini + Mistral)

This project is a graphical AI chat interface built with **Pygame** that allows you to chat with a large language model (LLM) powered by either **Gemini (Google)** or **Mistral**. You can dynamically switch between models using clickable buttons in the interface.

---

##  Features

- Simple, Messenger-style chat interface
- Toggle between **Gemini** and **Mistral** live
- Input box and response rendering in real time
- Multiline message support (automatic wrapping)

---

##  Project Structure

| File                  | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `support_graphique.py`| Pygame-based user interface with input, model switch, chat |
| `arthurLLm.py`        | Logic for handling Gemini and Mistral API calls           |
| `.env.example`        | Sample file showing required environment variables        |
| `.gitignore`          | Git ignore rules to prevent leaking sensitive files       |

---

##  API Key Setup

You’ll need valid API keys for both Gemini and Mistral.

### 1. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
