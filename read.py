import pdfplumber
import re

results = []

with pdfplumber.open("merged_all.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if not text:
            continue

        # Extract Name
        name_match = re.search(r"CANDIDATE'S NAME\s*:\s*(.+?)\s+ROLL", text)

        # Extract ONLY "SEMESTER TOTAL" (not third semester / grand total)
        sem_match = re.search(r"SEMESTER TOTAL\s*:\s*\d+\s+\d+\s+(\d+)", text)

        if name_match and sem_match:
            name = name_match.group(1).strip()
            semester_total = int(sem_match.group(1))
            results.append((name, semester_total))

# Sort by Semester Total (highest first)
results.sort(key=lambda x: x[1], reverse=True)

print("\nSEMESTER TOTAL LIST (Sorted):\n")

for i,(name, total) in enumerate(results):
    print(f" {i+1}. {name}  -->  {total}")
