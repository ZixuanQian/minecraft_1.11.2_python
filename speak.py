from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
mc.postToChat("Hello,Minecraft World")
time.sleep(5)
if __name__ == '__main__':
    print(mc.player)