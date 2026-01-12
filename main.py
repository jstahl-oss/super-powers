def on_item_interacted_diamond_sword():
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 6000, 255)
player.on_item_interacted(DIAMOND_SWORD, on_item_interacted_diamond_sword)

def on_item_interacted_netherite_sword():
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 6000, 255)
player.on_item_interacted(NETHERITE_SWORD, on_item_interacted_netherite_sword)

def on_item_interacted_mace():
    mobs.apply_effect(JUMP_BOOST, mobs.target(LOCAL_PLAYER), 10, 1)
    mobs.apply_effect(STRENGTH, mobs.target(LOCAL_PLAYER), 10, 1)
    mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 10, 1)
player.on_item_interacted(MACE, on_item_interacted_mace)

def on_item_interacted_shield():
    mobs.apply_effect(RESISTANCE, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.apply_effect(REGENERATION, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.apply_effect(FIRE_RESISTANCE, mobs.target(LOCAL_PLAYER), 6000, 255)
    mobs.apply_effect(INVISIBILITY, mobs.target(LOCAL_PLAYER), 6000, 255)
player.on_item_interacted(SHIELD, on_item_interacted_shield)

def on_item_interacted_diamond_boots():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 6000, 255)
player.on_item_interacted(DIAMOND_BOOTS, on_item_interacted_diamond_boots)

def on_item_interacted_netherite_boots():
    mobs.apply_effect(SPEED, mobs.target(LOCAL_PLAYER), 6000, 255)
player.on_item_interacted(NETHERITE_BOOTS, on_item_interacted_netherite_boots)
