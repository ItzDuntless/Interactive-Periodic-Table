#Making an interactive periodic table using Ursina

#Importing the modules
from ursina import *
from ursina.shaders import *

#Basic screen
app = Ursina()

#Settings default font
Text.default_font = "font_normal.ttf"
Button.default_font = "font_normal.ttf"

#Setting default shader
Entity.default_shader = basic_lighting_shader

hide_button = Button(
    text='Hide Text',
    color=color.gold,
    scale=(0.4,0.1), # x, y, z scale. This makes it tall and thin like a portrait billboard.
    enabled= False, # Initially hidden,
    position = (0,-0.3)
)

text_shower = Button(position = (0,0), 
                      text = "",
                      enabled = False,
                      origin = (0,0),
                      text_size = 1.5,
                      scale = (1.2, 0.4), # x, y scale
                      color = color.gray,
                      highlight_color = color.gray
                      )

#Navigation
editor_camera = EditorCamera()
editor_camera.position = (100,100,100)

#Sky
Sky(texture = None, color = color.white)

#Home screen text
title = Text(text="Interactive Periodic Table", scale = 4,
             position = (0,0.25), color = color.black, origin = (0,0),
             font = "font_bold.ttf")

play_button = Button(text = "Start", position = (0,-0.1), scale = (0.4,0.15),
                     color = color.lime, text_color = color.black,
                     highlight_color = color.green, text_size = 2)

ins_button = Button(text = "Instructions", position = (0,-0.35), scale = (0.4,0.15),
                    color = color.pink, hightlight_color = color.red, text_color = color.black,
                    enabled = True, text_size = 2)

#Show instructions text (putting as button for the background)
ins_text = Button(text = '''INSTRUCTIONS
                  \n\n- Click on an element to see more information about it.
                  \n-Use W,A,S,D keys to move the view.
                  \n- Use mouse to rotate the view.
                  \n- Use scroll wheel to zoom in and out.
                  \n- Press right mouse button and move mouse to pan the view.
                  \n- Click on the element types in the legend for a specific element type.
                  \n\nEnjoy exploring the periodic table!''',
                position = (0,0.12), scale = (1.35,0.7),
                color = color.light_gray, text_color = color.black,
                enabled = False, text_size = 1.5, origin = (0,0), highlight_color = color.light_gray)

home_screen = True
show_ins = False

#Function to show instructions
def show_instructions():
    global show_ins
    #Hide all the home screen parts except instructions button
    if not show_ins:
        title.enabled = False
        play_button.enabled = False
        ins_button.text = "Back"
        ins_button.color = color.red
        ins_button.highlight_color = color.pink
        ins_text.enabled = True
        show_ins = True
    else:
        title.enabled = True
        play_button.enabled = True
        ins_button.text = "Instructions"
        ins_text.enabled = False
        show_ins = False
        ins_button.color = color.pink
        ins_button.highlight_color = color.red

ins_button.on_click = show_instructions

#Function to start the game
def start_game():
    global home_screen, show_ins

    if home_screen:
        title.enabled = False
        play_button.enabled = False
        home_screen = False
        editor_camera.position = (0,0,0)
        ins_button.enabled = False
        ins_text.enabled = False
        show_ins = False
        ins_button.text = "Instructions"
        ins_button.color = color.pink
        ins_button.highlight_color = color.red

        #Show all the legend parts
        legend_title.enabled = True
        alkaline_metal.enabled = True
        alkaline_earth_metal.enabled = True
        non_metal.enabled = True
        metalloid.enabled = True
        noble_gas.enabled = True
        halogen.enabled = True
        lathanides.enabled = True
        actinides.enabled = True
        transition.enabled = True
        post_transition.enabled = True

    else:
        title.enabled = True
        play_button.enabled = True
        home_screen = True
        ins_button.enabled = True

play_button.on_click = start_game

#Making a Legend

legend_title = Button(text="Legend",
                    origin = (0,0.5),
                    position = (-0.75,0.45),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_color = color.white,
                    text_size = 1.5,
                    highlight_color = color.black,
                    enabled = False)

alkaline_metal = Button(text=" Alkaline Metal",
                    origin = (0,0.5),
                    position = (-0.75,0.38),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.blue,
                    enabled = False)

alkaline_earth_metal = Button(text="Alkaline\nEarth Metal",
                    origin = (0,0.5),
                    position = (-0.75,0.31),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.red,
                    enabled = False)

non_metal = Button(text="Non-Metal",
                    origin = (0,0.5),
                    position = (-0.75,0.24),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.azure,
                    enabled = False)

metalloid = Button(text="Metalloid",
                    origin = (0,0.5),
                    position = (-0.75,0.17),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.yellow,
                    enabled = False)

noble_gas = Button(text="Noble Gas",
                    origin = (0,0.5),
                    position = (-0.75,0.10),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.orange,
                    enabled = False)

halogen = Button(text="Halogen",
                    origin = (0,0.5),
                    position = (-0.75,0.03),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.pink,
                    enabled = False)

lathanides = Button(text="Lathanides",
                    origin = (0,0.5),
                    position = (-0.75,-0.04),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.violet,
                    enabled = False)

actinides = Button(text="Actinides",
                    origin = (0,0.5),
                    position = (-0.75,-0.11),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.cyan,
                    enabled = False)  

transition = Button(text="Transition",
                    origin = (0,0.5),
                    position = (-0.75,-0.18),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.green,
                    enabled = False)

post_transition = Button(text="Post-Transition",
                    origin = (0,0.5),
                    position = (-0.75,-0.25),
                    scale = (0.2,0.1),
                    color= color.black,
                    text_size = 1,
                    text_color= color.brown,
                    enabled = False)    

