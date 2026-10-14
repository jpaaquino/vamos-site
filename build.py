#!/usr/bin/env python3
"""Generates the static site. Rename the app or fill placeholders HERE, then run: python3 build.py"""
import os
APP = "¡Vamos!"                      # store name may become "Vamos Espanha!" — change only here
OWNER = "[NOME DO RESPONSÁVEL / EMPRESA]"
NIF = "[NIF/NIE]"
ADDR = "[ENDEREÇO]"
EMAIL = "[E-MAIL DE CONTATO]"
DATE_PT = "14 de outubro de 2026"
DATE_EN = "October 14, 2026"
ROOT = os.path.dirname(os.path.abspath(__file__))

CSS = """
:root{--red:#D7263D;--yellow:#FFC233;--orange:#FF7A3D;--cream:#FFF6E9;--green:#2BB673;--ink:#2D1E2F;--terra:#B4532A;--teal:#1B998B}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}
a{color:var(--teal)}
header{display:flex;align-items:center;justify-content:space-between;padding:14px 18px;max-width:1040px;margin:auto}
.logo{font-weight:900;font-size:1.4rem;color:var(--red);text-decoration:none}
nav a{margin-left:14px;font-weight:700;text-decoration:none;color:var(--ink);font-size:.95rem}
nav .lang{background:var(--ink);color:#fff;padding:4px 10px;border-radius:999px}
.hero{max-width:1040px;margin:auto;padding:20px 18px 40px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px}
.hero img{width:180px}
h1{font-size:2rem;line-height:1.15;margin:.3em 0}
.hero p{font-size:1.1rem;max-width:560px}
.badges{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:10px}
.badge{display:flex;flex-direction:column;align-items:flex-start;background:var(--ink);color:#fff;border-radius:12px;padding:8px 16px;min-width:170px;opacity:.9;cursor:default}
.badge small{font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;color:var(--yellow)}
.badge b{font-size:1.1rem}
.stripe{height:10px;background:linear-gradient(90deg,var(--red) 0 25%,var(--yellow) 25% 75%,var(--red) 75%)}
section{max-width:1040px;margin:auto;padding:36px 18px}
.features{display:grid;gap:14px;grid-template-columns:1fr}
.card{background:#fff;border-radius:18px;padding:18px;border:2px solid #0001}
.card h3{margin:.2em 0}
.shots{display:flex;gap:14px;overflow-x:auto;padding-bottom:10px;scroll-snap-type:x mandatory}
.shots img{width:220px;border-radius:22px;box-shadow:0 6px 18px #0002;scroll-snap-align:center;flex:none}
.contact{text-align:center}
footer{background:var(--ink);color:#fff;padding:24px 18px;text-align:center;font-size:.9rem}
footer a{color:var(--yellow);margin:0 8px}
.doc{max-width:780px;margin:auto;padding:10px 18px 50px}
.doc h1{font-size:1.7rem}.doc h2{font-size:1.2rem;margin-top:1.8em;color:var(--terra)}
.doc table{border-collapse:collapse;width:100%;font-size:.9rem;background:#fff}
.doc td,.doc th{border:1px solid #0002;padding:6px 8px;vertical-align:top;text-align:left}
.ph{background:#fff3b0;padding:0 3px;border-radius:4px}
.meta{color:#6b5a6e}
@media(min-width:760px){h1{font-size:2.8rem}.hero{flex-direction:row;text-align:left;justify-content:center}.hero img{width:260px}.badges{justify-content:flex-start}.features{grid-template-columns:repeat(3,1fr)}.shots{justify-content:center}}
"""

def ph(s): return f'<span class="ph">{s}</span>'

def page(lang, path, title, body, alt):
    pre = "../" if lang == "en" else ""
    home = "index.html"
    if lang == "pt":
        nav = f'<a href="privacidade.html">Privacidade</a><a href="termos.html">Termos</a><a class="lang" href="{alt}" hreflang="en">EN</a>'
        foot = f'<a href="index.html">Início</a><a href="privacidade.html">Política de Privacidade</a><a href="termos.html">Termos e Condições</a><a href="{alt}">English</a>'
    else:
        nav = f'<a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a class="lang" href="{alt}" hreflang="pt">PT</a>'
        foot = f'<a href="index.html">Home</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms &amp; Conditions</a><a href="{alt}">Português</a>'
    html = f"""<!doctype html><html lang="{'pt-BR' if lang=='pt' else 'en'}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<meta name="description" content="{APP} — {'aprenda o espanhol da Espanha com a Lu' if lang=='pt' else 'learn the Spanish of Spain with Lu'}">
<link rel="icon" href="{pre}img/lu_small.png"><link rel="stylesheet" href="{pre}style.css"></head><body>
<div class="stripe"></div><header><a class="logo" href="{home}">{APP}</a><nav>{nav}</nav></header>
{body}
<footer>{foot}<p>© 2026 {OWNER} · {APP}</p></footer></body></html>"""
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(html)

