web_url = "https://practice.automationtesting.in/"

Email_Address = "dheeraj.patil32@gmail.com"
Password_btn = "Samartha@1234567"

#Login
Login_Username = "dheeraj.patil32@gmail.com"
Login_Psd = "Samartha@1234567"

# --- negative (invalid) credentials ---
invalid_admins = [
    {"Login_Username": "abc",   "Login_Psd": "wrong"},
    {"Login_Username": "user", "Login_Psd": "admin123"},
    {"Login_Username": "",        "Login_Psd": "admin45"},        # blank user
    {"Login_Username": "admin456",   "Login_Psd": ""},             # blank pass
    {"Login_Username": "   ",     "Login_Psd": "   "}           # whitespace only
]