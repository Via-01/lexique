# Lexique 💜

Lexique is an elegant, minimalist dictionary utility designed to simplify complex Database Management System (DBMS) concepts through clear explanations, structured definitions, and practical SQL implementations. Built with Flask and vanilla web technologies, the application leverages Google's Gemini API to generate concise, educational content while maintaining a lightweight and responsive user experience.

The project follows a low-overhead architecture using Python, HTML5, CSS3, and JavaScript, and is deployed as a serverless application on Vercel.

## 🔗 Live Application

**Production URL:** https://lexique-vyhk.vercel.app

---

## ✨ Features

### AI-Powered Explanations

Lexique uses Google's `gemini-2.5-flash` model to generate fast, accurate, and easy-to-understand explanations for DBMS concepts, SQL queries, normalization techniques, and database structures.

### Minimalist User Interface

The application features a French-inspired aesthetic with a carefully designed dark-mode experience, pastel-purple accents, glassmorphic elements, and subtle visual effects that prioritize readability and accessibility.

### Structured Data Processing

Responses from the AI backend follow strict JSON schemas, enabling deterministic parsing and reliable rendering on the frontend.

### One-Click Copy Functionality

Users can instantly copy generated SQL snippets, definitions, and explanations for use in assignments, projects, or practice environments.

---

## 🏗️ Technology Stack

### Backend

* Python 3.x
* Flask

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript
* Fetch API

### AI Integration

* Google Gemini API (`gemini-2.5-flash`)

### Deployment

* Vercel Serverless Functions (`@vercel/python`)

### Dependency Management

* UV Package Manager

---

## 📂 Project Structure

```text
├── main.py
├── .env                  # Local environment variables (Git ignored)
├── .gitignore
├── requirements.txt
├── vercel.json
├── README.md
├── static/
│   └── bg.png            # Background asset
└── templates/
    └── index.html        # Frontend interface
```

---

## 🚀 Local Development Setup

### Prerequisites

Before running the project locally, ensure you have:

* Python 3.x installed
* UV package manager installed

### 1. Clone the Repository

```bash
git clone <repository-url>
cd test2
```

### 2. Create a Virtual Environment

```bash
pip install uv
uv venv
```

### 3. Activate the Environment

**macOS/Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate.bat
```

### 4. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_google_ai_studio_key_here
```

### 6. Run the Application

```bash
python main.py
```

Once the server starts, open:

```text
http://127.0.0.1:5000
```

in your browser.

---

## 🌐 Deployment

Lexique is configured for deployment on Vercel using Python Serverless Functions.

Before deploying:

1. Connect your GitHub repository to Vercel.
2. Open your Vercel project settings.
3. Add the `GEMINI_API_KEY` under **Environment Variables**.
4. Deploy the project.

The local `.env` file is protected by `.gitignore` and should never be committed to the repository.

---

## 👩‍💻 Author

**Vaishnavi Bhan**
Lead Developer

---

Built with Flask, Gemini AI, and a passion for making database concepts easier to understand.