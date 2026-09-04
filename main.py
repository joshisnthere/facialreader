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