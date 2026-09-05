"""
Face Expression Reader

Reads a rough facial expression (neutral, smiling, surprised, eyes closed)
from your webcam using face landmark geometry. No cloud APIs, no trained
model to download -- everything runs locally off distances between points
mediapipe already gives you.
"""

import datetime

import customtkinter as ctk
import cv2
import mediapipe as mp
from PIL import Image, ImageTk

import expression_logic as logic

ctk.set_appearance_mode("dark")

BG = "#0f1115"
PANEL = "#181b20"
ACCENT = "#7ee787"


class ExpressionReaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Face Expression Reader")
        self.geometry("760x600")
        self.configure(fg_color=BG)

        self.video_label = ctk.CTkLabel(self, text="", fg_color=PANEL, corner_radius=12)
        self.video_label.pack(padx=20, pady=(20, 10))

        self.expression_var = ctk.StringVar(value="Reading...")
        ctk.CTkLabel(
            self, textvariable=self.expression_var,
            font=ctk.CTkFont(size=26, weight="bold"), text_color=ACCENT,
        ).pack(pady=(0, 4))

        ctk.CTkLabel(self, text="Recent changes", text_color="#8a8a8a").pack(anchor="w", padx=24)
        self.history_box = ctk.CTkTextbox(self, fg_color=PANEL, height=120, width=700)
        self.history_box.pack(padx=20, pady=(4, 20))
        self.history_box.configure(state="disabled")