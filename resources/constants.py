#  Work under Copyright. Licensed under the EUPL.
#  See the project README.md and LICENSE.txt for more information.

from collections import namedtuple
from typing import Dict, List

Rock = namedtuple('Rock', ('category', 'sand_color'))
Metal = namedtuple('Metal', (
    'tier', 'has_parts', 'has_tools', 'has_armor', 'has_utilities', 'heat_capacity', 'melt_temperature'))
MetalItem = namedtuple('MetalItem', ('type', 'smelt_amount', 'parent_model', 'tag'))
Ore = namedtuple('Ore', ('metal', 'graded'))
OreGrade = namedtuple('OreGrade', ('weight',))
Vein = namedtuple('Vein', ('ore', 'type', 'rarity', 'size', 'min_y', 'max_y', 'density', 'poor', 'normal', 'rich', 'rocks'))

HORIZONTAL_DIRECTIONS: List[str] = ['east', 'west', 'north', 'south']

ROCK_CATEGORIES: List[str] = ['sedimentary', 'metamorphic', 'igneous_extrusive', 'igneous_intrusive']
ROCK_ITEMS: List[str] = ['axe', 'axe_head', 'hammer', 'hammer_head', 'hoe', 'hoe_head', 'javelin', 'javelin_head', 'knife', 'knife_head', 'shovel', 'shovel_head']

