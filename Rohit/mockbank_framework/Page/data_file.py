web_url = "https://practice.automationtesting.in/"

Email_Address = "mahesh_jadhav02@gmail.com"
Password_btn = "Karad@12345"

#Login
Login_Username = "mahesh_jadhav02@gmail.com"
Login_Psd = "Karad@12345"

# --- negative (invalid) credentials ---
invalid_admins = [
    {"Login_Username": "abc",   "Login_Psd": "wrong"},
    {"Login_Username": "user", "Login_Psd": "admin123"},
    {"Login_Username": "",        "Login_Psd": "admin45"},        # blank user
    {"Login_Username": "admin456",   "Login_Psd": ""},             # blank pass
    {"Login_Username": "   ",     "Login_Psd": "   "}           # whitespace only
]