# 📰 The LinkedIn Intelligence Recap Agent

Welcome! If you're here, you probably want to turn your saved LinkedIn posts into a beautiful, curated email newsletter without doing any manual work. You are in the right place.

This guide is written for **everyone**—even if you've never used a command line before. We will walk through this step-by-step.

---

## 🤔 What is this?
This is a "Skill" for the Gemini AI. Once installed, you can simply ask your AI to read your saved LinkedIn posts, find the common trends, and email you a beautifully designed summary. 

---

## 🛠 Phase 1: The One-Time Setup
Before the AI can do its magic, we need to give your computer the right tools. You only have to do this once.

### Step 1: Open your "Terminal"
The Terminal is just a text-based way to talk to your computer.
*   **🍎 If you are on a Mac:** Press `Command + Space` on your keyboard, type the word **Terminal**, and press `Enter`. A black or white box will pop up.
*   **🪟 If you are on Windows:** Open your Start menu, type the word **PowerShell**, and press `Enter`.

### Step 2: Install the Gemini CLI
This skill runs on the Gemini AI Command Line tool. You need to install it first:
1. Copy this code, paste it into your Terminal, and press `Enter`:
   ```bash
   npm install -g @google/gemini-cli
   ```
2. **Note:** If you get an error saying 'npm not found', you need to install **Node.js** first from [nodejs.org](https://nodejs.org).
3. **Note:** If you get a "permission denied" error, try adding `sudo` to the beginning: `sudo npm install -g @google/gemini-cli`.
4. **🔐 Password Warning:** When typing `sudo` commands, your Terminal will ask for your computer password. **You will not see any characters or stars as you type.** This is a security feature—just type it blindly and hit `Enter`!

---

## 🛠 Troubleshooting (Common Fixes)

*   **"npm: command not found":** Go to [nodejs.org](https://nodejs.org) and install the "LTS" version.
*   **"gemini: command not found":** Close your Terminal and open it again to refresh it.
*   **"Missing API Key":** Follow the steps in Phase 2 below exactly.
*   **"Playwright error":** Make sure you ran the code in Step 3 to install the browser tools!

### Step 3: Install the Helper Tools
The AI needs a couple of small tools to be able to open a web browser and read your posts.
1. Copy this exact line of code:
   ```bash
   pip install playwright beautifulsoup4 && playwright install chromium
   ```
2. **Go back to your Terminal**, paste that code in, and press `Enter`. 

### Step 4: Install the Skill
Now, let's teach the AI how to do this specific job.
1. Make sure the `linkedin-newsletter.skill` file is downloaded to your computer.
2. In your Terminal, paste this code and press `Enter`:
   ```bash
   gemini skills install linkedin-newsletter.skill
   ```

---

## ⚠️ Phase 2: Connecting the AI's "Brain" (The API Key)

To use the Gemini AI, it needs a key to connect to Google's servers. 

**Did you get an error saying *"you must specify the GEMINI_API_KEY"*?** 
Don't panic! This just means your AI needs its key. Here is exactly how to fix it:

1.  **Get your free key:** Go to [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) in your web browser.
2.  Click the blue button that says **"Create API key"**. 
3.  Copy the long string of letters and numbers it gives you.
4.  **Go back to your Terminal.** We are going to save this key to a hidden file so you never have to enter it again. 
5.  Copy the code below, but **replace `PASTE_YOUR_KEY_HERE` with your actual long key**, then paste it into the Terminal and press `Enter`:
    ```bash
    echo "GEMINI_API_KEY=PASTE_YOUR_KEY_HERE" >> .env
    ```

---

## 🚀 Phase 3: How to Actually Use It!

You are fully set up! Whenever you want your newsletter, here is what you do:

1. Open your Terminal.
2. Type `gemini` and press `Enter`. You will see a greeting welcoming you to the Gemini CLI.
3. Now that you are inside the AI chat, simply ask it:
   > *"Extract my saved LinkedIn posts and send me a newsletter recap."*

### What to expect when you run this:
*   A new web browser window will magically pop open on its own. 
*   **If you aren't logged into LinkedIn:** The browser will wait for you. Take your time, type in your password, and go to your [Saved Posts](https://www.linkedin.com/my-items/saved-posts/).
*   Once you are on the saved posts page, let go of the mouse! The AI will automatically scroll down, read your posts, and then close the window.
*   Wait about 30 seconds, then **check your Gmail**. Your beautifully formatted intelligence brief will be waiting in your inbox.

---

## 🎨 Make it Yours (No coding required)
Don't like the colors? Want the AI to write in a different tone? You don't need to be a developer to customize this!

*   **Change the Design:** Open the `email_template.html` file in any basic text editor (like Notepad or TextEdit). You can change the hex color codes (like `#FFFFFF` for white) or swap out the fonts without breaking the AI's logic.
*   **Change the AI's Instructions:** If you want the AI to summarize differently (e.g., "focus more on AI news," or "write it in a funny tone"), just open the `SKILL.md` file and type your new instructions in plain English.
*   **Share your changes:** If you create a great new color scheme or rule set, go to your Terminal and run:
    ```bash
    gemini skills package ./
    ```
    This creates a new `.skill` file that you can send to your friends or team so they can use your exact version!
    ```bash
    gemini skills package ./
    ```
    This creates a new `.skill` file that you can send to your friends or team so they can use your exact version!
