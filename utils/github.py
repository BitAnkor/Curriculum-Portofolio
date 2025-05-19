# utils/github.py
import httpx

GITHUB_USERNAME = "BitAnkor"

async def obtener_proyectos(limit=3):
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            repos = response.json()
            return [
                {
                    "nombre": repo["name"],
                    "descripcion": repo["description"],
                    "url": repo["html_url"],
                    "imagen": f"/static/proyectos/{repo['name']}.jpg"
                }
                for repo in sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)[:limit]
            ]
        return []
