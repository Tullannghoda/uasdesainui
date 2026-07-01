# IKAMABA Hub - Web Platform

Proyek tugas akhir mata kuliah UI/UX: Membangun platform digital untuk Ikatan Mahasiswa Batak (IKAMABA).

## 🚀 Fitur Utama
- **Landing Page & Profile**: Menampilkan informasi organisasi dan visi misi.
- **Katalog & Keranjang (Frontend-only)**: Simulasi e-commerce dengan DOM manipulation dan LocalStorage.
- **Mockup Back-Office (Admin)**: UI Panel Admin untuk mengelola data website.
- **Integrasi CMS WordPress**: Fitur Blog/Artikel dikelola langsung menggunakan CMS WordPress.

## 🛠️ Cara Menjalankan Proyek (Localhost)

Karena proyek ini menggunakan integrasi **WordPress CMS**, maka dibutuhkan web server lokal (seperti **Laragon** atau **XAMPP**) yang memiliki PHP dan MySQL.

### Langkah-langkah Setup (Bagi Dosen Penilai):
1. Pindahkan folder proyek ini (yang berisi halaman HTML statis) ke dalam folder `htdocs` (jika pakai XAMPP) atau `www` (jika pakai Laragon).
2. Proyek ini terhubung ke *instance* WordPress lokal dengan *path* `http://localhost/blog-ikamaba/`. 
3. Buka browser dan akses halaman utama statis:
   ```
   http://localhost/uas_ui/
   ```
4. Jika ingin mencoba fitur **Artikel**, pastikan *environment* WordPress sudah disiapkan di folder `blog-ikamaba` dengan *database* yang sesuai.

---
*Catatan untuk dosen penilai: File presentasi atau link video demo (jika ada) disarankan untuk dilihat guna melihat fungsionalitas WordPress secara penuh tanpa perlu mengatur database lokal secara manual.*
