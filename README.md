# IKAMABA Hub - Web Platform

Proyek tugas akhir mata kuliah UI/UX: Membangun platform digital untuk Ikatan Mahasiswa Batak (IKAMABA).

## 🚀 Fitur Utama
- **Landing Page & Profile**: Menampilkan informasi organisasi dan visi misi.
- **Katalog & Keranjang (Frontend-only)**: Simulasi e-commerce dengan DOM manipulation dan LocalStorage.
- **Mockup Back-Office (Admin)**: UI Panel Admin untuk mengelola data website.
- **Integrasi CMS WordPress**: Fitur Blog/Artikel dikelola langsung menggunakan CMS WordPress.

## 🛠️ Cara Menjalankan Proyek

Karena proyek ini menggunakan integrasi **WordPress CMS**, maka dibutuhkan web server lokal (seperti **Laragon** atau **XAMPP**) yang memiliki PHP dan MySQL.

### Langkah-langkah Setup:
1. Pindahkan folder proyek ini (yang berisi halaman HTML statis) ke dalam folder `htdocs` (jika pakai XAMPP) atau `www` (jika pakai Laragon).
2. Proyek ini terhubung ke *instance* WordPress lokal dengan *path* `http://localhost/blog-ikamaba/`. 
3. Buat database baru di MySQL (cth via phpMyAdmin) dengan nama `blog_ikamaba`.
4. Import file `database_blog_ikamaba.sql` yang ada di folder utama proyek ini ke dalam database yang baru dibuat tersebut.
5. Buka browser dan akses halaman utama statis:
   ```
   http://localhost/uas_ui/
   ```
6. Menu Artikel dan Kelola Artikel di panel Admin akan otomatis terhubung ke WordPress lokal.

---
*Catatan untuk dosen penilai: File presentasi atau link video demo (jika ada) disarankan untuk dilihat guna melihat fungsionalitas web secara penuh jika tidak ingin mengatur database lokal secara manual.*