# ───────── Landing ─────────
def landing(lang):
    pre = "../" if lang == "en" else ""
    shots = "".join(f'<img src="{pre}img/{n}.jpg" alt="{a}" loading="lazy">' for n, a in [
        ("mapa", "Mapa da Espanha" if lang=="pt" else "Map of Spain"), ("dialogo", "Diálogo com a Lu" if lang=="pt" else "Dialogue with Lu"),
        ("ligar", "Palavras novas" if lang=="pt" else "New words"), ("passaporte", "Passaporte" if lang=="pt" else "Passport"),
        ("papelada", "Papelada" if lang=="pt" else "Paperwork")])
    if lang == "pt":
        b = f"""<div class="hero"><img src="img/lu.png" alt="Lu, a guia do app"><div>
<h1>Aprenda o espanhol <span style="color:var(--red)">da Espanha</span> viajando com a Lu</h1>
<p>{APP} é o app para brasileiros que vão viajar, estudar ou morar na Espanha. Lições curtas com diálogos reais, áudio em espanhol da Espanha e os falsos amigos que mais enganam quem fala português.</p>
<div class="badges"><span class="badge"><small>Em breve na</small><b> App Store</b></span><span class="badge"><small>Em breve no</small><b>▶ Google Play</b></span></div></div></div>
<div class="stripe"></div>
<section><div class="features">
<div class="card"><h3>🗺️ Uma viagem pela Espanha</h3><p>Madri, Barcelona, Andaluzia, Valência, Galícia, País Basco, Canárias: cada região tem episódios com situações do dia a dia.</p></div>
<div class="card"><h3>⚠️ Igual, quase ou armadilha?</h3><p>Treine os falsos amigos entre espanhol e português, como <i>exquisito</i>, <i>embarazada</i> e <i>oficina</i>.</p></div>
<div class="card"><h3>📄 Papelada sem medo</h3><p>NIE, TIE, empadronamiento, cita previa: o vocabulário para resolver a burocracia de quem vai morar lá.</p></div>
<div class="card"><h3>🎧 Áudio da Espanha</h3><p>Todas as frases com áudio em espanhol peninsular, com <i>vosotros</i>, <i>vale</i> e <i>ordenador</i>.</p></div>
<div class="card"><h3>🔁 Revisão dos seus erros</h3><p>O que você erra volta nas próximas lições até você acertar.</p></div>
<div class="card"><h3>🛂 Carimbos no passaporte</h3><p>Complete regiões, ganhe selos e mantenha sua ofensiva diária.</p></div>
</div></section>
<section><h2 style="text-align:center">Por dentro do app</h2><div class="shots">{shots}</div></section>
<section class="contact"><h2>Contato</h2><p>Dúvidas, sugestões ou imprensa: <a href="mailto:{EMAIL}">{EMAIL}</a></p></section>"""
        page("pt", "index.html", f"{APP} — espanhol da Espanha para brasileiros", b, "en/index.html")
    else:
        b = f"""<div class="hero"><img src="../img/lu.png" alt="Lu, the app's guide"><div>
<h1>Learn the Spanish <span style="color:var(--red)">of Spain</span>, travelling with Lu</h1>
<p>{APP} is the app for Brazilians who are going to travel, study or live in Spain. Short lessons with real dialogues, audio in Spain's Spanish, and the false friends that trip up Portuguese speakers most.</p>
<div class="badges"><span class="badge"><small>Coming soon to the</small><b> App Store</b></span><span class="badge"><small>Coming soon to</small><b>▶ Google Play</b></span></div></div></div>
<div class="stripe"></div>
<section><div class="features">
<div class="card"><h3>🗺️ A trip across Spain</h3><p>Madrid, Barcelona, Andalusia, Valencia, Galicia, the Basque Country, the Canary Islands: every region has episodes built on everyday situations.</p></div>
<div class="card"><h3>⚠️ Same, close or trap?</h3><p>Practise the Spanish–Portuguese false friends, like <i>exquisito</i>, <i>embarazada</i> and <i>oficina</i>.</p></div>
<div class="card"><h3>📄 Paperwork without fear</h3><p>NIE, TIE, empadronamiento, cita previa: the vocabulary you need for the bureaucracy of moving there.</p></div>
<div class="card"><h3>🎧 Audio from Spain</h3><p>Every sentence has audio in peninsular Spanish, with <i>vosotros</i>, <i>vale</i> and <i>ordenador</i>.</p></div>
<div class="card"><h3>🔁 Review your mistakes</h3><p>What you get wrong comes back in later lessons until you get it right.</p></div>
<div class="card"><h3>🛂 Passport stamps</h3><p>Finish regions, earn seals and keep your daily streak going.</p></div>
</div><p class="meta" style="text-align:center">The app itself is in Portuguese (Brazil).</p></section>
<section><h2 style="text-align:center">Inside the app</h2><div class="shots">{shots}</div></section>
<section class="contact"><h2>Contact</h2><p>Questions, feedback or press: <a href="mailto:{EMAIL}">{EMAIL}</a></p></section>"""
        page("en", "en/index.html", f"{APP} — Spain's Spanish for Brazilians", b, "../index.html")