#List of all required elements
elements = [
    # [Name, Group, Period, Atomic Number, Symbol, Color]
    ["Hydrogen", 1, 1, 1, "H", color.azure],                 # Reactive non metal
    ["Helium", 18, 1, 2, "He", color.orange],                # Noble gas
    ["Lithium", 1, 2, 3, "Li", color.blue],                  # Alkali metal
    ["Beryllium", 2, 2, 4, "Be", color.red],                 # Alkaline earth metal
    ["Boron", 13, 2, 5, "B", color.yellow],                  # Metalloid
    ["Carbon", 14, 2, 6, "C", color.azure],                  # Reactive non metal
    ["Nitrogen", 15, 2, 7, "N", color.azure],                # Reactive non metal
    ["Oxygen", 16, 2, 8, "O", color.azure],                  # Reactive non metal
    ["Fluorine", 17, 2, 9, "F", color.pink],                 # Halogen
    ["Neon", 18, 2, 10, "Ne", color.orange],                 # Noble gas
    ["Sodium", 1, 3, 11, "Na", color.blue],                  # Alkali metal
    ["Magnesium", 2, 3, 12, "Mg", color.red],                # Alkaline earth metal
    ["Aluminum", 13, 3, 13, "Al", color.brown],              # Post-transition metal (light brown)
    ["Silicon", 14, 3, 14, "Si", color.yellow],              # Metalloid
    ["Phosphorus", 15, 3, 15, "P", color.azure],             # Reactive non metal
    ["Sulfur", 16, 3, 16, "S", color.azure],                 # Reactive non metal
    ["Chlorine", 17, 3, 17, "Cl", color.pink],               # Halogen
    ["Argon", 18, 3, 18, "Ar", color.orange],                # Noble gas
    ["Potassium", 1, 4, 19, "K", color.blue],                # Alkali metal
    ["Calcium", 2, 4, 20, "Ca", color.red],                  # Alkaline earth metal
    ["Scandium", 3, 4, 21, "Sc", color.green],               # Transition metal
    ["Titanium", 4, 4, 22, "Ti", color.green],               # Transition metal
    ["Vanadium", 5, 4, 23, "V", color.green],                # Transition metal
    ["Chromium", 6, 4, 24, "Cr", color.green],               # Transition metal
    ["Manganese", 7, 4, 25, "Mn", color.green],              # Transition metal
    ["Iron", 8, 4, 26, "Fe", color.green],                   # Transition metal
    ["Cobalt", 9, 4, 27, "Co", color.green],                 # Transition metal
    ["Nickel", 10, 4, 28, "Ni", color.green],                # Transition metal
    ["Copper", 11, 4, 29, "Cu", color.green],                # Transition metal
    ["Zinc", 12, 4, 30, "Zn", color.green],                  # Transition metal
    ["Gallium", 13, 4, 31, "Ga", color.brown],               # Post-transition metal (light brown)
    ["Germanium", 14, 4, 32, "Ge", color.yellow],            # Metalloid
    ["Arsenic", 15, 4, 33, "As", color.yellow],              # Metalloid
    ["Selenium", 16, 4, 34, "Se", color.azure],              # Reactive non metal
    ["Bromine", 17, 4, 35, "Br", color.pink],                # Halogen
    ["Krypton", 18, 4, 36, "Kr", color.orange],              # Noble gas
    ["Rubidium", 1, 5, 37, "Rb", color.blue],                # Alkali metal
    ["Strontium", 2, 5, 38, "Sr", color.red],                # Alkaline earth metal
    ["Yttrium", 3, 5, 39, "Y", color.green],                 # Transition metal
    ["Zirconium", 4, 5, 40, "Zr", color.green],              # Transition metal
    ["Niobium", 5, 5, 41, "Nb", color.green],                # Transition metal
    ["Molybdenum", 6, 5, 42, "Mo", color.green],             # Transition metal
    ["Technetium", 7, 5, 43, "Tc", color.green],             # Transition metal
    ["Ruthenium", 8, 5, 44, "Ru", color.green],              # Transition metal
    ["Rhodium", 9, 5, 45, "Rh", color.green],                # Transition metal
    ["Palladium", 10, 5, 46, "Pd", color.green],             # Transition metal
    ["Silver", 11, 5, 47, "Ag", color.green],                # Transition metal
    ["Cadmium", 12, 5, 48, "Cd", color.green],               # Transition metal
    ["Indium", 13, 5, 49, "In", color.brown],                # Post-transition metal (light brown)
    ["Tin", 14, 5, 50, "Sn", color.brown],                   # Post-transition metal (light brown)
    ["Antimony", 15, 5, 51, "Sb", color.yellow],             # Metalloid
    ["Tellurium", 16, 5, 52, "Te", color.yellow],            # Metalloid
    ["Iodine", 17, 5, 53, "I", color.pink],                  # Halogen
    ["Xenon", 18, 5, 54, "Xe", color.orange],                # Noble gas
    ["Cesium", 1, 6, 55, "Cs", color.blue],                  # Alkali metal
    ["Barium", 2, 6, 56, "Ba", color.red],                   # Alkaline earth metal
    # --- Lanthanides (f-block, Period 9 for your coordinate system) ---
    ["Lanthanum", 1, 9, 57, "La", color.violet],
    ["Cerium", 2, 9, 58, "Ce", color.violet],
    ["Praseodymium", 3, 9, 59, "Pr", color.violet],
    ["Neodymium", 4, 9, 60, "Nd", color.violet],
    ["Promethium", 5, 9, 61, "Pm", color.violet],
    ["Samarium", 6, 9, 62, "Sm", color.violet],
    ["Europium", 7, 9, 63, "Eu", color.violet],
    ["Gadolinium", 8, 9, 64, "Gd", color.violet],
    ["Terbium", 9, 9, 65, "Tb", color.violet],
    ["Dysprosium", 10, 9, 66, "Dy", color.violet],
    ["Holmium", 11, 9, 67, "Ho", color.violet],
    ["Erbium", 12, 9, 68, "Er", color.violet],
    ["Thulium", 13, 9, 69, "Tm", color.violet],
    ["Ytterbium", 14, 9, 70, "Yb", color.violet],
    ["Lutetium", 15, 9, 71, "Lu", color.violet],
    # --- End of Lanthanides ---
    ["Hafnium", 4, 6, 72, "Hf", color.green],                # Transition metal
    ["Tantalum", 5, 6, 73, "Ta", color.green],               # Transition metal
    ["Tungsten", 6, 6, 74, "W", color.green],                # Transition metal
    ["Rhenium", 7, 6, 75, "Re", color.green],                # Transition metal
    ["Osmium", 8, 6, 76, "Os", color.green],                 # Transition metal
    ["Iridium", 9, 6, 77, "Ir", color.green],                # Transition metal
    ["Platinum", 10, 6, 78, "Pt", color.green],              # Transition metal
    ["Gold", 11, 6, 79, "Au", color.green],                  # Transition metal
    ["Mercury", 12, 6, 80, "Hg", color.green],               # Transition metal
    ["Thallium", 13, 6, 81, "Tl", color.brown],              # Post-transition metal
    ["Lead", 14, 6, 82, "Pb", color.brown],                  # Post-transition metal
    ["Bismuth", 15, 6, 83, "Bi", color.brown],               # Post-transition metal
    ["Polonium", 16, 6, 84, "Po", color.brown],             # Post-transition metal
    ["Astatine", 17, 6, 85, "At", color.pink],               # Halogen
    ["Radon", 18, 6, 86, "Rn", color.orange],                # Noble gas
    ["Francium", 1, 7, 87, "Fr", color.blue],                # Alkali metal
    ["Radium", 2, 7, 88, "Ra", color.red],                   # Alkaline earth metal
    # --- Actinides (f-block, Period 10 for your coordinate system) ---
    ["Actinium", 1, 10, 89, "Ac", color.cyan],
    ["Thorium", 2, 10, 90, "Th", color.cyan],
    ["Protactinium", 3, 10, 91, "Pa", color.cyan],
    ["Uranium", 4, 10, 92, "U", color.cyan],
    ["Neptunium", 5, 10, 93, "Np", color.cyan],
    ["Plutonium", 6, 10, 94, "Pu", color.cyan],
    ["Americium", 7, 10, 95, "Am", color.cyan],
    ["Curium", 8, 10, 96, "Cm", color.cyan],
    ["Berkelium", 9, 10, 97, "Bk", color.cyan],
    ["Californium", 10, 10, 98, "Cf", color.cyan],
    ["Einsteinium", 11, 10, 99, "Es", color.cyan],
    ["Fermium", 12, 10, 100, "Fm", color.cyan],
    ["Mendelevium", 13, 10, 101, "Md", color.cyan],
    ["Nobelium", 14, 10, 102, "No", color.cyan],
    ["Lawrencium", 15, 10, 103, "Lr", color.cyan],
    # --- End of Actinides ---
    ["Rutherfordium", 4, 7, 104, "Rf", color.green],         # Transition metal
    ["Dubnium", 5, 7, 105, "Db", color.green],               # Transition metal
    ["Seaborgium", 6, 7, 106, "Sg", color.green],            # Transition metal
    ["Bohrium", 7, 7, 107, "Bh", color.green],               # Transition metal
    ["Hassium", 8, 7, 108, "Hs", color.green],               # Transition metal
    ["Meitnerium", 9, 7, 109, "Mt", color.green],            # Transition metal
    ["Darmstadtium", 10, 7, 110, "Ds", color.green],         # Transition metal
    ["Roentgenium", 11, 7, 111, "Rg", color.green],          # Transition metal
    ["Copernicium", 12, 7, 112, "Cn", color.green],          # Transition metal
    ["Nihonium", 13, 7, 113, "Nh", color.brown],             # Post-transition metal
    ["Flerovium", 14, 7, 114, "Fl", color.brown],            # Post-transition metal
    ["Moscovium", 15, 7, 115, "Mc", color.brown],            # Post-transition metal
    ["Livermorium", 16, 7, 116, "Lv", color.brown],          # Post-transition metal
    ["Tennessine", 17, 7, 117, "Ts", color.pink],            # Halogen
    ["Oganesson", 18, 7, 118, "Og", color.orange]             # Noble gas
]

