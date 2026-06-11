import re

filepath = "c:\\laragon\\www\\uas_ui\\admin\\kelola-transaksi.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace tbody
new_tbody = """
            <tbody id="transaksiTableBody">
              <!-- Transaksi 1 -->
              <tr>
                <td><strong>#TRX-1001</strong></td>
                <td>Budi Santoso</td>
                <td>1x Hoodie, 1x Lanyard</td>
                <td>Rp 285.000</td>
                <td>12 Jun 2026</td>
                <td><span class="badge badge-warning">Menunggu</span></td>
                <td>
                  <div style="display: flex; gap: var(--space-2);">
                    <button class="btn btn-ghost btn-sm" onclick="openEditStatusModal('#TRX-1001', 'Menunggu')" style="padding: var(--space-2); color: var(--info);" title="Edit Status">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    </button>
                    <button class="btn btn-ghost btn-sm" onclick="openDetailModal('#TRX-1001', 'Budi Santoso', 'budi@example.com', 'Jl. Merdeka No. 1, Jakarta', '1x Hoodie IKAMABA, 1x Lanyard IKAMABA', 'Rp 285.000', 'Menunggu')" style="padding: var(--space-2); color: var(--primary);" title="Lihat Detail">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    </button>
                  </div>
                </td>
              </tr>
              <!-- Transaksi 2 -->
              <tr>
                <td><strong>#TRX-1002</strong></td>
                <td>Siti Aminah</td>
                <td>2x Kaos Polo</td>
                <td>Rp 240.000</td>
                <td>11 Jun 2026</td>
                <td><span class="badge badge-info">Dibayar</span></td>
                <td>
                  <div style="display: flex; gap: var(--space-2);">
                    <button class="btn btn-ghost btn-sm" onclick="openEditStatusModal('#TRX-1002', 'Dibayar')" style="padding: var(--space-2); color: var(--info);" title="Edit Status">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    </button>
                    <button class="btn btn-ghost btn-sm" onclick="openDetailModal('#TRX-1002', 'Siti Aminah', 'siti@example.com', 'Jl. Sudirman No. 2, Bandung', '2x Kaos Polo IKAMABA', 'Rp 240.000', 'Dibayar')" style="padding: var(--space-2); color: var(--primary);" title="Lihat Detail">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    </button>
                  </div>
                </td>
              </tr>
              <!-- Transaksi 3 -->
              <tr>
                <td><strong>#TRX-1003</strong></td>
                <td>Andi Wijaya</td>
                <td>1x Totebag</td>
                <td>Rp 85.000</td>
                <td>10 Jun 2026</td>
                <td><span class="badge badge-success">Selesai</span></td>
                <td>
                  <div style="display: flex; gap: var(--space-2);">
                    <button class="btn btn-ghost btn-sm" onclick="openEditStatusModal('#TRX-1003', 'Selesai')" style="padding: var(--space-2); color: var(--info);" title="Edit Status">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    </button>
                    <button class="btn btn-ghost btn-sm" onclick="openDetailModal('#TRX-1003', 'Andi Wijaya', 'andi@example.com', 'Jl. Thamrin No. 3, Surabaya', '1x Totebag IKAMABA', 'Rp 85.000', 'Selesai')" style="padding: var(--space-2); color: var(--primary);" title="Lihat Detail">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    </button>
                  </div>
                </td>
              </tr>
              <!-- Transaksi 4 -->
              <tr>
                <td><strong>#TRX-1004</strong></td>
                <td>Rina Kartika</td>
                <td>1x Hoodie, 2x Kaos Polo</td>
                <td>Rp 490.000</td>
                <td>09 Jun 2026</td>
                <td><span class="badge badge-danger">Dibatalkan</span></td>
                <td>
                  <div style="display: flex; gap: var(--space-2);">
                    <button class="btn btn-ghost btn-sm" onclick="openEditStatusModal('#TRX-1004', 'Dibatalkan')" style="padding: var(--space-2); color: var(--info);" title="Edit Status">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    </button>
                    <button class="btn btn-ghost btn-sm" onclick="openDetailModal('#TRX-1004', 'Rina Kartika', 'rina@example.com', 'Jl. Gatot Subroto No. 4, Medan', '1x Hoodie IKAMABA, 2x Kaos Polo IKAMABA', 'Rp 490.000', 'Dibatalkan')" style="padding: var(--space-2); color: var(--primary);" title="Lihat Detail">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    </button>
                  </div>
                </td>
              </tr>
              <!-- Transaksi 5 -->
              <tr>
                <td><strong>#TRX-1005</strong></td>
                <td>Reza Pahlevi</td>
                <td>3x Lanyard</td>
                <td>Rp 105.000</td>
                <td>08 Jun 2026</td>
                <td><span class="badge badge-success">Selesai</span></td>
                <td>
                  <div style="display: flex; gap: var(--space-2);">
                    <button class="btn btn-ghost btn-sm" onclick="openEditStatusModal('#TRX-1005', 'Selesai')" style="padding: var(--space-2); color: var(--info);" title="Edit Status">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                    </button>
                    <button class="btn btn-ghost btn-sm" onclick="openDetailModal('#TRX-1005', 'Reza Pahlevi', 'reza@example.com', 'Jl. Asia Afrika No. 5, Makassar', '3x Lanyard IKAMABA', 'Rp 105.000', 'Selesai')" style="padding: var(--space-2); color: var(--primary);" title="Lihat Detail">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>"""
