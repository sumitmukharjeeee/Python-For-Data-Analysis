from bs4 import BeautifulSoup

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Test Workshop</title>
</head>
<body>
    <h1 id="main-title">Welcome to the Scraping Sandbox</h1>
    <p class="description">This is a simple HTML paragraph used for testing Python web scrapers.</p>
    
    <div class="content-box" data-category="featured">
        <h2>Featured Articles</h2>
        <ul class="article-list">
            <li><a href="https://example.com" class="link" id="link-1">How to Learn Python</a></li>
            <li><a href="https://example.com" class="link" id="link-2">Mastering Beautiful Soup</a></li>
            <li><a href="https://example.com" class="link" id="link-3">Understanding HTML Structures</a></li>
        </ul>
    </div>

    <div class="content-box" data-category="archived">
        <h2>Archived Content</h2>
        <p class="description">Old articles are stored here.</p>
    </div>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')

# Page title
print(soup.title.text)

