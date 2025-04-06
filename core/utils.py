def detect_tech_stack(html, headers=None):
    headers = headers or {}
    stack = []

    # Basic CMS + JS framework detection
    if "wp-content" in html or "WordPress" in headers.get("X-Powered-By", ""):
        stack.append("WordPress")
    if "Joomla" in html:
        stack.append("Joomla")
    if "Drupal" in html:
        stack.append("Drupal")
    if "Magento" in html:
        stack.append("Magento")

    if "React" in html or "react" in html:
        stack.append("ReactJS")
    if "vue" in html or "Vue" in html:
        stack.append("VueJS")
    if "angular" in html:
        stack.append("Angular")

    if "php" in headers.get("X-Powered-By", "").lower():
        stack.append("PHP")
    if "java" in headers.get("X-Powered-By", "").lower():
        stack.append("Java")
    if "asp.net" in headers.get("X-Powered-By", "").lower():
        stack.append("ASP.NET")

    if not stack:
        stack.append("Unknown")

    return list(set(stack))

