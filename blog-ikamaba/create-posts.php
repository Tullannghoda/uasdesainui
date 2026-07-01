<?php
/**
 * Script otomatis buat artikel dummy IKAMABA di WordPress
 * Jalankan sekali di browser: http://localhost/blog-ikamaba/create-posts.php
 * Hapus file ini setelah selesai.
 */

// Load WordPress
require_once __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/taxonomy.php';

// ── Buat Kategori ──
$categories = ['Budaya', 'Event', 'Organisasi'];
$cat_ids = [];

foreach ($categories as $cat_name) {
    $existing = get_cat_ID($cat_name);
    if ($existing) {
        $cat_ids[$cat_name] = $existing;
    } else {
        $cat_ids[$cat_name] = wp_create_category($cat_name);
    }
}

// ── Data Artikel ──
$articles = [
    [
        'title' => 'Mengenal Budaya Batak: Warisan Leluhur yang Tetap Lestari',
        'category' => 'Budaya',
        'content' => '
<p>Budaya Batak merupakan salah satu kekayaan budaya Indonesia yang berasal dari Sumatera Utara. Dengan sejarah panjang dan tradisi yang kaya, masyarakat Batak memiliki keunikan tersendiri dalam adat istiadat, seni, dan kehidupan sosial.</p>

<h2>Elemen Penting Budaya Batak</h2>

<p>Beberapa elemen penting budaya Batak yang masih dilestarikan hingga saat ini meliputi:</p>

<ol>
<li><strong>Ulos</strong> — Kain tenun tradisional yang memiliki makna simbolis mendalam. Ulos diberikan dalam berbagai upacara adat sebagai simbol kasih sayang, doa, dan restu.</li>
<li><strong>Tor-Tor</strong> — Tarian tradisional yang biasa ditampilkan dalam upacara adat. Gerakan Tor-Tor memiliki makna spiritual dan sosial yang kuat.</li>
<li><strong>Gondang</strong> — Musik tradisional menggunakan instrumen khas Batak seperti taganing, gordang, dan sarune. Gondang mengiringi berbagai ritual adat.</li>
<li><strong>Dalihan Na Tolu</strong> — Sistem kekerabatan yang menjadi fondasi kehidupan sosial masyarakat Batak, terdiri dari Dongan Tubu, Hula-hula, dan Boru.</li>
</ol>

<h2>Peran IKAMABA dalam Pelestarian Budaya</h2>

<p>IKAMABA sebagai organisasi mahasiswa Batak berkomitmen untuk melestarikan dan memperkenalkan budaya Batak kepada generasi muda, khususnya di lingkungan kampus Universitas Airlangga. Melalui berbagai kegiatan seperti seminar budaya, pertunjukan seni, dan festival, IKAMABA berupaya menjadi jembatan antara tradisi dan modernitas.</p>

<p>Dengan semangat <em>"Horas!"</em>, IKAMABA terus menginspirasi generasi muda untuk bangga dengan identitas budayanya sambil tetap berkontribusi positif di dunia akademik dan masyarakat luas.</p>
'
    ],
    [
        'title' => 'BatakFest 2025: Festival Budaya Terbesar IKAMABA',
        'category' => 'Event',
        'content' => '
<p>IKAMABA dengan bangga mengumumkan <strong>BatakFest 2025</strong>, festival budaya tahunan terbesar yang diselenggarakan oleh Ikatan Mahasiswa Batak Universitas Airlangga. Acara ini akan berlangsung pada <strong>12-14 Desember 2025</strong> di Medan, Sumatera Utara.</p>

<h2>Rangkaian Acara</h2>

<p>BatakFest 2025 menghadirkan berbagai rangkaian acara menarik yang dirancang untuk memperkenalkan dan merayakan kekayaan budaya Batak:</p>

<ul>
<li>🎤 Seminar Budaya Batak bersama tokoh-tokoh adat dan akademisi</li>
<li>💃 Pertunjukan Tor-Tor dan Gondang Sabangunan</li>
<li>🧵 Pameran Ulos dan Kerajinan Tradisional dari berbagai daerah</li>
<li>🎵 Lomba Cipta Lagu Batak Modern</li>
<li>🍲 Bazaar Kuliner Khas Batak (Saksang, Arsik, Naniura, dll)</li>
<li>📸 Photo Booth dengan tema adat Batak</li>
</ul>

<h2>Informasi Tiket</h2>

<p>Tiket tersedia dalam 3 kategori:</p>
<ul>
<li><strong>Regular</strong> — Rp 75.000 (akses area umum)</li>
<li><strong>VIP</strong> — Rp 250.000 (akses area VIP + merchandise kit)</li>
<li><strong>VVIP</strong> — Rp 500.000 (akses semua area + meet & greet + merchandise exclusive)</li>
</ul>

<p>Dapatkan tiketmu sekarang melalui <strong>IKAMABA Hub</strong>! Jangan lewatkan kesempatan untuk merasakan kemegahan budaya Batak dalam satu festival spektakuler.</p>

<p><em>BatakFest 2025 — Merayakan Warisan, Menginspirasi Masa Depan.</em></p>
'
    ],
    [
        'title' => 'Rapat Kerja IKAMABA 2025: Menyusun Program Kerja Baru',
        'category' => 'Organisasi',
        'content' => '
<p>Pada tanggal <strong>15-16 Februari 2025</strong>, IKAMABA mengadakan Rapat Kerja (Raker) tahunan di Surabaya. Kegiatan ini dihadiri oleh seluruh pengurus inti dan koordinator divisi untuk menyusun program kerja periode 2025-2026.</p>

<h2>Agenda Raker</h2>

<p>Raker berlangsung selama dua hari penuh dengan agenda yang padat:</p>

<p><strong>Hari Pertama:</strong></p>
<ul>
<li>Evaluasi program kerja periode sebelumnya</li>
<li>Presentasi laporan keuangan organisasi</li>
<li>Diskusi kelompok per divisi</li>
</ul>

<p><strong>Hari Kedua:</strong></p>
<ul>
<li>Penyusunan program kerja baru</li>
<li>Penetapan timeline dan penanggung jawab</li>
<li>Pengesahan hasil raker</li>
</ul>

<h2>Program Kerja yang Disepakati</h2>

<p>Beberapa program kerja utama yang disepakati untuk periode 2025-2026:</p>

<ol>
<li><strong>Peluncuran Platform Digital IKAMABA Hub</strong> — Pengembangan website resmi sebagai pusat informasi dan layanan e-commerce organisasi</li>
<li><strong>Penyelenggaraan BatakFest 2025</strong> — Festival budaya tahunan terbesar IKAMABA</li>
<li><strong>Program Mentoring Akademik</strong> — Pendampingan untuk mahasiswa Batak baru di lingkungan kampus</li>
<li><strong>Kolaborasi Budaya Lintas Organisasi</strong> — Kerja sama dengan organisasi daerah lain untuk pertukaran budaya</li>
<li><strong>Pengembangan Merchandise IKAMABA</strong> — Produksi dan penjualan merch sebagai identitas dan sumber dana organisasi</li>
</ol>

<p>Raker berlangsung dengan penuh semangat dan kebersamaan. Seluruh peserta menunjukkan komitmen yang tinggi untuk membawa IKAMABA ke tingkat yang lebih baik di tahun mendatang. <strong>Horas!</strong> 🎉</p>
'
    ],
];

