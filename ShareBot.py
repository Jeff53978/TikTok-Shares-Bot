import threading, requests, sys, random

def send_request(url, thread):
    for i in range(10):
        request = requests.get(f"{url}?lang=en&is_copy_url=0&is_from_webapp=v1&sender_device=pc&sender_web_id={random.randint(10000000, 90000000)}")
        if request.status_code == 200:
            sys.stdout.write(f"[*] Shared video Thread: {thread} \n")
        else:
            sys.stdout.write(f"[!] Rate limited Thread: {thread} \n")

def main():
    print("TikTok Share Bot - Snikker#1337", "\n")
    url = input("[?] Enter tiktok video url: ")
    for thread in range(800): threading.Thread(target=send_request, args=(url, thread)).start()

main()