import requests

def search_jobs(role):
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)
    data = response.json()

    role = role.lower()
    jobs = []

    # Auto-keyword generation based on role input
    keywords = []

    # Split role into words → Example: "flutter developer" → ["flutter", "developer"]
    for word in role.split():
        keywords.append(word)

    # Add role-specific boosters
    if "python" in role:
        keywords += ["python", "django", "flask"]
    if "flutter" in role:
        keywords += ["flutter"]
    if "backend" in role:
        keywords += ["backend", "node", "api", "server"]
    if "full stack" in role or "fullstack" in role:
        keywords += ["full stack", "mern", "react", "node"]
    if "frontend" in role:
        keywords += ["frontend", "react", "ui", "javascript"]
    if "java" in role:
        keywords += ["java", "spring", "spring boot"]

    # Remove duplicates
    keywords = list(set(keywords))

    # Start matching
    for job in data["jobs"]:
        title = job["title"].lower()

        # Strict Matching → title must contain ANY keyword
        if any(kw in title for kw in keywords):
            jobs.append({
                "company": job["company_name"],
                "title": job["title"],
                "link": job["url"]
            })

        if len(jobs) == 5:
            break

    return jobs if jobs else [{"company": "No Jobs Found", "title": "", "link": "#"}]
