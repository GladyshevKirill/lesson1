import requests


class YougileClient:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def create_project(self, title: str):
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            headers=self.headers,
            json={"title": title},
            timeout=15,
        )

    def get_project(self, project_id: str):
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers,
            timeout=15,
        )

    def update_project(self, project_id: str, title: str):
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers,
            json={"title": title},
            timeout=15,
        )
