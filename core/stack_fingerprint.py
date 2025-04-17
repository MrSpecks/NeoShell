def detect_stack(headers, body):
    guess = []

    # Server headers
    server = headers.get("Server", "").lower()
    powered = headers.get("X-Powered-By", "").lower()

    # Detecting various server technologies based on header data
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
    if "tomcat" in server:
        guess.append("Tomcat")

   
    # Detecting additional server technologies based on body content
    if "wp-content" in body or "wp-json" in body:
        guess.append("WordPress")
    if "thinkphp" in powered or "thinkphp" in body.lower():
        guess.append("ThinkPHP")
    if "react" in body.lower():
        guess.append("ReactJS")
    if "vue" in body.lower():
        guess.append("VueJS")
    if "angular" in body.lower():
        guess.append("Angular")
    if "tomcat" in powered or "JSESSIONID" in headers.get("Set-Cookie", "").lower():
        guess.append("Tomcat")
    if "java" in powered:
        guess.append("Java")
    if "apache" in powered:
        guess.append("Apache")

    # Return list of tech stacks found, or 'Unknown' if none
    return list(set(guess)) if guess else ["Unknown"]