# Создать приложение по картинке
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Admin Panel - HTML5 Template")
root.geometry("550x450")

main_frame = tk.Frame(root, padx=30, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(main_frame, text="ADMIN PANEL", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

subtitle_label = tk.Label(main_frame, text="User Management", font=("Arial", 10))
subtitle_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 15))

tk.Label(main_frame, text="Username").grid(row=2, column=0, sticky="w", pady=5)
username_entry = tk.Entry(main_frame, width=35)
username_entry.grid(row=2, column=1, sticky="w", padx=10, pady=5)

tk.Label(main_frame, text="Email Address").grid(row=3, column=0, sticky="w", pady=5)
email_entry = tk.Entry(main_frame, width=35)
email_entry.grid(row=3, column=1, sticky="w", padx=10, pady=5)

tk.Label(main_frame, text="Password").grid(row=4, column=0, sticky="w", pady=5)
password_entry = tk.Entry(main_frame, width=35, show="*")
password_entry.grid(row=4, column=1, sticky="w", padx=10, pady=5)

tk.Label(main_frame, text="Confirm Password").grid(row=5, column=0, sticky="w", pady=5)
confirm_entry = tk.Entry(main_frame, width=35, show="*")
confirm_entry.grid(row=5, column=1, sticky="w", padx=10, pady=5)

tk.Label(main_frame, text="Role").grid(row=6, column=0, sticky="w", pady=5)
role_var = tk.StringVar(value="Select role...")
role_menu = ttk.OptionMenu(
    main_frame,
    role_var,
    "Select role...",
    "Administrator",
    "Manager",
    "Editor",
    "User"
)
role_menu.config(width=33)
role_menu.grid(row=6, column=1, sticky="w", padx=10, pady=5)

tk.Label(main_frame, text="Status").grid(row=7, column=0, sticky="nw", pady=5)

status_frame = tk.Frame(main_frame)
status_frame.grid(row=7, column=1, sticky="w", padx=10, pady=5)

status_active = tk.IntVar(value=1)
status_inactive = tk.IntVar()

tk.Checkbutton(status_frame, text="Active", variable=status_active).pack(anchor="w")
tk.Checkbutton(status_frame, text="Inactive", variable=status_inactive).pack(anchor="w")

button_frame = tk.Frame(main_frame)
button_frame.grid(row=8, column=0, columnspan=2, pady=(25, 0))

save_btn = tk.Button(button_frame, text="Save Changes", width=15)
save_btn.pack(side=tk.LEFT, padx=5)

cancel_btn = tk.Button(button_frame, text="Cancel", width=15)
cancel_btn.pack(side=tk.LEFT, padx=5)

reset_btn = tk.Button(button_frame, text="Reset", width=15)
reset_btn.pack(side=tk.LEFT, padx=5)

footer_label = tk.Label(main_frame, text="© 2026 Admin Panel v1.0", font=("Arial", 8))
footer_label.grid(row=9, column=0, columnspan=2, pady=(20, 0))

root.mainloop()