import csv


class PokemonEntry:
    def __init__(self, asset):
        self.pokedex_number: int = asset["dexNr"]
        self.name: str = asset["names"]["English"]
        self.generation: int = asset["generation"]
        self.pokemon_class: str = (
            " ".join(str(asset["pokemonClass"]).split("_")[2:])
            if asset["pokemonClass"]
            else ""
        )
        self.image: str = (
            asset["assets"]["image"]
            if asset["assets"]
            else "https://static.wikia.nocookie.net/pokemongo/images/e/e3/None.png/revision/latest/scale-to-width-down/98?cb=20231013060329"
        )
        self.shiny_image: str = (
            asset["assets"]["shinyImage"]
            if asset["assets"] and asset["assets"]["shinyImage"]
            else ""
        )
        self.shiny_caught: str = "X" if not self.shiny_image else ""
        self.regional_forms: str = (
            self.add_regional_forms(
                asset["regionForms"],
                "_".join(
                    "".join(
                        [x for x in self.name if x.isalnum() or x.isspace()]
                    ).split()
                ),
            )
            if asset["regionForms"]
            else ""
        )

    def add_regional_forms(self, regional_forms: dict, pokemon_name: str) -> str:
        sheet_name = f"{pokemon_name}_regional"
        with open("output/" + sheet_name + ".csv", "a") as fileptr:
            writer = csv.writer(fileptr)
            writer.writerow(
                [
                    "Pokedex #",
                    "Name",
                    "Generation",
                    "Class",
                    "Image",
                    "Caught?",
                    "Shiny Image",
                    "Shiny Caught?",
                    "Regional Forms",
                ]
            )
            for form in regional_forms.values():
                pokemon = PokemonEntry(form)
                pokemon.write_to_sheet(writer)
        return sheet_name

    def write_to_sheet(self, writer) -> None:
        row = [
            self.pokedex_number,
            self.name,
            self.generation,
            self.pokemon_class,
            self.format_image(self.image),
            "",
            self.format_image(self.shiny_image),
            self.shiny_caught,
            self.link_sheet(self.regional_forms),
        ]
        writer.writerow(row)

    @staticmethod
    def format_image(image_url: str) -> str:
        return f'=IMAGE("{image_url}")' if image_url else ""

    @staticmethod
    def link_sheet(sheet_name: str) -> str:
        return f"={sheet_name}!A1" if sheet_name else ""
