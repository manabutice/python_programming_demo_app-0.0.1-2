import tkinter as tk
from tkinter import ttk, messagebox
import colorsys
import tkinter.font as tkfont
import importlib  # <- ここだけでOK（pyperclipは動的読み込み）

# クリップボードコピー（pyperclip が無くても tkinter で代替）
def copy_to_clipboard(text: str):
    try:
        m = importlib.import_module("pyperclip")  # 必要ならここで読み込む
        m.copy(text)
        return True
    except Exception:
        try:
            root = tk._default_root
            root.clipboard_clear()
            root.clipboard_append(text)
            return True
        except Exception:
            return False


class ColorApp(ttk.Frame):
    def __init__(self, master):
        super().__init__(master, padding=12)
        self.pack(fill="both", expand=True)

        self.mode_var = tk.StringVar(value="HSL")  # "HSL" or "HSV"
        self.h_var = tk.DoubleVar(value=0)
        self.s_var = tk.DoubleVar(value=100)
        self.lv_var = tk.DoubleVar(value=50)  # Lightness or Value

        self._build_ui()
        self._update_color()

    def _build_ui(self):
        title = ttk.Label(self, text="HSL / HSV カラービューア", font=tkfont.Font(size=14, weight="bold"))
        title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 8))

        mode_frame = ttk.Frame(self)
        ttk.Radiobutton(mode_frame, text="HSL（色相・彩度・明度）", value="HSL", variable=self.mode_var, command=self._on_mode_change).pack(side="left", padx=(0, 12))
        ttk.Radiobutton(mode_frame, text="HSV（色相・彩度・輝度）", value="HSV", variable=self.mode_var, command=self._on_mode_change).pack(side="left")
        mode_frame.grid(row=1, column=0, columnspan=3, sticky="w")

        self._add_slider("Hue（色相）", 0, 360, self.h_var, row=2, on_change=self._update_color)
        self._add_slider("Saturation（彩度）", 0, 100, self.s_var, row=3, on_change=self._update_color)
        self._add_slider("Lightness / Value（明度/輝度）", 0, 100, self.lv_var, row=4, on_change=self._update_color)

        preview = ttk.LabelFrame(self, text="プレビュー")
        preview.grid(row=2, column=2, rowspan=3, padx=(12, 0), sticky="nsew")
        self.columnconfigure(2, weight=1)
        self.rowconfigure(5, weight=1)

        self.color_canvas = tk.Canvas(preview, width=240, height=140, highlightthickness=1, highlightbackground="#ccc")
        self.color_canvas.pack(padx=8, pady=8)

        self.hex_var = tk.StringVar(value="#000000")
        self.rgb_var = tk.StringVar(value="(0, 0, 0)")

        rowf = ttk.Frame(preview)
        rowf.pack(fill="x", padx=8, pady=(0, 8))

        ttk.Label(rowf, text="HEX").grid(row=0, column=0, sticky="w")
        ttk.Entry(rowf, textvariable=self.hex_var, width=16).grid(row=0, column=1, padx=6, sticky="w")
        ttk.Button(rowf, text="コピー", command=lambda: self._copy(self.hex_var.get())).grid(row=0, column=2)

        ttk.Label(rowf, text="RGB").grid(row=1, column=0, sticky="w", pady=(6, 0))
        ttk.Entry(rowf, textvariable=self.rgb_var, width=16).grid(row=1, column=1, padx=6, sticky="w", pady=(6, 0))
        ttk.Button(rowf, text="コピー", command=lambda: self._copy(self.rgb_var.get())).grid(row=1, column=2, pady=(6, 0))

        self.status = ttk.Label(self, text="", foreground="#666")
        self.status.grid(row=6, column=0, columnspan=3, sticky="w", pady=(8, 0))

        for c in (0, 1, 2):
            self.columnconfigure(c, weight=1)

    def _add_slider(self, label, frm, to, var, row, on_change):
        ttk.Label(self, text=label).grid(row=row, column=0, sticky="w", pady=(10, 0))
        scale = ttk.Scale(self, from_=frm, to=to, orient="horizontal", variable=var, command=lambda _=None: on_change())
        scale.grid(row=row, column=1, sticky="ew", padx=8, pady=(10, 0))
        val_label = ttk.Label(self, textvariable=tk.StringVar(value=str(int(var.get()))))
        val_label.grid(row=row, column=2, sticky="w", pady=(10, 0))

        def _update_value_label(*args):
            val_label.config(text=str(int(var.get())))
        var.trace_add("write", lambda *_: _update_value_label())
        return label

    def _on_mode_change(self):
        if self.mode_var.get() == "HSL":
            self.status.config(text="現在モード: HSL（Hue, Saturation, Lightness）")
        else:
            self.status.config(text="現在モード: HSV（Hue, Saturation, Value）")
        self._update_color()

    def _copy(self, text):
        ok = copy_to_clipboard(text)
        if ok:
            self.status.config(text=f"コピーしました: {text}")
        else:
            messagebox.showinfo("コピー", "クリップボードにコピーできませんでした。")

    def _update_color(self):
        h = self.h_var.get() / 360.0
        s = self.s_var.get() / 100.0
        lv = self.lv_var.get() / 100.0

        if self.mode_var.get() == "HSL":
            r, g, b = colorsys.hls_to_rgb(h, lv, s)  # 注意: colorsysはHLS順
        else:
            r, g, b = colorsys.hsv_to_rgb(h, s, lv)

        R, G, B = int(round(r * 255)), int(round(g * 255)), int(round(b * 255))
        hex_code = f"#{R:02x}{G:02x}{B:02x}"

        self.hex_var.set(hex_code.upper())
        self.rgb_var.set(f"({R}, {G}, {B})")

        self.color_canvas.delete("all")
        self.color_canvas.create_rectangle(0, 0, 999, 999, fill=hex_code, outline="")
        self._draw_gradients()

    def _draw_gradients(self):
        w = 240
        h_px = 20
        y0 = 100
        for x in range(w):
            s = x / (w - 1)
            h = self.h_var.get() / 360.0
            lv = self.lv_var.get() / 100.0
            if self.mode_var.get() == "HSL":
                r, g, b = colorsys.hls_to_rgb(h, lv, s)
            else:
                r, g, b = colorsys.hsv_to_rgb(h, s, lv)
            R, G, B = int(r * 255), int(g * 255), int(b * 255)
            color = f"#{R:02x}{G:02x}{B:02x}"
            self.color_canvas.create_line(x, y0, x, y0 + h_px, fill=color)

        y1 = 100 + h_px + 6
        for x in range(w):
            lv = x / (w - 1)
            h = self.h_var.get() / 360.0
            s = self.s_var.get() / 100.0
            if self.mode_var.get() == "HSL":
                r, g, b = colorsys.hls_to_rgb(h, lv, s)
            else:
                r, g, b = colorsys.hsv_to_rgb(h, s, lv)
            R, G, B = int(r * 255), int(g * 255), int(b * 255)
            color = f"#{R:02x}{G:02x}{B:02x}"
            self.color_canvas.create_line(x, y1, x, y1 + h_px, fill=color)


def main():
    global root
    root = tk.Tk()
    root.title("HSL / HSV カラービューア")
    try:
        style = ttk.Style()
        style.theme_use("clam")
    except Exception:
        pass

    ColorApp(root)
    root.minsize(660, 320)
    root.mainloop()


if __name__ == "__main__":
    main()
