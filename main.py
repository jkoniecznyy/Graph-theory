from pathlib import Path

from graph_theory import present_map, process_image


def main() -> None:
    """The main function of the code"""
    present_map(process_image(Path("D:\\Pobrane\\map2.jpg")))


if __name__ == '__main__':
    main()
