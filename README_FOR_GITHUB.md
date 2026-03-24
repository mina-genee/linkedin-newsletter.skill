# 📰 LinkedIn Intelligence Recap (Skill)

Turn your saved LinkedIn posts into a professional, glassmorphic email newsletter with one click. 

---

## 🛠 One-Time Setup (Do this first!)

### 1. Open your "Terminal"
*   **On Mac:** Press `Command + Space` on your keyboard, type **"Terminal"**, and press Enter.
*   **On Windows:** Open the Start menu, type **"PowerShell"**, and press Enter.

### 2. Connect your AI Key
The agent needs a "brain" to work. If you see an error saying **"you must specify the GEMINI_API_KEY"**, do this:
1.  Get a free key from [aistudio.google.com](https://aistudio.google.com/app/apikey).
2.  In your Terminal, type this (replace `YOUR_KEY_HERE` with your actual key from step 1):
    ```bash
    echo "GEMINI_API_KEY=YOUR_KEY_HERE" >> .env
    ```
    *This creates a hidden file that remembers your key so you don't have to type it again.*

### 3. Install the Helper Tools
Copy and paste this entire line into your Terminal and press Enter:
```bash
pip install playwright beautifulsoup4 && playwright install chromium
```

---

## 🚀 How to Use

### 1. Install the Skill
Make sure you have the `linkedin-newsletter.skill` file in your current folder, then run:
```bash
gemini skills install linkedin-newsletter.skill
```

### 2. Start the Agent
Type `gemini` to open the chat, then simply say:
> *"Extract my saved LinkedIn posts and send me a newsletter recap."*

**What to expect:**
*   A browser window will pop up. 
*   **If you aren't logged in:** Log in to LinkedIn and go to your [Saved Posts](https://www.linkedin.com/my-items/saved-posts/).
*   The agent will watch the screen, read your posts, and then close the window automatically.
*   Check your Gmail! Your newsletter will be waiting for you.

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