# ───────── Privacy ─────────
def privacy_pt():
    b = f"""<main class="doc"><h1>Política de Privacidade</h1><p class="meta">Data de vigência: {DATE_PT}</p>
<p>Esta política explica quais dados o app <b>{APP}</b> (o “App”) trata, por quê, com quem os compartilha e quais são os seus direitos. Ela descreve o que o App realmente faz hoje. Se isso mudar, atualizaremos esta página.</p>
<h2>1. Responsável pelo tratamento</h2>
<p>{OWNER}, NIF/NIE {NIF}, {ADDR}, Espanha. Contato para privacidade: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. Resumo</h2><ul>
<li>Você pode usar o App <b>sem criar conta</b>. Nesse caso, seu progresso fica só no seu aparelho.</li>
<li>A conta é opcional e serve só para salvar o progresso na nuvem. Pedimos apenas <b>e-mail e senha</b> (ou um link de acesso enviado por e-mail).</li>
<li><b>Não usamos</b> publicidade, rastreamento publicitário, ferramentas de analytics ou de relatório de falhas, e não vendemos dados.</li>
<li>Assinaturas são processadas pela Apple ou pelo Google. <b>Nunca recebemos os dados do seu cartão.</b></li></ul>
<h2>3. Dados que tratamos</h2>
<table><tr><th>Dados</th><th>Quando</th><th>Finalidade e base legal</th><th>Onde ficam</th></tr>
<tr><td><b>Progresso de aprendizagem</b>: objetivo e minutos diários escolhidos no início, XP, ofensiva (streak), último dia de prática, corações, lições concluídas, selos e carimbos, a lição interrompida e os itens que você errou (para a revisão).</td><td>Sempre que você usa o App</td><td>Prestar o serviço (execução de contrato).</td><td>No aparelho (armazenamento local do app ou do navegador). Se você tiver conta, também na nuvem (Supabase).</td></tr>
<tr><td><b>Dados da conta</b>: e-mail, senha (guardada só em formato criptografado, com hash), identificador de usuário, datas de criação e de último acesso.</td><td>Só se você criar conta</td><td>Autenticação e sincronização do progresso (execução de contrato).</td><td>Supabase (UE, Irlanda).</td></tr>
<tr><td><b>Dados técnicos de segurança</b>: endereço IP e informações do navegador ou do aparelho registrados nos logs de autenticação e de acesso do provedor.</td><td>Ao entrar, criar conta ou sincronizar</td><td>Segurança e prevenção de abuso (interesse legítimo).</td><td>Supabase, por tempo limitado.</td></tr>
<tr><td><b>Dados de compra</b>: identificador anônimo gerado pelo App, produtos comprados, status e datas da assinatura e do período de teste, país/moeda da loja.</td><td>Se você abrir a tela de assinatura ou assinar</td><td>Vender e verificar a assinatura Premium (execução de contrato) e cumprir obrigações fiscais (obrigação legal).</td><td>RevenueCat (EUA) e Apple / Google.</td></tr>
<tr><td><b>Região do aparelho</b> (código do país)</td><td>Na tela de assinatura</td><td>Exibir o preço na moeda certa. Usado só no aparelho, não é enviado a nós.</td><td>Só no aparelho.</td></tr></table>
<p><b>Não coletamos</b> nome, telefone, localização (GPS), contatos, fotos, microfone, identificador de publicidade nem dados sensíveis. O áudio das frases vem gravado dentro do App. Se uma frase não tiver áudio próprio, o App pode usar a voz de leitura em espanhol do seu aparelho (função do sistema operacional, feita no próprio aparelho). O App também baixa do nosso servidor uma configuração pública (por exemplo, o número de regiões grátis), sem enviar dados seus.</p>
<h2>4. Com quem compartilhamos (operadores)</h2><ul>
<li><b>Supabase</b>: banco de dados e autenticação, hospedados na região UE (Irlanda, eu-west-1). Também envia os e-mails de confirmação e de acesso.</li>
<li><b>RevenueCat, Inc.</b> (EUA): gestão das assinaturas.</li>
<li><b>Apple</b> (App Store) e <b>Google</b> (Google Play): pagamento, cobrança, renovação e reembolsos, de acordo com as políticas de privacidade de cada um.</li>
<li><b>GitHub Pages</b>: hospeda este site e a versão web de demonstração, e pode registrar endereços IP em logs técnicos.</li></ul>
<p>Transferências para fora do Espaço Econômico Europeu (por exemplo, para os EUA) são feitas com garantias adequadas, como as Cláusulas Contratuais Padrão da Comissão Europeia ou o EU-US Data Privacy Framework, quando aplicável. Não vendemos nem compartilhamos dados para publicidade.</p>
<h2>5. Por quanto tempo guardamos</h2><ul>
<li>Dados locais: até você apagar o App ou limpar os dados do navegador.</li>
<li>Conta e progresso na nuvem: enquanto a conta existir. Depois de um pedido de exclusão, apagamos em até 30 dias.</li>
<li>Registros de compra: pelo prazo exigido pela legislação fiscal e contábil.</li>
<li>Logs técnicos: pelo período de retenção do provedor.</li></ul>
<h2>6. Como apagar seus dados</h2>
<p>Sem conta: desinstale o App (ou limpe os dados do site no navegador) e tudo some do aparelho. Com conta: peça a exclusão da conta e do progresso pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>, a partir do endereço cadastrado. Apagar a conta <b>não cancela</b> uma assinatura: cancele na App Store ou no Google Play.</p>
<h2>7. Idade mínima</h2>
<p>O App é destinado a pessoas com <b>14 anos ou mais</b> (idade de consentimento digital na Espanha, segundo a LOPDGDD), ou com a idade mínima exigida no seu país, se for maior. Se você tiver menos idade, só use o App com autorização e supervisão do seu responsável legal. Para crianças e adolescentes no Brasil, o tratamento segue o melhor interesse do menor (art. 14 da LGPD). Se soubermos que coletamos dados de uma criança sem autorização, vamos apagá-los.</p>
<h2>8. Seus direitos (RGPD / LOPDGDD, Espanha e UE)</h2>
<p>Você tem direito de acesso, retificação, exclusão, oposição, limitação do tratamento e portabilidade, além de não ser objeto de decisões só automatizadas. Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>. Respondemos em até um mês. Você também pode reclamar na <b>Agencia Española de Protección de Datos (AEPD)</b>, em <a href="https://www.aepd.es">www.aepd.es</a>.</p>
<h2>9. Usuários no Brasil (LGPD)</h2>
<p>Você pode pedir confirmação do tratamento, acesso, correção, anonimização, bloqueio ou eliminação, portabilidade, informação sobre compartilhamentos e a revisão de decisões automatizadas (art. 18 da LGPD). Pode também reclamar à <b>ANPD</b> (<a href="https://www.gov.br/anpd">gov.br/anpd</a>). As bases legais usadas são a execução de contrato, o cumprimento de obrigação legal e o legítimo interesse.</p>
<h2>10. Usuários na Califórnia (CCPA/CPRA)</h2>
<p>Você pode saber quais dados pessoais coletamos, pedir a exclusão ou a correção deles e não ser discriminado por exercer esses direitos. <b>Não vendemos nem “compartilhamos”</b> (no sentido da CCPA) dados pessoais e não usamos dados sensíveis. Pedidos: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. Segurança</h2><p>As conexões usam HTTPS. Cada usuário só acessa os próprios dados (regras de segurança no banco de dados). As senhas são guardadas com hash. Nenhum sistema é 100% seguro: se houver um incidente relevante, avisaremos você e as autoridades, como manda a lei.</p>
<h2>12. Alterações</h2><p>Se fizermos mudanças importantes, avisaremos no App ou nesta página, com a nova data de vigência.</p></main>"""
    page("pt", "privacidade.html", f"Política de Privacidade — {APP}", b, "en/privacy.html")

