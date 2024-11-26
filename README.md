# TWSE Sector Classification

This project involves classifying Taiwanese stocks (TWSE) into different sectors using their GICS (Global Industry Classification Standard) sectors. The goal is to organize, categorize, and store stock data based on their sectors for further analysis.

## Features

- **Stock Classification**: Categorize Taiwanese stocks based on GICS sectors.
- **Data Collection**: Retrieve stock data, including sector information, using the Yahoo Finance API.
- **Data Storage**: Store classified stock information in JSON files for each sector.
- **Stock Information**: Includes detailed stock data such as stock symbol, sector, and industry.

## Installation

To run this project locally, you'll need to have Python and several Python packages installed.

   ## Clone the repository 

      ```bash
      git clone https://github.com/Zaphkiel1031/TWSE_Sector_Classification.git
      cd TWSE_Sector_Classification
      ```
   Install dependencies:
   Ensure you have Python 3 installed. Then, create a virtual environment and install the required dependencies.

       ```bash
       python -m venv venv
       source venv/bin/activate  # For Mac/Linux
       venv\Scripts\activate     # For Windows
       pip install -r requirements.txt
       ```
    
    ### Required Libraries:

    - **yfinance**: To fetch stock data from Yahoo Finance.
   
    - **json**: For reading and writing JSON files.
   
    - **os**: For file and directory management.
   
    ### Usage
    Run the classification script:
    
    After installing dependencies, run the GICS_sector.py script to start the classification process.

    ```bash
    python GICS_sector.py
    ```
    Output Data:

    The classified data will be saved as JSON files under the TWSE_sector_data folder. Each file will contain stock data grouped by sector.

    ### Files
   
    - **GICS_sector.py**: The main Python script for classifying stocks into sectors.
    - **TWSE_sector_data/**: Directory containing JSON files for each sector.
    - **stock_infos.json**: The stock data file containing details of stocks to be classified.
    - **.gitignore**: Specifies files to be ignored by Git.
    - **README.md**: Project documentation.
   
    ### Contributing
   
    - Fork the repository.
    - Create a new branch (git checkout -b feature-branch).
    - Commit your changes (git commit -m 'Add new feature').
    - Push to the branch (git push origin feature-branch).
    - Create a new Pull Request.


    ### Key Sections Explained
      
    - **Features**: A summary of what the project does.
    - **Installation**: Step-by-step guide to setting up the project locally.
    - **Usage**: Instructions for how to run the project.
    - **Files**: Overview of key files in the project.
    - **Contributing**: Basic guidelines for contributing to the project.
    - **License**: A simple open-source license (MIT License is a popular choice).
   
