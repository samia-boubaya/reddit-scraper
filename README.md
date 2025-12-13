# Reddit Scraper for Posts 🎵

A Python-based scraper to extract high-engagement Reddit posts related to **music**. Automatically collects post data, including title, description, votes, comments, visuals (images/videos), and metadata. Ideal for content analysis, research, or curating trending music posts. Supports filtering by **Hot, Top, New, Comments, and Relevance**, with time-based searches like **past hour**, **week**, **month**, or **all-time**.  

## Features
- Extract post metadata: title, link, ID, votes, comments, post date & time.
- Download visuals (image, video, carousel) with automatic file naming.
- Filter posts by engagement, relevance, and time period.
- Focused on **music-related content**, including theory, instruments, production, memes, and historical highlights.

Perfect for researchers, content creators, or music enthusiasts looking to track trends and high-performing posts on Reddit.

---

## ⭐ **Reddit/Music Threads Guidelines**

**Conditions:**  
- Description: 100–300 characters  
- Posts must be HOT & relevant to music  
- Downloadable visuals (images/videos)  
- Only include posts with ≥100 shares  
- High engagement / top-performing posts  

**Essentials:**  
- Keyword: `music`  
- Focus: short text or image, simplicity, relevance  

**Relevance Categories:**  
- Music theory, instruments, production, teaching  
- Historical highlights, facts, memes, communities  
- Target: anyone learning, playing, or producing music  

**Threads Post Rules:**  
- Video under 15 seconds  
- If both image & video exist, use only video  

---

## ⭐ **Reddit Post Data Fields**

The main data fields to extract from the Reddit Post :
| Field Name         | Python Data Type | Description |
|--------------------|-----------------|-------------|
| <span style="color:green">**post_title**</span>     | `str`            | Title of the post. |
| **post_link**      | `str`            | Direct URL to the post. |
| **post_id**        | `str`            | Unique identifier for the post. |
| <span style="color:red">**num_votes**</span>      | `int`            | Total number of upvotes the post received. |
| <span style="color:red">**num_comments**</span>   | `int`            | Total number of comments on the post. |
| **text_length**    | `int`            | Character count of the post’s text description. |
| <span style="color:green">**post_description**</span> | `str`          | Full text description or caption of the post. |
| **post_date**      | `date`           | Calendar date when the post was published. |
| **post_time**      | `str`            | Time (with timezone) when the post was published. |
| <span style="color:green">**post_visual**</span>    | `list[str]`      | Direct URLs to visual content (images or videos). |
| **visual_type**    | `str`            | Type of visual content: `"IMAGE"`, `"VIDEO"`,`"CAROUSEL"`, or `"NONE"`. |
| **visual_count**   | `int`            | Number of visual items in the post. |
| <span style="color:blue">**filter**</span>         | `str`            | Reddit search filter used. Must be one of: `"Relevance"`, `"Hot"`, `"Top"`, `"New"`, `"Comment count"`. |
| <span style="color:blue">**keyword**</span>        | `str`            | Search keyword or query. |
| <span style="color:blue">**limit**</span>          | `int`            | Number of posts requested. |
| <span style="color:blue">**period**</span>         | `str`            | Time filter used when searching posts. Must be one of: `"All time"`, `"Past year"`, `"Past month"`, `"Past week"`, `"Today"`, `"Past hour"`. |
| <span style="color:red">**time_ago**</span>       | `str`            | Relative time since the post was published (e.g., `"3 hours ago"`). |

---

## ⭐ **POST LINK - EXPLORING**

| Link             | Keyword       | Filter       |
|------------------------|-----------------------|-----------------------|
| https://www.reddit.com/search/?q=music             |  ```music```  | ```Relevance``` by default |
| https://www.reddit.com/search/?q=***keyword***             |  ```keyword```  | ```Relevance``` by default |
| https://www.reddit.com/search/?q=music&type=posts&sort=hot             |  ```music``` |  ```HOT```  |
| https://www.reddit.com/search/?q=music&type=posts&sort=top             |  ```music``` |  ```Top```  |
| https://www.reddit.com/search/?q=***keyword***&type=posts&sort=***filter***             |  ```keyword``` |  ```filter```  |

---

## ⭐ **SEARCH FILTER**

| Filter       | What it does                                             | Use it when                                      |
|--------------|----------------------------------------------------------|-------------------------------------------------|
| ```Relevance```    | Shows posts most related to your search terms           | You want posts that best match your search query |
| ```Hot```          | Shows currently trending posts based on upvotes, recency, and engagement | You want popular and active posts right now    |
| ```Top```          | Shows posts with the highest score for a given time period | You want the most upvoted or "best" content for a topic |
| ```New```          | Shows posts in chronological order, newest first       | You want fresh content or to track recent activity |
| ```Comments Count```     | Sorts posts by number of comments (descending)          | You want posts with lots of community discussion |

---

## ⭐ **PERIOD FILTER**

| Filter       | What it does                                             | Use it when                                      |
|--------------|----------------------------------------------------------|-------------------------------------------------|
| ```All time```    | Shows posts most related to your search terms           | You want posts that best match your search query |
| ```Past year```          | Shows currently trending posts based on upvotes, recency, and engagement | You want popular and active posts right now    |
| ```Past month```          | Shows posts with the highest score for a given time period | You want the most upvoted or "best" content for a topic |
| ```Past week```          | Shows posts in chronological order, newest first       | You want fresh content or to track recent activity |
| ```Past hour```     | Sorts posts by number of comments (descending)          | You want posts with lots of community discussion |

