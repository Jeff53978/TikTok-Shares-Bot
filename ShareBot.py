import threading, requests, sys, random, time, os

def send_request(url, thread, proxy):
    for i in range(100):
        try:
            request = requests.get(f"{url}?lang=en&is_copy_url=0&is_from_webapp=v1&sender_device=pc&sender_web_id={random.randint(10000000, 90000000)}", proxies=proxy, timeout=10)
            if request.status_code == 200:
                sys.stdout.write(f"\033[92m [*] Shared video Thread: {thread} \n")
            else:
                sys.stdout.write(f"\033[93m [!] Rate limited Thread: {thread} \n")
        except:
            pass

def main():
    print("TikTok Share Bot - Snikker#1337", "\n")
    time.sleep(0.5)
    url = input("[?] Enter tiktok video url: ")
    time.sleep(1)
    print("[*] Sending Requests...", "\n")
    time.sleep(2)
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all"
    open(f"{os.getenv('TEMP')}\\proxies.txt", "wb").write(requests.get(url).content)
    proxies = []
    for line in open(f"{os.getenv('TEMP')}\\proxies.txt", "r"):
        proxy = line.strip("\n")
        proxydict = {
            "https": f"socks5://{proxy}"
        }
        proxies.append(proxydict)
    for thread in range(400):
        threading.Thread(target=send_request, args=(url, thread, random.choice(proxies))).start()

main()