#Text Content for each element (really long list LOL)
text_content = [
    "Hydrogen\n\nAtomic Mass = 1.008 u\nMelting Point = 13.99 K\nBoiling Point = 20.28 K\nSpecial Property = Most abundant element.\nPopular Use = Rocket fuel, fertilizer.",
    "Helium\n\nAtomic Mass = 4.0026 u\nMelting Point = 0.95 K\nBoiling Point = 4.22 K\nSpecial Property = Lowest boiling point.\nPopular Use = Balloons, MRI magnets.",
    "Lithium\n\nAtomic Mass = 6.94 u\nMelting Point = 453.69 K\nBoiling Point = 1603 K\nSpecial Property = Lightest metal, least dense.\nPopular Use = Batteries and medicine.",
    "Beryllium\n\nAtomic Mass = 9.0122 u\nMelting Point = 1560 K\nBoiling Point = 2742 K\nSpecial Property = High melting point.\nPopular Use = Spacecraft, aircraft drills.",
    "Boron\n\nAtomic Mass = 10.81 u\nMelting Point = 2348 K\nBoiling Point = 4200 K\nSpecial Property = Hard semiconductor.\nPopular Use = Heat-resistant glass, detergents.",
    "Carbon\n\nAtomic Mass = 12.011 u\nMelting Point = 3800 K\nBoiling Point = 5100 K\nSpecial Property = Basis of life, allotropes.\nPopular Use = Pencils, cutting tools.",
    "Nitrogen\n\nAtomic Mass = 14.007 u\nMelting Point = 63.15 K\nBoiling Point = 77.35 K\nSpecial Property = 78% of Earth's atmosphere.\nPopular Use = Fertilizers, liquid refrigerant.",
    "Oxygen\n\nAtomic Mass = 15.999 u\nMelting Point = 54.36 K\nBoiling Point = 90.20 K\nSpecial Property = Essential for respiration.\nPopular Use = Medical oxygen, steel manufacturing.",
    "Fluorine\n\nAtomic Mass = 18.998 u\nMelting Point = 53.53 K\nBoiling Point = 85.03 K\nSpecial Property = Most reactive element.\nPopular Use = Toothpaste, non-stick coatings.",
    "Neon\n\nAtomic Mass = 20.180 u\nMelting Point = 24.56 K\nBoiling Point = 27.10 K\nSpecial Property = Bright reddish-orange light.\nPopular Use = Neon signs, lasers.",
    "Sodium\n\nAtomic Mass = 22.990 u\nMelting Point = 370.95 K\nBoiling Point = 1156 K\nSpecial Property = Highly reactive with water.\nPopular Use = Streetlights, table salt.",
    "Magnesium\n\nAtomic Mass = 24.305 u\nMelting Point = 923 K\nBoiling Point = 1363 K\nSpecial Property = Burns with white light.\nPopular Use = Fireworks, lightweight alloys.",
    "Aluminum\n\nAtomic Mass = 26.982 u\nMelting Point = 933.47 K\nBoiling Point = 2792 K\nSpecial Property = Lightweight and corrosion-resistant.\nPopular Use = Foil, cans, aircraft parts.",
    "Silicon\n\nAtomic Mass = 28.085 u\nMelting Point = 1687 K\nBoiling Point = 3538 K\nSpecial Property = Glass component, semiconductor.\nPopular Use = Computer chips, solar cells.",
    "Phosphorus\n\nAtomic Mass = 30.974 u\nMelting Point = 317.3 K\nBoiling Point = 553.6 K\nSpecial Property = Toxic allotropes.\nPopular Use = Fertilizers, matches.",
    "Sulfur\n\nAtomic Mass = 32.06 u\nMelting Point = 388.36 K\nBoiling Point = 717.8 K\nSpecial Property = Forms colorful crystals.\nPopular Use = Gunpowder, matches, acid.",
    "Chlorine\n\nAtomic Mass = 35.45 u\nMelting Point = 171.6 K\nBoiling Point = 239.1 K\nSpecial Property = Strong corrosive oxidant.\nPopular Use = Water disinfectant, pools.",
    "Argon\n\nAtomic Mass = 39.948 u\nMelting Point = 83.8 K\nBoiling Point = 87.3 K\nSpecial Property = Inert gas.\nPopular Use = Welding, light bulbs.",
    "Potassium\n\nAtomic Mass = 39.098 u\nMelting Point = 336.53 K\nBoiling Point = 1032 K\nSpecial Property = Reacts violently with water.\nPopular Use = Fertilizers, human health.",
    "Calcium\n\nAtomic Mass = 40.078 u\nMelting Point = 1115 K\nBoiling Point = 1757 K\nSpecial Property = Strong bones, teeth.\nPopular Use = Cement, mortar.",
    "Scandium\n\nAtomic Mass = 44.956 u\nMelting Point = 1814 K\nBoiling Point = 3109 K\nSpecial Property = Silvery-white metal.\nPopular Use = Aerospace alloys.",
    "Titanium\n\nAtomic Mass = 47.867 u\nMelting Point = 1941 K\nBoiling Point = 3560 K\nSpecial Property = High strength-to-weight ratio.\nPopular Use = Surgical implants, aircraft.",
    "Vanadium\n\nAtomic Mass = 50.942 u\nMelting Point = 2183 K\nBoiling Point = 3680 K\nSpecial Property = Found in meteorites.\nPopular Use = Steel alloys.",
    "Chromium\n\nAtomic Mass = 51.996 u\nMelting Point = 2180 K\nBoiling Point = 2944 K\nSpecial Property = Corrosion resistant.\nPopular Use = Stainless steel, chrome plating.",
    "Manganese\n\nAtomic Mass = 54.938 u\nMelting Point = 1519 K\nBoiling Point = 2334 K\nSpecial Property = Brittle metal.\nPopular Use = Steelmaking.",
    "Iron\n\nAtomic Mass = 55.845 u\nMelting Point = 1811 K\nBoiling Point = 3134 K\nSpecial Property = Earth's most common element.\nPopular Use = Steel, construction.",
    "Cobalt\n\nAtomic Mass = 58.933 u\nMelting Point = 1768 K\nBoiling Point = 3200 K\nSpecial Property = Blue color in glass.\nPopular Use = Batteries, magnets, alloys.",
    "Nickel\n\nAtomic Mass = 58.693 u\nMelting Point = 1728 K\nBoiling Point = 3003 K\nSpecial Property = Corrosion resistant, ductile.\nPopular Use = Stainless steel, coins.",
    "Copper\n\nAtomic Mass = 63.546 u\nMelting Point = 1357.77 K\nBoiling Point = 2835 K\nSpecial Property = High electrical conductivity.\nPopular Use = Electrical wiring, plumbing.",
    "Zinc\n\nAtomic Mass = 65.38 u\nMelting Point = 692.68 K\nBoiling Point = 1180 K\nSpecial Property = Galvanizing steel, batteries.",
    "Gallium\n\nAtomic Mass = 69.723 u\nMelting Point = 302.91 K\nBoiling Point = 2477 K\nSpecial Property = Melts in your hand.\nPopular Use = Electronics, thermometers.",
    "Germanium\n\nAtomic Mass = 72.630 u\nMelting Point = 1211.4 K\nBoiling Point = 3106 K\nSpecial Property = Metalloid, semiconductor.\nPopular Use = Fiber-optic systems, optics.",
    "Arsenic\n\nAtomic Mass = 74.922 u\nMelting Point = 1090 K\nBoiling Point = 887 K\nSpecial Property = Sublimes when heated.\nPopular Use = Semiconductors, pest control.",
    "Selenium\n\nAtomic Mass = 78.971 u\nMelting Point = 494 K\nBoiling Point = 958 K\nSpecial Property = Photoconductivity.\nPopular Use = Photocopiers, laser printers.",
    "Bromine\n\nAtomic Mass = 79.904 u\nMelting Point = 265.8 K\nBoiling Point = 332.0 K\nSpecial Property = Liquid at room temperature.\nPopular Use = Flame retardants, pesticides.",
    "Krypton\n\nAtomic Mass = 83.798 u\nMelting Point = 115.79 K\nBoiling Point = 119.93 K\nSpecial Property = Emits green/orange light.\nPopular Use = Fluorescent lamps, windows.",
    "Rubidium\n\nAtomic Mass = 85.468 u\nMelting Point = 312.46 K\nBoiling Point = 961 K\nSpecial Property = Ignites spontaneously in air.\nPopular Use = Fireworks (violet color).",
    "Strontium\n\nAtomic Mass = 87.62 u\nMelting Point = 1050 K\nBoiling Point = 1655 K\nSpecial Property = Ignites with crimson flame.\nPopular Use = Fireworks and magnets.",
    "Yttrium\n\nAtomic Mass = 88.906 u\nMelting Point = 1799 K\nBoiling Point = 3609 K\nSpecial Property = Strong corrosion resistance.\nPopular Use = TV phosphors, LED lighting.",
    "Zirconium\n\nAtomic Mass = 91.224 u\nMelting Point = 2128 K\nBoiling Point = 4650 K\nSpecial Property = Corrosion resistant, biocompatible.\nPopular Use = Nuclear reactors, surgical tools.",
    "Niobium\n\nAtomic Mass = 92.906 u\nMelting Point = 2750 K\nBoiling Point = 5017 K\nSpecial Property = Superconducting metal.\nPopular Use = Jet engines, magnets.",
    "Molybdenum\n\nAtomic Mass = 95.95 u\nMelting Point = 2896 K\nBoiling Point = 4912 K\nSpecial Property = Highest melting point.\nPopular Use = High-strength steel alloys.",
    "Technetium\n\nAtomic Mass = (98) u\nMelting Point = 2430 K\nBoiling Point = 4538 K\nSpecial Property = No stable isotopes.\nPopular Use = Medical imaging tracer.",
    "Ruthenium\n\nAtomic Mass = 101.07 u\nMelting Point = 2607 K\nBoiling Point = 4423 K\nSpecial Property = Hard and chemically inert.\nPopular Use = Electrical contacts, catalyst.",
    "Rhodium\n\nAtomic Mass = 102.91 u\nMelting Point = 2237 K\nBoiling Point = 3968 K\nSpecial Property = Expensive, rare metal.\nPopular Use = Catalytic converters, jewelry.",
    "Palladium\n\nAtomic Mass = 106.42 u\nMelting Point = 1828.05 K\nBoiling Point = 3236 K\nSpecial Property = Absorbs a lot of hydrogen.\nPopular Use = Catalytic converters, dentistry.",
    "Silver\n\nAtomic Mass = 107.87 u\nMelting Point = 1234.93 K\nBoiling Point = 2435 K\nSpecial Property = High electrical conductivity.\nPopular Use = Jewelry, electronics.",
    "Cadmium\n\nAtomic Mass = 112.41 u\nMelting Point = 594.22 K\nBoiling Point = 1040 K\nSpecial Property = Highly toxic.\nPopular Use = Rechargeable batteries, pigment.",
    "Indium\n\nAtomic Mass = 114.82 u\nMelting Point = 429.75 K\nBoiling Point = 2345 K\nSpecial Property = Makes a distinctive 'cry'.\nPopular Use = LCD screens, conductors.",
    "Tin\n\nAtomic Mass = 118.71 u\nMelting Point = 505.08 K\nBoiling Point = 2875 K\nSpecial Property = Key component in solder.\nPopular Use = Soldering, food cans.",
    "Antimony\n\nAtomic Mass = 121.76 u\nMelting Point = 903.78 K\nBoiling Point = 1908 K\nSpecial Property = Expands on solidification.\nPopular Use = Fire retardant, lead alloys.",
    "Tellurium\n\nAtomic Mass = 127.60 u\nMelting Point = 722.66 K\nBoiling Point = 1261 K\nSpecial Property = Electrical conductivity from light.\nPopular Use = Solar cells, electronics.",
    "Iodine\n\nAtomic Mass = 126.90 u\nMelting Point = 386.85 K\nBoiling Point = 457.4 K\nSpecial Property = Sublimes to a violet gas.\nPopular Use = Disinfectant, medical imaging.",
    "Xenon\n\nAtomic Mass = 131.29 u\nMelting Point = 161.4 K\nBoiling Point = 165.0 K\nSpecial Property = Forms chemical compounds.\nPopular Use = Arc lamps, anesthetic.",
    "Cesium\n\nAtomic Mass = 132.91 u\nMelting Point = 301.59 K\nBoiling Point = 944 K\nSpecial Property = Most electropositive element.\nPopular Use = Atomic clocks, drilling fluids.",
    "Barium\n\nAtomic Mass = 137.33 u\nMelting Point = 1000 K\nBoiling Point = 2170 K\nSpecial Property = Soft and silvery-white.\nPopular Use = Medical imaging, fireworks.",
    "Lanthanum\n\nAtomic Mass = 138.91 u\nMelting Point = 1193 K\nBoiling Point = 3737 K\nSpecial Property = Reacts quickly with acids.\nPopular Use = Camera lenses, lighter flints.",
    "Cerium\n\nAtomic Mass = 140.12 u\nMelting Point = 1068 K\nBoiling Point = 3716 K\nSpecial Property = Most abundant rare-earth metal.\nPopular Use = Self-cleaning ovens, lighters.",
    "Praseodymium\n\nAtomic Mass = 140.91 u\nMelting Point = 1208 K\nBoiling Point = 3793 K\nSpecial Property = Forms a green glass.\nPopular Use = Aircraft engines, welding goggles.",
    "Neodymium\n\nAtomic Mass = 144.24 u\nMelting Point = 1294 K\nBoiling Point = 3347 K\nSpecial Property = Strongest permanent magnets.\nPopular Use = Magnets, speakers, microphones.",
    "Promethium\n\nAtomic Mass = (145) u\nMelting Point = 1315 K\nBoiling Point = 3273 K\nSpecial Property = The only radioactive lanthanide.\nPopular Use = Nuclear batteries, luminous paint.",
    "Samarium\n\nAtomic Mass = 150.36 u\nMelting Point = 1345 K\nBoiling Point = 2067 K\nSpecial Property = Stable at high temperatures.\nPopular Use = Magnets, carbon arc lighting.",
    "Europium\n\nAtomic Mass = 151.96 u\nMelting Point = 1099 K\nBoiling Point = 1870 K\nSpecial Property = Most reactive rare-earth element.\nPopular Use = Red and blue phosphors in TVs.",
    "Gadolinium\n\nAtomic Mass = 157.25 u\nMelting Point = 1585 K\nBoiling Point = 3273 K\nSpecial Property = Strong magnetic properties.\nPopular Use = MRI contrast agents, neutron capture.",
    "Terbium\n\nAtomic Mass = 158.93 u\nMelting Point = 1629 K\nBoiling Point = 3503 K\nSpecial Property = Bright phosphorescent glow.\nPopular Use = Color TV screens, fuel cells.",
    "Dysprosium\n\nAtomic Mass = 162.50 u\nMelting Point = 1680 K\nBoiling Point = 2840 K\nSpecial Property = High thermal neutron absorption.\nPopular Use = Magnets, data storage.",
    "Holmium\n\nAtomic Mass = 164.93 u\nMelting Point = 1734 K\nBoiling Point = 2873 K\nSpecial Property = Highest magnetic strength.\nPopular Use = Magnets, medical lasers.",
    "Erbium\n\nAtomic Mass = 167.26 u\nMelting Point = 1802 K\nBoiling Point = 3141 K\nSpecial Property = Pink color in glass.\nPopular Use = Fiber optics, lasers.",
    "Thulium\n\nAtomic Mass = 168.93 u\nMelting Point = 1818 K\nBoiling Point = 2223 K\nSpecial Property = Soft, silver-gray metal.\nPopular Use = Portable X-ray machines, lasers.",
    "Ytterbium\n\nAtomic Mass = 173.04 u\nMelting Point = 1097 K\nBoiling Point = 1469 K\nSpecial Property = Soft and malleable.\nPopular Use = Steel alloys, nuclear medicine.",
    "Lutetium\n\nAtomic Mass = 174.97 u\nMelting Point = 1925 K\nBoiling Point = 3675 K\nSpecial Property = Very hard to isolate.\nPopular Use = High-refractive-index glass.",
    "Hafnium\n\nAtomic Mass = 178.49 u\nMelting Point = 2506 K\nBoiling Point = 4876 K\nSpecial Property = Excellent corrosion resistance.\nPopular Use = Nuclear control rods, microchips.",
    "Tantalum\n\nAtomic Mass = 180.95 u\nMelting Point = 3290 K\nBoiling Point = 5731 K\nSpecial Property = Highly ductile.\nPopular Use = Electronic capacitors, surgical implants.",
    "Tungsten\n\nAtomic Mass = 183.84 u\nMelting Point = 3695 K\nBoiling Point = 6203 K\nSpecial Property = Highest melting point of all elements.\nPopular Use = Light bulb filaments, cutting tools.",
    "Rhenium\n\nAtomic Mass = 186.21 u\nMelting Point = 3459 K\nBoiling Point = 5869 K\nSpecial Property = One of the densest elements.\nPopular Use = Jet engine parts, thermocouples.",
    "Osmium\n\nAtomic Mass = 190.23 u\nMelting Point = 3306 K\nBoiling Point = 5285 K\nSpecial Property = Densest naturally occurring element.\nPopular Use = Fountain pen nibs, electrical contacts.",
    "Iridium\n\nAtomic Mass = 192.22 u\nMelting Point = 2719 K\nBoiling Point = 4428 K\nSpecial Property = Most corrosion-resistant metal.\nPopular Use = Spark plugs, medical devices.",
    "Platinum\n\nAtomic Mass = 195.08 u\nMelting Point = 2041.4 K\nBoiling Point = 4098 K\nSpecial Property = Highly valued, very dense.\nPopular Use = Catalytic converters, jewelry.",
    "Gold\n\nAtomic Mass = 196.97 u\nMelting Point = 1337.33 K\nBoiling Point = 3129 K\nSpecial Property = Highly malleable and ductile.\nPopular Use = Jewelry, electronics, currency.",
    "Mercury\n\nAtomic Mass = 200.59 u\nMelting Point = 234.32 K\nBoiling Point = 630 K\nSpecial Property = Liquid at room temperature.\nPopular Use = Thermometers, barometers.",
    "Thallium\n\nAtomic Mass = 204.38 u\nMelting Point = 577 K\nBoiling Point = 1730 K\nSpecial Property = Highly toxic.\nPopular Use = Electronics, infrared detectors.",
    "Lead\n\nAtomic Mass = 207.2 u\nMelting Point = 600.61 K\nBoiling Point = 2022 K\nSpecial Property = Heaviest stable element.\nPopular Use = Batteries, radiation shielding.",
    "Bismuth\n\nAtomic Mass = 208.98 u\nMelting Point = 544.7 K\nBoiling Point = 1837 K\nSpecial Property = Low toxicity, iridescent.\nPopular Use = Cosmetics, pharmaceuticals.",
    "Polonium\n\nAtomic Mass = (209) u\nMelting Point = 527 K\nBoiling Point = 1235 K\nSpecial Property = Highly radioactive.\nPopular Use = Alpha-particle sources.",
    "Astatine\n\nAtomic Mass = (210) u\nMelting Point = 575 K\nBoiling Point = 610 K\nSpecial Property = Rarest naturally occurring element.\nPopular Use = Radiotherapy.",
    "Radon\n\nAtomic Mass = (222) u\nMelting Point = 202 K\nBoiling Point = 211.3 K\nSpecial Property = Radioactive noble gas.\nPopular Use = Radiotherapy.",
    "Francium\n\nAtomic Mass = (223) u\nMelting Point = 300 K\nBoiling Point = 950 K\nSpecial Property = Most unstable element.\nPopular Use = Used in atomic research.",
    "Radium\n\nAtomic Mass = (226) u\nMelting Point = 973 K\nBoiling Point = 2010 K\nSpecial Property = Luminous paints (historically).",
    "Actinium\n\nAtomic Mass = (227) u\nMelting Point = 1500 K\nBoiling Point = 3500 K\nSpecial Property = Highly radioactive.\nPopular Use = Used as a neutron source.",
    "Thorium\n\nAtomic Mass = 232.04 u\nMelting Point = 2023 K\nBoiling Point = 5061 K\nSpecial Property = A possible nuclear fuel.\nPopular Use = Gas lantern mantles, welding electrodes.",
    "Protactinium\n\nAtomic Mass = 231.04 u\nMelting Point = 1845 K\nBoiling Point = 4300 K\nSpecial Property = Toxic and highly radioactive.\nPopular Use = Scientific research.",
    "Uranium\n\nAtomic Mass = 238.03 u\nMelting Point = 1405.3 K\nBoiling Point = 4404 K\nSpecial Property = Most famous radioactive element.\nPopular Use = Nuclear fuel, armor plating.",
    "Neptunium\n\nAtomic Mass = (237) u\nMelting Point = 912 K\nBoiling Point = 4174 K\nSpecial Property = Radioactive and silvery.\nPopular Use = Neutron detection equipment.",
    "Plutonium\n\nAtomic Mass = (244) u\nMelting Point = 912.5 K\nBoiling Point = 3505 K\nSpecial Property = Key component of nuclear weapons.\nPopular Use = Nuclear reactors, space probes.",
    "Americium\n\nAtomic Mass = (243) u\nMelting Point = 1449 K\nBoiling Point = 2880 K\nSpecial Property = Radioactive, used in smoke detectors.\nPopular Use = Smoke detectors, neutron sources.",
    "Curium\n\nAtomic Mass = (247) u\nMelting Point = 1618 K\nBoiling Point = 3383 K\nSpecial Property = Highly radioactive.\nPopular Use = Scientific research.",
    "Berkelium\n\nAtomic Mass = (247) u\nMelting Point = 1259 K\nBoiling Point = 2900 K\nSpecial Property = Soft and silvery-white.\nPopular Use = Scientific research.",
    "Californium\n\nAtomic Mass = (251) u\nMelting Point = 1173 K\nBoiling Point = 1743 K\nSpecial Property = Strong neutron emitter.\nPopular Use = Neutron activation, medicine.",
    "Einsteinium\n\nAtomic Mass = (252) u\nMelting Point = 1133 K\nBoiling Point = 1269 K\nSpecial Property = First element found in debris of H-bomb.\nPopular Use = Scientific research.",
    "Fermium\n\nAtomic Mass = (257) u\nMelting Point = 1800 K\nBoiling Point = 1173 K\nSpecial Property = Only produced in laboratories.\nPopular Use = Scientific research.",
    "Mendelevium\n\nAtomic Mass = (258) u\nMelting Point = 1100 K\nBoiling Point = Unknown\nSpecial Property = Created by bombarding Einsteinium.\nPopular Use = Scientific research.",
    "Nobelium\n\nAtomic Mass = (259) u\nMelting Point = 1100 K\nBoiling Point = Unknown\nSpecial Property = Synthetic radioactive element.\nPopular Use = Scientific research.",
    "Lawrencium\n\nAtomic Mass = (262) u\nMelting Point = 1900 K\nBoiling Point = Unknown\nSpecial Property = Shortest-lived known isotope.\nPopular Use = Scientific research.",
    "Rutherfordium\n\nAtomic Mass = (267) u\nMelting Point = 2400 K\nBoiling Point = 5500 K\nSpecial Property = First to have a superheavy isotope.\nPopular Use = Scientific research.",
    "Dubnium\n\nAtomic Mass = (268) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Superheavy, radioactive.\nPopular Use = Scientific research.",
    "Seaborgium\n\nAtomic Mass = (269) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Extremely radioactive.\nPopular Use = Scientific research.",
    "Bohrium\n\nAtomic Mass = (270) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Synthetic, named after Niels Bohr.\nPopular Use = Scientific research.",
    "Hassium\n\nAtomic Mass = (277) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Very heavy, radioactive.\nPopular Use = Scientific research.",
    "Meitnerium\n\nAtomic Mass = (278) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Named after Lise Meitner.\nPopular Use = Scientific research.",
    "Darmstadtium\n\nAtomic Mass = (281) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Made by fusing lead and nickel.\nPopular Use = Scientific research.",
    "Roentgenium\n\nAtomic Mass = (282) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Named after Wilhelm Rontgen.\nPopular Use = Scientific research.",
    "Copernicium\n\nAtomic Mass = (285) u\nMelting Point = 283 K\nBoiling Point = 340 K\nSpecial Property = Volatile and radioactive.\nPopular Use = Scientific research.",
    "Nihonium\n\nAtomic Mass = (286) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = The first element discovered in Asia.\nPopular Use = Scientific research.",
    "Flerovium\n\nAtomic Mass = (289) u\nMelting Point = 283 K\nBoiling Point = 340 K\nSpecial Property = Predicted to be a volatile metal.\nPopular Use = Scientific research.",
    "Moscovium\n\nAtomic Mass = (289) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Named after Moscow region.\nPopular Use = Scientific research.",
    "Livermorium\n\nAtomic Mass = (293) u\nMelting Point = Unknown\nBoiling Point = Unknown\nSpecial Property = Named after Livermore lab.\nPopular Use = Scientific research.",
    "Tennessine\n\nAtomic Mass = (294) u\nMelting Point = 623-823 K (Predicted)\nBoiling Point = Unknown\nSpecial Property = Halogen with metallic properties.\nPopular Use = Scientific research.",
    "Oganesson\n\nAtomic Mass = (294) u\nMelting Point = 263 K (Predicted)\nBoiling Point = 263 K (Predicted)\nSpecial Property = Heavier than any other noble gas.\nPopular Use = Scientific research."
]


