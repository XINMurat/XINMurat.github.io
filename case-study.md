---
layout: default
title: "Case study — four AI reviews, audited"
description: "A worked run of Mizan and Kıyas on real material: four AI assessments of this family, atomized and tiered, the auditor's own two errors reversed on the record, one escape turned into a control, and five seeds generated under negative constraints."
lang: en
---

<!--
  Two panes, one content model — same rule as index.md. Every section exists in
  BOTH languages with the same depth. A case study that is thorough in one
  language and a summary in the other is two case studies, and the shorter one
  is the dishonest one.

  SOURCE NOTE: everything below happened in one session on 2026-09-06 against
  the four repositories and this page. Nothing is reconstructed and nothing is
  improved after the fact. Where the audit was WRONG, the wrong finding is
  printed next to its correction rather than replaced by it — that is the
  behaviour being demonstrated, and a case study that quietly fixed its own
  mistakes would be demonstrating the opposite.
-->

<div id="pane-en" lang="en">

<section class="hero">
  <div class="wrap">
    <h1>A worked run</h1>
    <p class="lede">Someone asked four different AI assistants what they thought
    of these four skills, collected the answers, and brought them back to be
    audited. This page is what happened — including the two findings the audit
    got wrong and had to reverse, and the defect the generator found in a
    proposal that three of the four assistants had praised.</p>
    <p class="canon">Session date 2026-09-06 · Mizan v2.6.0 · Kıyas v1.4.0 ·
    the entries behind this page are published as an excerpt; what is withheld
    is named — see <em>The artefacts</em> at the end.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The material</h2>
    <p class="sub">Four AI assessments, ~40 atomized claims.</p>

    <p>The input was ordinary: four long, fluent, complimentary write-ups about
    this family of skills — one reading the architecture, two proposing ways to
    use Mizan's evidence tiers as a reward signal in LLM training, one reporting
    on the contents of this page. This is exactly the <strong>You → Mizan</strong>
    arrow on the front page: material that already exists, entering at the audit.</p>

    <p>Atomization produced roughly forty checkable claims. In the first pass
    only fourteen were verifiable, because the audit ran against one repository
    and could not see the others. That number is a coverage statement, not a
    footnote: an audit that checks a third of the claims and reports like a full
    audit is the failure this method is named after.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Pass one — what the audit found</h2>

    <div class="tablewrap">
      <table>
        <thead><tr><th>Claim</th><th>Tier</th><th>Evidence</th></tr></thead>
        <tbody>
          <tr><td><strong>Mizan is v2.5.0</strong></td><td><code>[R]</code></td>
          <td><code>SKILL.md</code> declares 2.6. All four write-ups were one release behind.</td></tr>
          <tr><td><strong>The validator enforces R1–R21</strong></td><td><code>[R]</code></td>
          <td>The rule set is R1–R22. Off by one, in all four.</td></tr>
          <tr><td><strong>Identifier <code>GEN:CIFT</code></strong></td><td><code>[Y]</code></td>
          <td>Appears in no file in any repository. The real identifier is <code>G13</code>.</td></tr>
          <tr><td><strong>The methodology audits itself; <code>[R]</code> rows survive</strong></td><td><code>[K]</code></td>
          <td>Two refuted rows in the product registry, undeleted.</td></tr>
        </tbody>
      </table>
    </div>

    <p>The interesting part is not that four assistants were wrong. It is that
    they were wrong <em>in the same direction by the same amount</em>. Four
    independent sources do not drift one release stale together; a shared stale
    source does. The pattern reclassified the error: not fabrication, but a
    reconstruction presented as a reading.</p>

    <h3>The denominator</h3>
    <p>Across four long documents, the core claims of the project were refuted
    <strong>zero times</strong> in three of them. The negatives on offer were
    "add a diagram", "add a demo", "the theme could be more modern". One of the
    four was different, and said the sharp things: that Mizan is not a loss
    function but a labelling layer feeding one; that a <code>[K] = 1.0</code>
    weight does not follow from Mizan mathematically; that a refuted registry
    row is not automatically a preference pair. Reporting <em>one in four</em>
    is worth more than quoting the three.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Pass two — the audit was wrong twice</h2>
    <p class="sub">This is the part worth reading.</p>

    <p>The owner then pointed out that the live page and the other three
    repositories were available locally. Coverage went from 14 checkable claims
    to 31 — and two of the audit's own findings did not survive.</p>

    <div class="tablewrap">
      <table>
        <thead><tr><th>The audit said</th><th>What was true</th></tr></thead>
        <tbody>
          <tr><td><code>[R]</code> "there is no version table on the page"</td>
          <td>There is. The audit looked in <code>Mizan/docs/index.md</code>; the table lives in a <em>different repository</em>, the one that builds this site. Wrong artefact, confident verdict.</td></tr>
          <tr><td><code>[Y]</code> "<code>U13</code> is fabricated"</td>
          <td><code>U13</code> is real — it is ux-mizan's conjunction rule, on this page. The reviewer was right and the auditor was not.</td></tr>
        </tbody>
      </table>
    </div>

    <p>Both were demoted in place, dated and appended, with the original lines
    left standing. That is <code>RR-11</code>, and it is not decoration: an
    audit's own output is a claim set, and a method that exempts its own
    verdicts from the rule it enforces on everyone else has stopped being a
    method. Two findings out of three in that group were mine to withdraw.</p>

    <p>What the second pass also produced was <em>stronger</em> evidence for the
    project than the four write-ups had assembled: the feedback loop from Mizan
    to Kıyas has actually fired (six real entries in
    <code>refuted-patterns.yaml</code>, each with a reason); ux-mizan carries an
    <code>[R]</code> on one of its own design decisions; and
    <code>iskele_to_registry.py</code> defaults its arbiter class to
    <code>author</code>, which under R8 permanently blocks promotion to
    <code>[K]</code>. That default is in code, not in prose — which is the whole
    point of the rule that says the script is what travels.</p>

    <div class="note">
      <p><strong>The uncomfortable finding:</strong> the repositories audit
      themselves more harshly than any of the four assistants audited them.
      Kıyas refuses to claim that it works. ux-mizan refutes its own design.
      İskele defaults to the arbiter that forbids proof. The praise was the part
      that violated the method.</p>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The escape, and the control it produced</h2>
    <p class="sub">Counting a miss is not learning from one.</p>

    <p>The stale-version error was recorded as an escape,
    <code>ESC-M003</code> — and its class already existed. Two earlier entries
    in the same registry had recorded the identical lesson: an external AI's
    claim to have "read" or "researched" something is not evidence. Both entries
    are in the same registry, both predate this session. The lesson had been written down
    twice and never turned into a control. So it escaped a third time, in four
    places at once.</p>

    <p>The control now exists: this page carries a build stamp in its footer —
    a date and a commit hash. It does not stop anyone from reading a cached
    copy. What it does is make the version part of the claim, so that "I read
    the page" becomes checkable instead of unfalsifiable. It is preregistered as
    <code>YZ-004</code> with its own refutation condition: if reviews written
    after the stamp still repeat old numbers without naming a version, the stamp
    is not being read and the entry is refuted.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Handoff — Mizan to Kıyas</h2>
    <p class="sub">Five seeds, three discards, three independent bets.</p>

    <p>The audit left two claims alive but untestable: that an evidence-gated
    loop outproduces a free one, and that mapping evidence tiers to fixed reward
    values improves reasoning. Both were registered as <code>[S]</code> with no
    refutation condition — which is where Kıyas is for. The negative constraints
    came from the registry itself: three candidates were discarded before
    generation finished, two of them as <code>[GB]</code> — relatives of
    patterns already refuted (a productised "epistemic dashboard"; a
    tier-native pretrained model, which falls in the same class as a
    kill-condition-free scaling ladder the registry had already refused).</p>

    <div class="tablewrap">
      <table>
        <thead><tr><th>Seed</th><th>Move</th><th>Cheapest refutation</th></tr></thead>
        <tbody>
          <tr><td><strong>K-01</strong> six tiers give nothing a binary verdict does not</td><td>limit</td><td>Three arms at equal compute: binary / three-valued / six-tier.</td></tr>
          <tr><td><strong>K-02</strong> reward correct self-labelling, not the label's value</td><td>inversion</td><td>Calibration error plus a capacity-matched generic auxiliary head.</td></tr>
          <tr><td><strong>K-03</strong> run the pair pass at decoding, not in the loss</td><td>substrate swap</td><td>Against equal-compute best-of-n — not against greedy.</td></tr>
          <tr><td><strong>K-04</strong> test the gate by blinded replay of past hypotheses</td><td>constraint relaxation</td><td>Ranking AUC against a plausibility-only ranker.</td></tr>
          <tr><td><strong>K-05</strong> the proposed constants open a safe harbour</td><td>inversion (symmetry)</td><td>Read off K-01's own run at zero extra cost.</td></tr>
        </tbody>
      </table>
    </div>

    <p>The pair pass reports the number that matters: <strong>five seeds, three
    independent bets.</strong> K-01, K-02 and K-05 share one premise and one
    experiment. Listed as five they read as five; counted honestly they are
    three.</p>

    <h3>K-05 — the seed that cuts against the thesis</h3>
    <p>Every batch must carry one candidate that damages the position being
    argued for. Here it turned out to be the most load-bearing result of the
    session.</p>
    <p>The reward mapping the assistants proposed assigns
    <code>[S]</code> — speculative — a value of <strong>0.0</strong>. In a
    scheme whose other negatives carry real penalties, that leaves exactly one
    action that is always available and never punished. A policy under pressure
    converges on it: emit speculative steps, commit to nothing. The failure mode
    <em>looks like epistemic humility</em>, which is precisely why it would be
    hard to catch by reading outputs.</p>
    <p>The mechanism follows directly from the proposed constants, so if it
    holds, the proposal is refuted <em>as specified</em> — the tier idea
    survives, the numbers do not. It costs nothing to measure: it is a second
    reading of an experiment already being run. None of the four assessments
    noticed it; two of them defended the constants.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Back to Mizan</h2>
    <p>The seeds returned as refutation conditions on the entries that lacked
    them. <code>YZ-002</code> went from "threshold: none" to a locked numeric
    threshold calibrated against the harness's own seed-to-seed spread, plus two
    refutation conditions — K-01's and K-05's. <code>YZ-001</code> received
    K-04's design <em>and</em> its precondition: the experiment cannot be run
    today, because it needs thirty settled hypotheses and the ledger holds six,
    none of them scored. Recording a test that cannot run yet is not a failure;
    pretending it can is.</p>
    <p>The registry passes its own validator — <code>R1–R22</code>, no
    violations — and the seed batch passes Kıyas's, <code>G1–G14</code>, with
    one warning that is worth repeating rather than hiding: every seed in the
    batch landed at <code>[H-aday]</code>, and a batch where nothing lands lower
    is usually a batch that skipped the sweep. Here the sweep did run — three
    discards and one symmetry seed are the evidence — but the warning is fair
    and stays on the record.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>What this does not show</h2>
    <p class="sub">The section the four assessments did not have.</p>
    <ul class="plain">
      <li><strong>n = 1.</strong> One session, one claim set. Nothing here is a
      hit rate, and no rate can be computed from it.</li>
      <li><strong>The arbiter was the author.</strong> Every verdict on this
      page was returned by the same party that ran the audit. Under R8 that
      carries a permanent <code>[KKE]</code>, and no amount of format makes it
      <code>[K]</code>. The exceptions are the two mechanical checks — the two
      validators — which is exactly why they exist.</li>
      <li><strong>Kıyas still cannot claim it works.</strong> Its survival
      ledger holds six unscored seeds from one draw and prints a permanent
      <code>[KKE]</code>. A control arm has now been preregistered — matched
      arms, a locked threshold, a stopping rule, and the author's own prediction
      that the result will land in the underpowered band — but nothing has been
      measured. The rate is undefined, not favourable.</li>
      <li><strong>None of the five seeds has been run.</strong> They are
      preregistrations. The accumulation of unrun preregistrations is this
      family's current risk, not a shortage of ideas.</li>
      <li><strong>No third-party arbiter exists anywhere in the four
      repositories.</strong> Every arbiter class is <code>runtime</code> or
      <code>author</code>. That empty cell is the only place this project could
      earn a <code>[K]</code>, and it is still empty.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The artefacts</h2>
    <ul class="plain">
      <li><a href="https://github.com/XINMurat/Kiyas/blob/main/ledger/kiyas-ledger.yaml"><code>kiyas-ledger.yaml</code></a> — tracked and public: six unscored seeds, the permanent <code>[KKE]</code>, and the newly preregistered control arm.</li>
      <li><a href="https://github.com/XINMurat/Mizan/blob/main/docs/registry-excerpt.yaml"><code>registry-excerpt.yaml</code></a> — the entries this page is about: <code>YZ-001</code>…<code>YZ-004</code> with their thresholds and refutation conditions, and the escape <code>ESC-M003</code>. It is an <em>excerpt</em>, and its own header says so and prints the ratio: nine of twenty-three entries. The registry it comes from is gitignored — it carries pricing and roadmap notes — and the export is an allowlist, so an entry that is not explicitly marked public stays private. Generated by <a href="https://github.com/XINMurat/Mizan/blob/main/tools/mizan_export_public.py"><code>mizan_export_public.py</code></a>; it passes the same validator as the source.</li>
      <li><code>refuted-patterns.yaml</code> — <strong>still unpublished.</strong> The six refuted patterns two of the discards were checked against are not readable by anyone but the author, so that specific claim on this page remains author-reported and carries a permanent <code>[KKE]</code>. The excerpt above narrowed that gap; it did not close it.</li>
      <li>The two mechanical results are reproducible by anyone who runs the tools on their own registry: <code>mizan_validate.py</code> (R1–R22) and <code>kiyas_validate.py</code> (G1–G14). Those are the only verdicts here that do not depend on trusting the author.</li>
      <li><a href="/">Back to the four verbs</a></li>
    </ul>
  </div>
