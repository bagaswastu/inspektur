import random

from bs4 import BeautifulSoup

from holehe.localuseragent import ua


async def pornhub(email, client, out):
    name = "Pornhub"
    domain = "pornhub.com"
    method = "register"
    frequent_rate_limit = False

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en,en-US;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    try:
        req = await client.get("https://www.pornhub.com/signup", headers=headers)
    except BaseException:
        out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
        return None
    soup = BeautifulSoup(req.content, features="html.parser")
    try:
        toe = soup.find(attrs={"name": "token"}).get("value")
    except BaseException:
        out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
        return None

    params = {
        'token': toe,
    }

    data = {
        'check_what': 'email',
        'email': email
    }

    response = await client.post(
        'https://www.pornhub.com/user/create_account_check',
        headers=headers,
        params=params,
        data=data)
    try:
        if response.json()["error_message"] == "Email has been taken.":
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rate_limit": False,
                        "exists": True,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
        else:
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rate_limit": False,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
    except BaseException:
        out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
