# 📰 LinkedIn Intelligence Recap (Skill)

Turn your saved LinkedIn posts into a professional, glassmorphic email newsletter with one click. 

---

## 🚀 Get Started in 3 Steps

### 1. Open your "Terminal"
*   **On Mac:** Press `Command + Space` on your keyboard, type **"Terminal"**, and press Enter.
*   **On Windows:** Open the Start menu, type **"PowerShell"**, and press Enter.

### 2. Prepare your computer
Copy and paste this code into your Terminal and press Enter to install the helper tools:
```bash
pip install playwright beautifulsoup4 && playwright install chromium
```

### 3. Install the Skill
Make sure you have the `linkedin-newsletter.skill` file in your folder, then run this code:
```bash
gemini skills install linkedin-newsletter.skill
```

---

## 🤖 Running the Agent

Now, type `gemini` to open the chat and say:
> *"Extract my saved LinkedIn posts and send me a newsletter recap."*

### ⚠️ If the "API Key" error pops up...
If you see a message saying **"you must specify the GEMINI_API_KEY"**, don't worry! Just follow these quick steps:

1.  Go to [aistudio.google.com](https://aistudio.google.com/app/apikey) and click **"Create API key"** (it's free).
2.  Copy that long code (the API key).
3.  **Now go back to your Terminal** and run this code (replace `PASTE_YOUR_KEY_HERE` with the code you just copied):
    ```bash
    echo "GEMINI_API_KEY=PASTE_YOUR_KEY_HERE" >> .env
    ```
4.  **Try again!** Simply type your request into the Gemini chat again and it will work perfectly.

---

## 🏗 How to Push Updates (For Maintainers)

1.  **Edit:** Change the files in the `linkedin-newsletter/` folder.
2.  **Save:** In your Terminal, run:
    ```bash
    gemini skills package linkedin-newsletter
    ```
3.  **Upload to GitHub:**
    ```bash
    git add .
    git commit -m "Update design"
    git push origin main
    ```

---
*Created with ❤️ by your AI Design Assistant.*
