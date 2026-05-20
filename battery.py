# Ishga tushirishdan oldin terminalda: pip install psutil
import psutil

battery = psutil.sensors_battery()
foiz = battery.percent
ulangan = battery.power_plugged

print("🔋 Noutbuk Batareya Holati:")
print("-" * 35)
print(f"📍 Hozirgi zaryad miqdori: {foiz}%")

if ulangan:
    print("⚡ Holati: Quvvat olmoqda (Tokka ulangan).")
else:
    print("🔋 Holati: Batareyadan ishlamoqda (Tokka ulanmagan).")
print("-" * 35)

if foiz <= 20 and not ulangan:
    print("⚠️ OGOHLANTIRISH: Zaryad kam qoldi! Noutbukni tokka ulang!")