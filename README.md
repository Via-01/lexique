# Lexique 💜

An elegant, minimalist dictionary utility designed to break down complex Database Management System (DBMS) concepts into crystal-clear structural definitions and practical code implementations. Built using a low-overhead architecture with **Flask (Python)** and vanilla **HTML5/CSS3**, powered by the **Gemini API**, and deployed as a serverless instance on **Vercel**.

### 🔗 Live Application
**Production URL:** [Insert Live Vercel Link Here]

---

## Key Features

- **French-Inspired Minimalist Aesthetic:** A carefully structured, accessible dark-mode UI centered around a distinctive pastel-purple palette with subtle glassmorphic container elements.
- **AI-Driven Explanations:** Leverages `gemini-2.5-flash` for high-speed, structural data processing with minimal runtime overhead.
- **Deterministic Data Structure:** Enforces strict JSON schemas directly from the language model backend, ensuring seamless structural parsing into the DOM.
- **Clipboard Management:** Native, single-click copy utility for practical SQL script executions and schema definitions.

---

## Architecture & System Design

- **Backend Context:** Python 3.x / Flask Framework
- **Frontend Context:** Semantic HTML5, CSS Variables, Asynchronous Vanilla JavaScript (Fetch API)
- **Dependency Management:** Configured via `uv` for lightning-fast compilation and deterministic virtual environment isolation.
- **Serverless Hosting:** Hosted via Vercel Serverless Functions (`@vercel/python`) mapping inbound routing states efficiently via `vercel.json`.

---

## Local Development Setup

### Prerequisites
Ensure you have Python 3.x and `uv` installed on your machine.

1. **Clone the repository and enter the directory:**
   ```bash
   cd test2