# Inference Overlay Program

This project showcases a minimal structure for a background utility that
captures images, sends them for inference, and displays status using an
always-on-top overlay window.  The code is organised into modules so the
responsibilities of each part are clear at a glance.

## Modules
- `overlay.py` — manages the overlay window with PySDL3.
- `controller.py` — event loop reacting to user shortcuts.
- `capture.py` — stubs for capturing images of interest.
- `inference.py` — stubs for sending data to an inference service.
- `automation.py` — stubs for providing keyboard and mouse input.
- `main.py` — entry point wiring everything together.

Run `python3 -m py_compile *.py` to check the files compile.
