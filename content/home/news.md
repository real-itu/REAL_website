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

<div id="bluesky-feed"></div>
<script>
  const blueskyHandle = '@real.itu.dk';

  async function fetchBlueSkyFeed() {
    try {
      const response = await fetch(`https://bsky.app/profile/real.itu.dk`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      
      const feedContainer = document.getElementById('bluesky-feed');
      data.posts.forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.className = 'bluesky-post';
        postDiv.innerHTML = `<p>${post.text}</p>`;
        feedContainer.appendChild(postDiv);
      });
    } catch (error) {
      console.error('Error fetching Bluesky feed:', error);
    }
  }
  fetchBlueSkyFeed();
</script>