l1 = ["", 3, 6, '', "L", color.violet]
l2 = ["", 3, 7, '', "A", color.cyan]

#Fucntion to display information about the element
def display_info(index):
    #Setting the text for the billboard
    text_shower.text = text_content[index]
    text_shower.enabled = True

    #Enabling the hide button
    hide_button.enabled = True

#Function to hide the text
def hide_text():
    text_shower.enabled = False
    hide_button.enabled = False

#Button to hide the text
hide_button.on_click = hide_text

#Class object for element entity
class Element(Button):
	def __init__(self, x, z, set_color, index):
		super().__init__(
			parent=scene,
			model="cube",
            color = set_color,
			scale=1,
			position=(x,0,z),
            texture = "white_cube",
            highlight_color = color.white,
            enabled = True,
            on_click = lambda: display_info(index))


table = [None]*len(elements)

lathi = Entity(model = "cube", scale = 1, position = (l1[2],0,l1[1]), color = l1[5],
                        texture = "white_cube")
    
lathi_symbol = Text(text = f'{l1[4]}',
            parent = lathi,
            origin = (0,-3), 
            scale = 14, # Increased the scale to make it more visible
            color = color.black,
            font = "font_bold.ttf",
            billboard = True) # This is the crucial fix!

actini = Entity(model = "cube", scale = 1, position = (l2[2],0,l2[1]), color = l2[5],
                        texture = "white_cube")
    
