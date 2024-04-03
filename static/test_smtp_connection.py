import smtplib

try:
    server = smtplib.SMTP('smtpout.secureserver.net', 465)
    server.login('Info@mamamialife.com', '')  # Use your actual password or app password
    print("SMTP connection successful.")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()