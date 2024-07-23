import sys
if len(sys.argv) != 2:
	print("Usage: %s <n>"%sys.argv[0])
else:
	print("Prevaram broj %s u heksadecimalni: %s"%(sys.argv[1], hex(int(sys.argv[1]))))