---

## ⭐ **DOWNLOAD AUTOMATICALLY**

| Visual Type | File Naming Formula | Example File Names |
|-------------|-------------------|------------------|
| ```CAROUSEL```    | **keyword_filter_period_**`<post_number>_<type>_<sequence>` | **keyword_filter_period_**`1_img_01`<br>**keyword_filter_period_**`1_img_02`<br>**keyword_filter_period_**`1_img_03` |
| ```IMAGE```       | **keyword_filter_period_**`<post_number>_<type>` | **keyword_filter_period_**`2_img`<br>**keyword_filter_period_**`3_img`<br>**keyword_filter_period_**`4_img` |
| ```VIDEO```       | **keyword_filter_period_**`<post_number>_<type>` | **keyword_filter_period_**`5_vid`<br>**keyword_filter_period_**`6_vid`<br>**keyword_filter_period_**`7_vid` |

---

## ⭐ **HOW TO USE - STEPS**

| Step | Instruction |
|------|-------------|
| **01**  | Run the code |
| **02**  | Input what you want to search (example: `"music"`) |
| **03**  | Input the Reddit search filter: `"Relevance"`, `"Hot"`, `"Top"`, `"New"`, `"Comment count"` |
| **04**  | Input the time filter: `"All time"`, `"Past year"`, `"Past month"`, `"Past week"`, `"Today"`, `"Past hour"` |
| **05**  | Input the limit of how many posts you want to extract (example: `"17"`) |
| **06**  |Wait for the automatic download of visuals then check all saved media in `../data/visuals/` and use the CSV for analysis  |

---

## ⭐ **SEARCH FILTER 5 CHOICES**

| Step | Description |
|------|-------------|
| **01**   | `"Hot"` |
| **02**   | `"Top"` |
| **03**   | `"New"` |
| **04**   | `"Comments Count"` |
| **05**   | `"Relevance"` |

---

## ⭐ **PERIOD FILTER 6 CHOICES**

| Step | Description |
|------|-------------|
| **01**   | `"All time"` |
| **02**   | `"Past year"` |
| **03**   | `"Past month"` |
| **04**   | `"Past week"` |
| **05**   | `"Today"` |
| **06**   | `"Past hour"` |

---

# 🚀 Setup Guide: Install to Run `main_scraper.ipynb` in VS Code

This guide shows how to install the required tools, clone the repository, and run the Jupyter notebook in VS Code.

---

## STEP 1️⃣ Install Visual Studio Code

1. Download VS Code:  
   https://code.visualstudio.com/
2. Install it:
   - **Windows**: Run the `.exe`, accept defaults.
   - **macOS**: Drag **Visual Studio Code.app** into **Applications**.
   - **Linux**: Install the `.deb` file or use your package manager.

---

## STEP 2️⃣ Install Python (with pip)

1. Download the latest **Python 3**:  
   https://www.python.org/downloads/
2. **Windows only**:  
   ✔️ Check **“Add Python to PATH”** during installation.
3. **Linux**:
   ```bash
   sudo apt install python3 python3-pip
4. **Verify installation:**
python --version
pip --version

---

## STEP 3 Install Git and Git Bash
1. Download Git:
https://git-scm.com/downloads

2. Windows:
- Install Git for Windows (includes Git Bash).
- Keep default installer options.

3. **Verify:**
git --version

---

## Step 4 – Create GitHub Account and Fork the repository
4.1. Create a Github account
- Go to github.com
- create an account

4.2. Fork the repository 
- Open the original repository in your browser.
- Click **Fork** (top-right).
- You will be redirected to your forked repository : https://github.com/<your-username>/<repository-name>
---
## STEP 5 Install GitHub Desktop
1. Download & Install Github Desktop https://desktop.github.com/
2. Sign in with your GitHub account.

---

## Step 6 – Clone the Repository
1. Option A – Clone with GitHub Desktop
- Open GitHub Desktop.
- File → Clone repository…
- Select your fork (or paste the URL).
- Choose a local path (e.g. Documents/GitHub/<repo-name>).
- Click Clone.

2. Option B – Clone with Git Bash / Terminal
- type and enter : cd ~/Documents/GitHub
- type and enter : git clone https://github.com/<your-username>/<repo-name>.git
- type and enter : cd <repo-name>

## Step 7 – Open the Project in VS Code
1. Open VS Code from Github Desktop
2. Select the cloned repository folder **reddit-scraper**

---

## Step 8 – Install VS Code Extensions
1. Open Extensions (Ctrl+Shift+X / Cmd+Shift+X)

2. Install:
- Python (Microsoft)
- Jupyter (Microsoft)

3. Reload VS Code if prompted.

---

## STEP 9 - RUN THE CODE
1. Open **main_scraper.ipynb**
2. Go to 🪜 **STEPS EXTRACT+DOWNLOAD**
3. Run the code cell **🗃️ 1 - FIX EXTRACTION OF GIF CAROUSEL**
3.1. type what you want to search
3.2. type the filter
3.3. type the period
3.4. type the number of posts you want to extract and download
4. Run the code cell **🗃️ 2 - MERGE MUTE VIDEOS with AUDIOS**

---

## STEP 10 - Use CSVs files & visual content
1. All of the visual content files are in the repository directory `../data/visuals/`
2. All of the `CSV`s files are in the repository directory `../data/reddit/`
3. Use them however you like :-)
---