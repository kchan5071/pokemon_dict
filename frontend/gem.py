import customtkinter as ctk

# Set the overall theme and color
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class VSCodeStyleApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configure window
        self.title("VS Code Style Sidebar App")
        self.geometry("1100 x 600")

        # Configure grid layout (1 row, 2 columns)
        # Column 0: Sidebar (narrow), Column 1: Main Content (expands)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Track the currently active tab
        self.active_tab = None

        # --- SIDEBAR NAVIGATION ---
        self.sidebar_frame = ctk.CTkFrame(self, width=80, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(
            4, weight=1
        )  # Pushes bottom elements down if needed

        # Sidebar Title / Logo
        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, text="APP", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=10, pady=20)

        # Sidebar Buttons (Tabs)
        self.tab1_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="Explorer",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=lambda: self.select_frame("explorer"),
        )
        self.tab1_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.tab2_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="Search",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=lambda: self.select_frame("search"),
        )
        self.tab2_btn.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.tab3_btn = ctk.CTkButton(
            self.sidebar_frame,
            text="Settings",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=lambda: self.select_frame("settings"),
        )
        self.tab3_btn.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        # --- CONTENT FRAMES ---
        # 1. Explorer Frame
        self.explorer_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.explorer_frame.grid_columnconfigure(0, weight=1)
        # Add widgets to explorer frame
        self.exp_label = ctk.CTkLabel(
            self.explorer_frame,
            text="Explorer View",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.exp_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # 2. Search Frame
        self.search_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.search_frame.grid_columnconfigure(0, weight=1)
        # Add widgets to search frame
        self.search_label = ctk.CTkLabel(
            self.search_frame,
            text="Search View",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.search_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.search_input = ctk.CTkEntry(
            self.search_frame, placeholder_text="Search files..."
        )
        self.search_input.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # 3. Settings Frame
        self.settings_frame = ctk.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.settings_frame.grid_columnconfigure(0, weight=1)
        # Add widgets to settings frame
        self.settings_label = ctk.CTkLabel(
            self.settings_frame,
            text="Settings View",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.settings_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Select default frame on startup
        self.select_frame("explorer")

    def select_frame(self, name):
        """Handles switching visibility of content frames and highlighting active buttons."""
        # 1. Reset all button backgrounds to transparent
        self.tab1_btn.configure(fg_color="transparent")
        self.tab2_btn.configure(fg_color="transparent")
        self.tab3_btn.configure(fg_color="transparent")

        # 2. Hide all content frames
        self.explorer_frame.grid_forget()
        self.search_frame.grid_forget()
        self.settings_frame.grid_forget()

        # 3. Show the selected frame and highlight its corresponding button
        if name == "explorer":
            self.explorer_frame.grid(row=0, column=1, sticky="nsew")
            self.tab1_btn.configure(
                fg_color=("gray75", "gray25")
            )  # Light/Dark mode colors
        elif name == "search":
            self.search_frame.grid(row=0, column=1, sticky="nsew")
            self.tab2_btn.configure(fg_color=("gray75", "gray25"))
        elif name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
            self.tab3_btn.configure(fg_color=("gray75", "gray25"))


if __name__ == "__main__":
    app = VSCodeStyleApp()
    app.mainloop()