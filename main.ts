player.onItemInteracted(DIAMOND_SWORD, function () {
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 6000, 255)
})
player.onItemInteracted(NETHERITE_SWORD, function () {
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 6000, 255)
})
player.onItemInteracted(MACE, function () {
    mobs.applyEffect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 10, 1)
    mobs.applyEffect(STRENGTH, mobs.target(LOCAL_PLAYER), 10, 1)
    mobs.applyEffect(REGENERATION, mobs.target(NEAREST_PLAYER), 10, 1)
})
player.onItemInteracted(SHIELD, function () {
    mobs.applyEffect(RESISTANCE, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.applyEffect(REGENERATION, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.applyEffect(FIRE_RESISTANCE, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.applyEffect(INVISIBILITY, mobs.target(LOCAL_PLAYER), 6000, 255)
})
player.onItemInteracted(DIAMOND_BOOTS, function () {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 6000, 255)
})
player.onItemInteracted(NETHERITE_BOOTS, function () {
    mobs.applyEffect(SPEED, mobs.target(LOCAL_PLAYER), 6000, 255)
})
