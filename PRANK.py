#SCREWUP
import time
import rotatescreen as screwup
screwup = screwup.get_primary_display()
for i in range(10):
    time.sleep(1)
    screwup.rotate_to(i*90 % 360)