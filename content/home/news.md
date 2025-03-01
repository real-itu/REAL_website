---
# Documentation: https://sourcethemes.com/academic/docs/page-builder/
widget: blank

# Activate this widget? true/false
active: true

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 25

title: News
---

<div id="bsky-feed" style="width:100%; height:550px; overflow-y:auto;"></div>

<script>
  (function() {
    // Function to fetch and display Bluesky posts
    async function fetchBskyPosts() {
      try {
        // Replace with the actual API endpoint when Bluesky provides one
        // This is a placeholder as Bluesky doesn't have a public embed API yet
        const response = await fetch('https://api.bsky.app/v1/feed/profile/roboevoartlab.bsky.social');
        const data = await response.json();
        
        const feedContainer = document.getElementById('bsky-feed');
        
        if (data && data.posts) {
          data.posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.className = 'bsky-post';
            postElement.innerHTML = `
              <div style="border: 1px solid #e1e8ed; border-radius: 12px; padding: 15px; margin-bottom: 15px;">
                <div style="font-weight: bold;">${post.author}</div>
                <div style="margin-top: 10px;">${post.text}</div>
                <div style="color: #657786; font-size: 0.85em; margin-top: 10px;">${new Date(post.createdAt).toLocaleString()}</div>
              </div>
            `;
            feedContainer.appendChild(postElement);
          });
        } else {
          feedContainer.innerHTML = '<p>Please visit our <a href="https://bsky.app/profile/roboevoartlab.bsky.social" target="_blank">Bluesky profile</a> to see our latest updates.</p>';
        }
      } catch (error) {
        console.error('Error fetching Bluesky posts:', error);
        document.getElementById('bsky-feed').innerHTML = '<p>Unable to load Bluesky feed. Please visit our <a href="https://bsky.app/profile/roboevoartlab.bsky.social" target="_blank">Bluesky profile</a> directly.</p>';
      }
    }
    
    // Call the function when the page loads
    window.addEventListener('DOMContentLoaded', fetchBskyPosts);
  })();
</script>
