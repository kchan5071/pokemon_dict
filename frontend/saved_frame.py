import customtkinter
from customtkinter import CTkScrollableFrame
from typing import Any

ITEMS_PER_PAGE = 20

class SavedFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.app: Any = master
        self.grid_columnconfigure(0, weight=1)

        self.frame_widgets = []


        self.label = customtkinter.CTkLabel(
            master=self,
            text="Saved Pokemon",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label.grid(row=0, column=0, padx=20)
        self.saved_scrollable_frame = customtkinter.CTkScrollableFrame(
            self,
            width=1000,
            label_text="Saved Pokemon"
        )

    def show(self) -> CTkScrollableFrame:
        self.frame_widgets.clear()

        dict_list = self.app.data_manager.get_names(range(ITEMS_PER_PAGE))
        for child in self.saved_scrollable_frame.winfo_children():
            child.destroy()

        self.saved_scrollable_frame.grid(
            row=1,
            column=0,
            columnspan=5,
            padx=20,
            pady=20,
            sticky="nsew"
        )
        self.saved_scrollable_frame.grid_columnconfigure(0, weight=1)
        self.saved_scrollable_frame.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        for i, pokemon_dict in enumerate(dict_list):
            label = customtkinter.CTkLabel(
                master=self.saved_scrollable_frame,
                text=pokemon_dict["name"]
            )
            label.grid(row=i, column=0, padx=10, pady=(0, 20), sticky="w")

            switch = customtkinter.CTkSwitch(
                master=self.saved_scrollable_frame,
                text="ADD TO TEAM"
            )
            switch.grid(row=i, column=1, padx=10, pady=(0, 20), sticky="e")

        self.frame_widgets.append(self.saved_scrollable_frame)
        return self.saved_scrollable_frame
