# Automated Cover Letter Generator - README

## Overview
This Python script automates the creation of personalized cover letters in PDF format for job applications. Using scraped job data from LinkedIn and predefined resume information, it generates tailored cover letters and saves them to a specified directory. The script integrates OpenAI's API for enhanced customization and ensures compatibility with PDF output.

---

## Features
1. **Dynamic Cover Letter Generation**:
   - Personalizes cover letters based on job title, company name, and required skills.
   - Integrates resume details, including experience, leadership, skills, and certifications.

2. **PDF Export**:
   - Generates cover letters in PDF format with a professional layout and reduced line spacing.
   - Saves the PDF files to a specified directory.

3. **Data Sanitization**:
   - Replaces unsupported characters to ensure compatibility with PDF and file systems.

4. **Batch Processing**:
   - Processes multiple job entries from a LinkedIn jobs CSV file.

---

## Prerequisites
1. **Python 3.x** installed on your machine.
2. Required libraries:
   - `fpdf`
   - `openai`
   - `pandas`
   - `re`
   - `os`
3. An OpenAI API key. Replace `"YOUR_API_KEY"` in the script with your API key.
4. A CSV file containing scraped job data, structured as follows:
   - `Title`: Job title
   - `Company Name`: Employer
   - `Skills`: Required skills for the job

---

## Installation
1. Clone the repository or download the script file.
2. Install required dependencies:
   ```bash
   pip install fpdf openai pandas
   ```
3. Place your LinkedIn jobs CSV file in a known directory and update the `file_path` variable in the script with the file's location.

---

## Usage

### 1. Run the Script
Execute the script using Python:
```bash
python cover_letter_generator.py
```

### 2. Process Job Entries
- The script iterates through the job entries in the provided CSV file.
- For each job:
  - Generates a personalized cover letter.
  - Saves the cover letter as a PDF in the specified output directory (`C:\\Users\\aiden\\Documents\\CoverLetters`).

---

## Example Interaction
### Input
- A CSV file (`LinkedInJobsScraper_20_jobs_2024-09-07.csv`) with the following structure:
   ```csv
   Title,Company Name,Skills
   Software Engineer,OpenAI,Python, Machine Learning, APIs
   Data Analyst,Google,SQL, Data Visualization, Tableau
   ```

### Output
- A PDF file for each job, saved with sanitized filenames:
   ```
   CoverLetters/
   ├── Software_Engineer_at_OpenAI.pdf
   ├── Data_Analyst_at_Google.pdf
   ```

### Sample Cover Letter
```plaintext
Your Name
Your Address
Your Email | Your Phone Number
    
September 7, 2024

Hiring Manager
OpenAI

Dear Hiring Manager,

I am writing to express my interest in the Software Engineer position at OpenAI. With a dual degree in "Degree" from "School", and hands-on experience in a variety of technical projects, I am confident that my background aligns perfectly with the requirements of this role.

Throughout my academic and project work, I have developed an array of skills, from Python to APIs. For instance, [Project Example]. These projects allowed me to apply my problem-solving and critical thinking abilities to real-world challenges.

With proficiency in Python, Machine Learning, APIs, I am confident that my technical skills and leadership experience would allow me to make meaningful contributions to OpenAI. I am enthusiastic about the opportunity to bring my expertise to your team and help OpenAI achieve its goals.

Thank you for considering my application. I look forward to discussing how I can contribute to the success of your team.

Sincerely,
Your Name
```

---

## Customization
1. **Resume Details**:
   Update the `get_resume_info()` function with your personal information, experience, leadership roles, skills, and certifications.

2. **Output Directory**:
   Modify the `output_directory` variable in the `create_pdf()` function to change the destination folder for PDFs.

3. **Skills and Project Examples**:
   Customize the `generate_cover_letter()` function to include specific projects or skills relevant to your resume.

---

## Error Handling
- Skips job entries with missing titles or skills.
- Sanitizes file and text content to avoid encoding issues.
- Creates the output directory if it does not exist.

---

## Limitations
1. **Resume Details**: Must be manually updated in the script.
2. **File Path**: Ensure the CSV file path is correctly set in the `file_path` variable.
3. **API Costs**: Using OpenAI's API may incur costs based on usage.

---

## Future Enhancements
- Add a GUI for easier input and customization.
- Support for additional document formats (e.g., Word).
- Integration with job application platforms for direct submission.

---

## License
This script is provided for personal and educational use. Ensure compliance with OpenAI's API terms of service when using this code.
