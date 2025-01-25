"""
https://python.langchain.com/docs/how_to/multimodal_prompts/
"""
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter as tk
import os

# --------------------------------------------------------------------------------------------------
class ImageApp:

    # ----------------------------------------------------------------------------------------------
    def __init__(self, root):
        self.good_image_path= "good.jpg"
        self.root = root
        self.root.title("Image Viewer")

        # Load previously saved directory
        self.load_last_directory()

        # Define layout: top area for image, bottom area for buttons, result area, and text area
        self.image_label = tk.Label(self.root, bg="gray")
        self.image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.good_image = Image.open( self.good_image_path)
        self.good_image_label = tk.Label(self.root, bg="gray")
        self.good_image_label.grid(row=0, column=2, columnspan=2, sticky="nsew")
        self.good_image_tk = ImageTk.PhotoImage(self.good_image)

        self.good_image_label.config(image=self.good_image_tk)
        self.good_image_label.image = self.good_image_tk

        # Buttons
        self.open_button = tk.Button(self.root, text="Open", command=self.open_image)
        self.open_button.grid(row=1, column=0)

        self.check_button = tk.Button(self.root, text="Check", state="disabled", command=self.check_image)
        self.check_button.grid(row=1, column=1)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=1, column=2)

        # Result area (color square)
        self.result_area = tk.Label(self.root, width=5, height=2, bg="gray")
        self.result_area.grid(row=1, column=3)

        # Text area for messages
        self.message_text = tk.Label(self.root, text="Welcome", anchor="w", relief="sunken")
        self.message_text.grid(row=2, column=0, columnspan=4, sticky="ew")

        # Configure grid weights for resizing
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.image_path = None
        self.image = None
        self.image_tk = None

        self.root.bind("<Configure>", self.on_resize)

        self.init_llm()

    # ----------------------------------------------------------------------------------------------
    def init_llm(self):
        pass

    # ----------------------------------------------------------------------------------------------
    def execute_llm(self, image) -> bool:
        return False

    # ----------------------------------------------------------------------------------------------
    def on_resize(self, event):
        # This method will be triggered when the window is resized
        # We can adjust the image size to fit within the window, keeping the aspect ratio

        if self.image_tk:
            # Get current dimensions of the window (excluding borders and padding)
            width = event.width // 2
            height = event.height

            # Maintain aspect ratio of the image
            if self.image:
                img_width, img_height = self.image.size
                aspect_ratio = img_width / img_height

                # Determine the new width and height for the image based on aspect ratio
                if width / height > aspect_ratio:
                    new_width = int(height * aspect_ratio)
                    new_height = height
                else:
                    new_width = width
                    new_height = int(width / aspect_ratio)

                # Resize the image to the new dimensions
                resized_image = self.image.resize((new_width, new_height))
                self.image_tk = ImageTk.PhotoImage(resized_image)

    # ----------------------------------------------------------------------------------------------
    def load_last_directory(self):
        # Load the last used directory path from a file, default to the current directory
        self.last_dir = os.getcwd()
        try:
            with open("last_directory.txt", "r") as f:
                self.last_dir = f.read().strip()
        except FileNotFoundError:
            pass
    # ----------------------------------------------------------------------------------------------
    def open_image(self):
        # Open file dialog to select an image
        file_path = filedialog.askopenfilename(
            title="Open Image",
            initialdir=self.last_dir,
            filetypes=[("Image Files", ".png; .jpg .jpeg  .bmp .gif")]
        )
        if file_path:
            try:
                # Open image and resize it to fit within the image area while keeping aspect ratio
                self.image_path = file_path
                self.image = Image.open(self.image_path)
                self.image_tk = ImageTk.PhotoImage(self.image)
                self.display_image()

                # Save the directory of the image
                self.last_dir = os.path.dirname(file_path)
                with open("last_directory.txt", "w") as f:
                    f.write(self.last_dir)

                # Update result area and message
                self.result_area.config(bg="blue")
                self.message_text.config(text="Success")
                self.check_button.config(state="normal")

                self.root.grid_rowconfigure(0, weight=1)  # Ensure the image area takes up space
                self.root.grid_propagate(True)

            except Exception as e:
                self.result_area.config(bg="orange")
                self.check_button.config(state="disabled")
                self.message_text.config(text="Open Failed: " + str(e))

    # ----------------------------------------------------------------------------------------------
    def display_image(self):
        # Resize the image to fit the image area while maintaining aspect ratio
        if self.image_tk:
            self.image_label.config(image=self.image_tk)
            self.image_label.image = self.image_tk

    # ----------------------------------------------------------------------------------------------
    def exit_app(self):
        # Terminate the application
        self.root.quit()

    # ----------------------------------------------------------------------------------------------
    def check_image(self):
        # When "Check" is pressed, show "Checked" in the message text
        try:
            isOk= self.execute_llm( self.image)
            self.message_text.config(text="Checked")
            if isOk:
                self.result_area.config(bg="green")
                self.message_text.config(text="OK")
            else:
                self.result_area.config(bg="red")
                self.message_text.config(text="KO")
        except Exception as e:
            self.result_area.config(bg="orange")
            self.message_text.config(text="Check Failed: " + str(e))

# --------------------------------------------------------------------------------------------------
def main():
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()

# --------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
