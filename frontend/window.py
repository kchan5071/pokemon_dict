import customtkinter

from data_manager import DataManager
from frontend.saved_frame import SavedFrame

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 580
SIDEBAR_WIDTH = 80
BUFFER = 50

ITEMS_PER_PAGE = 20

FRAMES = [
    "SEARCH",
    "SAVED",
    "EXPORT/IMPORT",
    "CURRENT TEAM",
    "SETTINGS",
]

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.data_manager = DataManager()
        self.save_frame = SavedFrame(self)

        self.buttons = []
        self.content_frames = []
        self.content_labels = []
        self.current_frame = ""
        self.frame_widgets = []

        # configure window
        self.title("PokeTracker")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # configure grid layout (3x5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # # create sidebar frame with widgets
        self.create_sidebar()

        # create label for sidebar
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="PokeTracker",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        sidebar_buttons = len(FRAMES)
        for row in range(sidebar_buttons):
            self.create_sidebar_button(row + 1)

        self.appearence_mode_menu()
        self.ui_scaling_menu()
        self.add_frames()
        self.select_frame(FRAMES[0])


        # self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
        #                                                 values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        # self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
        #                                                    command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # # create radiobutton frame
        # self.radiobutton_frame = customtkinter.CTkFrame(self)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tkinter.IntVar(value=0)
        # self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # # create slider and progressbar frame
        # self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # # create scrollable frame
        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(100):
        #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # # set default values
        # self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        # self.appearance_mode_optionemenu.set("Dark")
        # self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

    def add_widgets_to_frame(self):
        pass

    def show_frame(self):
        print(self.current_frame)
        if self.current_frame == "SAVED":
            self.save_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
            self.save_frame.lift()
            self.save_frame.show()
            if not any(frame_name == self.current_frame for frame_name, _ in self.frame_widgets):
                self.frame_widgets.append((self.current_frame, self.save_frame))
            # dict_list = self.data_manager.get_names(range(ITEMS_PER_PAGE))
            # saved_scrollable_frame = customtkinter.CTkScrollableFrame(
            #     self,
            #     label_text="CTkScrollableFrame"
            # )
            # saved_scrollable_frame.grid(
            #     row=1,
            #     column=1,
            #     columnspan=5,
            #     padx=(20, 0),
            #     pady=(20, 0),
            #     sticky="nsew"
            # )
            # saved_scrollable_frame.grid_columnconfigure(0, weight=1)
            # saved_scrollable_frame_switches = []
            # for i, dict in enumerate(dict_list):
            #     print(dict)
            #     switch = customtkinter.CTkSwitch(
            #         master=saved_scrollable_frame,
            #         text=dict["name"]
            #     )
            #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            #     saved_scrollable_frame_switches.append(switch)

            # self.frame_widgets.append((self.current_frame, saved_scrollable_frame))
        else:
            pass

    def add_frames(self):
        for frame_name in FRAMES:
            frame = customtkinter.CTkFrame(
                self,
                corner_radius=0,
                fg_color="transparent",
                height=WINDOW_HEIGHT
            )
            frame.grid_columnconfigure(0, weight=1)
            self.content_frames.append(frame)
            frame_label = customtkinter.CTkLabel(
                frame,
                text=frame_name,
                font=customtkinter.CTkFont(size=20, weight="bold"),
            )
            frame_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.content_labels.append(frame_label)

    def create_sidebar(self):
        self.sidebar_frame = customtkinter.CTkFrame(self, width=SIDEBAR_WIDTH, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(len(FRAMES) + 1, weight=1)

    def appearence_mode_menu(self):
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=len(FRAMES) + 1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame, values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_optionemenu.grid(row=len(FRAMES) + 2, column=0, padx=20, pady=(10, 10))

    def ui_scaling_menu(self):
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=len(FRAMES) + 3, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["80%", "90%", "100%", "110%", "120%"],
            command=self.change_scaling_event
        )
        self.scaling_optionemenu.grid(row=len(FRAMES) + 4, column=0, padx=20, pady=(10, 20))

    def create_sidebar_button(self, row: int):
        button = customtkinter.CTkButton(
            self.sidebar_frame,
            command=lambda: self.select_frame(FRAMES[row - 1]),
        )
        button.grid(row=row, column=0, padx=20, pady=10)
        self.buttons.append(button)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def select_frame(self, name):
        """Handles switching visibility of content frames and highlighting active buttons."""
        # 1. Reset all button backgrounds to transparent
        # for button in self.buttons:
        #     button.configure(fg_color="transparent")
        #     pass

        # 2. Hide all content frames
        for frame in self.content_frames:
            frame.grid_forget()

        for frame_widget in self.frame_widgets:
            frame_widget[1].grid_forget()

        # 3. Show the selected frame and highlight its corresponding button
        for frame_name, frame in zip(FRAMES, self.content_frames):
            if frame_name == name:
                self.current_frame = frame_name
                if frame_name != "SAVED":
                    frame.grid(row=0, column=1, sticky="nsew")

        self.show_frame()
