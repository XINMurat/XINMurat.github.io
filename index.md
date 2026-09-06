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
      <svg viewBox="0 0 850 300" role="img" aria-label="Material enters at Mizan — a document or a chat, a repo or legacy code, a project already running, or the output of an earlier Mizan mode — and it can enter at any turn, not only at the start. Mizan and Kıyas exchange in both directions: gaps and refuted patterns go to Kıyas, seeds come back as preregistered hypotheses. That pair can run on its own. When something survives and is worth building, İskele takes it, and İskele's acceptance criteria return to Mizan as entries. ux-mizan hands measured findings both into the backlog and back into the audit.">
        <defs>
          <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
          </marker>
        </defs>
        <g class="chain-inlet">
          <rect x="6" y="14" width="184" height="88" rx="12" fill="currentColor" fill-opacity=".035" stroke="currentColor" stroke-opacity=".45" stroke-width="1.3" stroke-dasharray="6 4"/>
          <text class="chain-cap" x="98" y="8" text-anchor="middle">INPUT — AT ANY TURN</text>
          <text class="chain-in" x="98" y="38" text-anchor="middle">a document or a chat,</text>
          <text class="chain-in" x="98" y="55" text-anchor="middle">a repo, legacy code,</text>
          <text class="chain-in" x="98" y="72" text-anchor="middle">a running project,</text>
          <text class="chain-in" x="98" y="89" text-anchor="middle">an earlier mode&#39;s output</text>
        </g>
        <g transform="translate(70,0)">
          <g fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55" marker-end="url(#ar)">
            <path d="M124,58 H192"/>
            <path d="M350,46 H426"/>
            <path d="M426,74 H350"/>
            <path d="M388,90 V176"/>
            <path d="M313,208 H240 V90"/>
            <path d="M556,208 H467"/>
            <path d="M635,176 V140 H505 V90"/>
          </g>
          <g>
            <rect x="192" y="30" width="158" height="60" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="271" y="66" text-anchor="middle">Mizan</text>
            <rect x="426" y="30" width="150" height="60" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="501" y="66" text-anchor="middle">Kıyas</text>
            <rect x="313" y="176" width="154" height="56" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="390" y="209" text-anchor="middle">İskele</text>
            <rect x="556" y="176" width="154" height="56" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="633" y="209" text-anchor="middle">ux-mizan</text>
          </g>
          <g class="chain-txt" text-anchor="middle">
            <text x="388" y="24">gaps · refuted</text>
            <text x="398" y="112" text-anchor="start">seeds → preregistered</text>
            <text x="398" y="152" text-anchor="start">worth building</text>
            <text x="200" y="152" text-anchor="start">criteria</text>
            <text x="512" y="200">tasks</text>
            <text x="560" y="134">findings</text>
          </g>
        </g>
      </svg>
      <figcaption>Two loops, not one ring. Mizan and Kıyas can go round on their
      own for as long as the thinking needs — İskele is entered when something
      survives and is worth building, not on the way past. The dashed box is not
      a starting gun: material enters at Mizan on any turn, and what an earlier
      mode produced is legitimate material for the next one.</figcaption>
    </figure>

    <ul class="plain">
      <li><strong>You → Mizan:</strong> the entry, and the one arrow that starts
      outside the system. Something you already have gets atomized into claims
      and tiered — an AI conversation, an article, an old note, a rough idea,
      but equally <strong>a repository, a legacy codebase, a project already
      under way</strong>: that is what modes 3–5 are for, and in an undocumented
      project the audit report <em>is</em> the documentation. What an earlier
      mode produced — a gap map, a bug registry, a gated PRD — re-enters the
      same way. What survives is <code>[H]</code>; what does not is recorded
      rather than deleted.</li>
      <li><strong>The entry is not a one-time event.</strong> The dashed box is
      not the start of a pipeline: while the loop is turning, a new idea, a new
      document, a fresh piece of code can enter at Mizan on any turn. The
      registry is append-only precisely so that late material joins what is
      already there instead of restarting it.</li>
      <li><strong>Mizan ⇄ Kıyas — the inner loop.</strong> The audit's gap map
      and its refuted entries become Kıyas's brief and its negative constraints;
      Kıyas's surviving seeds come back as preregistered entries, already
      carrying the arbiter the registry will demand
      (<code>mizan_export_refuted.py</code> one way, the registry-entry shape
      the other). <strong>This pair can go round on its own, many times, with no
      project in sight</strong> — which is what happens when the domain shifts,
      when a case turns out to be special, or when the honest answer is still
      being looked for.</li>
      <li><strong>→ İskele, when it is worth building.</strong> Surviving seeds
      become backlog tasks (<code>kiyas_to_backlog.py</code>) — a seed is not a
      plan, and not every seed earns a project. İskele is a branch off the inner
      loop, not a station on the way.</li>
      <li><strong>İskele → Mizan:</strong> acceptance criteria become
      preregistration entries (<code>iskele_to_registry.py</code>); every
      sentence claiming "verified" enters the counter-example sweep. This is the
      arrow that closes the outer loop.</li>
      <li><strong>ux-mizan → both.</strong> A measured finding is two things at
      once: a task for the backlog, and a claim about the application. The first
      goes to İskele with its own acceptance criteria; the second re-enters the
      inner loop — as an entry for Mizan when it needs tiering, or as the brief
      for Kıyas when the question is <em>why</em> users do that.</li>
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

<div id="pane-tr" lang="tr" class="pane-init">

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
      <svg viewBox="0 0 850 300" role="img" aria-label="Malzeme Mizan'a girer — bir doküman ya da sohbet, bir repo ya da legacy kod, hâlihazırda süren bir proje, ya da daha önceki bir Mizan modunun çıktısı — ve yalnızca başta değil, her turda girebilir. Mizan ile Kıyas iki yönde alışveriş eder: boşluklar ve çürütülenler Kıyas'a gider, tohumlar önkayıtlı hipotez olarak geri döner. Bu çift kendi başına dönebilir. Sağ kalan bir şey inşa edilmeye değdiğinde İskele devreye girer ve kabul kriterleri Mizan'a girdi olarak döner. ux-mizan ölçülmüş bulguları hem backlog'a hem denetime verir.">
        <defs>
          <marker id="ar-tr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
          </marker>
        </defs>
        <g class="chain-inlet">
          <rect x="6" y="14" width="184" height="88" rx="12" fill="currentColor" fill-opacity=".035" stroke="currentColor" stroke-opacity=".45" stroke-width="1.3" stroke-dasharray="6 4"/>
          <text class="chain-cap" x="98" y="8" text-anchor="middle">GİRDİ — HER TURDA</text>
          <text class="chain-in" x="98" y="38" text-anchor="middle">doküman, sohbet, fikir,</text>
          <text class="chain-in" x="98" y="55" text-anchor="middle">repo, legacy kod,</text>
          <text class="chain-in" x="98" y="72" text-anchor="middle">süren bir proje,</text>
          <text class="chain-in" x="98" y="89" text-anchor="middle">önceki modun çıktısı</text>
        </g>
        <g transform="translate(70,0)">
          <g fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55" marker-end="url(#ar-tr)">
            <path d="M124,58 H192"/>
            <path d="M350,46 H426"/>
            <path d="M426,74 H350"/>
            <path d="M388,90 V176"/>
            <path d="M313,208 H240 V90"/>
            <path d="M556,208 H467"/>
            <path d="M635,176 V140 H505 V90"/>
          </g>
          <g>
            <rect x="192" y="30" width="158" height="60" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="271" y="66" text-anchor="middle">Mizan</text>
            <rect x="426" y="30" width="150" height="60" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="501" y="66" text-anchor="middle">Kıyas</text>
            <rect x="313" y="176" width="154" height="56" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="390" y="209" text-anchor="middle">İskele</text>
            <rect x="556" y="176" width="154" height="56" rx="10" fill="none" stroke="currentColor" opacity=".35"/>
            <text class="chain-node" x="633" y="209" text-anchor="middle">ux-mizan</text>
          </g>
          <g class="chain-txt" text-anchor="middle">
            <text x="388" y="24">boşluklar · çürütülenler</text>
            <text x="398" y="112" text-anchor="start">tohumlar → önkayıt</text>
            <text x="398" y="152" text-anchor="start">inşa etmeye değer</text>
            <text x="200" y="152" text-anchor="start">kriterler</text>
            <text x="512" y="200">görevler</text>
            <text x="560" y="134">bulgular</text>
          </g>
        </g>
      </svg>
      <figcaption>Tek halka değil, iki döngü. Mizan ile Kıyas, düşünme ne kadar
      sürerse o kadar kendi aralarında dönebilir — İskele, sağ kalan bir şey inşa
      edilmeye değdiğinde devreye girer; yol üstünde uğranan bir durak değil.
      Kesik çizgili kutu bir başlangıç işareti değildir: malzeme Mizan'a her
      turda girebilir ve önceki bir modun ürettiği şey bir sonrakinin meşru
      malzemesidir.</figcaption>
    </figure>

    <ul class="plain">
      <li><strong>Siz → Mizan:</strong> giriş, ve sistemin dışından başlayan tek
      ok. Elinizde zaten olan bir şey iddialara ayrılır ve katmanlanır — bir YZ
      sohbeti, bir makale, eski bir not, ham bir fikir, ama aynı ölçüde
      <strong>bir repo, bir legacy kod tabanı, hâlihazırda süren bir
      proje</strong>: 3–5. modlar tam bunun için, ve dokümansız bir projede
      denetim raporunun kendisi <em>dokümantasyondur</em>. Önceki bir modun
      ürettiği şey — boşluk haritası, bug registry'si, kapıdan geçmiş bir PRD —
      aynı yoldan yeniden girer. Ayakta kalan <code>[H]</code> olur; kalmayan
      silinmez, kaydedilir.</li>
      <li><strong>Giriş tek seferlik değildir.</strong> Kesik çizgili kutu bir
      hattın başlangıcı değil: döngü dönerken yeni bir fikir, yeni bir doküman,
      taze bir kod parçası her turda Mizan'a girebilir. Registry'nin
      yalnızca-eklenir olmasının sebebi tam da bu — sonradan gelen malzeme var
      olanı sıfırlamaz, ona katılır.</li>
      <li><strong>Mizan ⇄ Kıyas — iç döngü.</strong> Denetimin boşluk haritası
      ve reddedilen kayıtları Kıyas'ın brief'i ve negatif kısıtları olur;
      Kıyas'ın sağ kalan tohumları, registry'nin isteyeceği hakemi zaten
      taşıyarak önkayıt girdisi olarak geri döner
      (<code>mizan_export_refuted.py</code> bir yöne, registry-girdi biçimi
      diğerine). <strong>Bu çift, ortada hiçbir proje yokken kendi arasında
      defalarca dönebilir</strong> — alan farklılaştığında, bir vaka özel
      çıktığında, ya da dürüst cevap hâlâ aranırken olan tam budur.</li>
      <li><strong>→ İskele, inşa etmeye değdiğinde.</strong> Sağ kalan tohumlar
      backlog görevine dönüşür (<code>kiyas_to_backlog.py</code>) — bir tohum
      plan değildir ve her tohum bir projeyi hak etmez. İskele, iç döngüden
      çıkan bir <em>dal</em>dır; yol üstünde uğranan bir durak değil.</li>
      <li><strong>İskele → Mizan:</strong> kabul kriterleri önkayıt girdilerine
      dönüşür (<code>iskele_to_registry.py</code>); "doğrulandı" diyen her cümle
      karşı-örnek taramasına girer. Dış döngüyü kapatan ok budur.</li>
      <li><strong>ux-mizan → ikisine birden.</strong> Ölçülmüş bir bulgu aynı
      anda iki şeydir: backlog için bir görev, ve uygulama hakkında bir iddia.
      Birincisi kendi kabul kriteriyle İskele'ye gider; ikincisi iç döngüye
      girer — katmanlanması gerekiyorsa Mizan'a girdi, soru <em>kullanıcılar
      bunu neden yapıyor</em> ise Kıyas'a brief olarak.</li>
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
