from overlay import Overlay
from controller import EventLoop


def main():
    overlay = Overlay()
    loop = EventLoop(overlay)
    loop.run()


if __name__ == "__main__":
    main()
