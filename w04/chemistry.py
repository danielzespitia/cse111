from formula import parse_formula

def make_periodic_table():
    periodic_table_dict = {
        "Ac": ("Actinium", 227, 89),
        "Ag": ("Silver", 107.8682, 47),
        "Al": ("Aluminum", 26.9815386, 13),
        "Ar": ("Argon", 39.948, 18),
        "As": ("Arsenic", 74.9216, 33),
        "At": ("Astatine", 210, 85),
        "Au": ("Gold", 196.966569, 79),
        "B": ("Boron", 10.811, 5),
        "Ba": ("Barium", 137.327, 56),
        "Be": ("Beryllium", 9.012182, 4),
        "Bi": ("Bismuth", 208.9804, 83),
        "Br": ("Bromine", 79.904, 35),
        "C": ("Carbon", 12.0107, 6),
        "Ca": ("Calcium", 40.078, 20),
        "Cd": ("Cadmium", 112.411, 48),
        "Ce": ("Cerium", 140.116, 58),
        "Cl": ("Chlorine", 35.453, 17),
        "Co": ("Cobalt", 58.933195, 27),
        "Cr": ("Chromium", 51.9961, 24),
        "Cs": ("Cesium", 132.9054519, 55),
        "Cu": ("Copper", 63.546, 29),
        "Dy": ("Dysprosium", 162.5, 66),
        "Er": ("Erbium", 167.259, 68),
        "Eu": ("Europium", 151.964, 63),
        "F": ("Fluorine", 18.9984032, 9),
        "Fe": ("Iron", 55.845, 26),
        "Fr": ("Francium", 223, 87),
        "Ga": ("Gallium", 69.723, 31),
        "Gd": ("Gadolinium", 157.25, 64),
        "Ge": ("Germanium", 72.64, 32),
        "H": ("Hydrogen", 1.00794, 1),
        "He": ("Helium", 4.002602, 2),
        "Hf": ("Hafnium", 178.49, 72),
        "Hg": ("Mercury", 200.59, 80),
        "Ho": ("Holmium", 164.93032, 67),
        "I": ("Iodine", 126.90447, 53),
        "In": ("Indium", 114.818, 49),
        "Ir": ("Iridium", 192.217, 77),
        "K": ("Potassium", 39.0983, 19),
        "Kr": ("Krypton", 83.798, 36),
        "La": ("Lanthanum", 138.90547, 57),
        "Li": ("Lithium", 6.941, 3),
        "Lu": ("Lutetium", 174.9668, 71),
        "Mg": ("Magnesium", 24.305, 12),
        "Mn": ("Manganese", 54.938045, 25),
        "Mo": ("Molybdenum", 95.96, 42),
        "N": ("Nitrogen", 14.0067, 7),
        "Na": ("Sodium", 22.98976928, 11),
        "Nb": ("Niobium", 92.90638, 41),
        "Nd": ("Neodymium", 144.242, 60),
        "Ne": ("Neon", 20.1797, 10),
        "Ni": ("Nickel", 58.6934, 28),
        "Np": ("Neptunium", 237, 93),
        "O": ("Oxygen", 15.9994, 8),
        "Os": ("Osmium", 190.23, 76),
        "P": ("Phosphorus", 30.973762, 15),
        "Pa": ("Protactinium", 231.03588, 91),
        "Pb": ("Lead", 207.2, 82),
        "Pd": ("Palladium", 106.42, 46),
        "Pm": ("Promethium", 145, 61),
        "Po": ("Polonium", 209, 84),
        "Pr": ("Praseodymium", 140.90765, 59),
        "Pt": ("Platinum", 195.084, 78),
        "Pu": ("Plutonium", 244, 94),
        "Ra": ("Radium", 226, 88),
        "Rb": ("Rubidium", 85.4678, 37),
        "Re": ("Rhenium", 186.207, 75),
        "Rh": ("Rhodium", 102.9055, 45),
        "Rn": ("Radon", 222, 86),
        "Ru": ("Ruthenium", 101.07, 44),
        "S": ("Sulfur", 32.065, 16),
        "Sb": ("Antimony", 121.76, 51),
        "Sc": ("Scandium", 44.955912, 21),
        "Se": ("Selenium", 78.96, 34),
        "Sg": ("Seaborgium", 271, 106),
        "Si": ("Silicon", 28.0855, 14),
        "Sm": ("Samarium", 150.36, 62),
        "Sn": ("Tin", 118.71, 50),
        "Sr": ("Strontium", 87.62, 38),
        "Ta": ("Tantalum", 180.94788, 73),
        "Tb": ("Terbium", 158.92535, 65),
        "Tc": ("Technetium", 98, 43),
        "Te": ("Tellurium", 127.6, 52),
        "Th": ("Thorium", 232.03806, 90),
        "Ti": ("Titanium", 47.867, 22),
        "Tl": ("Thallium", 204.3833, 81),
        "Tm": ("Thulium", 168.93421, 69),
        "U": ("Uranium", 238.02891, 92),
        "V": ("Vanadium", 50.9415, 23),
        "W": ("Tungsten", 183.84, 74),
        "Xe": ("Xenon", 131.293, 54),
        "Y": ("Yttrium", 88.90585, 39),
        "Yb": ("Ytterbium", 173.054, 70),
        "Zn": ("Zinc", 65.38, 30),
        "Zr": ("Zirconium", 91.224, 40)
    }
    return periodic_table_dict

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.

    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.

    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.

    # Return the total molar mass.
    return

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_molar_mass = 0.0
    for item in symbol_quantity_list:
        symbol = item[SYMBOL_INDEX]
        quantity = item[QUANTITY_INDEX]
        if symbol in periodic_table_dict:
            atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
            molar_mass = atomic_mass * quantity
            total_molar_mass += molar_mass
    return total_molar_mass

def sum_protons(symbol_quantity_list, periodic_table_dict):
    total_protons = 0
    for item in symbol_quantity_list:
        symbol = item[SYMBOL_INDEX]
        quantity = item[QUANTITY_INDEX]
        if symbol in periodic_table_dict:
            atomic_number = periodic_table_dict[symbol][ATOMIC_NUMBER_INDEX]
            protons = atomic_number * quantity
            total_protons += protons
    return total_protons

def main():
    periodic_table_dict = make_periodic_table()
    formula = input("Enter the chemical formula: ")
    sample_mass = float(input("Enter the mass of the sample (grams): "))
    symbol_quantity_list = parse_formula(formula, periodic_table_dict)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    number_of_moles = sample_mass / molar_mass
    total_protons = sum_protons(symbol_quantity_list, periodic_table_dict)
    print("Molar mass:", molar_mass, "grams/mole")
    print("Number of moles:", number_of_moles, "moles")
    print("Total number of protons:", total_protons)

if __name__ == "__main__":
    main()