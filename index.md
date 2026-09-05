---
title: "Dört fiil"
description: "İskele kurar · Mizan tartar · Kıyas üretir · ux-mizan deneyimi ölçer"
---

# Dört fiil

**Birbirini dürüst tutan dört Claude skill'i.** Fiiller bilinçli olarak
ayrıdır: biri yapıyı kurar, biri iddiaları tartar, biri adayları üretir, biri
deneyimi ölçer. Karıştırılan fiil, hiçbirini iyi yapmayan tek bir araç üretir.

> **İskele kurar · Mizan tartar · Kıyas üretir · ux-mizan deneyimi ölçer**

*Bu sayfa ailenin kanonik tanımıdır; depolar buraya işaret eder.*
*(English below.)*

---

## Skill'ler

### [İskele](https://github.com/XINMurat/Iskele) — kurar

Belirsiz bir niyeti **yürütülebilir ve izlenebilir** bir iş sistemine çevirir:
alan modeli, kapılı fazlar, atomik backlog, çalıştırılabilir kabul kriterleri,
ve elle tahmin edilmek yerine çizelgeden **hesaplanan** ilerleme raporu.

Kilit fikir: *her kabul kriteri, iş başlamadan önce yazılmış bir çürütme
koşuludur.* Bu yüzden backlog zaten bir önkayıt kümesidir.

