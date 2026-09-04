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