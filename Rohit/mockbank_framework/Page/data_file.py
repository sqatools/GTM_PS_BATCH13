web_url = "https://practice.automationtesting.in/"

Email_Address = "dheeraj.patil26@gmail.com"
Password_btn = "Samartha@1234567"

#Login
Login_Username = "dheeraj.patil26@gmail.com"
Login_Psd = "Samartha@1234567"

# --- negative (invalid) credentials ---
invalid_admins = [
    {"Login_Username": "admin",   "Login_Psd": "wrongpass"},
    {"Login_Username": "baduser", "Login_Psd": "admin"},
    {"Login_Username": "",        "Login_Psd": "admin"},        # blank user
    {"Login_Username": "admin",   "Login_Psd": ""},             # blank pass
    {"Login_Username": "   ",     "Login_Psd": "   "}           # whitespace only
]