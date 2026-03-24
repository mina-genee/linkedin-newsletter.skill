# 📰 LinkedIn Intelligence Recap (Skill)

Turn your saved LinkedIn posts into a professional, glassmorphic email newsletter with one click. This tool live-scrapes your "Saved Items" on LinkedIn, categorizes them into actionable trends using AI, and sends a beautifully formatted brief to your inbox.

---

## 🚀 How to Use (For Everyone)

### 1. Installation
If you have the `.skill` file, simply run this command in your terminal:
```bash
gemini skills install linkedin-newsletter.skill
```

### 2. Running the Agent
Once installed, just open your Gemini CLI and say:
> *"Extract my saved LinkedIn posts and send me a newsletter recap."*

**What happens next:**
*   A browser window will open automatically.
*   **If you aren't logged in:** Log in to LinkedIn and navigate to your [Saved Posts](https://www.linkedin.com/my-items/saved-posts/).
*   The agent will wait for you, extract your posts, and close the browser.
*   Check your Gmail! A curated intelligence brief will arrive shortly.

---

## 🛠 Prerequisites (One-time Setup)

To run the extraction script, you need Python and a few helper libraries installed on your computer:

1.  **Install Python:** Download from [python.org](https://www.python.org/downloads/).
2.  **Install Helpers:** Open your terminal and run:
    ```bash
    pip install playwright beautifulsoup4
    playwright install chromium
    ```

---

## 🏗 How to Push Updates (For Maintainers)

If you want to change the design, the colors, or the logic and push it to your GitHub repository, follow these simple steps:

### 1. Edit the Skill
Modify the files inside the `linkedin-newsletter/` folder:
*   **Design:** Edit `assets/email_template.html`.
*   **Logic:** Edit `scripts/fetch_and_extract_posts.py`.
*   **Agent Instructions:** Edit `SKILL.md`.

### 2. Re-package the Skill
Every time you make a change, you need to "zip" it back into a `.skill` file:
```bash
gemini skills package linkedin-newsletter
```

### 3. Push to GitHub
Run these three commands to send your updates to the cloud:
```bash
git add .
git commit -m "Update design and logic"
git push origin main
```

---

## 🎨 Design Features
*   **Glassmorphic Layout:** Clean, translucent containers with soft shadows.
*   **Mobile Optimized:** Scales perfectly for iPhone and Android.
*   **Agnostic Branding:** Professional "Saved & Synthesized" title, ready for sharing.
*   **Action Oriented:** Every trend includes a specific "Action Plan" checklist.

---
*Created with ❤️ by your AI Design Assistant.*