content = re.sub(r'<tbody id="transaksiTableBody">.*?</tbody>', new_tbody, content, flags=re.DOTALL)

# 2. Replace modals
new_modals = """
  <!-- ========== Modal Detail Transaksi ========== -->
  <div id="modalTransaksi" class="modal-overlay">
    <div class="modal-content" style="background: white; width: 100%; max-width: 600px; border-radius: var(--radius-lg); padding: var(--space-6); position: relative; max-height: 90vh; overflow-y: auto;">
      <button onclick="closeModal('modalTransaksi')" style="position: absolute; top: var(--space-4); right: var(--space-4); background: none; border: none; cursor: pointer; color: var(--gray-500);">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      
      <h2 id="modalTransaksiTitle" style="font-size: var(--text-xl); margin-bottom: var(--space-6);">Detail Transaksi</h2>
      
      <div>
        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Order ID</label>
          <input type="text" id="detOrderId" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
        </div>
        
        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Nama Pelanggan</label>
          <input type="text" id="detName" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
        </div>
        
        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Email</label>
          <input type="text" id="detEmail" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
        </div>

        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Alamat</label>
          <textarea id="detAddress" class="form-input" rows="2" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled></textarea>
        </div>

        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Produk yang Dipesan</label>
          <textarea id="detItems" class="form-input" rows="2" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled></textarea>
        </div>

        <div style="display: flex; gap: var(--space-4); margin-bottom: var(--space-6);">
          <div class="form-group" style="flex: 1;">
            <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Total Harga</label>
            <input type="text" id="detTotal" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
          </div>
          <div class="form-group" style="flex: 1;">
            <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Status</label>
            <input type="text" id="detStatus" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
          </div>
        </div>

        <div style="display: flex; justify-content: flex-end;">
          <button type="button" class="btn btn-primary" onclick="closeModal('modalTransaksi')">Tutup</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ========== Modal Edit Status ========== -->
  <div id="modalEditStatus" class="modal-overlay">
    <div class="modal-content" style="background: white; width: 100%; max-width: 400px; border-radius: var(--radius-lg); padding: var(--space-6); position: relative;">
      <button onclick="closeModal('modalEditStatus')" style="position: absolute; top: var(--space-4); right: var(--space-4); background: none; border: none; cursor: pointer; color: var(--gray-500);">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
      
      <h2 style="font-size: var(--text-xl); margin-bottom: var(--space-6);">Edit Status Transaksi</h2>
      
      <div>
        <div class="form-group" style="margin-bottom: var(--space-4);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Order ID</label>
          <input type="text" id="editOrderId" class="form-input" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: var(--gray-100);" disabled>
        </div>
        
        <div class="form-group" style="margin-bottom: var(--space-6);">
          <label class="form-label" style="display: block; margin-bottom: var(--space-2); font-weight: 500;">Status</label>
          <select id="editStatus" class="form-select" style="width: 100%; padding: var(--space-3); border: 1px solid var(--gray-300); border-radius: var(--radius-md); background: white;">
            <option value="Menunggu">Menunggu</option>
            <option value="Dibayar">Dibayar</option>
            <option value="Selesai">Selesai</option>
            <option value="Dibatalkan">Dibatalkan</option>
          </select>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: var(--space-3);">
          <button type="button" class="btn btn-ghost" onclick="closeModal('modalEditStatus')">Batal</button>
          <button type="button" class="btn btn-primary" onclick="saveStatus()">Simpan Perubahan</button>
        </div>
      </div>
    </div>
  </div>"""
content = re.sub(r'<!-- ========== Modal Detail Transaksi ========== -->.*?</div>\s*</div>\s*</div>', new_modals, content, flags=re.DOTALL)

# 3. Add openEditStatusModal to JS
new_js = """    window.openDetailModal = function(orderId, name, email, address, items, total, status) {
      try {
        document.getElementById('detOrderId').value = orderId || '';
        document.getElementById('detName').value = name || '';
        document.getElementById('detEmail').value = email || '';
        document.getElementById('detAddress').value = address || '';
        document.getElementById('detItems').value = items || '';
        document.getElementById('detTotal').value = total || '';
        document.getElementById('detStatus').value = status || '';
        
        const modal = document.getElementById('modalTransaksi');
        if(modal) {
          modal.classList.add('active');
          document.body.style.overflow = 'hidden';
        }
      } catch (e) {
        alert("Error Detail: " + e.message);
      }
    };

    window.openEditStatusModal = function(orderId, status) {
      try {
        document.getElementById('editOrderId').value = orderId || '';
        document.getElementById('editStatus').value = status || 'Menunggu';
        
        const modal = document.getElementById('modalEditStatus');
        if(modal) {
          modal.classList.add('active');
          document.body.style.overflow = 'hidden';
        }
      } catch (e) {
        alert("Error Edit: " + e.message);
      }
    };

    window.saveStatus = function() {
      closeModal('modalEditStatus');
      if (typeof showToast === 'function') {
        showToast('Status pesanan berhasil diperbarui!', 'success');
      } else {
        alert('Status pesanan berhasil diperbarui!');
      }
    };"""
content = re.sub(r'window\.openDetailModal = function\(.*?\};', new_js, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
