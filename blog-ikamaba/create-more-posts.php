<?php
/**
 * Script otomatis buat artikel tambahan IKAMABA di WordPress
 * Jalankan sekali di browser: http://localhost/blog-ikamaba/create-more-posts.php
 * Hapus file ini setelah selesai.
 */

// Load WordPress
require_once __DIR__ . '/wp-load.php';
require_once ABSPATH . 'wp-admin/includes/taxonomy.php';

// ── Buat Kategori (Jika belum ada) ──
$categories = ['Budaya', 'Kuliner', 'Pariwisata'];
$cat_ids = [];

foreach ($categories as $cat_name) {
    $existing = get_cat_ID($cat_name);
    if ($existing) {
        $cat_ids[$cat_name] = $existing;
    } else {
        $cat_ids[$cat_name] = wp_create_category($cat_name);
    }
}

// ── Data Artikel Tambahan ──
$articles = [
    [
        'title' => 'Saur Matua: Puncak Penghormatan dalam Tradisi Kematian Batak',
        'category' => 'Budaya',
        'content' => '
<p>Dalam tradisi adat Batak Toba, kematian bukanlah sekadar akhir dari kehidupan, melainkan sebuah prosesi adat yang memiliki tingkatan tersendiri berdasarkan status sosial dan keturunan mendiang. Tingkatan tertinggi dan paling dihormati dalam upacara kematian ini dikenal sebagai <strong>Saur Matua</strong>.</p>

<h2>Apa itu Saur Matua?</h2>
<p>Seorang tetua adat Batak dikatakan meninggal dalam keadaan <em>Saur Matua</em> apabila ia meninggal pada usia lanjut, dan seluruh anak-anaknya (baik laki-laki maupun perempuan) telah menikah dan memiliki keturunan. Ini dianggap sebagai pencapaian hidup paling sempurna dan penuh berkah (<em>pasu-pasu</em>) dalam pandangan masyarakat Batak.</p>

<h2>Prosesi dan Makna</h2>
<p>Upacara Saur Matua dirayakan bukan dengan ratapan kesedihan semata, melainkan dengan rasa syukur dan sukacita karena mendiang telah menyelesaikan tugasnya di dunia dengan paripurna. Prosesi ini diiringi dengan tabuhan musik <strong>Gondang Sabangunan</strong>, tarian Tor-tor dari seluruh kerabat (Dalihan Na Tolu), serta pemotongan hewan kurban seperti kerbau (<em>sigagat duhut</em>).</p>
<p>Setiap keturunan akan memberikan penghormatan terakhir dengan menarikan Tor-tor mengelilingi jenazah, mengenakan ulos khusus, dan memberikan <em>tumpak</em> (sumbangan tanda kasih). Puncak acara ini menunjukkan betapa kuatnya ikatan kekerabatan dan penghormatan orang Batak terhadap orang tua dan leluhurnya.</p>
'
    ],
    [
        'title' => 'Andaliman: Merica Batak yang Menggetarkan Lidah Dunia',
        'category' => 'Kuliner',
        'content' => '
<p>Bicara tentang kuliner khas Batak tidak akan pernah lepas dari satu bumbu magis yang menjadi primadona: <strong>Andaliman</strong> (<em>Zanthoxylum acanthopodium</em>). Rempah ini sering dijuluki sebagai "Merica Batak" karena bentuknya yang menyerupai lada, namun memberikan sensasi rasa yang jauh berbeda dan tak tergantikan.</p>

<h2>Sensasi Rasa yang Unik</h2>
<p>Keistimewaan Andaliman terletak pada sensasi kebas, kelu, dan getir (<em>tingling sensation</em>) yang ditinggalkannya di lidah saat dikunyah, disusul dengan aroma jeruk nipis yang sangat segar. Sensasi ini berasal dari senyawa <em>hydroxy-alpha-sanshool</em> yang juga ditemukan pada <em>Sichuan pepper</em> di Tiongkok.</p>

<h2>Penggunaan dalam Masakan</h2>
<p>Andaliman adalah kunci kelezatan berbagai hidangan tradisional Batak. Tanpa Andaliman, sebuah masakan belum bisa disebut otentik Batak. Beberapa hidangan yang wajib menggunakan Andaliman antara lain:</p>
<ul>
<li><strong>Arsik:</strong> Ikan mas bumbu kuning yang dimasak perlahan hingga bumbunya meresap ke tulang.</li>
<li><strong>Saksang:</strong> Daging babi atau anjing (terkadang diganti daging sapi/kerbau) yang dimasak dengan bumbu darah atau rempah kaya.</li>
<li><strong>Naniura:</strong> "Sushi" ala Batak, ikan mentah yang dimatangkan menggunakan asam jungga dan andaliman tanpa dimasak di atas api.</li>
<li><strong>Mie Gomak:</strong> Spageti ala Toba yang disajikan dengan kuah santan dan bumbu andaliman yang kuat.</li>
</ul>
<p>Kini, Andaliman tidak hanya digunakan di dapur rumah tangga Batak, tetapi juga mulai dilirik oleh para chef internasional untuk dieksplorasi ke dalam berbagai hidangan <em>fusion</em>.</p>
'
    ],
    [
        'title' => 'Eksplorasi Kuliner Khas Batak: Lebih dari Sekadar Rasa',
        'category' => 'Kuliner',
        'content' => '
<p>Sumatera Utara, khususnya kawasan Danau Toba dan sekitarnya, bukan hanya kaya akan keindahan alam dan budaya, tetapi juga menyimpan harta karun kuliner yang menggugah selera. Kuliner Batak dikenal dengan bumbunya yang berani, kaya rempah, dan teknik memasak yang diwariskan turun-temurun.</p>

<h2>Hidangan Ikonik Batak</h2>
<p>Berikut adalah beberapa mahakarya kuliner Batak yang wajib Anda ketahui:</p>
<ol>
<li><strong>Ikan Mas Arsik:</strong> Simbol kehidupan dalam budaya Batak. Ikan mas dibumbui dengan kunyit, andaliman, bawang Batak (lokio), kincung (kecombrang), dan asam cikala. Hidangan ini wajib hadir dalam setiap upacara adat, mulai dari kelahiran, pernikahan, hingga kematian.</li>
<li><strong>Dengke Naniura:</strong> Sering disebut sebagai sashimi ala Batak. Ikan mas mentah yang dibersihkan, lalu direndam dengan perasan jeruk purut atau asam jungga hingga matang secara kimiawi, kemudian dilumuri bumbu andaliman dan kemiri gongseng.</li>
<li><strong>Mie Gomak:</strong> Disebut "Spageti Batak" karena menggunakan mi lidi yang tebal. Disajikan dengan kuah santan pedas atau digoreng, selalu dengan ciri khas aroma andaliman yang kuat. Nama "gomak" berasal dari cara penyajiannya di masa lalu yang digenggam (digomak) dengan tangan.</li>
<li><strong>Saksang:</strong> Cincangan daging (biasanya babi atau kerbau) yang dimasak dengan bumbu rempah lengkap dan seringkali menggunakan darah hewan tersebut (<em>margota</em>) sebagai pengental, memberikan warna gelap dan rasa gurih yang mendalam.</li>
</ol>
<p>Setiap gigitan kuliner Batak adalah representasi dari alam yang kaya dan tradisi yang tak lekang oleh waktu.</p>
'
    ],
    [
        'title' => 'Danau Toba: Mahakarya Vulkanik dan Pusat Spiritual Batak',
        'category' => 'Pariwisata',
        'content' => '
<p>Terletak di jantung Provinsi Sumatera Utara, <strong>Danau Toba</strong> bukan hanya danau terbesar di Indonesia dan danau vulkanik terbesar di dunia, melainkan juga pusat peradaban dan episentrum spiritual bagi masyarakat Batak.</p>

<h2>Sejarah Terciptanya Kaldera Raksasa</h2>
<p>Danau Toba terbentuk dari letusan supervulkanik sekitar 74.000 tahun yang lalu. Letusan ini begitu dahsyat hingga memengaruhi iklim global dan menyisakan kaldera raksasa yang perlahan terisi air, membentuk apa yang kita kenal sekarang sebagai Danau Toba. Di tengahnya, terangkatlah daratan yang kita sebut <strong>Pulau Samosir</strong>, sebuah pulau yang unik karena besarnya hampir menyerupai negara Singapura.</p>

<h2>Destinasi Wisata dan Budaya</h2>
<p>Kini, Danau Toba telah ditetapkan sebagai salah satu Destinasi Pariwisata Super Prioritas (DPSP) oleh pemerintah Indonesia. Beberapa daya tarik utamanya meliputi:</p>
<ul>
<li><strong>Desa Tomok dan Ambarita:</strong> Tempat Anda dapat menemukan peninggalan megalitik, seperti kursi batu persidangan Raja Siallagan dan makam Raja Sidabutar.</li>
<li><strong>Air Terjun Sipiso-piso:</strong> Berada di bibir kaldera bagian utara, menawarkan pemandangan spektakuler air jatuh dari ketinggian 120 meter dengan latar belakang Danau Toba.</li>
<li><strong>Tari Sigale-gale:</strong> Pertunjukan boneka kayu seukuran manusia yang dapat menari secara mistis, diiringi musik gondang, yang dulunya digunakan untuk menghibur raja yang berduka.</li>
</ul>
<p>Bagi orang Batak, Toba adalah "Bona Pasogit" (kampung halaman). Sebuah tempat yang selalu memanggil untuk pulang, memancarkan kedamaian, dan menceritakan kebesaran Sang Pencipta (<em>Mula Jadi Na Bolon</em>).</p>
'
    ],
    [
        'title' => 'Ulos: Untaian Doa dan Kasih Sayang dalam Selembar Kain',
        'category' => 'Budaya',
        'content' => '
<p>Dalam kebudayaan Batak, selembar kain bukan hanya berfungsi sebagai penutup tubuh. <strong>Ulos</strong> adalah simbol ikatan kasih sayang, berkat, pelindung, dan doa yang diwariskan dari generasi ke generasi.</p>

<h2>Makna Filosofis Ulos</h2>
<p>Filosofi orang Batak mengatakan: <em>"Ijuk pangihot ni hodong, Ulos pangihot ni holong"</em>, yang berarti seperti ijuk yang mengikat pelepah, begitulah Ulos mengikat kasih sayang antar sesama. Ulos diberikan oleh mereka yang memiliki kedudukan lebih tinggi dalam hierarki adat (Hula-hula) kepada mereka yang lebih rendah (Boru), sebagai bentuk penyaluran berkat.</p>

<h2>Jenis-jenis Ulos dan Fungsinya</h2>
<p>Ada puluhan jenis Ulos, masing-masing ditenun dengan motif khusus dan digunakan pada momen yang spesifik:</p>
<ul>
<li><strong>Ulos Ragidup:</strong> Ulos tertinggi nilainya, sering digunakan dalam upacara adat besar dan diberikan kepada orang tua dari pengantin. Melambangkan harapan akan kehidupan yang panjang dan sejahtera.</li>
<li><strong>Ulos Sadum:</strong> Berwarna cerah (merah) dan penuh motif manik-manik. Digunakan dalam suasana sukacita.</li>
<li><strong>Ulos Bintang Maratur:</strong> Diberikan kepada keluarga yang sedang bersukacita karena kelahiran anak pertama atau meresmikan rumah baru. Simbol keteraturan dan keberuntungan beruntun bagai bintang di langit.</li>
<li><strong>Ulos Tujung:</strong> Diberikan kepada seorang janda atau duda yang baru ditinggal mati oleh pasangannya, sebagai simbol perlindungan di masa berkabung.</li>
</ul>
<p>Ulos adalah seni tenun yang bukan sekadar kerajinan tangan, melainkan naskah yang mencatat peradaban dan spiritualitas orang Batak sejak ratusan tahun lalu.</p>
'
    ]
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
    <title>IKAMABA - Setup Artikel Tambahan</title>
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
        <h1>✅ 5 Artikel Tambahan Selesai!</h1>
        <div class="stat"><?= $created ?></div>
        <div class="label">Artikel baru berhasil dibuat</div>
        <?php if ($skipped > 0): ?>
            <p class="success"><?= $skipped ?> artikel sudah ada (dilewati)</p>
        <?php endif; ?>
        <p>Artikel ditambahkan:</p>
        <ul style="text-align: left; color: #555;">
            <li>Saur Matua (Budaya)</li>
            <li>Andaliman (Kuliner)</li>
            <li>Eksplorasi Kuliner Batak (Kuliner)</li>
            <li>Danau Toba (Pariwisata)</li>
            <li>Ulos (Budaya)</li>
        </ul>
        <br>
        <a href="<?= home_url('/') ?>" class="btn">🌐 Lihat Blog</a>
        <a href="<?= admin_url('edit.php') ?>" class="btn btn-outline">📝 Kelola Artikel</a>
        <p class="info">⚠️ Hapus file <code>create-more-posts.php</code> setelah selesai.</p>
    </div>
</body>
</html>
