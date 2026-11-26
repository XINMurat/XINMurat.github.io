---
layout: default
title: "Case study — mapping a 175,187-file Lean proof"
description: "A worked run of Röntgen on the Lean 4 source of Levent Alpöge's claimed proof of the Riemann Hypothesis: four scans, three bugs found in the tool by its own numbers and a fourth in its drawing, two wrong guesses reversed on the record, and a map handed to a research project."
lang: en
---

<!--
  Two panes, one content model — same rule as index.md and case-study.md.
  Every section exists in BOTH languages with the same depth.

  SOURCE NOTE: everything below happened in one session on 2026-11-26. The
  numbers are the tool's own output from each run. Where a guess was wrong, the
  wrong guess is printed next to what replaced it.

  SCOPE NOTE: this page is about the tool, not about the proof. It makes no
  claim that the proof is correct or incorrect.
-->

<div id="pane-en" lang="en">

<section class="hero">
  <div class="wrap">
    <h1>Mapping a proof nobody can read whole</h1>
    <p class="lede">On 20 November 2026 Levent Alpöge released a claimed proof of
    the Riemann Hypothesis as Lean 4 code only: 175,187 files, about 17.5 million
    lines, no paper in prose. Röntgen had no Lean support that morning. This page
    is what happened when it was added and pointed at the release — four scans,
    each one exposing a bug in the tool through its own numbers.</p>
    <p class="canon">Session date 2026-11-26 · Röntgen at <code>3ddff39</code> ·
    source: the <code>tamnd/riemann-lean</code> mirror at <code>54f24d4</code> ·
    this page does not assess the proof.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Why Röntgen, and what it cannot do here</h2>
    <p>Lean decides whether a proof is correct; a text scanner cannot. But a
    full build of this release was estimated at 350 to 2,300 worker-hours, and
    nobody had run it. Until then, the only tools that work at this scale are
    ones that read text. Röntgen's job was the map: which module rests on which,
    what each file declares, and where the kernel is asked to take something on
    faith.</p>
    <p>Lean support was written for this run: <code>import</code> resolution
    through the lakefile's source roots, a declaration outline nested by
    namespace, and a trust inventory of <code>sorry</code>, <code>admit</code>,
    <code>axiom</code>, <code>opaque</code>, <code>unsafe</code>,
    <code>native_decide</code>, <code>implemented_by</code> and
    <code>extern</code>, with nested comments stripped.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Four scans</h2>
    <p class="sub">Each row is a complete run. Each run's numbers pointed at the next bug.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Run</th><th>Files read</th><th>Unresolved imports</th><th>What the numbers exposed</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>166,426</td><td>15,069</td>
          <td>5,518 files reported <em>unreadable</em>. The longest path is 244 characters; with the clone directory in front, Python's <code>open</code> passed the Windows 260-character limit and failed. Every sampled unresolved import pointed into an unreadable file.</td></tr>
          <tr><td>2</td><td>171,939</td><td>3,448</td>
          <td>Reads fixed with the <code>\\?\</code> prefix (<code>ortak.uzun_yol</code>). About 3,200 files were still missing: the directory walk skipped long directories <em>silently</em> — no error, no entry in the exclusion list.</td></tr>
          <tr><td>3</td><td>175,052</td><td>170</td>
          <td>Walk fixed. 135 files were now excluded as "looks generated (very long lines)". A Lean proof term can run 5,000 characters on one line; the heuristic was written for minified JavaScript. All 170 unresolved imports pointed into those 135 files.</td></tr>
          <tr><td>4</td><td><strong>175,187</strong></td><td><strong>0</strong></td>
          <td>Heuristic exempts <code>.lean</code>. Every file read, every import resolved, nothing excluded. About 17.5 minutes per run.</td></tr>
        </tbody>
      </table>
    </div>
    <p>The point is the shape, not the bugs. No run reported success it had not
    earned: each one printed a nonzero count of what it could not see, and each
    count was traceable to one cause. A tool that had reported "175,187 files,
    done" on run 1 would have been wrong by five thousand files and nobody would
    have known.</p>
    <p>A fifth bug was in the drawing, not the reading. The block diagram's
    layering pushed every member of a cycle down to its cap, so the 99-directory
    cycle put thirteen boxes in one row under an empty page, with labels cut
    mid-word. The layout now breaks cycles before it layers, wraps wide rows,
    and shortens a name by dropping its parent, never by cutting a word. It was
    found because the person reading said the diagram did not show.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>What the map shows</h2>
    <ul class="plain">
      <li><strong>753,569</strong> file-to-file imports resolved <code>[K]</code>; 156,253 more go to Mathlib and are counted, not drawn.</li>
      <li><strong>Every module is in the import cone of <code>Main</code></strong>, the longest chain 43 steps. So the file-level cone does not answer "which part is really used" — that needs the build.</li>
      <li>The trust inventory is <strong>empty</strong> across all 175,187 files. This agrees with the mirror's own scan. It is a text scan; the authority is <code>#print axioms</code> after a build.</li>
      <li>Half the mass — 8.2 million lines — is <code>Development/AbelianVarietyTheory</code>. The most-imported files sit in its <code>Definitions/Divisors</code>, each imported by 2,500–3,000 others: the natural place to start reading.</li>
      <li>One directory-level cycle spans 99 directories. Lean forbids cycles between files, so this says the folder names do not follow the proof's layering — read along imports from <code>Main</code>, not along folders.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Two wrong guesses, reversed</h2>
    <p>Not every error was the tool's. Two were the assistant's, made in
    conversation before the evidence was in.</p>
    <div class="tablewrap">
      <table class="prose">
        <colgroup><col style="width:42%"><col></colgroup>
        <thead><tr><th>Said first</th><th>What replaced it</th></tr></thead>
        <tbody>
          <tr><td>"There is no written exposition of the proof; only the code exists."</td>
          <td>The mirror's README links a community exposition: 12 chapters, about 58,000 words, written by the mirror's owner — itself unreviewed. Corrected as soon as the README was read.</td></tr>
          <tr><td>"<code>WeilBound</code>, <code>FunctionField</code> and <code>PositivityTheory</code> suggest Weil's explicit formula and the function-field route."</td>
          <td>Refuted. The exposition says <code>WeilBound</code> does not contain the explicit formula: it is arithmetic positivity on Shimura towers. The <code>FunctionField</code> hit is <code>CharZeroFunctionField</code>, the function field of a variety. The guess came from names; the names were false friends.</td></tr>
        </tbody>
      </table>
    </div>
    <p>The second one mattered downstream. It is now a section of its own in the
    research write-up below, because "the same word naming two objects" is the
    trap a reader of that project is most likely to fall into.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Where the map went</h2>
    <p><a href="https://github.com/XINMurat/sieve-to-spectrum">sieve-to-spectrum</a>
    is a bilingual research record that climbs a "fiber ladder" of seven rungs,
    from a multiplication table to the Langlands program. Its seeds came from
    <strong>Kıyas</strong>; its claims are tiered in a <strong>Mizan</strong>
    audit. The map placed the proof on that ladder:
    <a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/en/11-alpoge-proof-and-the-ladder.md">piece 11</a>.</p>
    <ul class="plain">
      <li>The proof sits on rung 7 (Langlands, Galois and automorphic representations) and descends to rung 4 (zeros). Rungs 1–3, 5 and 6 are absent from its path.</li>
      <li>The claimed theorems are about Dirichlet L-functions — the object of the project's Seed 3.</li>
      <li>The project had written that every upper rung "hits the same function-field / number-field gap". The proof, as claimed, does not cross from the function-field side. Piece 11 records this as a <strong>preregistered test</strong> of that sentence, to be settled when the proof's status is.</li>
    </ul>
    <p>That is the handoff the family is built for: a measurement turned into a
    claim the next piece of evidence can refute.</p>
    <p>The map also came back into the tool. The charts drawn for this release
    (block diagram, links in and out, where the lines are, most-used files) are
    now a Röntgen output for any repository: <code>pano.py</code> writes one
    <code>pano.html</code> with no network, its data inside, a TR / EN switch,
    and a first view in the report's language. Its first version drew nothing
    where scripts do not run, which the person reading found by opening it;
    headings and the summary are now written into the page itself.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>What one session cannot show</h2>
    <ul class="plain">
      <li><strong>Correctness.</strong> Nothing here bears on it.</li>
      <li><strong>Theorem-level dependencies.</strong> Tactics such as <code>simp</code> choose lemmas that never appear in the text. Which of the 1.06 million declarations the main theorem really uses needs the compiled environment.</li>
      <li><strong>Coverage of the exposition.</strong> Five of eleven chapters were read, by a fetching agent, not line by line.</li>
      <li><strong>Lean on other repositories.</strong> One release, one machine. The Lean support has self-tests and this run; it has not been measured against an architecture document the way the Rust, Go and C# rows on the Röntgen page were.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The artefacts</h2>
    <ul class="plain">
      <li>Röntgen commits: <a href="https://github.com/XINMurat/rontgen/commit/12f7609">Lean support</a>, <a href="https://github.com/XINMurat/rontgen/commit/5a5069f">long paths read and walked</a>, <a href="https://github.com/XINMurat/rontgen/commit/3ddff39">long-line heuristic exempts <code>.lean</code></a>. The Lean support and the heuristic change have self-tests; the long-path fix has none and is checked only by run 4.</li>
      <li>Upstream: <a href="https://github.com/tamnd/riemann-lean/pull/3">tamnd/riemann-lean#3</a> — a Windows note for <code>docs/BUILD.md</code>, because the clone itself broke the same way the tool did.</li>
      <li>Research: <a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/en/11-alpoge-proof-and-the-ladder.md">sieve-to-spectrum, piece 11</a> (<a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/tr/11-alpoge-ispati-ve-merdiven.md">Türkçe</a>).</li>
      <li>Reproduce: clone with <code>core.longpaths</code>, then <code>python scripts/yapi.py --repo riemann-lean/lean --out out</code>. The run-4 numbers should come back exactly.</li>
      <li><a href="/">Back to the five verbs</a></li>
    </ul>
  </div>
