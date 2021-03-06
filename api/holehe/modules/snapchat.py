import random

from holehe.localuseragent import ua


async def snapchat(email, client, out):
    name = "Snapchat"
    domain = "snapchat.com"
    method = "login"
    frequent_rate_limit=False

    req = await client.get("https://accounts.snapchat.com")
    xsrf = req.text.split('data-xsrf="')[1].split('"')[0]
    webClientId = req.text.split('ata-web-client-id="')[1].split('"')[0]
    url = "https://accounts.snapchat.com/accounts/merlin/login"
    headers = {
        "Host": "accounts.snapchat.com",
        "User-Agent": random.choice(ua["browsers"]["firefox"]),
        "Accept": "*/*",
        "X-XSRF-TOKEN": xsrf,
        "Accept-Encoding": "gzip, late",
        "Content-Type": "application/json",
        "Connection": "close",
        "Cookie": "xsrf_token=" + xsrf + "; web_client_id=" + webClientId
    }
    data = '{"email":' + email + ',"app":"BITMOJI_APP"}'

    response = await client.post(url, data=data, headers=headers)
    try:
        if response.status_code != 204:
            data = response.json()
            out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                        "rate_limit": False,
                        "exists": data["hasSnapchat"],
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
            return None
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": False,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
    except BaseException:
        out.append({"name": name,"domain":domain,"method":method,"frequent_rate_limit":frequent_rate_limit,
                    "rate_limit": True,
                    "exists": False,
                    "email_recovery": None,
                    "phone_number": None,
                    "others": None})
