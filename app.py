<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Latest Tech Headlines</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1, h2 { color: #333; }
        ul { list-style: none; padding: 0; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: #007BFF; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Latest Tech Headlines</h1>

    {% for headline, articles in articles_by_headline.items() %}
        <h2>{{ headline }}</h2>
        <ul>
            {% for article in articles %}
                <li><a href="{{ article.url }}" target="_blank">{{ article.title }}</a></li>
            {% endfor %}
        </ul>
    {% endfor %}
</body>
</html>
