import random

from holehe.localuseragent import ua


async def discord(email, client, out):
    name = "Discord"
    domain = "discord.com"
    method = "register"
    frequent_rate_limit = False

    def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return (result_str)

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'en-US',
        'Content-Type': 'application/json',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    data = '{"fingerprint":"","email":"' + str(email) + '","username":"' + get_random_string(
        20) + '","password":"' + get_random_string(
        20) + '","invite":null,"consent":true,"date_of_birth":"","gift_code_sku_id":null,"captcha_key":null}'

    response = await client.post(
        'https://discord.com/api/v8/auth/register',
        headers=headers,
        data=data)
    responseData = response.json()
    try:
        if "code" in responseData.keys():
            try:
                if responseData["errors"]["email"]["_errors"][0]['code'] == "EMAIL_ALREADY_REGISTERED":
                    out.append(
                        {"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                         "rate_limit": False,
                         "exists": True,
                         "email_recovery": None,
                         "phone_number": None,
                         "others": None})
                else:
                    out.append(
                        {"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                         "rate_limit": False,
                         "exists": False,
                         "email_recovery": None,
                         "phone_number": None,
                         "others": None})
            except BaseException:
                out.append(
                    {"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                     "rate_limit": True,
                     "exists": False,
                     "email_recovery": None,
                     "phone_number": None,
                     "others": None})
        elif responseData["captcha_key"][0] == "captcha-required":
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rate_limit": False,
                        "exists": False,
                        "email_recovery": None,
                        "phone_number": None,
                        "others": None})
        else:
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rate_limit": True,
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
