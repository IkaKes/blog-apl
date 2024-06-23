document.addEventListener('DOMContentLoaded', function () {
    fetchPosts();
});

function fetchPosts() {
    fetch('/api/posts')
        .then(response => response.json())
        .then(data => {
            const postsList = document.getElementById('posts-list');
            postsList.innerHTML = '';
            data.forEach(post => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <div>
                        <h2>${post.title}</h2>
                        <p>${post.content}</p>
                    </div>
                    <button onclick="deletePost(${post.id})">Delete</button>
                `;
                postsList.appendChild(li);
            });
        });
}

function addPost() {
    const title = document.getElementById('post-title').value;
    const content = document.getElementById('post-content').value;
    fetch('/api/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, content })
    })
    .then(response => response.json())
    .then(post => {
        fetchPosts();
        document.getElementById('post-title').value = '';
        document.getElementById('post-content').value = '';
    });
}

function deletePost(postId) {
    fetch(`/api/posts/${postId}`, {
        method: 'DELETE'
    })
    .then(() => {
        fetchPosts();
    });
}
