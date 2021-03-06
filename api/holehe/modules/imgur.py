import random

from holehe.localuseragent import ua


async def imgur(email, client, out):
    name = "Imgur"
    domain = "imgur.com"
    method = "register"
    frequent_rate_limit=True

    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://imgur.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    r = await client.get("https://imgur.com/register?redirect=%2Fuser", headers=headers)

    headers["X-Requested-With"] = "XMLHttpRequest"

    data = {
        'email': email
    }

    response = await client.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data)
    if response.status_code == 200:
        if response.json()["data"]["available"] or "Invalid email domain" in response.text :
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
        else:
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": True,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
    else:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
