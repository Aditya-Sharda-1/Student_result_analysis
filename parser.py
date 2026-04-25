import pdfplumber
import re

def extract_results(file):
    results = []

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            name_match = re.search(r"CANDIDATE'S NAME\s*:\s*(.+?)\s+ROLL", text)
            sem_match = re.search(r"SEMESTER TOTAL\s*:\s*\d+\s+\d+\s+(\d+)", text)

            if name_match and sem_match:
                name = name_match.group(1).strip()
                total = int(sem_match.group(1))
                results.append((name, total))

    return results