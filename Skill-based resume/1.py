class Resume:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.skills = []
        self.experience = []

    def add_skill(self, skill, proficiency):
        """Add a skill to the resume."""
        self.skills.append({"Skill": skill , "Proficiency": proficiency})

    def add_experience(self, position, company, start_date, end_date, responsibilities):
        """Add work experience to the resume."""
        experience_entry = {
            "Position": position,
            "Company": company,
            "Start Date": start_date,
            "End Date": end_date,
            "Responsibilities": responsibilities
        }
        self.experience.append(experience_entry)

    def generate_resume(self):
        """Generate the skills-based resume."""
        resume = f"Skills-Based Resume: {self.name}\n"
        resume += f"Email: {self.email} | Phone: {self.phone}\n\n"
        
        if self.skills:
            resume += "Skills:\n"
            for skill in self.skills:
                resume += f"- {skill['Skill']} ({skill['Proficiency']})\n"
            resume += "\n"
        
        if self.experience:
            resume += "Work Experience:\n"
            for entry in self.experience:
                resume += f"{entry['Position']} at {entry['Company']} ({entry['Start Date']} - {entry['End Date']})\n"
                for responsibility in entry['Responsibilities']:
                    resume += f"  - {responsibility}\n"
            resume += "\n"

        return resume

# Example usage:
resume_builder = Resume("Hritick Jha", "jhahritick@gmail.com", "9819875737")
resume_builder.add_skill("Python", "Advanced")
resume_builder.add_skill("Data Analysis", "Intermediate")
resume_builder.add_experience("Software Developer", "Tech Solutions Inc.", "2020-01-01", "2022-01-01", ["Developed and maintained web applications", "Collaborated with cross-functional teams"])
resume_builder.add_experience("Junior Developer", "CodeCrafters LLC", "2018-05-01", "2019-12-31", ["Assisted in designing and implementing software solutions"])
Hritick_resume = resume_builder.generate_resume()

print(Hritick_resume)

