import os

from html_minifier.minify import Minifier

def main():
    with open("templates/index.html") as file:
        content = file.read()
    
    content = content.replace("{{title}}", "Test Page")
    content = content.replace("{{content}}", "This is a test page.")
    content = Minifier(content).minify()
    
    os.makedirs("docs/", exist_ok=True)
    
    with open("docs/index.html", "w") as file:
        file.write(content)

if __name__ == "__main__":
    main()