lathi_symbol = Text(text = f'{l2[4]}',
            parent = actini,
            origin = (0,-3), 
            scale = 14, # Increased the scale to make it more visible
            color = color.black,
            font = "font_bold.ttf",
            billboard = True) # This is the crucial fix!

#Sample display
for i in range(len(elements)):
    table[i] = Element(x=elements[i][2], z=elements[i][1], set_color=elements[i][5], index=i)
     
    text_entity = Text(text = f'{elements[i][0]}\n{elements[i][3]}',
                     parent = table[i],
                     origin = (0,-2), 
                     scale = 6, # Increased the scale to make it more visible
                     color = color.black,
                     billboard = True) # This is the crucial fix!
    
    symbol = Text(text = f'{elements[i][4]}',
                     parent = table[i],
                     origin = (0,-3), 
                     scale = 14, # Increased the scale to make it more visible
                     color = color.black,
                     font = "font_bold.ttf",
                     billboard = True) # This is the crucial fix!

#Make only specific visible
show_specific = None

def to_metals_alkali():
    global show_specific

    if show_specific != color.blue:
        show_specific = color.blue
    else:
        show_specific = None

def to_metals_earth():
    global show_specific

    if show_specific != color.red:
        show_specific = color.red
    else:
        show_specific = None

def to_transition():
    global show_specific

    if show_specific != color.green:
        show_specific = color.green
    else:
        show_specific = None

