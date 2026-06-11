import re

filepath = "c:\\laragon\\www\\uas_ui\\event.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Title and Navbar links
content = content.replace("<title>IKAMABA</title>", "<title>Arsip Event — IKAMABA Hub</title>")
content = content.replace('href="#beranda" class="nav-link active"', 'href="index.html" class="nav-link"')
content = content.replace('href="#tentang" class="nav-link"', 'href="index.html#tentang" class="nav-link"')
content = content.replace('href="#event" class="nav-link"', 'href="#" class="nav-link active"')
# Also fix mobile menu links
content = content.replace('<a href="#beranda" class="nav-link active">', '<a href="index.html" class="nav-link">')
content = content.replace('<a href="#tentang" class="nav-link">', '<a href="index.html#tentang" class="nav-link">')
content = content.replace('<a href="#event" class="nav-link">', '<a href="#" class="nav-link active">')

# 2. Extract Header and Footer boundaries
# Replace everything between </nav> (or mobile menu) and <footer class="footer"> with our custom Event section.
main_content = """
  <!-- ========== Page Header ========== -->
  <section class="section" style="padding-top: 120px; padding-bottom: var(--space-8); background: linear-gradient(135deg, var(--gray-50) 0%, var(--gray-100) 100%); text-align: center;">
    <div class="container reveal">
      <h1 class="section-title">Arsip Event IKAMABA</h1>
      <p class="section-subtitle" style="margin: 0 auto;">Kumpulan dokumentasi dan informasi berbagai kegiatan serta program kerja IKAMABA dari masa ke masa.</p>
    </div>
  </section>

  <!-- ========== Event Grid ========== -->
  <section class="section" style="padding-top: var(--space-4);">
    <div class="container">
      <div class="event-grid">
        
        <!-- Event 1 -->
        <div class="event-card reveal" style="transition-delay: 100ms;">
          <div class="event-img">
            <img src="assets/img/event1.jpg" alt="Welcoming Party 2026">
            <div class="event-badge">Selesai</div>
          </div>
          <div class="event-content">
            <div class="event-meta">
              <span>📅 15 Sep 2026</span>
              <span>📍 Aula Utama</span>
            </div>
            <h3 class="event-title">Welcoming Party Mahasiswa Baru 2026</h3>
            <p class="event-desc">Penyambutan mahasiswa baru Batak yang merantau. Acara penuh keakraban dan pengenalan budaya.</p>
            <a href="#" class="btn btn-ghost" style="padding-left: 0; padding-right: 0; display: inline-flex; align-items: center; gap: 8px;">
              Lihat Detail <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <!-- Event 2 -->
        <div class="event-card reveal" style="transition-delay: 200ms;">
          <div class="event-img">
            <img src="assets/img/event2.jpg" alt="Makrab & LDK">
            <div class="event-badge badge-warning" style="background: var(--warning); color: white;">Akan Datang</div>
          </div>
          <div class="event-content">
            <div class="event-meta">
              <span>📅 28-30 Okt 2026</span>
              <span>📍 Villa Puncak</span>
            </div>
            <h3 class="event-title">Malam Keakraban & LDK IKAMABA</h3>
            <p class="event-desc">Membentuk jiwa kepemimpinan dan rasa persaudaraan yang kuat antar sesama anggota IKAMABA.</p>
            <a href="#" class="btn btn-ghost" style="padding-left: 0; padding-right: 0; display: inline-flex; align-items: center; gap: 8px;">
              Lihat Detail <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <!-- Event 3 -->
        <div class="event-card reveal" style="transition-delay: 300ms;">
          <div class="event-img">
            <img src="assets/img/event3.jpg" alt="Batakfest">
            <div class="event-badge badge-info" style="background: var(--info); color: white;">Pendaftaran Buka</div>
          </div>
          <div class="event-content">
            <div class="event-meta">
              <span>📅 15 Nov 2026</span>
              <span>📍 Gedung Serbaguna</span>
            </div>
            <h3 class="event-title">Festival Budaya Batak (Batakfest)</h3>
            <p class="event-desc">Pameran seni, tari Tortor massal, dan bazar makanan khas Batak terbesar tahun ini.</p>
            <a href="#" class="btn btn-ghost" style="padding-left: 0; padding-right: 0; display: inline-flex; align-items: center; gap: 8px;">
              Lihat Detail <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

        <!-- Event 4 -->
        <div class="event-card reveal" style="transition-delay: 400ms;">
          <div class="event-img">
            <img src="assets/img/placeholder.jpg" alt="Bakti Sosial" style="width: 100%; height: 100%; object-fit: cover;">
            <div class="event-badge">Selesai</div>
          </div>
          <div class="event-content">
            <div class="event-meta">
              <span>📅 10 Ags 2026</span>
              <span>📍 Panti Asuhan</span>
            </div>
            <h3 class="event-title">Bakti Sosial IKAMABA</h3>
            <p class="event-desc">Kegiatan sosial penggalangan dana dan pembagian sembako untuk panti asuhan sekitar.</p>
            <a href="#" class="btn btn-ghost" style="padding-left: 0; padding-right: 0; display: inline-flex; align-items: center; gap: 8px;">
              Lihat Detail <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>
"""

# Regex to replace everything from the end of <div class="mobile-menu" ...></div> down to <footer class="footer">
content = re.sub(r'(<div class="mobile-menu"[^>]*>.*?</div>).*?(<footer class="footer">)', r'\1\n\n' + main_content + r'\n\n\2', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
