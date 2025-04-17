import requests
from bs4 import BeautifulSoup

def detect_tech_stack(url):
    """
    Detects the tech stack of a given website by analyzing headers and body content.
    Args:
    - url (str): The target website URL.

    Returns:
    - List of identified tech stacks (str).
    """
    headers = requests.head(url).headers  # We do a HEAD request for quicker response
    tech_stack = []

    # Checking HTTP Headers
    if "X-Powered-By" in headers:
        powered_by = headers["X-Powered-By"].lower()
       
        # PHP Detection
        if "php" in powered_by:
            tech_stack.append("PHP")
       
        # Node.js Detection
        elif "express" in powered_by:
            tech_stack.append("Node.js (Express)")
       
        # ASP.NET Detection
        elif "asp.net" in powered_by:
            tech_stack.append("ASP.NET")
       
        # ThinkPHP Detection
        elif "thinkphp" in powered_by:
            tech_stack.append("ThinkPHP")
       
        # Tomcat Detection
        elif "tomcat" in powered_by:
            tech_stack.append("Tomcat")

    # Checking HTML Body for Known Patterns
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # WordPress detection (search for wp-content)
    if "wp-content" in response.text or "wp-admin" in response.text:
        tech_stack.append("WordPress")

    # ReactJS detection (check for React specific window object)
    if "window.__REACT_DEVTOOLS_GLOBAL_HOOK__" in response.text:
        tech_stack.append("ReactJS")

    # Joomla detection
    if "Joomla!" in response.text:
        tech_stack.append("Joomla")

    # Java (Servlet/JSP) detection (look for servlet-related patterns)
    if "X-Powered-By" in headers and "java" in headers["X-Powered-By"].lower():
        tech_stack.append("Java (Servlet/JSP)")

    # Apache Detection (look for Apache in the server header)
    if "server" in headers and "apache" in headers["server"].lower():
        tech_stack.append("Apache")

    # Check for file extensions in URLs that indicate certain technologies
    if ".php" in url:
        tech_stack.append("PHP")
    if ".asp" in url or ".aspx" in url:
        tech_stack.append("ASP.NET")
    if ".jsp" in url:
        tech_stack.append("Java (JSP)")

    # Return the identified tech stacks
    return tech_stack