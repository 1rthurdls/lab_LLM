# 💬 AI Chat with Pygame (Gemini + Mistral)

This project is a graphical AI chat interface built with **Pygame** that allows you to chat with a large language model (LLM) powered by either **Gemini (Google)** or **Mistral**. You can dynamically switch between models using clickable buttons in the interface.

---

## 🚀 Features

- Simple, Messenger-style chat interface
- Toggle between **Gemini** and **Mistral** live
- Input box and response rendering in real time
- Multiline message support (automatic wrapping)

---

## 🗂️ Project Structure

| File                  | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `support_graphique.py`| Pygame-based user interface with input, model switch, chat |
| `arthurLLm.py`        | Logic for handling Gemini and Mistral API calls           |
| `.env.example`        | Sample file showing required environment variables        |
| `.gitignore`          | Git ignore rules to prevent leaking sensitive files       |
| `requirements.txt`    | List of dependencies needed to run the app                |

---

## 🔐 API Key Setup

You’ll need valid API keys for both Gemini and Mistral.

### 1. Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

✅ This file is already listed in `.gitignore` so it will not be pushed to GitHub.

### 2. Use the example provided:

```bash
cp .env.example .env
```

Then fill in your real keys.

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/1rthurdls/lab_LLM
cd your-repo-name
```

### 2. Install dependencies

Use the `requirements.txt` file provided to install all necessary Python packages:

```bash
pip install -r requirements.txt
```

---

## 📦 What is `requirements.txt`?

`requirements.txt` is a text file that lists all the Python libraries your project depends on. Instead of installing each package manually, you can run one command:

```bash
pip install -r requirements.txt
```

This makes your setup reproducible and fast.  
The file contains:

```
pygame
python-dotenv
google-generativeai
mistralai
```




## ▶️ Usage

Once installed, launch the app using:

```bash
python support_graphique.py
```

Then:

- Click the **Gemini** or **Mistral** button to choose the model
- Type a message and hit `Enter`
- The AI responds using the selected model 🧠

---

## ✅ Security Best Practices

- `.env` is in `.gitignore` so it won't be tracked by Git
- API keys are stored securely using the `dotenv` library
- Never hardcode sensitive information like keys directly in your code

---

## 📚 Useful Links

- [🔑 Gemini API (MakerSuite)](https://makersuite.google.com/app/apikey)
- [📘 Mistral API Docs](https://docs.mistral.ai/)
- [🐍 Pygame Documentation](https://www.pygame.org/docs/)

---

