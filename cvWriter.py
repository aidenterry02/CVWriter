from fpdf import FPDF
import openai
import pandas as pd
import re
import os

# Set up your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Load your scraped LinkedIn data
file_path = r"C:\\Users\\aiden\\Downloads\\LinkedInJobsScraper_20_jobs_2024-09-07.csv"
linkedin_jobs_df = pd.read_csv(file_path)

# Check if the CSV loaded correctly
print(f"Loaded {len(linkedin_jobs_df)} jobs from CSV")

# Function to extract details from Aiden's resume with expanded project descriptions
def get_resume_info():
    resume_info = {
        "name": "your name",
        "email": "Your Email",
        "phone": "Your Phone Number",
        "address": "Your Address",
        "experience": [
            "Your Experince"
        ],
        "leadership": [
            "Your Leadership"
        ],
        "skills": [
            "Your Skills"
        ],
        "certifications": [
            "Your Certs"
        ]
    }
    return resume_info

# Function to sanitize text by replacing unsupported characters
def sanitize_text(text):
    replacements = {
        "\u2013": "-",  # Replace en dash with regular dash
        "\u2014": "-",  # Replace em dash with regular dash
        "\u2018": "'",  # Replace left single quote
        "\u2019": "'",  # Replace right single quote
        "\u2026": "...",  # Replace ellipsis with three dots
    }
    for target, replacement in replacements.items():
        text = text.replace(target, replacement)
    return text

# Function to generate a personalized cover letter using Aiden Terry's resume details
def generate_cover_letter(job_title, company_name, skills, resume_info):
    experience = "\n".join(resume_info["experience"])
    leadership = "\n".join(resume_info["leadership"])
    skills_list = ", ".join(resume_info["skills"])
    certifications = ", ".join(resume_info["certifications"])

    cover_letter = f"""
{resume_info["name"]}
{resume_info["address"]}
{resume_info["email"]} | {resume_info["phone"]}
    
September 7, 2024

Hiring Manager
{company_name}

Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company_name}. With a dual degree in "Degree" from "School", and hands-on experience in a variety of technical projects, I am confident that my background aligns perfectly with the requirements of this role.

Throughout my academic and project work, I have developed an array of skills, from "Expand Here". For instance, "Give Examples" These projects allowed me to apply my problem-solving and critical thinking abilities to real-world challenges.

In leadership roles such as "Blah Blah Blah"

With proficiency in {skills_list}, I am confident that my technical skills and leadership experience would allow me to make meaningful contributions to {company_name}. I am enthusiastic about the opportunity to bring my expertise to your team and help {company_name} achieve its goals.

Thank you for considering my application. I look forward to discussing how I can contribute to the success of your team.

Sincerely,
"Your Name"
"""

    return sanitize_text(cover_letter.strip())

# Function to generate a PDF for each job application with reduced line spacing
def create_pdf(job_title, company_name, cover_letter, file_name):
    pdf = FPDF()
    pdf.add_page()

    # Set font (replace with Aptos equivalent or system font like Arial)
    pdf.set_font('Arial', '', 11)

    # Title and Company
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 8, f"Cover Letter for {sanitize_text(job_title)} at {sanitize_text(company_name)}", ln=True, align='C')
    
    # Line break
    pdf.ln(5)
    
    # Cover letter content - sanitize it to avoid encoding issues, reduced line spacing
    pdf.set_font("Arial", '', 11)
    pdf.multi_cell(0, 7, cover_letter)  # Reduced line spacing to 7

    # Sanitize the file name by removing invalid characters
    if pd.isna(company_name):  # Handle missing company name
        company_name = "Unknown_Company"
    
    sanitized_file_name = re.sub(r'[\\/*?:"<>|]', "", f"{sanitize_text(job_title.replace(' ', '_'))}_at_{sanitize_text(company_name.replace(' ', '_'))}")
    
    # Debug: Show the file name
    print(f"Saving PDF as {sanitized_file_name}.pdf")

    # Save the PDF file to a specific directory
    output_directory = "C:\\Users\\aiden\\Documents\\CoverLetters"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    pdf.output(os.path.join(output_directory, f'{sanitized_file_name}.pdf'))

# Main process to generate cover letters for all jobs
resume_info = get_resume_info()

for index, row in linkedin_jobs_df.iterrows():
    job_title = row['Title']
    company_name = row['Company Name']
    skills = row['Skills']
    
    # Ensure job title and skills are not NaN
    if pd.isna(job_title):
        print(f"Skipping job at index {index} due to missing title.")
        continue
    if pd.isna(skills):
        skills = "No specific skills listed"
    
    # Generate the cover letter
    cover_letter = generate_cover_letter(job_title, company_name, skills, resume_info)
    
    # Create and save the PDF
    create_pdf(job_title, company_name, cover_letter, job_title)

print("Cover letter generation completed.")
