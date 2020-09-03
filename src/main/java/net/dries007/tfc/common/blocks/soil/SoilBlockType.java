/*
 * Work under Copyright. Licensed under the EUPL.
 * See the project README.md and LICENSE.txt for more information.
 */

package net.dries007.tfc.common.blocks.soil;

import net.minecraft.block.Block;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.block.material.MaterialColor;

import net.dries007.tfc.common.blocks.TFCBlocks;

public enum SoilBlockType
{
    DIRT,
    GRASS,
    GRASS_PATH,
    CLAY,
    CLAY_GRASS;

    public static final SoilBlockType[] VALUES = values();

    public static SoilBlockType valueOf(int i)
    {
        return i >= 0 && i < VALUES.length ? VALUES[i] : DIRT;
    }

    public Block create(Variant variant)
    {
        switch (this)
        {
            case DIRT:
                return new TFCDirtBlock(Block.Properties.create(Material.EARTH, MaterialColor.DIRT).hardnessAndResistance(0.5F).sound(SoundType.GROUND), () -> TFCBlocks.SOIL.get(GRASS).get(variant).get());
            case CLAY:
                return new TFCDirtBlock(Block.Properties.create(Material.EARTH, MaterialColor.DIRT).hardnessAndResistance(0.5F).sound(SoundType.GROUND), () -> TFCBlocks.SOIL.get(CLAY_GRASS).get(variant).get());
            case GRASS:
                return new TFCGrassBlock(Block.Properties.create(Material.ORGANIC).tickRandomly().hardnessAndResistance(0.6F).sound(SoundType.PLANT), () -> TFCBlocks.SOIL.get(DIRT).get(variant).get());
            case CLAY_GRASS:
                return new TFCGrassBlock(Block.Properties.create(Material.ORGANIC).tickRandomly().hardnessAndResistance(0.6F).sound(SoundType.PLANT), () -> TFCBlocks.SOIL.get(CLAY).get(variant).get());
            case GRASS_PATH:
                return new TFCGrassPathBlock(Block.Properties.create(Material.EARTH).hardnessAndResistance(0.65F).sound(SoundType.PLANT));
        }
        throw new IllegalArgumentException("Unknown block type");
    }

    public enum Variant
    {
        SILT,
        LOAM,
        SANDY_LOAM,
        SILTY_LOAM;

        public static final int TOTAL = values().length;

        private static final Variant[] VALUES = values();

        public static Variant valueOf(int i)
        {
            return i >= 0 && i < TOTAL ? VALUES[i] : SILT;
        }
    }
}
