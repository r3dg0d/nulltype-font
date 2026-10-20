// Playground: every control drives real font rendering (variable or static WOFF2).
(function () {
  const $ = (id) => document.getElementById(id);
  const stage = $("stage");
  const fam = window.FAMILY;
  const defaults = {};
  ["size", "weight", "track", "lh", "align", "fg", "bg", "engine"].forEach((k) => (defaults[k] = $(k).value));
  function feats() {
    return Array.from(document.querySelectorAll("[data-feat]"))
      .map((c) => `"${c.dataset.feat}" ${c.checked ? 1 : 0}`).join(", ");
  }
  function apply() {
    const eng = $("engine").value;
    let w = parseInt($("weight").value, 10);
    if (eng === "Static") w = Math.min(900, Math.max(100, Math.round(w / 100) * 100));
    const s = stage.style;
    s.fontFamily = `"${fam} ${eng}", monospace`;
    s.fontWeight = w;
    s.fontStyle = $("italic").checked ? "italic" : "normal";
    s.fontSize = $("size").value + "px";
    s.letterSpacing = $("track").value + "em";
    s.lineHeight = $("lh").value;
    s.textAlign = $("align").value;
    s.color = $("fg").value;
    s.background = $("bg").value;
    s.fontFeatureSettings = feats();
    $("sizeo").textContent = $("size").value + "px";
    $("weighto").textContent = w;
    $("tracko").textContent = $("track").value + "em";
    $("lho").textContent = $("lh").value;
    $("cssout").textContent = `font-family:"${fam}"; font-weight:${w}; font-style:${s.fontStyle}; font-size:${s.fontSize}; letter-spacing:${s.letterSpacing}; line-height:${s.lineHeight}; font-feature-settings:${s.fontFeatureSettings};`;
    stage.classList.toggle("multi", $("waterfall").checked || $("compare").checked);
    if ($("waterfall").checked || $("compare").checked) render(w);
  }
  let source = stage.textContent;
  stage.addEventListener("input", () => { if (!stage.classList.contains("multi")) source = stage.innerText; });
  function render(w) {
    stage.innerHTML = "";
    const lines = $("compare").checked ? [100, 200, 300, 400, 500, 600, 700, 800, 900].map((x) => [x, null])
      : [12, 16, 24, 32, 48, 64, 96].map((x) => [w, x]);
    lines.forEach(([wt, sz]) => {
      const d = document.createElement("div");
      d.textContent = source;
      d.style.fontWeight = wt;
      if (sz) d.style.fontSize = sz + "px";
      stage.appendChild(d);
    });
  }
  function unmulti() { if (!$("waterfall").checked && !$("compare").checked) stage.textContent = source; }
  document.querySelectorAll(".controls input, .controls select, [data-feat]").forEach((el) =>
    el.addEventListener("input", () => { unmulti(); apply(); }));
  $("preset").addEventListener("change", () => { source = $("preset").value; stage.textContent = source; apply(); });
  $("reset").addEventListener("click", () => {
    Object.entries(defaults).forEach(([k, v]) => ($(k).value = v));
    $("italic").checked = $("waterfall").checked = $("compare").checked = false;
    unmulti(); apply();
  });
  document.querySelectorAll(".g").forEach((b) => b.addEventListener("click", () => {
    $("big").textContent = b.textContent;
    $("meta").textContent = `${b.dataset.cp}  ·  ${b.textContent}`;
  }));
  apply();
})();