def privacy_en():
    b = f"""<main class="doc"><h1>Privacy Policy</h1><p class="meta">Effective date: {DATE_EN}</p>
<p>This policy explains what data the <b>{APP}</b> app (the “App”) processes, why, who it is shared with, and your rights. It describes what the App actually does today. If that changes, we will update this page. The Portuguese version is the primary one.</p>
<h2>1. Controller</h2><p>{OWNER}, NIF/NIE {NIF}, {ADDR}, Spain. Privacy contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. Summary</h2><ul><li>You can use the App <b>without an account</b>. Your progress then stays only on your device.</li>
<li>An account is optional and only saves your progress to the cloud. We ask only for an <b>email and password</b> (or a sign-in link sent by email).</li>
<li><b>No</b> advertising, ad tracking, analytics or crash-reporting tools, and no sale of data.</li>
<li>Subscriptions are processed by Apple or Google. <b>We never receive your card details.</b></li></ul>
<h2>3. Data we process</h2>
<table><tr><th>Data</th><th>When</th><th>Purpose and legal basis</th><th>Where</th></tr>
<tr><td><b>Learning progress</b>: the goal and daily minutes you chose at the start, XP, streak, last practice day, hearts, completed lessons, seals and stamps, any interrupted lesson, and the items you got wrong (for review).</td><td>Whenever you use the App</td><td>Providing the service (contract).</td><td>On your device (app or browser local storage). If you have an account, also in the cloud (Supabase).</td></tr>
<tr><td><b>Account data</b>: email, password (stored only as a hash), user ID, created and last sign-in dates.</td><td>Only if you create an account</td><td>Authentication and progress sync (contract).</td><td>Supabase (EU, Ireland).</td></tr>
<tr><td><b>Technical security data</b>: IP address and browser or device information in the provider's authentication and access logs.</td><td>When you sign in, sign up or sync</td><td>Security and abuse prevention (legitimate interest).</td><td>Supabase, for a limited time.</td></tr>
<tr><td><b>Purchase data</b>: an anonymous ID generated by the App, products bought, subscription and trial status and dates, store country/currency.</td><td>If you open the subscription screen or subscribe</td><td>Selling and verifying Premium (contract) and tax duties (legal obligation).</td><td>RevenueCat (USA) and Apple / Google.</td></tr>
<tr><td><b>Device region</b> (country code)</td><td>On the subscription screen</td><td>Showing prices in the right currency. Used on the device only and never sent to us.</td><td>Device only.</td></tr></table>
<p>We do <b>not</b> collect your name, phone number, location (GPS), contacts, photos, microphone, advertising ID or sensitive data. Sentence audio is recorded and bundled with the App. If a sentence has no recording, the App may use your device's Spanish text-to-speech voice (an operating-system feature that runs on the device). The App also downloads a public configuration from our server (for example, how many regions are free) without sending any of your data.</p>
<h2>4. Processors</h2><ul>
<li><b>Supabase</b>: database and authentication, hosted in the EU region (Ireland, eu-west-1). It also sends the confirmation and sign-in emails.</li>
<li><b>RevenueCat, Inc.</b> (USA): subscription management.</li>
<li><b>Apple</b> (App Store) and <b>Google</b> (Google Play): payment, billing, renewals and refunds, under their own privacy policies.</li>
<li><b>GitHub Pages</b>: hosts this website and the web demo, and may log IP addresses in technical logs.</li></ul>
<p>Transfers outside the European Economic Area (for example, to the USA) rely on appropriate safeguards, such as the European Commission's Standard Contractual Clauses or the EU-US Data Privacy Framework where applicable. We do not sell data or share it for advertising.</p>
<h2>5. Retention</h2><ul>
<li>Local data: until you delete the App or clear your browser data.</li>
<li>Cloud account and progress: while the account exists. After a deletion request, deleted within 30 days.</li>
<li>Purchase records: as long as tax and accounting law requires.</li>
<li>Technical logs: for the provider's retention period.</li></ul>
<h2>6. Deleting your data</h2><p>Without an account: uninstall the App (or clear the site data in your browser) and everything is gone from the device. With an account: request deletion of your account and progress by emailing <a href="mailto:{EMAIL}">{EMAIL}</a> from your registered address. Deleting the account <b>does not cancel</b> a subscription: cancel it in the App Store or Google Play.</p>
<h2>7. Minimum age</h2><p>The App is meant for people <b>aged 14 or over</b> (the digital-consent age in Spain under the LOPDGDD), or the minimum age required in your country if that is higher. If you are younger, use the App only with your parent's or guardian's permission and supervision. If we learn that we collected a child's data without that permission, we will delete it.</p>
<h2>8. Your rights (GDPR / LOPDGDD)</h2><p>You have the right of access, rectification, erasure, objection, restriction and portability, and the right not to be subject to solely automated decisions. Email <a href="mailto:{EMAIL}">{EMAIL}</a>; we reply within one month. You may also complain to the <b>Spanish Data Protection Agency (AEPD)</b> at <a href="https://www.aepd.es">www.aepd.es</a>.</p>
<h2>9. Brazil (LGPD)</h2><p>You may request confirmation of processing, access, correction, anonymisation, blocking or deletion, portability, information about sharing, and review of automated decisions (LGPD art. 18). You may also complain to the <b>ANPD</b>. The legal bases we use are contract, legal obligation and legitimate interest.</p>
<h2>10. California (CCPA/CPRA)</h2><p>You may know what personal information we collect, request its deletion or correction, and not be discriminated against for exercising these rights. We <b>do not sell or “share”</b> personal information (in the CCPA sense) and do not use sensitive personal information. Requests: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. Security</h2><p>Connections use HTTPS. Database security rules mean each user can access only their own data. Passwords are hashed. No system is 100% secure: if a significant incident happens, we will notify you and the authorities as the law requires.</p>
<h2>12. Changes</h2><p>If we make material changes, we will announce them in the App or on this page, with a new effective date.</p></main>"""
    page("en", "en/privacy.html", f"Privacy Policy — {APP}", b, "../privacidade.html")