</section>

</div>

<div id="pane-tr" lang="tr" class="pane-init">

<section class="hero">
  <div class="wrap">
    <h1>Kimsenin baştan sona okuyamadığı bir ispatı haritalamak</h1>
    <p class="lede">20 Kasım 2026'da Levent Alpöge, Riemann Hipotezi'nin iddia
    edilen bir ispatını yalnızca Lean 4 kodu olarak yayımladı: 175.187 dosya,
    yaklaşık 17,5 milyon satır, düzyazı bir makale yok. Röntgen'in o sabah Lean
    desteği yoktu. Bu sayfa, destek eklenip yayına çevrildiğinde olanları
    anlatıyor — dört tarama, her biri kendi sayılarıyla araçta bir hata
    açığa çıkarıyor.</p>
    <p class="canon">Oturum tarihi 2026-11-26 · Röntgen <code>3ddff39</code> ·
    kaynak: <code>tamnd/riemann-lean</code> aynası, <code>54f24d4</code> ·
    bu sayfa ispatı değerlendirmez.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Neden Röntgen, ve burada neyi yapamaz</h2>
    <p>Bir ispatın doğru olup olmadığına Lean karar verir; bir metin tarayıcısı
    veremez. Ama bu yayının tam derlemesi 350 ile 2.300 işçi-saat arasında
    tahmin ediliyordu ve kimse yapmamıştı. O zamana kadar bu ölçekte çalışan
    tek araçlar metni okuyanlar. Röntgen'in işi haritaydı: hangi modül hangisine
    dayanıyor, her dosya ne bildiriyor, çekirdekten nerede bir şeyi kanıtsız
    kabul etmesi isteniyor.</p>
    <p>Lean desteği bu koşum için yazıldı: lakefile'ın kaynak kökleri üzerinden
    <code>import</code> çözümü, namespace'e göre iç içe bir bildirim iskeleti, ve
    iç içe yorumlar ayıklanmış bir güven envanteri: <code>sorry</code>,
    <code>admit</code>, <code>axiom</code>, <code>opaque</code>,
    <code>unsafe</code>, <code>native_decide</code>, <code>implemented_by</code>,
    <code>extern</code>.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Dört tarama</h2>
    <p class="sub">Her satır eksiksiz bir koşum. Her koşumun sayıları bir sonraki hatayı gösterdi.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Koşum</th><th>Okunan dosya</th><th>Çözülemeyen import</th><th>Sayıların açığa çıkardığı</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>166.426</td><td>15.069</td>
          <td>5.518 dosya <em>okunamadı</em> diye raporlandı. En uzun yol 244 karakter; klon dizini önüne eklenince Python'un <code>open</code>'ı Windows'un 260 karakter sınırını aştı ve düştü. Örneklenen her çözülemeyen import okunamayan bir dosyaya gidiyordu.</td></tr>
          <tr><td>2</td><td>171.939</td><td>3.448</td>
          <td>Okuma <code>\\?\</code> önekiyle düzeldi (<code>ortak.uzun_yol</code>). Yaklaşık 3.200 dosya hâlâ eksikti: dizin gezintisi uzun dizinleri <em>sessizce</em> atlıyordu — hata yok, dışlama listesinde kayıt yok.</td></tr>
          <tr><td>3</td><td>175.052</td><td>170</td>
          <td>Gezinti düzeldi. 135 dosya şimdi "üretilmiş görünüyor (çok uzun satırlar)" diye dışlanıyordu. Bir Lean ispat terimi tek satırda 5.000 karaktere ulaşabilir; sezgi küçültülmüş JavaScript için yazılmıştı. Çözülemeyen 170 import'un hepsi o 135 dosyaya gidiyordu.</td></tr>
          <tr><td>4</td><td><strong>175.187</strong></td><td><strong>0</strong></td>
          <td>Sezgi <code>.lean</code>'i muaf tutuyor. Her dosya okundu, her import çözüldü, hiçbir şey dışlanmadı. Koşum başına yaklaşık 17,5 dakika.</td></tr>
        </tbody>
      </table>
    </div>
    <p>Önemli olan hatalar değil, biçim. Hiçbir koşum hak etmediği bir başarıyı
    raporlamadı: her biri göremediği şeyin sıfırdan büyük bir sayısını bastı, ve
    her sayı tek bir nedene izlenebildi. 1. koşumda "175.187 dosya, tamam" diyen
    bir araç beş bin dosya yanılmış olurdu ve kimse bilmezdi.</p>
    <p>Beşinci hata okumada değil, çizimdeydi. Blok şemasının katmanlaması bir
    döngünün her üyesini üst sınıra itiyordu; 99 dizinlik döngü on üç kutuyu boş
    bir sayfanın altında tek satıra yığdı, etiketler sözcük ortasından kesildi.
    Yerleşim artık katmanlamadan önce döngüleri kırıyor, geniş satırları
    bölüyor ve bir adı sözcük keserek değil üst klasörünü atarak kısaltıyor.
    Okuyan kişi şemanın görünmediğini söylediği için bulundu.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Haritanın gösterdikleri</h2>
    <ul class="plain">
      <li><strong>753.569</strong> dosyadan dosyaya import çözüldü <code>[K]</code>; 156.253'ü daha Mathlib'e gidiyor, sayılıyor ama çizilmiyor.</li>
      <li><strong>Her modül <code>Main</code>'in import konisinde</strong>, en uzun zincir 43 adım. Yani dosya düzeyindeki koni "hangi kısım gerçekten kullanılıyor" sorusunu cevaplamıyor — o derleme ister.</li>
      <li>Güven envanteri 175.187 dosyanın tamamında <strong>boş</strong>. Bu, aynanın kendi taramasıyla tutarlı. Bir metin taraması; kesin söz derlemeden sonra <code>#print axioms</code>'ta.</li>
      <li>Kütlenin yarısı — 8,2 milyon satır — <code>Development/AbelianVarietyTheory</code>. En çok import edilen dosyalar onun <code>Definitions/Divisors</code> klasöründe, her biri 2.500–3.000 dosyaya giriyor: okumaya başlamanın doğal yeri.</li>
      <li>Dizin düzeyinde bir döngü 99 dizini kapsıyor. Lean dosyalar arası döngüye izin vermez; demek ki klasör adları ispatın katmanlarını izlemiyor — klasörler boyunca değil, <code>Main</code>'den import'lar boyunca okuyun.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>İki yanlış tahmin, geri alındı</h2>
    <p>Hataların hepsi aracın değildi. İkisi asistanındı; kanıt gelmeden,
    sohbette yapılmıştı.</p>
    <div class="tablewrap">
      <table class="prose">
        <colgroup><col style="width:42%"><col></colgroup>
        <thead><tr><th>Önce söylenen</th><th>Yerine geçen</th></tr></thead>
        <tbody>
          <tr><td>"İspatın yazılı bir anlatımı yok; yalnızca kod var."</td>
          <td>Aynanın README'si bir topluluk anlatımına bağlanıyor: 12 bölüm, yaklaşık 58.000 sözcük, aynanın sahibi yazmış — kendisi de denetlenmemiş. README okunur okunmaz düzeltildi.</td></tr>
          <tr><td>"<code>WeilBound</code>, <code>FunctionField</code> ve <code>PositivityTheory</code> Weil'in açık formülüne ve fonksiyon cismi yoluna işaret ediyor."</td>
          <td>Çürütüldü. Anlatım <code>WeilBound</code>'un açık formülü içermediğini söylüyor: Shimura kuleleri üzerinde aritmetik pozitiflik. <code>FunctionField</code> eşleşmesi <code>CharZeroFunctionField</code>, bir çeşitlemenin fonksiyon cismi. Tahmin adlardan gelmişti; adlar yanıltıcıydı.</td></tr>
        </tbody>
      </table>
    </div>
    <p>İkincisi aşağı akışta önem kazandı. Aşağıdaki araştırma yazısında artık
    kendi bölümü var, çünkü "aynı kelimenin iki nesneyi adlandırması" o projenin
    okurunun düşeceği en olası tuzak.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Harita nereye gitti</h2>
    <p><a href="https://github.com/XINMurat/sieve-to-spectrum">sieve-to-spectrum</a>,
    bir çarpım tablosundan Langlands programına yedi basamaklı bir "lif
    merdiveni" çıkan iki dilli bir araştırma kaydı. Tohumları
    <strong>Kıyas</strong>'tan geldi; iddiaları bir <strong>Mizan</strong>
    denetiminde katmanlandı. Harita ispatı o merdivene yerleştirdi:
    <a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/tr/11-alpoge-ispati-ve-merdiven.md">11. yazı</a>.</p>
    <ul class="plain">
      <li>İspat 7. basamakta (Langlands, Galois ve otomorfik temsiller) duruyor ve 4. basamağa (sıfırlar) iniyor. 1–3, 5 ve 6. basamaklar yolunda yok.</li>
      <li>İddia edilen teoremler Dirichlet L-fonksiyonları hakkında — projenin Tohum 3'ünün nesnesi.</li>
      <li>Proje, her üst basamağın "aynı fonksiyon-cismi / sayı-cismi uçurumuna çarptığını" yazmıştı. İspat, iddia edildiği haliyle, fonksiyon cismi tarafından geçmiyor. 11. yazı bunu o cümlenin bir <strong>ön kayıt sınaması</strong> olarak kaydediyor; ispatın durumu netleşince sonuçlanacak.</li>
    </ul>
    <p>Ailenin kurulduğu devir bu: bir ölçüm, bir sonraki kanıtın
    çürütebileceği bir iddiaya dönüştü.</p>
    <p>Harita araca da geri döndü. Bu yayın için çizilen grafikler (blok
    şeması, gelen/giden bağlar, satırların yeri, en çok kullanılan dosyalar)
    artık her depo için bir Röntgen çıktısı: <code>pano.py</code> ağ
    gerektirmeyen, verisini içinde taşıyan, TR / EN düğmeli ve ilk görünümü
    rapor dilinde olan tek bir <code>pano.html</code> yazar. İlk sürümü betik
    çalışmayan görüntüleyicide hiçbir şey göstermiyordu; okuyan kişi açınca
    fark etti. Başlıklar ve özet artık sayfanın içine yazılıyor.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Tek bir oturumun gösteremedikleri</h2>
    <ul class="plain">
      <li><strong>Doğruluk.</strong> Buradaki hiçbir şey onunla ilgili değil.</li>
      <li><strong>Teorem düzeyinde bağımlılıklar.</strong> <code>simp</code> gibi taktikler metinde hiç geçmeyen lemmaları seçer. 1,06 milyon bildirimin hangisini ana teoremin gerçekten kullandığı derlenmiş ortam ister.</li>
      <li><strong>Anlatımın kapsamı.</strong> On bir bölümün beşi okundu, bir getirme ajanıyla, satır satır değil.</li>
      <li><strong>Başka depolarda Lean.</strong> Tek yayın, tek makine. Lean desteğinin öz-testleri ve bu koşumu var; Röntgen sayfasındaki Rust, Go ve C# satırları gibi bir mimari belgeye karşı ölçülmedi.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Artefaktlar</h2>
    <ul class="plain">
      <li>Röntgen commit'leri: <a href="https://github.com/XINMurat/rontgen/commit/12f7609">Lean desteği</a>, <a href="https://github.com/XINMurat/rontgen/commit/5a5069f">uzun yollar okunuyor ve geziliyor</a>, <a href="https://github.com/XINMurat/rontgen/commit/3ddff39">uzun satır sezgisi <code>.lean</code>'i muaf tutuyor</a>. Lean desteğinin ve sezgi değişikliğinin öz-testleri var; uzun yol düzeltmesinin yok, yalnızca 4. koşumla doğrulandı.</li>
      <li>Upstream: <a href="https://github.com/tamnd/riemann-lean/pull/3">tamnd/riemann-lean#3</a> — <code>docs/BUILD.md</code> için bir Windows notu, çünkü klonun kendisi de araçla aynı şekilde kırıldı.</li>
      <li>Araştırma: <a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/tr/11-alpoge-ispati-ve-merdiven.md">sieve-to-spectrum, 11. yazı</a> (<a href="https://github.com/XINMurat/sieve-to-spectrum/blob/main/docs/en/11-alpoge-proof-and-the-ladder.md">English</a>).</li>
      <li>Tekrarlamak için: <code>core.longpaths</code> ile klonlayın, sonra <code>python scripts/yapi.py --repo riemann-lean/lean --out out</code>. 4. koşumun sayıları birebir geri gelmeli.</li>
      <li><a href="/">Beş fiile dön</a></li>
    </ul>
  </div>
</section>

</div>
