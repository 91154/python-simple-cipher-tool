while True:
    print("\n--- منوی اصلی ---")
    print("1) رمزنگاری")
    print("2) رمزگشایی")
    print("3) خروج")

    choice = input("انتخاب تو: ")

    if choice == "1":
        plain_text = input("متنی که می‌خوای رمزنگاری کنی رو بنویس: ")
        encrypted_text = ""
        for i in plain_text:
            # فرمول رمزنگاری
            x = ord(i) * 2 + 5
            encrypted_text += chr(x)
        print("رمز شما برای باز کردن پیام:", encrypted_text)

    elif choice == "2":
        encrypted_input = input("رمز پیام رو بنویس: ")
        decrypted_text = ""  # یک متغیر جدید برای ذخیره متن اصلی
        for i in encrypted_input:
            # فرمول معکوس (رمزگشایی)
            x = (ord(i) - 5) // 2
            decrypted_text += chr(x)
        print("پیام اصلی تو:", decrypted_text)

    elif choice == "3":
        print("Goodbye! 👋")
        break  # استفاده از break برای خروج صحیح از حلقه
    else:
        print("❌ اشتباه انتخاب کردی، دوباره تلاش کن.")