# ───────── Terms ─────────
def terms_pt():
    b = f"""<main class="doc"><h1>Termos e Condições de Uso</h1><p class="meta">Data de vigência: {DATE_PT}</p>
<p>Estes termos regem o uso do app <b>{APP}</b> (o “App”), oferecido por {OWNER}, NIF/NIE {NIF}, {ADDR}, Espanha (“nós”). Ao usar o App, você concorda com estes termos e com a <a href="privacidade.html">Política de Privacidade</a>.</p>
<h2>1. O serviço</h2><p>O App ensina espanhol da Espanha para falantes de português, com lições, áudio, exercícios e acompanhamento de progresso. Ele tem conteúdo educativo e não substitui aconselhamento jurídico ou de imigração: as informações sobre trâmites (NIE, TIE, empadronamiento etc.) são gerais e podem mudar. Confirme sempre nas fontes oficiais.</p>
<h2>2. Idade</h2><p>Você precisa ter pelo menos 14 anos, ou a idade mínima do seu país, se for maior. Abaixo disso, só com autorização e supervisão do responsável legal, que aceita estes termos em seu nome.</p>
<h2>3. Conta</h2><p>A conta é opcional (e-mail e senha, ou link de acesso por e-mail) e serve para salvar o progresso na nuvem. Você é responsável por manter sua senha em segredo e por informar um e-mail verdadeiro. O progresso de quem usa sem conta fica só no aparelho e pode se perder se o App for apagado.</p>
<h2>4. Plano grátis e Premium</h2><ul>
<li>Parte do conteúdo é gratuita. A assinatura <b>Premium</b> libera todas as regiões e dá corações ilimitados.</li>
<li><b>Pagamento</b>: é feito pela sua conta da Apple (App Store) ou do Google (Google Play). O preço, a moeda e os impostos aparecem na loja antes da compra.</li>
<li><b>Renovação automática</b>: a assinatura (mensal ou anual) renova sozinha ao fim de cada período, e a cobrança é feita até 24 horas antes da renovação, a menos que você cancele pelo menos 24 horas antes do fim do período.</li>
<li><b>Teste grátis</b>: se a loja oferecer um período de teste e você tiver direito a ele, a duração aparece antes da compra. No fim do teste, a assinatura começa a ser cobrada, a menos que você cancele antes. Parte não usada do teste se perde quando você assina.</li>
<li><b>Cancelamento</b>: nas configurações de assinaturas da App Store ou do Google Play. O Premium continua até o fim do período já pago. Desinstalar o App ou apagar a conta não cancela a assinatura.</li>
<li><b>Reembolsos</b>: são decididos pela Apple ou pelo Google, de acordo com as políticas de cada loja. Não conseguimos fazer reembolsos diretamente.</li>
<li><b>Direito de desistência (UE)</b>: ao assinar, você pede que o conteúdo digital fique disponível imediatamente e reconhece que, por isso, perde o direito de desistência de 14 dias, na medida em que a lei permitir. Isso não afeta as políticas de reembolso das lojas.</li>
<li>Podemos mudar preços ou benefícios do Premium. Mudanças de preço seguem as regras das lojas e são avisadas com antecedência.</li></ul>
<h2>5. Uso permitido</h2><p>O App é para uso pessoal e não comercial. Não é permitido copiar, revender ou redistribuir o conteúdo (textos, áudios, ilustrações, personagens), fazer engenharia reversa, burlar travas ou pagamentos, nem usar o App de forma que prejudique o serviço ou outras pessoas.</p>
<h2>6. Propriedade intelectual</h2><p>O App, o conteúdo das lições, os áudios, as ilustrações e os personagens (como a Lu e o Lino) pertencem a {OWNER} ou aos seus licenciantes. Você recebe uma licença limitada, pessoal, intransferível e revogável para usar o App.</p>
<h2>7. Disponibilidade e mudanças</h2><p>Trabalhamos para manter o App funcionando, mas ele pode ter interrupções, erros ou mudanças de conteúdo. Podemos alterar, suspender ou encerrar funções. Se o Premium for encerrado, avisaremos e você poderá pedir reembolso à loja de acordo com as regras dela.</p>
<h2>8. Responsabilidade</h2><p>O App é fornecido “no estado em que se encontra”. Na medida permitida por lei, não respondemos por danos indiretos nem por perda de progresso guardado só no aparelho. Nada nestes termos limita direitos que você tem como consumidor pela lei aplicável (incluindo o Código de Defesa do Consumidor, para consumidores no Brasil, e a legislação espanhola e europeia de consumo), nem nossa responsabilidade por dolo ou culpa grave.</p>
<h2>9. Encerramento</h2><p>Você pode parar de usar o App e pedir a exclusão da conta a qualquer momento (veja a Política de Privacidade). Podemos suspender contas que violem estes termos.</p>
<h2>10. Lei aplicável e foro</h2><p>Estes termos são regidos pela lei da <b>Espanha</b>. Se você for consumidor, continua tendo a proteção das normas obrigatórias do país onde mora e pode recorrer aos tribunais do seu domicílio. Consumidores da UE também podem usar a plataforma europeia de resolução de litígios em linha: <a href="https://ec.europa.eu/consumers/odr">ec.europa.eu/consumers/odr</a>.</p>
<h2>11. Contato</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · {ADDR}</p>
<h2>12. Alterações</h2><p>Podemos atualizar estes termos. Mudanças importantes serão avisadas no App ou nesta página, com nova data de vigência.</p></main>"""
    page("pt", "termos.html", f"Termos e Condições — {APP}", b, "en/terms.html")

