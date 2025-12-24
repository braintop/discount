import requests
from typing import Any, Dict, List, Optional


class JsonPlaceholderPostsCRUD:
    """
    CRUD wrapper for https://jsonplaceholder.typicode.com/posts

    Note:
        This API is a fake demo API. POST/PUT/DELETE won't actually
        change data on the server, but will return a simulated response.
    """

    def __init__(self, base_url: str = "https://jsonplaceholder.typicode.com"):
        self.base_url = base_url.rstrip("/")

    # ---------- Helpers ----------
    def _url(self, path: str) -> str:
        return f"{self.base_url}/{path.lstrip('/')}"

    def _handle_response(self, resp: requests.Response) -> Any:
        resp.raise_for_status()
        # JSONPlaceholder always returns JSON for these endpoints
        return resp.json()

    # ---------- CRUD operations ----------
    def list_posts(self, user_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        GET /posts
        Optionally filter by userId.
        """
        params: Dict[str, Any] = {}
        if user_id is not None:
            params["userId"] = user_id
        resp = requests.get(self._url("posts"), params=params, timeout=10)
        return self._handle_response(resp)

    def get_post(self, post_id: int) -> Dict[str, Any]:
        """
        GET /posts/{id}
        """
        resp = requests.get(self._url(f"posts/{post_id}"), timeout=10)
        return self._handle_response(resp)

    def create_post(self, title: str, body: str, user_id: int) -> Dict[str, Any]:
        """
        POST /posts
        """
        payload = {"title": title, "body": body, "userId": user_id}
        resp = requests.post(self._url("posts"), json=payload, timeout=10)
        return self._handle_response(resp)

    def update_post(
        self,
        post_id: int,
        title: Optional[str] = None,
        body: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        PUT /posts/{id}
        Sends a full resource representation. Fields you don't pass
        are left as-is (we first GET current state, then merge).
        """
        # Get current data so that omitted fields are preserved
        current = self.get_post(post_id)

        updated = {
            "title": title if title is not None else current.get("title"),
            "body": body if body is not None else current.get("body"),
            "userId": user_id if user_id is not None else current.get("userId"),
            "id": post_id,
        }
        resp = requests.put(self._url(f"posts/{post_id}"), json=updated, timeout=10)
        return self._handle_response(resp)

    def patch_post(
        self,
        post_id: int,
        title: Optional[str] = None,
        body: Optional[str] = None,
        user_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        PATCH /posts/{id}
        Partially update a post (only the provided fields).
        """
        payload: Dict[str, Any] = {}
        if title is not None:
            payload["title"] = title
        if body is not None:
            payload["body"] = body
        if user_id is not None:
            payload["userId"] = user_id

        resp = requests.patch(self._url(f"posts/{post_id}"), json=payload, timeout=10)
        return self._handle_response(resp)

    def delete_post(self, post_id: int) -> bool:
        """
        DELETE /posts/{id}
        Returns True if the request succeeded (2xx).
        """
        resp = requests.delete(self._url(f"posts/{post_id}"), timeout=10)
        resp.raise_for_status()
        return True


if __name__ == "__main__":
    # Simple demo usage
    crud = JsonPlaceholderPostsCRUD()

    # List first 3 posts
    posts = crud.list_posts()
    print("First 3 posts:")
    for p in posts[:3]:
        print(f"{p['id']}: {p['title']}")

    # Get a single post
    one = crud.get_post(1)
    print("\nPost 1:", one)

    # Create a new post (fake)
    created = crud.create_post("My title", "My body", user_id=1)
    print("\nCreated:", created)

    # Use an existing real post id for update/patch/delete to avoid 404 from GET
    existing_post_id = 1

    # Update (PUT) the post (fake)
    updated = crud.update_post(existing_post_id, title="Updated title")
    print("\nUpdated:", updated)

    # Patch the post (fake)
    patched = crud.patch_post(existing_post_id, body="Patched body")
    print("\nPatched:", patched)

    # Delete (fake)
    deleted_ok = crud.delete_post(existing_post_id)
    print("\nDeleted OK:", deleted_ok)

