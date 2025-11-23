import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        """Fetch all posts from JSONPlaceholder."""
        try:
            response = requests.get(f"{self.BASE_URL}/posts")
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            return None

    def create_post(self, title, body, user_id):
        """Create a new post and return the response."""
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        try:
            response = requests.post(f"{self.BASE_URL}/posts", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating post: {e}")
            return None


# -----------------------------
# Example Usage
# ------------------------------

if __name__ == "__main__":
    client = JSONPlaceholderClient()

    # Fetch posts
    posts = client.get_posts()
    print("Fetched Posts:", posts[:3])  # Print first 3 posts

    # Create a new post
    new_post = client.create_post("My Title", "My Post Body", user_id=1)
    print("Created Post:", new_post)
