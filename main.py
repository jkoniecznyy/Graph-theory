from graph_theory import create_random_map, present_map, print_map_as_bits


def main() -> None:
    """The main function of the code"""
    for _ in range(3):
        map = create_random_map(10, 11)
        present_map(map)
        print_map_as_bits(map)


if __name__ == '__main__':
    main()
