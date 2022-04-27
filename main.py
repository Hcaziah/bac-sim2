from petri import Petri


def main():
    dish = Petri()
    dish.populate()
    print(dish.get_pop_arr())


if __name__ == "__main__":
    main()