[Doküman](https://xinmurat.github.io/Iskele/) · [Depo](https://github.com/XINMurat/Iskele)

### [Mizan](https://github.com/XINMurat/Mizan) — tartar

Herhangi bir iddia kümesini kanıt katmanlarıyla denetler ve yaşayan hipotez
registry'leri tutar. Eşikler sonuçlardan **önce** kilitlenir; her hipotez bir
çürütme koşulu taşır; reddedilen kayıt silinmez.

Kilit fikir: *sayısal bir eşik, ancak hükmü veren hakem kadar güçlüdür.*
Hakem iddianın sahibiyse, o iddia kanıtlanmış sayılamaz.

[Doküman](https://xinmurat.github.io/Mizan/) · [Depo](https://github.com/XINMurat/Mizan)

### [Kıyas](https://github.com/XINMurat/Kiyas) — üretir

Tıkanmış bir problemde ilkeli fikir üretimi ve analojik çıkarım. Ürettiği her
fikir, denetime hazır biçimde çıkar: mekanizması, en ucuz çürütmesi ve
katmanıyla.

Kilit fikir: *üretim ile denetim ayrı araçlarda kalmalı* — kendi fikrini
tartan bir üreteç, tartısını fikrine göre ayarlar.

[Doküman](https://xinmurat.github.io/Kiyas/) · [Depo](https://github.com/XINMurat/Kiyas)

### [ux-mizan](https://github.com/XINMurat/ux-mizan) — deneyimi ölçer

Mizan'ın disiplinini, kanıtın belgesel değil **davranışsal** olduğu alana
taşır: "kullanıcılar kayboluyor", "bu ekran karışık". İnsan-kilitli kapılar,
uygulama tipine kapılı metrikler, ve önceden yazılmış eşikler.

Kilit fikir: *bir model koda bakarak UX'i ölçemez.* Yapısal uygunluğu
denetleyebilir ve ölçüm düzeneğini kurabilir; kanıtı gerçek kullanıcı üretir.
**Hakem yazarsa kanıtlanmış yoktur.**

[Doküman](https://xinmurat.github.io/ux-mizan/) · [Depo](https://github.com/XINMurat/ux-mizan)

---

## Devir zinciri

Araçlar birbirine dosya devreder, düzyazı değil:

```
İskele ──backlog──> Mizan ──çürütülenler──> Kıyas ──tohumlar──> İskele
   │                                                              ▲
   └──────────── ux-mizan bulguları backlog'a görev olarak ────────┘
```

- **İskele → Mizan:** kabul kriterleri önkayıt girdilerine dönüşür
  (`iskele_to_registry.py`); "doğrulandı" diyen her cümle karşı-örnek
  taramasına girer.
- **Mizan → Kıyas:** reddedilen kayıtlar negatif kısıt olur; Kıyas
  çürütülmüş bir şeyin akrabasını önermeden önce oraya bakar.
- **Kıyas → İskele:** sağ kalan tohumlar backlog görevine dönüşür
  (`kiyas_to_backlog.py`) — bir tohum plan değildir.
- **ux-mizan → İskele:** ölçülmüş UX bulguları, kabul kriteri taşıyan
  görevler olarak geri girer.

---

## Ortak sabitler

Dördü de aynı birkaç kuralı paylaşır — ve bu kurallar araçları bir arada
tutan şeydir:

| Sabit | Ne demek |
|---|---|
| **Kanıt katmanları** | `[K]` kanıtlanmış · `[H]` makul hipotez · `[S]` spekülatif · `[R]` reddedildi · `[KKE]` kritik kontrol eksik · `[Y]` yanıltıcı. Etiketsiz iddia yok. |
| **Önce eşik, sonra sonuç** | Ölçümden sonra yazılan eşik, kendi bulduğunu bulmuş olur. |
| **Yalnızca ekleme** | Reddedilen kayıt silinmez. `[R]` satırları yöntemin kendi hata payıdır. |
| **Hakemi adlandır** | "Model" bir ölçüm aracı değildir. Hakem yazarın kendisiyse iddia tavanlıdır. |
| **Kuralı taşıyan şey betiktir** | Yalnızca düzyazıyla korunan kural, host'un düzyazısıyla pazarlık edilebilir. |
| **Skill başkasının kurulumunda koşar** | Sessizce uyma; hangi talimatın hangi adımı devre dışı bıraktığını söyle. |
| **Kaçan, sınıfa dönüşür** | Dışarıdan gelen tek sinyal — kullanıcının bulduğu, üretimde patlayan, batch'in dışından gelen. Sayılmakla kalmaz: onu yakalaması gereken kontrol adlandırılır, yoksa artık var olan kontrol yazılır. Dördünde de bir rampa bunu zorunlu kılar. |
| **Parçalayan, geri birleştirir** | Dördü de işi parçalara ayırarak ilerler — denetim iddiaları, plan görevleri, walkthrough akışları, üretim tohumları — ve yalnızca **iki parça aynı anda geçerliyken** var olan özellik tam o anda görünmez olur. Dördünde de sonda bir birleştirme pası var: her parça için dokunabildiği diğer parçalar, ve her çift için tek soru. Denetimde bu *"bu garanti hâlâ geçerli mi?"*, üretimde *"bunlar iki bahis mi, yoksa iki yüzü olan tek bahis mi?"* diye sorulur. En kırılganları: bir **yokluktan** hesaplanan sinyaller, tek tek çağrı yerinde uygulanan garantiler, ve tek bir öncüle dayanan tohum listeleri. Yeşil test paketi burada karşı kanıt değildir. Dördünde de pasın sonucunu yazacak bir alan var — kaydı olmayan pas, koşulmamış pastan ayırt edilemez. |

---

## Şu anki sürümler

| Skill | Sürüm | Bu sürümde ne var |
|---|---|---|
| [İskele](https://github.com/XINMurat/Iskele/releases/latest) | **v1.3.0** | Çift pası çizelgede bir yer kazandı (`Cift` sekmesi, `GEN:CIFT` bölgesi) · faz-kapanış çizelgesi · ADR defteri · `AGENTS.md` · rampalar `RR-00`…`RR-13` |
| [Mizan](https://github.com/XINMurat/Mizan/releases/latest) | **v2.5.0** | `probes` bloğu ve R19–R21: alan probu, bileşim pası, kaçak→sınıf döngüsü · R17 (duran girdiye son tarih) · R18 (önkayıt ne kilitlediğini söyler) · registry şeması 1.8 |
| [Kıyas](https://github.com/XINMurat/Kiyas/releases/latest) | **v1.3.0** | G13, çift pası: parti tohum tohum değil çift çift işaretlenir; hüküm satırı *N aday, K bağımsız bahis* basar · G12 ve rampalar (v1.2) |
| [ux-mizan](https://github.com/XINMurat/ux-mizan/releases/latest) | **v0.5** | U13: yalnızca iki akış aynı anda etkinken var olan kusur artık kaydedilebiliyor · U11/U12 · kayıp/ölü tık tanımları · rampalar ve R-13 |

Bu tablo bir anlık görüntüdür; bağlayıcı olan her deponun **Releases**
sayfasıdır — yukarıdaki bağlantılar oraya, en son sürüme gider.

---

## Kurulum

Her skill iki yolla kurulur:

- **Claude.ai / masaüstü / mobil:** deponun release'indeki `.skill` dosyasını
  yükleyin (Ayarlar → Yetenekler → Skills).
- **Claude Code:** `skill/<ad>/` klasörünü `~/.claude/skills/` içine
  kopyalayın. Yol `~/.claude/skills/<ad>/SKILL.md` olmalı — en sık hata çift
  iç içe klasördür.

Lisans: kod MIT, düzyazı CC BY 4.0 (her depoda ayrıntılı).

---

# Four verbs

**Four Claude skills that keep each other honest.** The verbs are kept apart
on purpose: one builds the structure, one weighs the claims, one generates the
candidates, one measures the experience. A conflated verb produces a single
tool that does none of them well.

> **İskele builds · Mizan weighs · Kıyas generates · ux-mizan measures experience**

*This page is the family's canonical description; the repositories point here.*

### [İskele](https://github.com/XINMurat/Iskele) — builds

Turns a vague intent into an **executable, trackable** system of work: domain
model, gated phases, an atomic backlog, executable acceptance criteria, and a
progress report **computed** from a tracker rather than estimated by hand.

The key idea: *every acceptance criterion is a refutation condition written
before the work started.* Which makes the backlog a preregistration set
already.

### [Mizan](https://github.com/XINMurat/Mizan) — weighs

Audits any claim set with evidence tiers and maintains living hypothesis
registries. Thresholds lock **before** results; every hypothesis carries a
refutation condition; a refuted entry is never deleted.

The key idea: *a numeric threshold is only as strong as the judge that returns
its verdict.* If the judge is the claim's own author, the claim cannot count
as proven.

### [Kıyas](https://github.com/XINMurat/Kiyas) — generates

Disciplined ideation and analogical inference for a problem that is stuck.
Every idea it produces arrives shaped for the audit: its mechanism, its
cheapest refutation, and its tier.

The key idea: *generation and audit belong in separate tools* — a generator
that weighs its own idea tunes the scale to the idea.

### [ux-mizan](https://github.com/XINMurat/ux-mizan) — measures experience

Carries Mizan's discipline into a domain where the evidence is **behavioural**
rather than documentary: "users get lost", "this screen is confusing".
Human-locked gates, metrics gated by application type, thresholds written in
advance.

The key idea: *a model cannot measure UX by reading code.* It can audit
structural conformance and build the measuring rig; the evidence comes from
real users. **If the referee writes it, there is no proof.**

### The handoff chain

The tools hand each other files, not prose: İskele's acceptance criteria
become Mizan preregistration entries; Mizan's refuted entries become negative
constraints Kıyas consults; Kıyas's surviving seeds become İskele backlog
tasks; and ux-mizan's measured findings re-enter that backlog as tasks with
acceptance criteria of their own.

### The shared constants

The same six evidence tiers (`[K] [H] [S] [R] [KKE] [Y]`); thresholds locked
before results; append-only history where refuted entries stay on the record;
every threshold names its arbiter; the rule that must survive an unknown host
goes in a script, not in a paragraph; and each skill states the conflict when
a host's instructions disable part of its method, instead of complying
quietly.

And one shared move rather than a rule: **what takes things apart puts them
back.** All four proceed by breaking work into parts — an audit atomizes
claims, a plan atomizes tasks, a walkthrough takes one flow at a time, a
generator draws one seed at a time — and anything that exists only while
**two** parts hold at once is destroyed by that very act. So all four run a
re-assembly pass at the end, over pairs. In the auditing three it asks whether
a guarantee still holds while both are live; in Kıyas it asks whether two
candidates are two bets or one bet with two faces. The fragile classes are
signals computed from an **absence**, guarantees enforced call site by call
site, and seed lists resting on a single premise. A green test suite is not
counter-evidence: tests are written per part.

One more, and it is the only one that comes from outside the method: **an escape becomes a class.** When something gets past a tool — a user hits it, it breaks in production, the idea arrives from outside the batch — each tool has a ramp that refuses to close on the fix alone. It asks which check should have caught it, and if none exists, the check that now does gets written. A count of escapes is not a feedback loop; naming the class is.

### Current releases

[İskele **v1.3.0**](https://github.com/XINMurat/Iskele/releases/latest) ·
[Mizan **v2.5.0**](https://github.com/XINMurat/Mizan/releases/latest) ·
[Kıyas **v1.3.0**](https://github.com/XINMurat/Kiyas/releases/latest) ·
[ux-mizan **v0.5**](https://github.com/XINMurat/ux-mizan/releases/latest)

A snapshot; each repository's Releases page is what binds, and the links above
go there.

### Install

Upload the release's `.skill` file (Claude.ai / desktop / mobile), or copy
`skill/<name>/` into `~/.claude/skills/` for Claude Code — the path must end
`~/.claude/skills/<name>/SKILL.md`.

Code is MIT; prose is CC BY 4.0. Details in each repository.
