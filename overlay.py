import sdl
import sdlttf

class Overlay:
    """Handles an always-on-top window for displaying status text."""

    def __init__(self, width=640, height=480):
        sdl.init(sdl.INIT_VIDEO)
        sdlttf.init()
        flags = sdl.WINDOW_ALWAYS_ON_TOP
        self.window = sdl.create_window(b"Inference Overlay", 100, 100, width, height, flags)
        self.renderer = sdl.create_renderer(self.window, -1, 0)
        font_path = b"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        self.font = sdlttf.open_font(font_path, 24)
        self.color = sdl.Color(255, 255, 255)

    def draw_text(self, message, x=10, y=10):
        surface = sdlttf.render_utf8_blended(self.font, message.encode(), self.color)
        texture = sdl.create_texture_from_surface(self.renderer, surface)
        sdl.free_surface(surface)
        w = sdl.int_ref()
        h = sdl.int_ref()
        sdl.query_texture(texture, None, None, w, h)
        dst_rect = sdl.Rect(x, y, w.value, h.value)
        sdl.render_copy(self.renderer, texture, None, dst_rect)
        sdl.destroy_texture(texture)

    def present(self):
        sdl.render_present(self.renderer)

    def clear(self):
        sdl.render_clear(self.renderer)

    def close(self):
        sdlttf.quit()
        sdl.destroy_renderer(self.renderer)
        sdl.destroy_window(self.window)
        sdl.quit()