def to_post_transition():
    global show_specific

    if show_specific != color.brown:
        show_specific = color.brown
    else:
        show_specific = None

def to_hallogens():
    global show_specific

    if show_specific != color.pink:
        show_specific = color.pink
    else:
        show_specific = None

def to_nobel():
    global show_specific

    if show_specific != color.orange:
        show_specific = color.orange
    else:
        show_specific = None

def to_lathanides():
    global show_specific

    if show_specific != color.violet:
        show_specific = color.violet
    else:
        show_specific = None

def to_actinides():
    global show_specific

    if show_specific != color.cyan:
        show_specific = color.cyan
    else:
        show_specific = None

def to_metalloid():
    global show_specific

    if show_specific != color.yellow:
        show_specific = color.yellow
    else:
        show_specific = None

def to_non_metal():
    global show_specific

    if show_specific != color.azure:
        show_specific = color.azure
    else:
        show_specific = None

alkaline_metal.on_click = to_metals_alkali
non_metal.on_click = to_non_metal
alkaline_earth_metal.on_click = to_metals_earth
transition.on_click = to_transition
post_transition.on_click = to_post_transition
halogen.on_click = to_hallogens
noble_gas.on_click = to_nobel
lathanides.on_click = to_lathanides
actinides.on_click = to_actinides
metalloid.on_click = to_metalloid

#Main game loop
def update():
    #Stop the editor camera from moving and rotating when on home screen
    if home_screen:
        editor_camera.position = (100,100,100)
        editor_camera.rotation = (0,0,0)

    for i in range(len(table)):
        if show_specific == None:
            table[i].enabled = True

            lathi.enabled = True
            actini.enabled = True
        else:
            lathi.enabled = False
            actini.enabled = False

            if table[i].color != show_specific:
                table[i].enabled = False
            elif table[i].color == show_specific:
                table[i].enabled = True

#Running the app
app.run()
