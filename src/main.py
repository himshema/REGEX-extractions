import re
from pathlib import Path
file = Path(__file__).parent.parent / "inputs" / "data.txt"

mail_pattern = re.compile(r"[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9\_\-\.]+\.com")
alueducation_mail = re.compile(r"[a-zA-Z0-9\-\_\.]+@alueducation+\.com")

def validate_emails(email):
    if alueducation_mail.fullmatch(email):
        return "Valid mail"
    else: return"Invalid email"

def extract_emails(text):
    emails = mail_pattern.findall(text)
    results = []
    for email in emails:
        results.append({
            "email": email,
            "status": validate_emails(email)
            })
    return results

def main():
    text = file.read_text(encoding="utf-8")
    emails = extract_emails(text)
    for item in emails:
        print(
            f"{item['email']:60}"
            F"{item['status']}"
        )

    
if __name__ == "__main__":
    main()