ROCKS: Dict[str, Rock] = {
    'chalk': Rock('sedimentary', 'yellow'),
    'chert': Rock('sedimentary', 'yellow'),
    'claystone': Rock('sedimentary', 'red'),
    'conglomerate': Rock('sedimentary', 'red'),
    'dolomite': Rock('sedimentary', 'green'),
    'limestone': Rock('sedimentary', 'white'),
    'shale': Rock('sedimentary', 'red'),
    'gneiss': Rock('metamorphic', 'red'),
    'marble': Rock('metamorphic', 'white'),
    'phyllite': Rock('metamorphic', 'white'),
    'quartzite': Rock('metamorphic', 'pink'),
    'schist': Rock('metamorphic', 'green'),
    'slate': Rock('metamorphic', 'yellow'),
    'diorite': Rock('igneous_intrusive', 'brown'),
    'gabbro': Rock('igneous_intrusive', 'black'),
    'granite': Rock('igneous_intrusive', 'brown'),
    'andesite': Rock('igneous_extrusive', 'black'),
    'basalt': Rock('igneous_extrusive', 'black'),
    'dacite': Rock('igneous_extrusive', 'black'),
    'rhyolite': Rock('igneous_extrusive', 'pink')
}
METALS: Dict[str, Metal] = {
    'bismuth': Metal(1, True, False, False, False, 0.14, 270),
    'bismuth_bronze': Metal(2, True, True, True, True, 0.35, 985),
    'black_bronze': Metal(2, True, True, True, True, 0.35, 1070),
    'bronze': Metal(2, True, True, True, True, 0.35, 950),
    'brass': Metal(2, True, False, False, False, 0.35, 930),
    'copper': Metal(1, True, True, True, True, 0.35, 1080),
    'gold': Metal(1, True, False, False, False, 0.6, 1060),
    'nickel': Metal(1, True, False, False, False, 0.48, 1453),
    'rose_gold': Metal(1, True, False, False, False, 0.35, 960),
    'silver': Metal(1, True, False, False, False, 0.48, 961),
    'tin': Metal(1, True, False, False, False, 0.14, 230),
    'zinc': Metal(1, True, False, False, False, 0.21, 420),
    'sterling_silver': Metal(1, True, False, False, False, 0.35, 950),
    'wrought_iron': Metal(3, True, True, True, True, 0.35, 1535),
    'cast_iron': Metal(1, False, True, False, False, 0.35, 1535),
    'pig_iron': Metal(3, False, False, False, False, 0.35, 1535),
    'steel': Metal(4, True, True, True, True, 0.35, 1540),
    'black_steel': Metal(5, True, True, True, True, 0.35, 1485),
    'blue_steel': Metal(6, True, True, True, True, 0.35, 1540),
    'red_steel': Metal(6, True, True, True, True, 0.35, 1540),
    'weak_steel': Metal(4, False, False, False, False, 0.35, 1540),
    'weak_blue_steel': Metal(5, False, False, False, False, 0.35, 1540),
    'weak_red_steel': Metal(5, False, False, False, False, 0.35, 1540),
    'high_carbon_steel': Metal(3, False, False, False, False, 0.35, 1540),
    'high_carbon_black_steel': Metal(4, False, False, False, False, 0.35, 1540),
    'high_carbon_blue_steel': Metal(5, False, False, False, False, 0.35, 1540),
    'high_carbon_red_steel': Metal(5, False, False, False, False, 0.35, 1540),
    'unknown': Metal(0, False, False, False, False, 0.5, 1250)
}
METAL_BLOCKS: Dict[str, MetalItem] = {
    'anvil': MetalItem('utility', 1400, 'tfc:block/anvil', ''),
    'lamp': MetalItem('utility', 100, 'tfc:block/lamp', '')
}
METAL_ITEMS: Dict[str, MetalItem] = {
    'ingot': MetalItem('default', 100, 'item/generated', 'forge:ingots'),
    'double_ingot': MetalItem('part', 200, 'item/generated', 'forge:double_ingots'),
    'sheet': MetalItem('part', 200, 'item/generated', 'forge:sheets'),
    'double_sheet': MetalItem('part', 400, 'item/generated', 'forge:double_sheets'),
    'rod': MetalItem('part', 100, 'item/generated', 'forge:rods'),

    'tuyere': MetalItem('tool', 100, 'item/generated', ''),
    'pickaxe': MetalItem('tool', 100, 'item/handheld', ''),
    'pickaxe_head': MetalItem('tool', 100, 'item/generated', ''),
    'shovel': MetalItem('tool', 100, 'item/handheld', ''),
    'shovel_head': MetalItem('tool', 100, 'item/generated', ''),
    'axe': MetalItem('tool', 100, 'item/handheld', ''),
    'axe_head': MetalItem('tool', 100, 'item/generated', ''),
    'hoe': MetalItem('tool', 100, 'item/handheld', ''),
    'hoe_head': MetalItem('tool', 100, 'item/generated', ''),
    'chisel': MetalItem('tool', 100, 'item/handheld', ''),
    'chisel_head': MetalItem('tool', 100, 'item/generated', ''),
    'sword': MetalItem('tool', 100, 'item/handheld', ''),
    'sword_blade': MetalItem('tool', 100, 'item/generated', ''),
    'mace': MetalItem('tool', 100, 'item/handheld', ''),
    'mace_head': MetalItem('tool', 100, 'item/generated', ''),
    'saw': MetalItem('tool', 100, 'item/handheld', ''),
    'saw_blade': MetalItem('tool', 100, 'item/generated', ''),
    'javelin': MetalItem('tool', 100, 'item/handheld', ''),
    'javelin_head': MetalItem('tool', 100, 'item/generated', ''),
    'hammer': MetalItem('tool', 100, 'item/handheld', ''),
    'hammer_head': MetalItem('tool', 100, 'item/generated', ''),
    'propick': MetalItem('tool', 100, 'item/handheld', ''),
    'propick_head': MetalItem('tool', 100, 'item/generated', ''),
    'knife': MetalItem('tool', 100, 'tfc:item/handheld_flipped', ''),
    'knife_blade': MetalItem('tool', 100, 'item/generated', ''),
    'scythe': MetalItem('tool', 100, 'item/handheld', ''),
    'scythe_blade': MetalItem('tool', 100, 'item/generated', ''),
    'shears': MetalItem('tool', 200, 'item/handheld', ''),
    
    'unfinished_helmet': MetalItem('armor', 400, 'item/generated', ''),
    'helmet': MetalItem('armor', 600, 'item/generated', ''),
    'unfinished_chestplate': MetalItem('armor', 400, 'item/generated', ''),
    'chestplate': MetalItem('armor', 800, 'item/generated', ''),
    'unfinished_greaves': MetalItem('armor', 400, 'item/generated', ''),
    'greaves': MetalItem('armor', 600, 'item/generated', ''),
    'unfinished_boots': MetalItem('armor', 200, 'item/generated', ''),
    'boots': MetalItem('armor', 400, 'item/generated', ''),
    
    'shield': MetalItem('tool', 400, 'item/handheld', '')
}
ORES: Dict[str, Ore] = {
    'native_copper': Ore('copper', True),
    'native_gold': Ore('gold', True),
    'hematite': Ore('cast_iron', True),
    'native_silver': Ore('silver', True),
    'cassiterite': Ore('tin', True),
    'bismuthinite': Ore('bismuth', True),
    'garnierite': Ore('nickel', True),
    'malachite': Ore('copper', True),
    'magnetite': Ore('cast_iron', True),
    'limonite': Ore('cast_iron', True),
    'sphalerite': Ore('zinc', True),
    'tetrahedrite': Ore('copper', True),
    'bituminous_coal': Ore(None, False),
    'lignite': Ore(None, False),
    'kaolinite': Ore(None, False),
    'gypsum': Ore(None, False),
    'graphite': Ore(None, False),
    'sulfur': Ore(None, False),
    'cinnabar': Ore(None, False),
    'cryolite': Ore(None, False),
    'saltpeter': Ore(None, False),
    'sylvite': Ore(None, False),
    'borax': Ore(None, False),
    'halite': Ore(None, False),
    'amethyst': Ore(None, False),
    'diamond': Ore(None, False),
    'emerald': Ore(None, False),
    'lapis_lazuli': Ore(None, False),
    'opal': Ore(None, False),
    'pyrite': Ore(None, False),
    'ruby': Ore(None, False),
    'sapphire': Ore(None, False),
    'topaz': Ore(None, False)
}
ORE_GRADES: Dict[str, OreGrade] = {
    'normal': OreGrade(50),
    'poor': OreGrade(30),
    'rich': OreGrade(20)
}
ORE_VEINS: Dict[str, Vein] = {
<<<<<<< HEAD
        'normal_native_copper': Vein('native_copper', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive']),
        'surface_native_copper': Vein('native_copper', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_extrusive']),
        'normal_native_gold': Vein('native_gold', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive', 'igneous_intrusive']),
        'deep_native_gold': Vein('native_gold', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['igneous_extrusive', 'igneous_intrusive']),
        'normal_native_silver': Vein('native_silver', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['granite', 'gneiss']),
        'poor_native_silver': Vein('native_silver', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['granite', 'metamorphic']),
        'normal_hematite': Vein('hematite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive']),
        'deep_hematite': Vein('hematite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['igneous_extrusive']),
        'normal_cassiterite': Vein('cassiterite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_intrusive']),
        'surface_cassiterite': Vein('cassiterite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_intrusive']),
        'normal_bismuthinite': Vein('bismuthinite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_intrusive', 'sedimentary']),
        'surface_bismuthinite': Vein('bismuthinite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_intrusive', 'sedimentary']),
        'normal_garnierite': Vein('garnierite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['gabbro']),
        'poor_garnierite': Vein('garnierite', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['igneous_intrusive']),
        'normal_malachite': Vein('malachite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['marble', 'limestone']),
        'poor_malachite': Vein('malachite', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['marble', 'limestone', 'phyllite', 'chalk', 'dolomite']),
        'normal_magnetite': Vein('magnetite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['sedimentary']),
        'deep_magnetite': Vein('magnetite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['sedimentary']),
        'normal_limonite': Vein('limonite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['sedimentary']),
        'deep_limonite': Vein('limonite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['sedimentary']),
        'normal_sphalerite': Vein('sphalerite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['metamorphic']),
        'surface_sphalerite': Vein('sphalerite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['metamorphic']),
        'normal_tetrahedrite': Vein('tetrahedrite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['metamorphic']),
        'surface_tetrahedrite': Vein('tetrahedrite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['metamorphic']),
=======
    'normal_native_copper': Vein('native_copper', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive']),
    'surface_native_copper': Vein('native_copper', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_extrusive']),
    'normal_native_gold': Vein('native_gold', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive', 'igneous_intrusive']),
    'deep_native_gold': Vein('native_gold', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['igneous_extrusive', 'igneous_intrusive']),
    'normal_native_silver': Vein('native_silver', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['granite', 'gneiss']),
    'poor_native_silver': Vein('native_silver', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['granite', 'metamorphic']),
    'normal_hematite': Vein('hematite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_extrusive']),
    'deep_hematite': Vein('hematite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['igneous_extrusive']),
    'normal_cassiterite': Vein('cassiterite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_intrusive']),
    'surface_cassiterite': Vein('cassiterite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_intrusive']),
    'normal_bismuthinite': Vein('bismuthinite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['igneous_intrusive', 'sedimentary']),
    'surface_bismuthinite': Vein('bismuthinite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['igneous_intrusive', 'sedimentary']),
    'normal_garnierite': Vein('garnierite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['gabbro']),
    'poor_garnierite': Vein('garnierite', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['igneous_intrusive']),
    'normal_malachite': Vein('malachite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['marble', 'limestone']),
    'poor_malachite': Vein('malachite', 'cluster', 140, 15, 5, 100, 60, 60, 30, 10, ['marble', 'limestone', 'phyllite', 'chalk', 'dolomite']),
    'normal_magnetite': Vein('magnetite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['sedimentary']),
    'deep_magnetite': Vein('magnetite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['sedimentary']),
    'normal_limonite': Vein('limonite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['sedimentary']),
    'deep_limonite': Vein('limonite', 'cluster', 120, 30, 5, 60, 60, 10, 30, 60, ['sedimentary']),
    'normal_sphalerite': Vein('sphalerite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['metamorphic']),
    'surface_sphalerite': Vein('sphalerite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['metamorphic']),
    'normal_tetrahedrite': Vein('tetrahedrite', 'cluster', 100, 20, 30, 100, 60, 20, 50, 30, ['metamorphic']),
    'surface_tetrahedrite': Vein('tetrahedrite', 'cluster', 80, 15, 60, 120, 60, 60, 30, 10, ['metamorphic']),
>>>>>>> cbeff1512e78942d033272a9b494e96e3b587f2b

        'bituminous_coal': Vein('bituminous_coal', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['sedimentary']),
        'lignite': Vein('lignite', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['sedimentary']),
        'kaolinite': Vein('kaolinite', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['sedimentary']),
        'graphite': Vein('graphite', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['gneiss', 'marble', 'quartzite', 'schist']),
        'cinnabar': Vein('cinnabar', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['igneous_extrusive', 'quartzite', 'shale']),
        'cryolite': Vein('cryolite', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['granite']),
        'saltpeter': Vein('saltpeter', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['sedimentary']),
        'sulfur': Vein('sulfur', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['igneous_extrusive']),
        'sylvite': Vein('sylvite', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['shale', 'claystone', 'chert']),
        'borax': Vein('borax', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['slate']),
        'gypsum': Vein('gypsum', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['metamorphic']),
        'lapis_lazuli': Vein('lapis_lazuli', 'cluster', 120, 10, 5, 100, 60, 0, 0, 0, ['limestone', 'marble']),
        'ruby': Vein('ruby', 'cluster', 80, 6, 5, 50, 70, 0, 0, 0, ['sedimentary']),
        'sapphire': Vein('sapphire', 'cluster', 80, 6, 5, 59, 70, 0, 0, 0, ['metamorphic']),
        'pyrite': Vein('pyrite', 'cluster', 100, 20, 30, 100, 60, 0, 0, 0, ['igneous_extrusive', 'igneous_intrusive']),
        'topaz': Vein('topaz', 'cluster', 80, 6, 96, 255, 60, 0, 0, 0, ['granite', 'rhyolite']),

<<<<<<< HEAD
        'clay': Vein('clay', 'disc', 20, 14, 90, 120, 100, 0, 0, 0, ['soil']),
        'peat': Vein('peat', 'disc', 50, 25, 90, 120, 100, 0, 0, 0, ['soil']),
        'gravel': Vein('gravel', 'disc', 100, 40, 20, 80, 60, 0, 0, 0, ['sedimentary', 'metamorphic', 'igneous_extrusive', 'igneous_intrusive']),
        'halite': Vein('halite', 'disc', 120, 30, 80, 100, 80, 0, 0, 0, ['sedimentary']),
        'amethyst': Vein('amethyst', 'disc', 20, 8, 80, 100, 50, 0, 0, 0, ['sedimentary']),
        'opal': Vein('opal', 'disc', 20, 8, 80, 100, 50, 0, 0, 0, ['sedimentary']),
=======
    'clay': Vein('clay', 'disc', 20, 14, 90, 120, 100, 0, 0, 0, ['soil']),
    'peat': Vein('peat', 'disc', 50, 25, 90, 120, 100, 0, 0, 0, ['soil']),
    'gravel': Vein('gravel', 'disc', 100, 40, 20, 80, 60, 0, 0, 0, ['sedimentary', 'metamorphic', 'igneous_extrusive', 'igneous_intrusive']),
    'halite': Vein('halite', 'disc', 120, 30, 80, 100, 80, 0, 0, 0, ['sedimentary']),
>>>>>>> cbeff1512e78942d033272a9b494e96e3b587f2b

        'diamond': Vein('diamond', 'pipe', 60, 60, 5, 140, 40, 0, 0, 0, ['gabbro']),
        'emerald': Vein('emerald', 'pipe', 80, 60, 5, 140, 40, 0, 0, 0, ['igneous_intrusive']),
}

ROCK_BLOCK_TYPES = ['raw', 'bricks', 'cobble', 'gravel', 'smooth', 'spike', 'mossy_cobble', 'mossy_bricks', 'cracked_bricks', 'chiseled']
ROCK_SPIKE_PARTS = ['base', 'middle', 'tip']
SAND_BLOCK_TYPES = ['brown', 'white', 'black', 'red', 'yellow', 'green', 'pink']
SOIL_BLOCK_TYPES = ['dirt', 'grass', 'grass_path', 'clay', 'clay_grass']
SOIL_BLOCK_VARIANTS = ['silt', 'loam', 'sandy_loam', 'silty_loam']

GEMS = ['amethyst','diamond','emerald','lapis_lazuli','opal','pyrite','ruby','sapphire','topaz']
GEM_GRADES = ['uncut','cut','powder']

def lang(key: str, *args) -> str:
    return ((key % args) if len(args) > 0 else key).replace('_', ' ').replace('/', ' ').title()
