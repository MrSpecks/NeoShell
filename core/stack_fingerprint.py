def detect_stack(headers, body):
    guess = []

    # Server headers
    server = headers.get("Server", "").lower()
    powered = headers.get("X-Powered-By", "").lower()

    if "nginx" in server:
        guess.append("Nginx")
    if "apache" in server:
        guess.append("Apache")
    if "iis" in server or "asp.net" in powered:
        guess.append("IIS / ASP.NET")
    if "php" in powered or ".php" in body:
        guess.append("PHP")
    if ".jsp" in body:
        guess.append("Java / JSP")
    if "wp-content" in body or "wp-login" in body:
        guess.append("WordPress")
    if "react" in body.lower():
        guess.append("ReactJS")
    if "vue" in body.lower():
        guess.append("VueJS")
    if "angular" in body.lower():
        guess.append("Angular")

    return list(set(guess)) if guess else ["Unknown"]