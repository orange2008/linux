#!/usr/bin/python3
import os
print("Now compiling the kernel.")
os.system("nproc > cpus")
with open("cpus") as f:
    cpus = f.read()

try:
    with open(".config") as f:
        config = f.read()
    config = config.replace('CONFIG_SYSTEM_TRUSTED_KEYS="debian/canonical-certs.pem"', 'CONFIG_SYSTEM_TRUSTED_KEYS=""')
    config = config.replace('CONFIG_SYSTEM_REVOCATION_KEYS="debian/canolical-revoked-certs.pem"', 'CONFIG_SYSTEM_REVOCATION_KEYS=""')
    with open(".config", 'w') as f:
        f.write(config)
except:
    print("Please change the .config by yourself")
    pause = input("Press any key to continue...")

os.system("make-kpkg --initrd kernel_image kernel-headers -j " + str(cpus))
print("\n\n\n\n\n")
print("Done.")
pause = input("Press any key to continue...")
