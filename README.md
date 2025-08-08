# Press-Search-Tool
- Author: Dagem Legesse
- Version: 1.0
## Overview
The Press Search Tool is a python CLI application helping users find, filter and export press articles from reputable sources based on keywords or location. It automatically filters out unreliable outlets, cleans the results and exports to a csv using an API application - NewsAPI. 

#### Key Features:
- Search articles by keyword or location
- Filter by date (optional)
- Automatically remove unreliable sources
- Export a clean, ready to use csv

#### How it works
- Tell the tool what you're looking for - either a keyword or location
- Tool searches the NewsApi database for relevant articles
- Removes unverified sources (This can be adjustable)
- Saves cleaned results as a csv file for you to open
- If needed, you may add or adjust the list of non reputable sources, refer to Option 1 - step 7

#### Ways to Use this Tool
1. Google Colab
2. On your Computer

#### Option 1 - Running in Google Colab
1. Open Google Colab link provided to you
    - https://colab.research.google.com/drive/1Avntt_UUZ9g281_ggxCz-pC-OB7rXKKe?usp=sharing
2. In Colab, go to each individual cell block numbered in order e.g. [1]
3. Once each block is executed, a green check mark should appear next to each block
    - If not then restart program by clicking the down arrow v which is to the left of the up arrow then click disconnect and delete runtime. Repeat steps 1-3.
4. When prompted, enter:
    - keyword (e.g. Medicaid)
    - whether you want to filter by date (yes or no)
    - if yes enter date in YYYY-MM-DD format
5. Wait for program to run
6. Download the csv file by clicking on the folder icon
7. OPTIONAL - To manually adjust list of "bad outlets" click the folder icon, then click Press-Search-Tool, then click src, then click cleaner.py. From there manually type in outlets you want to eliminate from the exported csv. Be sure the outlet is in lowercase.

#### Option 2
Requirements:
- Python
- Git
- NewAPI Key (free to sign up)

Step 1:
git clone https://github.com/YOUR-USERNAME 
    - real clone repository link can be found in block 1 of Google Colab file. Refer to Option 1 -step one for Colab access

Then:
cd press-search-tool

Step 2:
pip install all dependencies - there may be more!
    - pip install python-dotenv

Step 4:
Create an .env file and add the following
NEWS_API_KEY=your_api_key_here

Step 5:
run python src/main.py into terminal

A csv file should appear in your data folder.

#### Example Run
Welcome to Press Search Tool by Dagem Legesse.
Option A: Topic (e.g., Medicaid) or Option B: Location (e.g., New York City)
Please enter your keyword or location: New York City
Do you want to filter by date? (Y/N): NO
Exported results to data/press_search_new york city.csv

#### Challenges
- Only 100 API calls per day
- Manual addition of non reputable sources


#### Support 
For help using this tool, contact Dagem Legesse at dagemle@gmail.com








