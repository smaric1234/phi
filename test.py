import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
test = 5
emaill = 'sasamaric_9@hotmail.com'

def send_emails():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_emails = recipient_emails_entry.get().split(',')
    subject = subject_entry.get()
    message = message_text.get("1.0", tk.END)
    spoof_email = email_new.get()
    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            for recipient_email in recipient_emails:
                msg = MIMEText(message)
                msg['Subject'] = subject
                msg['From'] = spoof_email # if you want to spoof you type in spoof_email instead but you need a server that doesnt block it
                msg['To'] = recipient_email.strip()
                for x in range(int(number_num.get())):
                    print(x+1)
                    #abc = number_num
                    server.sendmail(sender_email, recipient_email.strip(), msg.as_string())

                
        messagebox.showinfo("Success", "Emails sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

# Create the main window
root = tk.Tk()
root.title("Email Sender")

# Create and pack widgets
ttk.Label(root, text="Sender Email:").grid(row=0, column=0, padx=10, pady=5)
sender_email_entry = ttk.Entry(root)
sender_email_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Sender Password:").grid(row=1, column=0, padx=10, pady=5)
sender_password_entry = ttk.Entry(root, show="*")
sender_password_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="send to").grid(row=2, column=0, padx=10, pady=5)
recipient_emails_entry = ttk.Entry(root)
recipient_emails_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Subject:").grid(row=3, column=0, padx=10, pady=5)
subject_entry = ttk.Entry(root)
subject_entry.grid(row=3, column=1, padx=10, pady=5)

ttk.Label(root, text="message:").grid(row=4, column=0, padx=10, pady=5)
message_text = tk.Text(root, height=5, width=40)
message_text.grid(row=4, column=1, padx=10, pady=5)

ttk.Label(root, text ="number of emails").grid(row=5)
number_num = tk.Entry(root, width = 5)
number_num.grid(row=5, column=1, padx=10, pady=5)

ttk.Label(root, text ="spoof email").grid(row=6)
email_new = tk.Entry(root, width = 40)
email_new.grid(row=6, column=1, padx=10, pady=5)

send_button = ttk.Button(root, text="Send Emails", command=send_emails)
send_button.grid(row=7, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()