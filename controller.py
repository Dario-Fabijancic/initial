import sdl

from overlay import Overlay
from capture import capture_interest_image
from inference import send_to_inference
from automation import send_keyboard_input, send_mouse_input

class EventLoop:
    """Handles events and updates the overlay."""

    def __init__(self, overlay: Overlay):
        self.overlay = overlay
        self.event = sdl.Event()
        self.running = True

    def handle_event(self, event):
        if event.type == sdl.QUIT:
            self.running = False
        elif event.type == sdl.KEYDOWN:
            sym = event.key.keysym.sym
            if sym == sdl.K_ESCAPE:
                self.running = False
            elif sym == sdl.K_c:
                image = capture_interest_image()
                send_to_inference(image)
            elif sym == sdl.K_k:
                send_keyboard_input(b"example")
            elif sym == sdl.K_m:
                send_mouse_input(10, 10)

    def run(self):
        while self.running:
            while sdl.poll_event(self.event):
                self.handle_event(self.event)
            self.overlay.clear()
            self.overlay.draw_text("Overlay running. Press ESC to quit.")
            self.overlay.present()
        self.overlay.close()
