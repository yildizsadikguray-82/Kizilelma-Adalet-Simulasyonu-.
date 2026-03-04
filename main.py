import time
import random
import sys

def yazi_yaz(metin, gecikme=0.03):
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def baris_haritasi_ciz():
    print("\n" + "🌐" + "═"*58)
    print("           DİJİTAL BARIŞ VE TÜRK HAKİMİYET HARİTASI")
    print("═"*60)
    # Sembolik dunya haritasi uzerinde Turk sancagi noktalari
    harita = [
        "       . _..---.._ .           [AVRUPA: TÜRK ADALETİNE TABİ]",
        "     .'     * '.         ",
        "    /   ( AL BAYRAK )  \       [ASYA: TURAN BİRLİĞİ KURULDU]",
        "   |    * GÜVENCESİ * |      ",
        "   \        * /       [AFRİKA: SÖMÜRGE BİTTİ, HUZUR GELDİ]",
        "    '.             .'         ",
        "       '--..___..--'           [OKYANUSLAR: MAVİ VATAN KONTROLÜNDE]"
    ]
    for satir in harita:
        print(satir)
        time.sleep(0.2)

def dunya_nizami_simulasyonu():
    # --- GİRİŞ VE TÜRK ORDUSU VURGUSU ---
    print("\n" + "🇹🇷 " + "═"*57)
    yazi_yaz(">>> KIZILELMA KÜRESEL ADALET SİSTEMİ DEVREYE GİRDİ...")
    yazi_yaz(">>> Türk Askerinin caydırıcı gücüyle küresel çatışmalar durduruldu.")
    yazi_yaz(">>> Türk Milletinin hakkaniyetiyle yeni bir dünya nizamı kuruluyor.")
    time.sleep(1)

    # --- ŞEHİRLER VE HUZUR ---
    print("\n" + "🏙️  KADİM ŞEHİRLERDE SON DURUM:")
    sehirler = {
        "İstanbul": "Cihanın Kalbi, Huzurun Merkezi",
        "Kudüs": "Mehmetçiğin Nöbetinde Selamet",
        "Semerkant": "İlim ve Türk Medeniyeti",
        "Gazze": "Yeniden İnşa, Tam Güvenlik",
        "Doğu Türkistan": "Zulüm Bitti, Al Bayrak Dalgalanıyor"
    }
    for sehir, durum in sehirler.items():
        skor = random.randint(99, 100)
        print(f"  [+] {sehir.ljust(15)} | {durum.ljust(35)} | Güven: %{skor}")
        time.sleep(0.4)

    # --- KÜRESEL REFAH MODÜLÜ ---
    print("\n" + "💰 KÜRESEL REFAH VE HAKKANİYET DAĞITIMI:")
    yazi_yaz("[!] Savaş bütçeleri iptal edildi; kaynaklar mazlumlara aktarılıyor.")
    yazi_yaz("[!] Türk Kızılayı ve AFAD koordinasyonunda açlık dünya üzerinden silindi.")

    # --- HARİTA VE FERMAN ---
    baris_haritasi_ciz()

    print("\n" + "📜" + "═"*58)
    yazi_yaz("FERMAN: 'Yaratılanı severiz Yaradan'dan ötürü.'")
    yazi_yaz("HÜKÜM : 'Zalim için yaşasın cehennem, mazlum için yaşasın TÜRKİYE!'")
    yazi_yaz("SON SÖZ: 'İnsanı yaşat ki devlet yaşasın!'")
    print("═"*60)

    # --- GELECEK ADIMLAR ---
    print("\n" + "🚀 [GELECEK VİZYON]:")
    print("- Uzayda Türk hakimiyeti ve Ay üzerinde ilk Adalet Üssü.")
    print("- Tam yapay zeka destekli 'Hızır' Diplomasi Motoru.")
    
    input("\n[!] Nizam-ı Alem sağlandı. Çıkmak için Enter'a basın...")

if __name__ == "__main__":
    dunya_nizami_simulasyonu()
  