def terms_en():
    b = f"""<main class="doc"><h1>Terms &amp; Conditions</h1><p class="meta">Effective date: {DATE_EN}</p>
<p>These terms govern your use of the <b>{APP}</b> app (the “App”), provided by {OWNER}, NIF/NIE {NIF}, {ADDR}, Spain (“we”). By using the App you agree to these terms and to the <a href="privacy.html">Privacy Policy</a>. The Portuguese version is the primary one; if the two versions conflict, the Portuguese one prevails to the extent the law allows.</p>
<h2>1. The service</h2><p>The App teaches the Spanish of Spain to Portuguese speakers, with lessons, audio, exercises and progress tracking. It is educational content, not legal or immigration advice: information about procedures (NIE, TIE, empadronamiento, etc.) is general and may change. Always check the official sources.</p>
<h2>2. Age</h2><p>You must be at least 14, or the minimum age in your country if that is higher. Younger users may use the App only with the permission and supervision of a parent or guardian, who accepts these terms on their behalf.</p>
<h2>3. Account</h2><p>An account is optional (email and password, or an email sign-in link) and saves your progress to the cloud. Keep your password secret and use a real email address. Progress of users without an account stays only on the device and may be lost if the App is deleted.</p>
<h2>4. Free plan and Premium</h2><ul>
<li>Part of the content is free. The <b>Premium</b> subscription unlocks all regions and gives you unlimited hearts.</li>
<li><b>Payment</b> is made through your Apple (App Store) or Google (Google Play) account. The price, currency and taxes are shown by the store before you buy.</li>
<li><b>Auto-renewal</b>: the subscription (monthly or yearly) renews automatically at the end of each period, and you are charged within 24 hours before renewal, unless you cancel at least 24 hours before the period ends.</li>
<li><b>Free trial</b>: if the store offers a trial and you are eligible, its length is shown before purchase. When the trial ends, the subscription starts being charged unless you cancel first. Any unused part of a trial is forfeited when you subscribe.</li>
<li><b>Cancellation</b>: in the App Store or Google Play subscription settings. Premium stays active until the end of the period you have paid for. Uninstalling the App or deleting your account does not cancel the subscription.</li>
<li><b>Refunds</b> are decided by Apple or Google under their own store policies. We cannot issue refunds directly.</li>
<li><b>EU right of withdrawal</b>: by subscribing, you request immediate access to digital content and acknowledge that you therefore lose the 14-day withdrawal right, to the extent the law allows. This does not affect the stores' refund policies.</li>
<li>We may change Premium prices or benefits. Price changes follow the store rules and are notified in advance.</li></ul>
<h2>5. Acceptable use</h2><p>The App is for personal, non-commercial use. You may not copy, resell or redistribute its content (texts, audio, illustrations, characters), reverse-engineer it, bypass locks or payments, or use it in ways that harm the service or other people.</p>
<h2>6. Intellectual property</h2><p>The App, the lesson content, audio, illustrations and characters (such as Lu and Lino) belong to {OWNER} or its licensors. You receive a limited, personal, non-transferable and revocable licence to use the App.</p>
<h2>7. Availability and changes</h2><p>We work to keep the App running, but it may have outages, bugs or content changes. We may change, suspend or discontinue features. If Premium is discontinued, we will let you know, and you may ask the store for a refund under its rules.</p>
<h2>8. Liability</h2><p>The App is provided “as is”. To the extent the law allows, we are not liable for indirect damages or for the loss of progress stored only on a device. Nothing in these terms limits your statutory consumer rights (including Spanish and EU consumer law, and the Brazilian Consumer Defence Code for consumers in Brazil), or our liability for wilful misconduct or gross negligence.</p>
<h2>9. Termination</h2><p>You may stop using the App and request deletion of your account at any time (see the Privacy Policy). We may suspend accounts that breach these terms.</p>
<h2>10. Governing law and jurisdiction</h2><p>These terms are governed by the laws of <b>Spain</b>. If you are a consumer, you keep the protection of the mandatory rules of your country of residence and may bring claims before the courts where you live. EU consumers may also use the EU Online Dispute Resolution platform: <a href="https://ec.europa.eu/consumers/odr">ec.europa.eu/consumers/odr</a>.</p>
<h2>11. Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · {ADDR}</p>
<h2>12. Changes</h2><p>We may update these terms. Material changes will be announced in the App or on this page, with a new effective date.</p></main>"""
    page("en", "en/terms.html", f"Terms & Conditions — {APP}", b, "../termos.html")

open(os.path.join(ROOT, "style.css"), "w").write(CSS)
landing("pt"); landing("en"); privacy_pt(); privacy_en(); terms_pt(); terms_en()
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
# aliases so /privacy and /terms also work in PT root and /en/privacidade etc.
print("built")
