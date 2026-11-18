# Make a QR code for a PDF

This program makes a PNG image that you can print or share. When someone scans it with their phone camera, their phone opens the PDF link you entered.

**First, get the link to your PDF.** If the PDF is already on a website, open it in your browser and copy the web address. If the PDF is only on your computer, upload it to a service such as Google Drive, give your intended readers permission to view it, and copy the sharing link. For a public handout, test the link in a private browser window while signed out. Anyone scanning the code will need access to that same link.

Follow the section for your computer. In each command box, copy **one line at a time**, paste it into the indicated window, press **Return** on Mac or **Enter** on Windows, and wait for the next prompt.

## Mac

1. **Install Python.** Visit [Python for macOS](https://www.python.org/downloads/macos/). Choose the latest stable Python 3 release and download the **macOS installer** (a file ending in `.pkg`). Open it from Downloads and follow the installer through **Install** and **Close**.
2. **Make a folder for the program.** Open Finder, click **Downloads**, then press **Shift + Command + N**. Name the new folder `PDF-QR` and press Return.
3. **Put the program in that folder.** If you have the Python file, move it into `PDF-QR` and name it `main.py`. If you only have the code, open **TextEdit**, choose **File → New**, then **Format → Make Plain Text** if that option appears. Paste the program from the end of this README. Save it in **Downloads → PDF-QR** as `main.py`. If TextEdit asks which extension to use, choose **Use .py**.
4. **Open Terminal.** Press **Command + Space**, type `Terminal`, and press Return. Paste these lines one at a time with **Command + V**. The first opens your project folder in Terminal. The next two prepare a private copy of Python for this project and install the QR code and image packages.

   ```sh
   cd ~/Downloads/PDF-QR
   python3 -m venv .venv
   .venv/bin/python -m pip install "qrcode[pil]"
   ```

5. **Start the program.** In the same Terminal window, run the line below. When you see `Enter the URL of the PDF file:`, continue to **Answer the three questions** below.

   ```sh
   .venv/bin/python main.py
   ```

## Windows 10 or 11

1. **Install Python.** Open the **Microsoft Store**, search for **Python install manager**, and install the app published by the **Python Software Foundation**. Open **Start**, type `cmd`, and select **Command Prompt**. Run the line below to install Python 3 and wait for it to finish.

   ```bat
   py install 3
   ```

2. **Make a folder for the program.** Open **File Explorer** (Windows key + E), click **Downloads**, and press **Ctrl + Shift + N**. Name the new folder `PDF-QR` and press Enter.
3. **Put the program in that folder.** If you have the Python file, move it into `PDF-QR` and name it `main.py`. If you only have the code, open **Notepad** and paste the program from the end of this README. Choose **File → Save As**, open **Downloads → PDF-QR**, set **Save as type** to **All files**, enter `main.py` as the file name, and click **Save**.
4. **Open Command Prompt inside the folder.** In File Explorer, open `PDF-QR` so you can see your file. Click the address bar at the top, type `cmd`, and press Enter. A new Command Prompt opens in that folder.
5. **Install the QR code and image packages.** Paste these lines into the new Command Prompt one at a time using **Ctrl + V**. The first prepares a private copy of Python for this project. The second installs the packages it needs.

   ```bat
   py -3 -m venv .venv
   .venv\Scripts\python.exe -m pip install "qrcode[pil]"
   ```

6. **Start the program.** In that same window, run this line.

   ```bat
   .venv\Scripts\python.exe main.py
   ```

## Answer the three questions

The program waits for one answer at a time. Press Return or Enter after each answer. Type the answers without quotation marks.

| When it asks for… | What to enter |
| --- | --- |
| **URL of the PDF file** | Paste the full sharing link you copied earlier, including `https://`. |
| **Hex code of the color** | For your first code, type `#000000` for black. You can also use a dark color such as `#BF504D`. Include the `#` and all six digits or letters. |
| **Path where you want to save** | Type `qr_code.png`. A filename by itself saves the image in the `PDF-QR` folder you opened earlier. |

**Find and test your image.** The program finishes quietly and returns to the command prompt. Open **Downloads → PDF-QR**, double-click **qr_code.png**, point your phone camera at it, and tap the link that appears. Check that it opens the intended PDF before printing or sharing.

## Make another QR code

If the command window is still open, repeat just the **Start the program** command for your computer. If you closed it, Mac users can reopen Terminal and run `cd ~/Downloads/PDF-QR` first. Windows users can repeat **Open Command Prompt inside the folder** first. The packages stay installed in the project folder.

Use a new image name, such as `menu.png` or `flyer.png`, to keep each code. Using an existing image name replaces that image.

## If something goes wrong

| What you see | What to do |
| --- | --- |
| The computer cannot find `python3` or `py` | Finish the Python installation for your computer, close the command window, then open a fresh one and retry. |
| An error mentions `main.py` and “No such file” | Open `PDF-QR` and check the filename. On Mac, select the file and press **Command + I** to see **Name & Extension**. On Windows 11, use **View → Show → File name extensions** in File Explorer. On Windows 10, check **File name extensions** on the **View** tab. Rename `main.py.txt` to `main.py` if needed. |
| `No module named 'qrcode'` or `No module named 'PIL'` | Repeat your computer’s package installation command, including the quotes around `"qrcode[pil]"`. Then run the exact **Start the program** command. |
| The program reports an invalid color or file path | Start the program again. Try `#000000` for the color and `qr_code.png` for the save location. |
| The phone scans the code but asks for access | Open the PDF’s sharing settings and grant access to your intended readers. If you change the link itself, generate a new QR code. |

## Program to copy into main.py

If you received only this README, copy the code below into the file when prompted in the setup steps. Copy from `import qrcode` through `img.save(path_to_save)`, keeping the indentation.

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_H

if __name__ == "__main__":
    pdf_url = input("Enter the URL of the PDF file: ")
    color = input("Please enter the hex code of the color you want for the QR code (e.g., #BF504D): ")
    path_to_save = input("Enter the path where you want to save the QR code image (e.g., /Users/username/Desktop/qr_code.png): ")

    qr = qrcode.QRCode(
        version=2,
        error_correction=ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )

    qr.add_data(pdf_url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=color
    )

    img.save(path_to_save)
```