// ── Buat Artikel ──
$created = 0;
$skipped = 0;

foreach ($articles as $article) {
    // Cek apakah sudah ada
    $existing = get_page_by_title($article['title'], OBJECT, 'post');
    if ($existing) {
        $skipped++;
        continue;
    }

    $post_id = wp_insert_post([
        'post_title'    => $article['title'],
        'post_content'  => trim($article['content']),
        'post_status'   => 'publish',
        'post_author'   => 1,
        'post_category' => [$cat_ids[$article['category']]],
    ]);

    if ($post_id && !is_wp_error($post_id)) {
        $created++;
    }
}

// ── Output Hasil ──
?>
<!DOCTYPE html>
<html>
<head>
    <title>IKAMABA - Setup Artikel</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; max-width: 600px; margin: 60px auto; background: #f5f5f5; }
        .card { background: white; padding: 40px; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #722F37; }
        .stat { font-size: 48px; font-weight: bold; color: #722F37; }
        .label { color: #666; margin-bottom: 20px; }
        .btn { display: inline-block; background: #722F37; color: white; padding: 12px 32px; border-radius: 8px; text-decoration: none; margin: 8px; }
        .btn:hover { background: #5a252c; }
        .btn-outline { background: white; color: #722F37; border: 2px solid #722F37; }
        .success { color: #28a745; }
        .info { color: #666; font-size: 14px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <h1>✅ Setup Selesai!</h1>
        <div class="stat"><?= $created ?></div>
        <div class="label">Artikel berhasil dibuat</div>
        <?php if ($skipped > 0): ?>
            <p class="success"><?= $skipped ?> artikel sudah ada (dilewati)</p>
        <?php endif; ?>
        <p>Kategori: <strong>Budaya, Event, Organisasi</strong></p>
        <br>
        <a href="<?= home_url('/') ?>" class="btn">🌐 Lihat Blog</a>
        <a href="<?= admin_url('edit.php') ?>" class="btn btn-outline">📝 Kelola Artikel</a>
        <p class="info">⚠️ Hapus file <code>create-posts.php</code> setelah selesai.</p>
    </div>
</body>
</html>
