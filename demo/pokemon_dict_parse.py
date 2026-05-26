from demo.pokemon_dict import first_gen_pokemon


def search_pokemon(
    pokemon_list,
    search_name,
):
    for pokemon in pokemon_list:
        if pokemon['name'] == search_name:
            return pokemon['type']
    return None


def main():
    all_pokemon = first_gen_pokemon
    print(
        search_pokemon(
            all_pokemon,
            "Bulbasaur"
        )
    )


if __name__ == "__main__":
    main()
