import tank

fire_tank = tank.Tank('Phol', 3)
fire_tank.fire_ammo()
print(fire_tank.ammo)

fire_tank.fire_ammo()
fire_tank.fire_ammo()
print(fire_tank.ammo)

fire_tank.add_ammo(4)
print(fire_tank.ammo)