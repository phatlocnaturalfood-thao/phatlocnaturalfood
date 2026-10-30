// Form báo giá quà Tết doanh nghiệp: gửi cùng địa chỉ nhận đơn, vào Pancake như một đơn chờ báo giá.
document.getElementById("b2b-form").addEventListener("submit", async e => {
  e.preventDefault();
  const v = id => document.getElementById(id).value.trim();
  const ok = v("b-company") && v("b-name") && v("b-phone");
  document.getElementById("b-err").hidden = !!ok;
  if (!ok) return;
  const msg = document.getElementById("b-ok"), btn = document.getElementById("b-btn");
  btn.disabled = true; msg.hidden = false; msg.textContent = "Đang gửi...";
  const note = `BÁO GIÁ QUÀ TẾT DOANH NGHIỆP\nCông ty: ${v("b-company")}\nSố lượng: ${v("b-qty")} hộp\nNgân sách/hộp: ${v("b-budget")}\nNgày nhận: ${v("b-date") || "chưa chọn"}\nYêu cầu: ${v("b-note") || "không"}`;
  try {
    await fetch(ORDER_ENDPOINT, { method: "POST", mode: "no-cors", body: new URLSearchParams({
      name: v("b-name") + " - " + v("b-company"), phone: v("b-phone"), addr: v("b-company") + " (báo giá doanh nghiệp, chưa có địa chỉ giao)",
      product: "Báo giá quà Tết doanh nghiệp", spec: v("b-budget"), qty: v("b-qty") || "1", total: 0, note, website: v("b-web") }) });
    try { fbq("track", "Lead", { content_name: "Báo giá quà Tết doanh nghiệp" }); } catch {}
    try { gtag("event", "generate_lead", { form: "bao_gia_doanh_nghiep", quantity: +v("b-qty") || 0 }); } catch {}
    msg.textContent = "Đã nhận yêu cầu. Phát Lộc sẽ gọi lại báo giá trong ngày làm việc.";
    e.target.reset();
  } catch { msg.textContent = "Chưa gửi được. Anh/chị vui lòng nhắn Zalo 0768 759 419."; }
  btn.disabled = false;
});