</section>

</div>

<div id="pane-tr" lang="tr" class="pane-init">

<section class="hero">
  <div class="wrap">
    <h1>Çalışılmış bir koşum</h1>
    <p class="lede">Biri bu dört skill hakkında dört ayrı yapay zekâya ne
    düşündüklerini sordu, cevapları topladı ve denetlenmek üzere geri getirdi.
    Bu sayfa olanları anlatıyor — denetimin yanlış çıkıp geri aldığı iki bulgu
    ve dört asistandan üçünün övdüğü bir öneride üretecin bulduğu kusur dahil.</p>
    <p class="canon">Oturum tarihi 2026-09-06 · Mizan v2.6.0 · Kıyas v1.4.0 ·
    bu sayfanın dayandığı girdiler alıntı olarak yayınlandı; dışarıda kalan
    adlandırıldı — sondaki <em>Artefaktlar</em> bölümüne bakın.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Malzeme</h2>
    <p class="sub">Dört YZ değerlendirmesi, ~40 atomlanmış iddia.</p>

    <p>Girdi sıradandı: bu skill ailesi hakkında dört uzun, akıcı ve iltifatkâr
    metin — biri mimariyi okuyan, ikisi Mizan'ın kanıt katmanlarını LLM
    eğitiminde ödül sinyaline çevirmeyi öneren, biri bu sayfanın içeriğini
    aktaran. Ön sayfadaki <strong>Siz → Mizan</strong> oku tam olarak budur:
    elde zaten var olan malzeme, denetimden giriyor.</p>

    <p>Atomlama yaklaşık kırk denetlenebilir iddia üretti. İlk pasta bunların
    yalnızca on dördü doğrulanabilirdi, çünkü denetim tek bir depoya karşı
    koşuyordu ve diğerlerini göremiyordu. Bu sayı bir dipnot değil, bir kapsam
    beyanıdır: iddiaların üçte birini denetleyip tam denetim gibi rapor eden bir
    çıktı, bu yöntemin adını taşıdığı başarısızlığın kendisidir.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Birinci pas — denetim ne buldu</h2>

    <div class="tablewrap">
      <table>
        <thead><tr><th>İddia</th><th>Katman</th><th>Kanıt</th></tr></thead>
        <tbody>
          <tr><td><strong>Mizan v2.5.0</strong></td><td><code>[R]</code></td>
          <td><code>SKILL.md</code> 2.6 diyor. Dört metin de tam bir sürüm geride.</td></tr>
          <tr><td><strong>Doğrulayıcı R1–R21'i uyguluyor</strong></td><td><code>[R]</code></td>
          <td>Kural seti R1–R22. Bir eksik, dördünde de.</td></tr>
          <tr><td><strong><code>GEN:CIFT</code> tanımlayıcısı</strong></td><td><code>[Y]</code></td>
          <td>Hiçbir depoda hiçbir dosyada geçmiyor. Gerçek tanımlayıcı <code>G13</code>.</td></tr>
          <tr><td><strong>Yöntem kendini denetliyor; <code>[R]</code> satırları duruyor</strong></td><td><code>[K]</code></td>
          <td>Ürün registry'sinde iki çürütülmüş satır, silinmemiş.</td></tr>
        </tbody>
      </table>
    </div>

    <p>İlginç olan dört asistanın yanılmış olması değil. <em>Aynı yönde, aynı
    büyüklükte</em> yanılmış olmaları. Dört bağımsız kaynak birlikte tam bir
    sürüm bayatlamaz; ortak bir bayat kaynak bayatlar. Örüntü hatayı yeniden
    sınıflandırdı: uydurma değil, okuma diye sunulmuş bir rekonstrüksiyon.</p>

    <h3>Payda</h3>
    <p>Dört uzun metin boyunca, projenin çekirdek iddiaları üçünde
    <strong>sıfır kez</strong> çürütüldü. Sunulan olumsuzluklar "diyagram
    ekleyin", "demo ekleyin", "tema daha modern olabilir"di. Dördüncüsü
    farklıydı ve keskin şeyleri söyledi: Mizan bir loss fonksiyonu değil, ona
    girdi veren bir etiketleme katmanıdır; <code>[K] = 1.0</code> ağırlığı
    Mizan'dan matematiksel olarak çıkmaz; çürütülmüş bir registry satırı
    kendiliğinden bir tercih çifti değildir. <em>Dörtte bir</em> demek, üçünü
    alıntılamaktan daha bilgilendirici.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>İkinci pas — denetim iki kez yanıldı</h2>
    <p class="sub">Okunmaya değer kısım burası.</p>

    <p>Sonra sahibi, canlı sayfanın ve diğer üç deponun yerelde bulunduğunu
    söyledi. Kapsam 14 denetlenebilir iddiadan 31'e çıktı — ve denetimin kendi
    bulgularından ikisi ayakta kalmadı.</p>

    <div class="tablewrap">
      <table>
        <thead><tr><th>Denetim şunu dedi</th><th>Doğrusu</th></tr></thead>
        <tbody>
          <tr><td><code>[R]</code> "sayfada sürüm tablosu yok"</td>
          <td>Var. Denetim <code>Mizan/docs/index.md</code>'ye baktı; tablo <em>başka bir depoda</em>, bu siteyi kuran depoda duruyor. Yanlış artefakt, kendinden emin hüküm.</td></tr>
          <tr><td><code>[Y]</code> "<code>U13</code> uydurma"</td>
          <td><code>U13</code> gerçek — ux-mizan'ın bileşim kuralı, bu sayfada. Değerlendiren haklıydı, denetçi değil.</td></tr>
        </tbody>
      </table>
    </div>

    <p>İkisi de yerinde düşürüldü: tarihli, eklenerek, özgün satırlar ayakta
    bırakılarak. Bu <code>RR-11</code>'dir ve süs değildir: bir denetimin kendi
    çıktısı da bir iddia kümesidir, ve kendi hükümlerini herkese uyguladığı
    kuraldan muaf tutan bir yöntem yöntem olmaktan çıkmıştır. O gruptaki üç
    bulgudan ikisi geri alınacaktı ve benimdi.</p>

    <p>İkinci pas ayrıca proje lehine, dört metnin toplayabildiğinden
    <em>daha güçlü</em> kanıt üretti: Mizan'dan Kıyas'a giden geri besleme
    gerçekten çalışmış (<code>refuted-patterns.yaml</code>'da altı gerçek girdi,
    her biri gerekçeli); ux-mizan kendi tasarım kararlarından birine
    <code>[R]</code> vermiş; ve <code>iskele_to_registry.py</code> hakem
    sınıfını varsayılan olarak <code>author</code> yapıyor — ki bu R8 gereği
    <code>[K]</code>'ye terfiyi kalıcı olarak kapatır. O varsayılan düzyazıda
    değil kodda; "kuralı taşıyan şey betiktir" kuralının bütün anlamı bu.</p>

    <div class="note">
      <p><strong>Rahatsız edici bulgu:</strong> depolar kendilerini, dört
      asistanın hiçbirinin denetlediğinden daha sert denetliyor. Kıyas işe
      yaradığını iddia etmeyi reddediyor. ux-mizan kendi tasarımını çürütüyor.
      İskele, kanıtlamayı yasaklayan hakemi varsayılan yapıyor. Yöntemi ihlal
      eden kısım övgüydü.</p>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Kaçak, ve doğurduğu kontrol</h2>
    <p class="sub">Kaçanı saymak, ondan öğrenmek değildir.</p>

    <p>Bayat sürüm hatası bir kaçak olarak kaydedildi: <code>ESC-M003</code> —
    ve sınıfı zaten vardı. Aynı registry'deki iki eski girdi tam olarak aynı
    dersi kaydetmişti: dış bir YZ'nin bir şeyi "okudum" ya da "araştırdım"
    beyanı kanıt değildir. İki girdi de aynı registry'de, ikisi de bu oturumdan
    eski. Ders iki kez yazılmış, hiç kontrole çevrilmemişti. Bu yüzden üçüncü kez kaçtı, üstelik
    aynı anda dört yerden.</p>

    <p>Kontrol artık var: bu sayfa altbilgisinde bir yapı damgası taşıyor —
    bir tarih ve bir commit hash. Kimseyi önbellekten okumaktan alıkoymuyor.
    Yaptığı şey sürümü iddianın parçası hâline getirmek; böylece "sayfayı
    okudum" cümlesi yanlışlanamaz olmaktan çıkıp denetlenebilir oluyor.
    <code>YZ-004</code> olarak, kendi çürütme koşuluyla önkayıtlı: damgadan
    sonra yazılan değerlendirmeler hâlâ sürüm belirtmeden eski numaraları
    tekrarlıyorsa damga okunmuyor demektir ve girdi çürür.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Devir — Mizan'dan Kıyas'a</h2>
    <p class="sub">Beş tohum, üç eleme, üç bağımsız bahis.</p>

    <p>Denetim iki iddiayı canlı ama test edilemez bıraktı: kanıt-kapılı bir
    döngünün serbest olandan daha çok üretmesi, ve kanıt katmanlarının sabit
    ödül değerlerine eşlenmesinin akıl yürütmeyi iyileştirmesi. İkisi de
    çürütme koşulu olmadan <code>[S]</code> kaydedildi — Kıyas tam da bunun
    için var. Negatif kısıtlar registry'nin kendisinden geldi: üretim bitmeden
    üç aday elendi, ikisi <code>[GB]</code> olarak — çürütülmüş örüntülerin
    akrabaları (ürünleştirilmiş bir "epistemik gösterge paneli"; katman-yerlisi
    bir ön-eğitimli model, ki bu registry'nin zaten reddettiği kill-condition'sız
    ölçek merdiveniyle aynı sınıfa düşüyor).</p>

    <div class="tablewrap">
      <table>
        <thead><tr><th>Tohum</th><th>Hamle</th><th>En ucuz çürütme</th></tr></thead>
        <tbody>
          <tr><td><strong>K-01</strong> altı katman, ikili yargının vermediği bir şey vermiyor</td><td>limit</td><td>Eşit compute'ta üç kol: ikili / üç değerli / altı katman.</td></tr>
          <tr><td><strong>K-02</strong> etiketin değerini değil, doğru öz-etiketlemeyi ödüllendir</td><td>tersleme</td><td>Kalibrasyon hatası + kapasite-eşli generik yardımcı başlık.</td></tr>
          <tr><td><strong>K-03</strong> çift pasını loss'ta değil dekodlamada koş</td><td>substrat değişimi</td><td>Eşit compute'lu best-of-n'e karşı — greedy'ye değil.</td></tr>
          <tr><td><strong>K-04</strong> kapıyı geçmiş hipotezlerin körlenmiş tekrarıyla test et</td><td>kısıt gevşetme</td><td>Yalnızca makullüğe bakan sıralayıcıya karşı AUC.</td></tr>
          <tr><td><strong>K-05</strong> önerilen sabitler bir güvenli liman açıyor</td><td>tersleme (simetri)</td><td>K-01'in kendi koşumundan sıfır ek maliyetle okunur.</td></tr>
        </tbody>
      </table>
    </div>

    <p>Çift pası asıl sayıyı veriyor: <strong>beş tohum, üç bağımsız
    bahis.</strong> K-01, K-02 ve K-05 tek bir öncülü ve tek bir deneyi
    paylaşıyor. Beş diye listelenince beş okunuyorlar; dürüstçe sayılınca
    üçler.</p>

    <h3>K-05 — tezi kesen tohum</h3>
    <p>Her parti, savunulan konumu hasar veren bir aday taşımak zorundadır.
    Burada oturumun en yük taşıyan sonucu o çıktı.</p>
    <p>Asistanların önerdiği ödül eşlemesi <code>[S]</code>'ye — spekülatif —
    <strong>0.0</strong> değeri veriyor. Diğer negatiflerinin gerçek cezalar
    taşıdığı bir şemada bu, her zaman erişilebilir ve asla cezalandırılmayan tek
    bir eylem bırakır. Baskı altındaki bir politika ona yakınsar: spekülatif
    adım üret, hiçbir şeye taahhüt etme. Ve bu hata biçimi
    <em>epistemik alçakgönüllülük gibi görünür</em> — çıktılara bakarak
    yakalanmasının bu kadar zor olmasının sebebi tam olarak budur.</p>
    <p>Mekanizma doğrudan önerilen sabitlerden çıkıyor; dolayısıyla doğrularsa
    öneri <em>belirtildiği haliyle</em> çürür — katman fikri ayakta kalır,
    sayılar kalmaz. Ölçmesi bedava: zaten koşulan bir deneyin ikinci okuması.
    Dört değerlendirmenin hiçbiri bunu görmedi; ikisi sabitleri savundu.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Mizan'a dönüş</h2>
    <p>Tohumlar, çürütme koşulu olmayan girdilere o koşul olarak döndü.
    <code>YZ-002</code> "eşik: yok"tan, koşum hattının kendi tohum-arası
    yayılımına göre kalibre edilmiş sayısal bir eşiğe ve iki çürütme koşuluna
    geçti — K-01'inki ve K-05'inki. <code>YZ-001</code> K-04'ün tasarımını
    <em>ve</em> ön koşulunu aldı: bu deney bugün koşulamaz, çünkü otuz
    kesinleşmiş hipotez istiyor ve ledger'da altı var, hiçbiri puanlanmamış.
    Henüz koşulamayan bir testi kaydetmek başarısızlık değildir; koşulabilirmiş
    gibi yapmak başarısızlıktır.</p>
    <p>Registry kendi doğrulayıcısından geçiyor — <code>R1–R22</code>, ihlal
    yok — ve tohum partisi Kıyas'ınkinden, <code>G1–G14</code>, gizlenmek yerine
    tekrarlanmayı hak eden bir uyarıyla: partideki her tohum
    <code>[H-aday]</code>'a düştü, ve hiçbir şeyin daha aşağı düşmediği bir
    parti genellikle süpürgeyi atlamış bir partidir. Burada süpürge koştu — üç
    eleme ve bir simetri tohumu bunun kanıtı — ama uyarı adil ve kayıtta
    kalıyor.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Bunun göstermediği şeyler</h2>
    <p class="sub">Dört değerlendirmede bulunmayan bölüm.</p>
    <ul class="plain">
      <li><strong>n = 1.</strong> Tek oturum, tek iddia kümesi. Buradaki hiçbir
      şey bir isabet oranı değildir ve bundan oran hesaplanamaz.</li>
      <li><strong>Hakem yazardı.</strong> Bu sayfadaki her hüküm, denetimi
      koşan tarafça verildi. R8 gereği bu kalıcı bir <code>[KKE]</code> taşır ve
      hiçbir biçim onu <code>[K]</code> yapmaz. İstisna iki mekanik denetim —
      iki doğrulayıcı — ki var olma sebepleri tam olarak budur.</li>
      <li><strong>Kıyas hâlâ işe yaradığını iddia edemiyor.</strong> Sağ-kalım
      ledger'ı tek bir çekilişten altı puanlanmamış tohum taşıyor ve kalıcı bir
      <code>[KKE]</code> basıyor. Bir kontrol kolu artık önkayıtlı — eşli
      kollar, kilitli eşik, durdurma kuralı ve yazarın sonucun güç-yetersiz
      bandında çıkacağına dair kendi tahmini — ama hiçbir şey ölçülmedi. Oran
      elverişli değil, <em>tanımsız</em>.</li>
      <li><strong>Beş tohumun hiçbiri koşulmadı.</strong> Bunlar önkayıt.
      Koşulmamış önkayıtların birikmesi bu ailenin şu anki riski; fikir kıtlığı
      değil.</li>
      <li><strong>Dört deponun hiçbirinde üçüncü-taraf hakem
      yok.</strong> Her hakem sınıfı ya <code>runtime</code> ya
      <code>author</code>. O boş hücre bu projenin <code>[K]</code>
      kazanabileceği tek yer, ve hâlâ boş.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Artefaktlar</h2>
    <ul class="plain">
      <li><a href="https://github.com/XINMurat/Kiyas/blob/main/ledger/kiyas-ledger.yaml"><code>kiyas-ledger.yaml</code></a> — izlenen ve açık: altı puanlanmamış tohum, kalıcı <code>[KKE]</code> ve yeni önkayıtlı kontrol kolu.</li>
      <li><a href="https://github.com/XINMurat/Mizan/blob/main/docs/registry-excerpt.yaml"><code>registry-excerpt.yaml</code></a> — bu sayfanın konusu olan girdiler: eşikleri ve çürütme koşullarıyla <code>YZ-001</code>…<code>YZ-004</code>, ve <code>ESC-M003</code> kaçağı. Bir <em>alıntıdır</em>; kendi başlığı bunu söylüyor ve oranı basıyor: yirmi üç girdinin dokuzu. Geldiği registry gitignore'lu — fiyat ve yol haritası notları taşıyor — ve export bir izin listesi: açıkça işaretlenmemiş girdi özel kalır. <a href="https://github.com/XINMurat/Mizan/blob/main/tools/mizan_export_public.py"><code>mizan_export_public.py</code></a> üretiyor; kaynağıyla aynı doğrulayıcıdan geçiyor.</li>
      <li><code>refuted-patterns.yaml</code> — <strong>hâlâ yayınlanmıyor.</strong> Elemelerden ikisinin karşısında denetlendiği altı çürütülmüş örüntüyü yazardan başkası okuyamıyor; dolayısıyla bu sayfadaki o iddia yazar-beyanı olarak kalıyor ve kalıcı bir <code>[KKE]</code> taşıyor. Yukarıdaki alıntı bu boşluğu daralttı, kapatmadı.</li>
      <li>İki mekanik sonuç, araçları kendi registry'sinde koşan herkes tarafından tekrarlanabilir: <code>mizan_validate.py</code> (R1–R22) ve <code>kiyas_validate.py</code> (G1–G14). Buradaki, yazara güvenmeyi gerektirmeyen tek hükümler bunlar.</li>
      <li><a href="/">Dört fiile dön</a></li>
    </ul>
  </div>
</section>

</div>
