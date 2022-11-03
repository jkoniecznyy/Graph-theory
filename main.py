from graph_theory import create_random_map, present_map


def main() -> None:
    """The main function of the code"""
    present_map(create_random_map(9, 10))


if __name__ == '__main__':
    main()
