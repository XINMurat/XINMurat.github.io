---
layout: default
title: "Four verbs — İskele · Mizan · Kıyas · ux-mizan"
description: "Four Claude skills that keep each other honest: one builds the structure, one weighs the claims, one generates the candidates, one measures the experience."
lang: en
---

<!--
  Two panes, one content model. Every section exists in BOTH languages with the
  same depth — if a row, a card or a caveat is added to one, it is added to the
  other in the same commit. This page is the family's canonical description, and
  a canonical description that says different things in two languages is two
  descriptions.
-->

<div id="pane-en" lang="en">

<section class="hero">
  <div class="wrap">
    <h1>Four verbs</h1>
    <p class="lede">Four Claude skills that keep each other honest. The verbs are
    kept apart on purpose: one builds the structure, one weighs the claims, one
    generates the candidates, one measures the experience. A conflated verb
    produces a single tool that does none of them well.</p>
    <ul class="verbs">
      <li><b>İskele</b> builds</li>
      <li><b>Mizan</b> weighs</li>
      <li><b>Kıyas</b> generates</li>
      <li><b>ux-mizan</b> measures experience</li>
    </ul>
    <p class="canon">This page is the family's canonical description; the four
    repositories point here rather than each carrying a copy that goes stale on
    its own.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The skills</h2>
    <p class="sub">One verb each, and the idea that carries it.</p>
    <div class="cards">

      <article class="card">
        <span class="verb">builds</span>
        <h3><a href="https://github.com/XINMurat/Iskele">İskele</a></h3>
        <p>Turns a vague intent into an <strong>executable, trackable</strong>
        system of work: domain model, gated phases, an atomic backlog,
        executable acceptance criteria, and a progress report
        <strong>computed</strong> from a tracker rather than estimated by hand.</p>
        <p class="key"><em>Every acceptance criterion is a refutation condition
        written before the work started</em> — which makes the backlog a
        preregistration set already.</p>
        <p class="links"><a href="https://xinmurat.github.io/Iskele/">docs</a> ·
        <a href="https://github.com/XINMurat/Iskele">repository</a></p>
      </article>

      <article class="card">
        <span class="verb">weighs</span>
        <h3><a href="https://github.com/XINMurat/Mizan">Mizan</a></h3>
        <p>Audits any claim set with evidence tiers and maintains living
        hypothesis registries. Thresholds lock <strong>before</strong> results;
        every hypothesis carries a refutation condition; a refuted entry is
        never deleted.</p>
        <p class="key"><em>A numeric threshold is only as strong as the judge
        that returns its verdict</em> — if the judge is the claim's own author,
        the claim cannot count as proven.</p>
        <p class="links"><a href="https://xinmurat.github.io/Mizan/">docs</a> ·
        <a href="https://github.com/XINMurat/Mizan">repository</a></p>
      </article>

      <article class="card">
        <span class="verb">generates</span>
        <h3><a href="https://github.com/XINMurat/Kiyas">Kıyas</a></h3>
        <p>Disciplined ideation and analogical inference for a problem that is
        stuck. Every idea it produces arrives shaped for the audit: its
        mechanism, its cheapest refutation, its prior art and its tier.</p>
        <p class="key"><em>Generation and audit belong in separate tools</em> —
        a generator that weighs its own idea tunes the scale to the idea.</p>
        <p class="links"><a href="https://xinmurat.github.io/Kiyas/">docs</a> ·
        <a href="https://github.com/XINMurat/Kiyas">repository</a></p>
      </article>

      <article class="card">
        <span class="verb">measures experience</span>
        <h3><a href="https://github.com/XINMurat/ux-mizan">ux-mizan</a></h3>
        <p>Carries Mizan's discipline into a domain where the evidence is
        <strong>behavioural</strong> rather than documentary: "users get lost",
        "this screen is confusing". Human-locked gates, metrics gated by
        application type, thresholds written in advance.</p>
        <p class="key"><em>A model cannot measure UX by reading code.</em> It can
        audit structural conformance and build the measuring rig; the evidence
        comes from real users.</p>
        <p class="links"><a href="https://xinmurat.github.io/ux-mizan/">docs</a> ·
        <a href="https://github.com/XINMurat/ux-mizan">repository</a></p>
      </article>

    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The handoff chain</h2>
    <p class="sub">The tools hand each other files, not prose.</p>

    <figure class="chain">
      <svg viewBox="0 0 720 250" role="img" aria-label="İskele hands a backlog to Mizan, Mizan hands refuted patterns to Kıyas, Kıyas hands seeds back to İskele, and ux-mizan hands measured findings into the backlog.">
        <defs>
          <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
          </marker>
        </defs>
        <g fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55" marker-end="url(#ar)">
          <path d="M186,66 H272"/>
          <path d="M446,66 H532"/>
          <path d="M646,96 V140 H120 V96"/>
          <path d="M272,192 H62 V96"/>
        </g>
        <g>
          <rect x="26" y="40" width="160" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="106" y="71" text-anchor="middle">İskele</text>
          <rect x="272" y="40" width="174" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="359" y="71" text-anchor="middle">Mizan</text>
          <rect x="532" y="40" width="160" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="612" y="71" text-anchor="middle">Kıyas</text>
          <rect x="272" y="166" width="174" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="359" y="197" text-anchor="middle">ux-mizan</text>
        </g>
        <g class="chain-txt" text-anchor="middle">
          <text x="229" y="56">backlog</text>
          <text x="489" y="56">refuted</text>
          <text x="176" y="185">findings</text>
          <text x="196" y="133">seeds</text>
        </g>
      </svg>
      <figcaption>One canonical loop: criteria become entries, refutations become
      constraints, surviving seeds become tasks.</figcaption>
    </figure>

    <ul class="plain">
      <li><strong>İskele → Mizan:</strong> acceptance criteria become
      preregistration entries (<code>iskele_to_registry.py</code>); every
      sentence claiming "verified" enters the counter-example sweep.</li>
      <li><strong>Mizan → Kıyas:</strong> refuted entries become negative
      constraints; Kıyas consults them before proposing a relative of something
      already refuted.</li>
      <li><strong>Kıyas → İskele:</strong> surviving seeds become backlog tasks
      (<code>kiyas_to_backlog.py</code>) — a seed is not a plan.</li>
      <li><strong>ux-mizan → İskele:</strong> measured UX findings re-enter the
      backlog as tasks carrying acceptance criteria of their own.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>The shared constants</h2>
    <p class="sub">The same few rules in all four — and what holds them together.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Constant</th><th>What it means</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>Evidence tiers</strong></td>
            <td><span class="tiers">[K]</span> proven · <span class="tiers">[H]</span>
            plausible hypothesis · <span class="tiers">[S]</span> speculative ·
            <span class="tiers">[R]</span> refuted · <span class="tiers">[KKE]</span>
            critical control missing · <span class="tiers">[Y]</span> misleading.
            No untagged assertions.</td>
          </tr>
          <tr>
            <td><strong>Threshold before result</strong></td>
            <td>A threshold written after the measurement has found whatever it
            was written to find.</td>
          </tr>
          <tr>
            <td><strong>Append-only</strong></td>
            <td>A refuted entry is never deleted. The <span class="tiers">[R]</span>
            rows are the method's own error rate.</td>
          </tr>
          <tr>
            <td><strong>Name the arbiter</strong></td>
            <td>"The model" is not an instrument. If the judge is the claim's own
            author, the claim is capped.</td>
          </tr>
          <tr>
            <td><strong>What carries a rule is a script</strong></td>
            <td>A rule protected only by prose can be negotiated away by the
            host's prose.</td>
          </tr>
          <tr>
            <td><strong>The skill runs inside someone else's setup</strong></td>
            <td>Do not comply quietly: say which instruction disabled which step.</td>
          </tr>
          <tr>
            <td><strong>An escape becomes a class</strong></td>
            <td>The one signal from outside — a user hit it, it broke in
            production, the idea came from outside the batch. Not merely counted:
            the check that should have caught it is named, or the check that now
            exists is written. A ramp in all four requires it.</td>
          </tr>
          <tr>
            <td><strong>What takes things apart puts them back</strong></td>
            <td>All four proceed by breaking work into parts — claims, tasks,
            flows, seeds — and anything that exists only while <strong>two</strong>
            parts hold at once is destroyed by that act. So all four run a
            re-assembly pass over pairs. In the auditing three it asks whether a
            guarantee still holds while both are live; in Kıyas, whether two
            candidates are two bets or one bet with two faces. The fragile
            classes: signals computed from an <strong>absence</strong>,
            guarantees enforced call site by call site, and seed lists resting on
            a single premise. A green test suite is not counter-evidence — tests
            are written per part.</td>
          </tr>
          <tr>
            <td><strong>A context with a budget</strong></td>
            <td>A skill costs tokens the way a dependency costs bytes: to
            everyone who installs it, on every cold start. In all four,
            <code>tools/token_budget.py</code> measures three tiers — the
            description that is in context in every session, the body, and the
            on-demand files — and enforces <strong>preregistered ceilings</strong>
            in CI. Raising a ceiling is a commit with a reason; growing silently
            is not one of the options.</td>
          </tr>
          <tr>
            <td><strong>Cost is measured, ROI is not claimed</strong></td>
            <td>All four can record what they spent — with the instrument, the
            window, the attribution and the <strong>comparison arm</strong>. With
            no arm the claim cannot be <span class="tiers">[K]</span>: what the
            work cost is a measurement, that the tool caused the difference is a
            claim. And each names the ratio it <strong>refuses</strong> to
            compute: Kıyas will not divide cost by seed count, ux-mizan will not
            divide by finding count — both would improve the number by rewarding
            the behaviour the discipline exists to prevent.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Current releases</h2>
    <p class="sub">A snapshot. Each repository's Releases page is what binds —
    the links go there.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Skill</th><th>Version</th><th>What is in it</th></tr></thead>
        <tbody>
          <tr>
            <td><a href="https://github.com/XINMurat/Iskele/releases/latest">İskele</a></td>
            <td><strong>v1.5.0</strong></td>
            <td>The expectation delta: a preregistered estimate against measured
            effort, with <code>estimate_basis</code> deciding what the number may
            be called · unit cost with two denominators ·
            <code>session_cost.py</code> · the pair pass (<code>Cift</code> sheet)
            · the ADR log</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/Mizan/releases/latest">Mizan</a></td>
            <td><strong>v2.6.0</strong></td>
            <td>R22: <code>cost_actual</code> — a cost claim names its
            instrument, window, attribution and comparison arm; an armless claim
            cannot be <span class="tiers">[K]</span> · the <code>probes</code>
            block and R19–R21 · R17, R18 · registry schema 1.9</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/Kiyas/releases/latest">Kıyas</a></td>
            <td><strong>v1.4.0</strong></td>
            <td>G14: the batch records what it cost — and cost per seed is
            deliberately not made easy; divide by surviving seeds instead · G13
            the pair pass · G12</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/ux-mizan/releases/latest">ux-mizan</a></td>
            <td><strong>v0.6</strong></td>
            <td>U14: the audit records its own cost, kept apart from every
            finding's tier — cost per finding refused · U13 the conjunction
            finding · U11/U12</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Install</h2>
    <p class="sub">Two ways, per skill.</p>
    <ul class="plain">
      <li><strong>Claude.ai / desktop / mobile:</strong> upload the
      <code>.skill</code> file from the repository's release
      (Settings → Capabilities → Skills).</li>
      <li><strong>Claude Code:</strong> copy the <code>skill/&lt;name&gt;/</code>
      folder into <code>~/.claude/skills/</code>. The path must end
      <code>~/.claude/skills/&lt;name&gt;/SKILL.md</code> — the most common
      mistake is a doubly nested folder.</li>
    </ul>
    <p class="note"><strong>You do not need to configure your assistant for this
    to work.</strong> No custom instructions, no system prompt, no house style.
    If a skill only behaves when your setup is arranged a particular way, that is
    a defect in the skill — please open an issue.</p>
  </div>
</section>

</div>

<div id="pane-tr" lang="tr" hidden>

<section class="hero">
  <div class="wrap">
    <h1>Dört fiil</h1>
    <p class="lede">Birbirini dürüst tutan dört Claude skill'i. Fiiller bilinçli
    olarak ayrıdır: biri yapıyı kurar, biri iddiaları tartar, biri adayları
    üretir, biri deneyimi ölçer. Karıştırılan fiil, hiçbirini iyi yapmayan tek
    bir araç üretir.</p>
    <ul class="verbs">
      <li><b>İskele</b> kurar</li>
      <li><b>Mizan</b> tartar</li>
      <li><b>Kıyas</b> üretir</li>
      <li><b>ux-mizan</b> deneyimi ölçer</li>
    </ul>
    <p class="canon">Bu sayfa ailenin kanonik tanımıdır; dört depo, her biri
    kendi başına bayatlayacak bir kopya taşımak yerine buraya işaret eder.</p>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Skill'ler</h2>
    <p class="sub">Her birine bir fiil, ve onu taşıyan fikir.</p>
    <div class="cards">

      <article class="card">
        <span class="verb">kurar</span>
        <h3><a href="https://github.com/XINMurat/Iskele">İskele</a></h3>
        <p>Belirsiz bir niyeti <strong>yürütülebilir ve izlenebilir</strong> bir
        iş sistemine çevirir: alan modeli, kapılı fazlar, atomik backlog,
        çalıştırılabilir kabul kriterleri, ve elle tahmin edilmek yerine
        çizelgeden <strong>hesaplanan</strong> ilerleme raporu.</p>
        <p class="key"><em>Her kabul kriteri, iş başlamadan önce yazılmış bir
        çürütme koşuludur</em> — bu yüzden backlog zaten bir önkayıt
        kümesidir.</p>
        <p class="links"><a href="https://xinmurat.github.io/Iskele/">doküman</a> ·
        <a href="https://github.com/XINMurat/Iskele">depo</a></p>
      </article>

      <article class="card">
        <span class="verb">tartar</span>
        <h3><a href="https://github.com/XINMurat/Mizan">Mizan</a></h3>
        <p>Herhangi bir iddia kümesini kanıt katmanlarıyla denetler ve yaşayan
        hipotez registry'leri tutar. Eşikler sonuçlardan <strong>önce</strong>
        kilitlenir; her hipotez bir çürütme koşulu taşır; reddedilen kayıt
        silinmez.</p>
        <p class="key"><em>Sayısal bir eşik, ancak hükmü veren hakem kadar
        güçlüdür</em> — hakem iddianın sahibiyse, o iddia kanıtlanmış
        sayılamaz.</p>
        <p class="links"><a href="https://xinmurat.github.io/Mizan/">doküman</a> ·
        <a href="https://github.com/XINMurat/Mizan">depo</a></p>
      </article>

      <article class="card">
        <span class="verb">üretir</span>
        <h3><a href="https://github.com/XINMurat/Kiyas">Kıyas</a></h3>
        <p>Tıkanmış bir problemde ilkeli fikir üretimi ve analojik çıkarım.
        Ürettiği her fikir denetime hazır biçimde çıkar: mekanizması, en ucuz
        çürütmesi, prior art'ı ve katmanıyla.</p>
        <p class="key"><em>Üretim ile denetim ayrı araçlarda kalmalı</em> —
        kendi fikrini tartan bir üreteç, tartısını fikrine göre ayarlar.</p>
        <p class="links"><a href="https://xinmurat.github.io/Kiyas/">doküman</a> ·
        <a href="https://github.com/XINMurat/Kiyas">depo</a></p>
      </article>

      <article class="card">
        <span class="verb">deneyimi ölçer</span>
        <h3><a href="https://github.com/XINMurat/ux-mizan">ux-mizan</a></h3>
        <p>Mizan'ın disiplinini, kanıtın belgesel değil
        <strong>davranışsal</strong> olduğu alana taşır: "kullanıcılar
        kayboluyor", "bu ekran karışık". İnsan-kilitli kapılar, uygulama tipine
        kapılı metrikler, önceden yazılmış eşikler.</p>
        <p class="key"><em>Bir model koda bakarak UX'i ölçemez.</em> Yapısal
        uygunluğu denetleyebilir ve ölçüm düzeneğini kurabilir; kanıtı gerçek
        kullanıcı üretir.</p>
        <p class="links"><a href="https://xinmurat.github.io/ux-mizan/">doküman</a> ·
        <a href="https://github.com/XINMurat/ux-mizan">depo</a></p>
      </article>

    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Devir zinciri</h2>
    <p class="sub">Araçlar birbirine dosya devreder, düzyazı değil.</p>

    <figure class="chain">
      <svg viewBox="0 0 720 250" role="img" aria-label="İskele backlog'u Mizan'a, Mizan çürütülenleri Kıyas'a, Kıyas tohumları İskele'ye devreder; ux-mizan ölçülmüş bulguları backlog'a verir.">
        <defs>
          <marker id="ar-tr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
          </marker>
        </defs>
        <g fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55" marker-end="url(#ar-tr)">
          <path d="M186,66 H272"/>
          <path d="M446,66 H532"/>
          <path d="M646,96 V140 H120 V96"/>
          <path d="M272,192 H62 V96"/>
        </g>
        <g>
          <rect x="26" y="40" width="160" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="106" y="71" text-anchor="middle">İskele</text>
          <rect x="272" y="40" width="174" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="359" y="71" text-anchor="middle">Mizan</text>
          <rect x="532" y="40" width="160" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="612" y="71" text-anchor="middle">Kıyas</text>
          <rect x="272" y="166" width="174" height="52" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
          <text class="chain-node" x="359" y="197" text-anchor="middle">ux-mizan</text>
        </g>
        <g class="chain-txt" text-anchor="middle">
          <text x="229" y="56">backlog</text>
          <text x="489" y="56">çürütülenler</text>
          <text x="176" y="185">bulgular</text>
          <text x="196" y="133">tohumlar</text>
        </g>
      </svg>
      <figcaption>Tek bir kanonik döngü: kriterler girdiye, çürütmeler kısıta,
      sağ kalan tohumlar göreve dönüşür.</figcaption>
    </figure>

    <ul class="plain">
      <li><strong>İskele → Mizan:</strong> kabul kriterleri önkayıt girdilerine
      dönüşür (<code>iskele_to_registry.py</code>); "doğrulandı" diyen her cümle
      karşı-örnek taramasına girer.</li>
      <li><strong>Mizan → Kıyas:</strong> reddedilen kayıtlar negatif kısıt olur;
      Kıyas, çürütülmüş bir şeyin akrabasını önermeden önce oraya bakar.</li>
      <li><strong>Kıyas → İskele:</strong> sağ kalan tohumlar backlog görevine
      dönüşür (<code>kiyas_to_backlog.py</code>) — bir tohum plan değildir.</li>
      <li><strong>ux-mizan → İskele:</strong> ölçülmüş UX bulguları, kendi kabul
      kriterini taşıyan görevler olarak backlog'a geri girer.</li>
    </ul>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Ortak sabitler</h2>
    <p class="sub">Dördünde de aynı birkaç kural — ve onları bir arada tutan şey.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Sabit</th><th>Ne demek</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>Kanıt katmanları</strong></td>
            <td><span class="tiers">[K]</span> kanıtlanmış ·
            <span class="tiers">[H]</span> makul hipotez ·
            <span class="tiers">[S]</span> spekülatif ·
            <span class="tiers">[R]</span> reddedildi ·
            <span class="tiers">[KKE]</span> kritik kontrol eksik ·
            <span class="tiers">[Y]</span> yanıltıcı. Etiketsiz iddia yok.</td>
          </tr>
          <tr>
            <td><strong>Önce eşik, sonra sonuç</strong></td>
            <td>Ölçümden sonra yazılan eşik, bulmak için yazıldığı şeyi bulmuş
            olur.</td>
          </tr>
          <tr>
            <td><strong>Yalnızca ekleme</strong></td>
            <td>Reddedilen kayıt silinmez. <span class="tiers">[R]</span>
            satırları yöntemin kendi hata payıdır.</td>
          </tr>
          <tr>
            <td><strong>Hakemi adlandır</strong></td>
            <td>"Model" bir ölçüm aracı değildir. Hakem iddianın sahibiyse iddia
            tavanlıdır.</td>
          </tr>
          <tr>
            <td><strong>Kuralı taşıyan şey betiktir</strong></td>
            <td>Yalnızca düzyazıyla korunan kural, host'un düzyazısıyla pazarlık
            edilebilir.</td>
          </tr>
          <tr>
            <td><strong>Skill başkasının kurulumunda koşar</strong></td>
            <td>Sessizce uyma: hangi talimatın hangi adımı devre dışı bıraktığını
            söyle.</td>
          </tr>
          <tr>
            <td><strong>Kaçan, sınıfa dönüşür</strong></td>
            <td>Dışarıdan gelen tek sinyal — kullanıcının bulduğu, üretimde
            patlayan, batch'in dışından gelen. Yalnızca sayılmaz: onu yakalaması
            gereken kontrol adlandırılır, yoksa artık var olan kontrol yazılır.
            Dördünde de bir rampa bunu zorunlu kılar.</td>
          </tr>
          <tr>
            <td><strong>Parçalayan, geri birleştirir</strong></td>
            <td>Dördü de işi parçalara ayırarak ilerler — iddialar, görevler,
            akışlar, tohumlar — ve yalnızca <strong>iki</strong> parça aynı anda
            geçerliyken var olan şey tam o eylemle yok olur. Bu yüzden dördünde
            de sonda bir çift pası vardır. Denetim yapan üçünde soru "bu garanti
            ikisi birden etkinken hâlâ geçerli mi?", Kıyas'ta "bunlar iki bahis
            mi, iki yüzü olan tek bahis mi?" olur. Kırılgan sınıflar: bir
            <strong>yokluktan</strong> hesaplanan sinyaller, tek tek çağrı
            yerinde uygulanan garantiler, ve tek bir öncüle dayanan tohum
            listeleri. Yeşil test paketi karşı kanıt değildir — testler parça
            başına yazılır.</td>
          </tr>
          <tr>
            <td><strong>Bütçesi olan bir bağlam</strong></td>
            <td>Bir skill, bir bağımlılığın bayt harcadığı gibi token harcar:
            kuran herkese, her soğuk başlangıçta. Dördünde de
            <code>tools/token_budget.py</code> üç katmanı ölçer — her oturumda
            bağlamda olan açıklama, gövde, ve talep üzerine okunanlar — ve
            <strong>önkayıtlı tavanları</strong> CI'da uygular. Tavanı
            yükseltmek gerekçeli bir commit'tir; sessizce büyümek seçeneklerden
            biri değildir.</td>
          </tr>
          <tr>
            <td><strong>Maliyet ölçülür, ROI iddia edilmez</strong></td>
            <td>Dördü de ne harcadığını kaydedebilir — enstrümanıyla,
            penceresiyle, atfıyla ve <strong>karşılaştırma koluyla</strong>. Kol
            yoksa iddia <span class="tiers">[K]</span> olamaz: işin ne kadara mal
            olduğu ölçümdür, farkı aracın yarattığı iddiadır. Ve her biri kendi
            <strong>reddettiği oranı</strong> adlandırır: Kıyas tohum başına
            maliyeti bölmez, ux-mizan bulgu başına maliyeti — ikisi de sayıyı,
            disiplinin önlemek için var olduğu davranışı ödüllendirerek
            iyileştirir.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Şu anki sürümler</h2>
    <p class="sub">Anlık görüntü. Bağlayıcı olan her deponun Releases sayfasıdır
    — bağlantılar oraya gider.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Skill</th><th>Sürüm</th><th>İçinde ne var</th></tr></thead>
        <tbody>
          <tr>
            <td><a href="https://github.com/XINMurat/Iskele/releases/latest">İskele</a></td>
            <td><strong>v1.5.0</strong></td>
            <td>Beklenti sapması: önkayıtlı tahmine karşı ölçülmüş efor,
            <code>estimate_basis</code> sayının ne olarak adlandırılabileceğine
            karar verir · iki paydalı birim maliyet ·
            <code>session_cost.py</code> · çift pası (<code>Cift</code> sekmesi)
            · ADR defteri</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/Mizan/releases/latest">Mizan</a></td>
            <td><strong>v2.6.0</strong></td>
            <td>R22: <code>cost_actual</code> — maliyet iddiası enstrümanını,
            penceresini, atfını ve karşılaştırma kolunu adlandırır; kolsuz iddia
            <span class="tiers">[K]</span> olamaz · <code>probes</code> bloğu ve
            R19–R21 · R17, R18 · registry şeması 1.9</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/Kiyas/releases/latest">Kıyas</a></td>
            <td><strong>v1.4.0</strong></td>
            <td>G14: parti ne harcadığını kaydeder — ve tohum başına maliyet
            bilerek kolaylaştırılmaz; onun yerine hayatta kalan tohuma bölünür ·
            G13 çift pası · G12</td>
          </tr>
          <tr>
            <td><a href="https://github.com/XINMurat/ux-mizan/releases/latest">ux-mizan</a></td>
            <td><strong>v0.6</strong></td>
            <td>U14: denetim kendi maliyetini kaydeder, her bulgunun katmanından
            ayrı tutularak — bulgu başına maliyet reddedilir · U13 bileşim
            bulgusu · U11/U12</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <h2>Kurulum</h2>
    <p class="sub">Skill başına iki yol.</p>
    <ul class="plain">
      <li><strong>Claude.ai / masaüstü / mobil:</strong> deponun release'indeki
      <code>.skill</code> dosyasını yükleyin
      (Ayarlar → Yetenekler → Skills).</li>
      <li><strong>Claude Code:</strong> <code>skill/&lt;ad&gt;/</code> klasörünü
      <code>~/.claude/skills/</code> içine kopyalayın. Yol
      <code>~/.claude/skills/&lt;ad&gt;/SKILL.md</code> ile bitmeli — en sık hata
      çift iç içe klasördür.</li>
    </ul>
    <p class="note"><strong>Bunun çalışması için asistanınızı yapılandırmanız
    gerekmez.</strong> Özel talimat yok, sistem promptu yok, ev stili yok. Bir
    skill yalnızca kurulumunuz belirli bir şekilde ayarlandığında düzgün
    davranıyorsa, bu skill'in kusurudur — lütfen issue açın.</p>
  </div>
</section>

</div>
