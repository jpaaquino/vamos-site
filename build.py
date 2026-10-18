#!/usr/bin/env python3
"""Generates the static site. Rename the app or fill placeholders HERE, then run: python3 build.py"""
import os
APP = "Vamos Espanha!"
OWNER = "Joao Paulo de Araujo Aquino"
NIF = "Z1454771A"
ADDR = "Calle Pascual i Genis, 15 5-17, 46002 Valencia"
EMAIL = "joaopaulo@acedigitallabs.com"
DATE_PT = "17 de outubro de 2026"
DATE_EN = "October 17, 2026"
PRIV_DATE_PT = "18 de outubro de 2026"
PRIV_DATE_EN = "October 18, 2026"
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
.shots figure{margin:0;flex:0 0 220px;scroll-snap-align:start}
.shots figcaption{text-align:center;font-weight:700;font-size:.9rem;margin-top:12px}
.shots img{display:block;width:220px;height:auto;border-radius:22px;box-shadow:0 6px 18px #0002;scroll-snap-align:center;flex:none}
.contact{text-align:center}
footer{background:var(--ink);color:#fff;padding:24px 18px;text-align:center;font-size:.9rem}
footer a{color:var(--yellow);margin:0 8px}
.doc{max-width:780px;margin:auto;padding:10px 18px 50px}
.doc h1{font-size:1.7rem}.doc h2{font-size:1.2rem;margin-top:1.8em;color:var(--terra)}
.doc table{border-collapse:collapse;width:100%;font-size:.9rem;background:#fff}
.doc td,.doc th{border:1px solid #0002;padding:6px 8px;vertical-align:top;text-align:left}
.ph{background:#fff3b0;padding:0 3px;border-radius:4px}
.meta{color:#6b5a6e}
@media(min-width:760px){h1{font-size:2.8rem}.hero{flex-direction:row;text-align:left;justify-content:center}.hero img{width:260px}.badges{justify-content:flex-start}.features{grid-template-columns:repeat(3,1fr)}}
"""

def ph(s): return f'<span class="ph">{s}</span>'

def page(lang, path, title, body, alt):
    pre = "../" if lang == "en" else ""
    home = "index.html"
    if lang == "pt":
        nav = f'<a href="privacidade.html">Privacidade</a><a href="termos.html">Termos</a><a class="lang" href="{alt}" hreflang="en">EN</a>'
        foot = f'<a href="index.html">Início</a><a href="privacidade.html">Política de Privacidade</a><a href="termos.html">Termos e Condições</a><a href="suporte.html">Suporte</a><a href="{alt}">English</a>'
    else:
        nav = f'<a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a class="lang" href="{alt}" hreflang="pt">PT</a>'
        foot = f'<a href="index.html">Home</a><a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms &amp; Conditions</a><a href="mailto:{EMAIL}">Support</a><a href="{alt}">Português</a>'
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
    screenshots = [
        ("mapa", "Explore a Espanha", "Explore Spain"),
        ("dialogo", "Diálogos do dia a dia", "Everyday conversations"),
        ("ligar", "Vocabulário com imagens", "Vocabulary with pictures"),
        ("papelada", "Espanhol para a papelada", "Spanish for paperwork"),
        ("passaporte", "Seu passaporte", "Your passport"),
        ("graduacao", "Celebre suas conquistas", "Celebrate your achievements"),
        ("configuracoes", "Seu ritmo de estudo", "Your learning pace"),
    ]
    shots = "".join(
        f'<figure><img src="{pre}img/{name}.jpg?v=20261016" alt="{pt if lang == "pt" else en}" '
        f'width="430" height="932" loading="lazy"><figcaption>{pt if lang == "pt" else en}</figcaption></figure>'
        for name, pt, en in screenshots
    )
    if lang == "pt":
        b = f"""<div class="hero"><img src="img/lu.png" alt="Lu, a guia do app"><div>
<h1>Aprenda o espanhol <span style="color:var(--red)">da Espanha</span> viajando com a Lu</h1>
<p>{APP} ajuda brasileiros a estudar o espanhol falado na Espanha com diálogos, áudio e exercícios em português do Brasil. O curso tem 117 lições, incluindo 21 lições educativas de vocabulário e situações sobre documentos e serviços em Papelada. Sete lições podem ser experimentadas gratuitamente.</p>
<div class="badges"><span class="badge"><small>Em breve na</small><b> App Store</b></span><span class="badge"><small>Em breve no</small><b>▶ Google Play</b></span></div></div></div>
<div class="stripe"></div>
<section><div class="features">
<div class="card"><h3>🗺️ Uma viagem pela Espanha</h3><p>Madri, Barcelona, Andaluzia, Valência, Galícia, País Basco, Canárias: cada região tem episódios com situações do dia a dia.</p></div>
<div class="card"><h3>⚠️ Igual, quase ou armadilha?</h3><p>Treine os falsos amigos entre espanhol e português, como <i>exquisito</i>, <i>embarazada</i> e <i>oficina</i>.</p></div>
<div class="card"><h3>📄 Vocabulário para Papelada</h3><p>21 lições educativas com palavras e situações sobre documentos e serviços. O conteúdo não substitui orientação profissional nem informa requisitos oficiais completos.</p></div>
<div class="card"><h3>🎧 Áudio da Espanha</h3><p>Todas as frases com áudio em espanhol peninsular, com <i>vosotros</i>, <i>vale</i> e <i>ordenador</i>.</p></div>
<div class="card"><h3>🔁 Revisão dos seus erros</h3><p>O que você erra volta nas próximas lições até você acertar.</p></div>
<div class="card"><h3>🛂 Carimbos no passaporte</h3><p>Complete regiões, ganhe selos e mantenha sua ofensiva diária.</p></div>
</div></section>
<section><h2 style="text-align:center">Por dentro do app</h2><div class="shots" tabindex="0" role="region" aria-label="Capturas do app">{shots}</div></section>
<section><h2>Como acessar o curso</h2><p>Depois das lições gratuitas, você pode acessar o curso atual por compra única ou por assinatura mensal enquanto ela estiver ativa. A loja mostra as condições e os valores disponíveis antes da compra. Novos cursos, se lançados, podem ser vendidos separadamente.</p></section>
<section class="contact"><h2>Contato</h2><p>Dúvidas, sugestões ou imprensa: <a href="mailto:{EMAIL}">{EMAIL}</a></p></section>"""
        page("pt", "index.html", f"{APP} — espanhol da Espanha para brasileiros", b, "en/index.html")
    else:
        b = f"""<div class="hero"><img src="../img/lu.png" alt="Lu, the app's guide"><div>
<h1>Learn the Spanish <span style="color:var(--red)">of Spain</span>, travelling with Lu</h1>
<p>{APP} helps Brazilians study the Spanish spoken in Spain with dialogues, audio and exercises explained in Brazilian Portuguese. The course has 117 lessons, including 21 educational lessons about vocabulary and everyday situations involving paperwork and services. Seven lessons are available to try for free.</p>
<div class="badges"><span class="badge"><small>Coming soon to the</small><b> App Store</b></span><span class="badge"><small>Coming soon to</small><b>▶ Google Play</b></span></div></div></div>
<div class="stripe"></div>
<section><div class="features">
<div class="card"><h3>🗺️ A trip across Spain</h3><p>Madrid, Barcelona, Andalusia, Valencia, Galicia, the Basque Country, the Canary Islands: every region has episodes built on everyday situations.</p></div>
<div class="card"><h3>⚠️ Same, close or trap?</h3><p>Practise the Spanish–Portuguese false friends, like <i>exquisito</i>, <i>embarazada</i> and <i>oficina</i>.</p></div>
<div class="card"><h3>📄 Paperwork vocabulary</h3><p>21 educational lessons with words and situations about documents and services. The content is not professional advice and does not provide complete official requirements.</p></div>
<div class="card"><h3>🎧 Audio from Spain</h3><p>Every sentence has audio in peninsular Spanish, with <i>vosotros</i>, <i>vale</i> and <i>ordenador</i>.</p></div>
<div class="card"><h3>🔁 Review your mistakes</h3><p>What you get wrong comes back in later lessons until you get it right.</p></div>
<div class="card"><h3>🛂 Passport stamps</h3><p>Finish regions, earn seals and keep your daily streak going.</p></div>
</div><p class="meta" style="text-align:center">The app itself is in Portuguese (Brazil).</p></section>
<section><h2 style="text-align:center">Inside the app</h2><div class="shots" tabindex="0" role="region" aria-label="App screenshots">{shots}</div></section>
<section><h2>Course access</h2><p>After the free lessons, you can access the current course with a one-time purchase or a monthly subscription while it is active. The store shows the available terms and prices before purchase. New courses, if released, may be sold separately.</p></section>
<section class="contact"><h2>Contact</h2><p>Questions, feedback or press: <a href="mailto:{EMAIL}">{EMAIL}</a></p></section>"""
        page("en", "en/index.html", f"{APP} — Spain's Spanish for Brazilians", b, "../index.html")

# ───────── Privacy ─────────
def privacy_pt():
    b = f"""<main class="doc"><h1>Política de Privacidade</h1><p class="meta">Data de vigência: {PRIV_DATE_PT}</p>
<p>Esta política explica quais dados o app <b>{APP}</b> (o “App”) trata, por quê, com quem os compartilha e quais são os seus direitos. Ela descreve o que o App realmente faz hoje. Se isso mudar, atualizaremos esta página.</p>
<h2>1. Responsável pelo tratamento</h2>
<p>{OWNER}, NIF/NIE {NIF}, {ADDR}, Espanha. Contato para privacidade: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. Resumo</h2><ul>
<li>Você pode usar o App <b>sem criar conta</b>. Nesse caso, seu progresso fica só no seu aparelho.</li>
<li>A conta é opcional e serve para salvar o progresso na nuvem. Você pode entrar com e-mail e senha, link enviado por e-mail, Google ou Apple quando disponíveis na plataforma. Nos logins sociais, o provedor pode enviar seu e-mail e, se disponível, seu nome.</li>
<li>Não usamos publicidade, rastreamento publicitário nem ferramentas de relatório de falhas, e não vendemos dados. O App (iOS e Android) usa <b>estatísticas de uso anônimas</b>, sem nome, e-mail ou respostas, para melhorar o curso. Na União Europeia, no Espaço Econômico Europeu, no Reino Unido e na Suíça (ou se não for possível identificar a região do aparelho), elas só são coletadas se você aceitar. Nos demais países, como o Brasil, ficam ligadas por padrão, com aviso no App. Em qualquer lugar, você pode desligá-las a qualquer momento em <b>Configurações › Privacidade</b>.</li>
<li>Compras e assinaturas são processadas pela Apple ou pelo Google, com apoio técnico da RevenueCat. <b>Nunca recebemos os dados do seu cartão.</b></li></ul>
<h2>3. Dados que tratamos</h2>
<table><tr><th>Dados</th><th>Quando</th><th>Finalidade e base legal</th><th>Onde ficam</th></tr>
<tr><td><b>Progresso de aprendizagem</b>: objetivo e minutos diários escolhidos no início, XP, ofensiva (streak), último dia de prática, corações, lições concluídas, selos e carimbos, as tentativas de lição interrompidas e os itens que você errou (para a revisão).</td><td>Sempre que você usa o App</td><td>Prestar o serviço (execução de contrato).</td><td>No aparelho (armazenamento local do app ou do navegador). Se você tiver conta, também na nuvem (Supabase).</td></tr>
<tr><td><b>Dados da conta</b>: e-mail, identificador de usuário, datas de criação e de último acesso; senha em formato de hash somente no login por e-mail e, se fornecido pelo Google ou Apple, seu nome.</td><td>Só se você criar ou acessar uma conta</td><td>Autenticação e sincronização do progresso (execução de contrato).</td><td>Supabase (UE, Irlanda); Google ou Apple fornecem os dados do login social.</td></tr>
<tr><td><b>Dados técnicos de segurança</b>: endereço IP e informações do navegador ou do aparelho registrados nos logs de autenticação e de acesso do provedor.</td><td>Ao entrar, criar conta ou sincronizar</td><td>Segurança e prevenção de abuso (interesse legítimo).</td><td>Supabase, por tempo limitado.</td></tr>
<tr><td><b>Dados de compra</b>: identificador pseudônimo do SDK de compras, produtos comprados, dados de transação e estado funcional da compra ou assinatura.</td><td>Ao abrir o App e ao consultar, realizar ou restaurar uma compra, ou usar acesso comprado</td><td>Processar, restaurar e verificar o acesso ao curso (execução de contrato) e gerar métricas agregadas de compras e receita no painel da RevenueCat.</td><td>RevenueCat (EUA) e Apple / Google.</td></tr>
<tr><td><b>Estatísticas de uso</b>: objetivo de estudo, evento e resultado, origem, conjunto de ofertas e plano, identificador da lição quando aplicável, data/hora, plataforma, versão do app e UUID aleatório pseudônimo. O evento não inclui e-mail, ID da conta, respostas dos exercícios nem endereço IP.</td><td>No App para iOS e Android. Na UE/EEE, no Reino Unido, na Suíça ou com região desconhecida: só depois que você aceitar. Nos demais países: ligadas por padrão, até você desligar.</td><td>Medir o uso do produto e orientar melhorias. Na UE/EEE, no Reino Unido e na Suíça: consentimento (art. 6(1)(a) do RGPD e regras de ePrivacy sobre acesso ao aparelho). Nos demais países: legítimo interesse (art. 7º, IX, da LGPD ou art. 6(1)(f) do RGPD, conforme o caso), com direito de oposição ao desligar.</td><td>Fila local no aparelho e Supabase para processamento.</td></tr>
<tr><td><b>Região do aparelho</b> (código do país das configurações de idioma e região)</td><td>Na tela de compra e ao abrir o App</td><td>Exibir informações da loja e decidir se as estatísticas de uso precisam de consentimento prévio. Lido só no aparelho, não é enviado a nós nem incluído nas estatísticas.</td><td>Só no aparelho.</td></tr></table>
<p><b>Não coletamos</b> telefone, localização (GPS), contatos, fotos, microfone, identificador de publicidade nem dados sensíveis. O áudio das frases vem gravado dentro do App. Se uma frase não tiver áudio próprio, o App pode solicitar leitura em espanhol pelo mecanismo de voz do sistema operacional; o funcionamento e eventual processamento dependem do sistema e do fornecedor desse mecanismo. O App também baixa do nosso servidor uma configuração pública (por exemplo, quais lições são grátis). Esse pedido não inclui dados de conta ou progresso, mas, como qualquer conexão à internet, pode gerar metadados técnicos como o endereço IP, que podem constar nos logs do servidor.</p>
<h2>4. Com quem compartilhamos (operadores)</h2><ul>
<li><b>Supabase</b>: banco de dados e autenticação, hospedados na região UE (Irlanda, eu-west-1). Também envia os e-mails de confirmação e de acesso.</li>
<li><b>Google</b> e <b>Apple</b>: provedores opcionais de login social, quando disponíveis na plataforma e se você escolher entrar por esses serviços.</li>
<li><b>RevenueCat, Inc.</b> (EUA): processamento técnico de compras e assinaturas.</li>
<li><b>Apple</b> (App Store) e <b>Google</b> (Google Play): pagamento, cobrança, renovação e reembolsos, de acordo com as políticas de privacidade de cada um.</li>
<li><b>GitHub Pages</b>: hospeda este site e a versão web de demonstração, e pode registrar endereços IP em logs técnicos.</li></ul>
<p>Transferências para fora do Espaço Econômico Europeu (por exemplo, para os EUA) são feitas com garantias adequadas, como as Cláusulas Contratuais Padrão da Comissão Europeia ou o EU-US Data Privacy Framework, quando aplicável. Não vendemos nem compartilhamos dados para publicidade.</p>
<h2>5. Por quanto tempo guardamos</h2><ul>
<li>Dados locais: até você apagar o App ou limpar os dados do navegador.</li>
<li>Conta e progresso na nuvem: enquanto a conta existir. A exclusão pelo App é imediata. Pedidos por e-mail são atendidos em até 30 dias.</li>
<li>Registros de compra: pelo prazo exigido pela legislação fiscal e contábil.</li>
<li>Estatísticas de uso: 90 dias no Supabase, com rotina diária de exclusão. Se você desligá-las (ou retirar o consentimento), a coleta para imediatamente e a fila local é apagada; a remoção dos eventos já enviados é solicitada ao Supabase na próxima conexão. Para impedir reenvios, um registro pseudônimo com o UUID aleatório da instalação e o hash do segredo de exclusão, sem vínculo com sua conta, fica por 90 dias.</li>
<li>Logs técnicos: pelo período de retenção do provedor.</li></ul>
<h2>6. Como apagar seus dados</h2>
<p>Sem conta: desinstale o App (ou limpe os dados do site no navegador) e o progresso local some do aparelho. Com conta: no App, abra <b>Configurações → Sua conta → Apagar conta</b>. A conta e o progresso na nuvem são apagados na hora. Para apagar as estatísticas de uso, desative <b>Compartilhar estatísticas de uso</b> na seção Privacidade das Configurações. Isso para a coleta, limpa a fila local e solicita a remoção dos eventos enviados na próxima conexão; o pedido de remoção fica pendente até poder ser enviado. Se você não tiver mais acesso ao App, peça pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. Veja <a href="apagar-conta.html">Como apagar sua conta</a>. Apagar a conta <b>não cancela</b> uma assinatura: cancele na App Store ou no Google Play.</p>
<h2>7. Idade mínima</h2>
<p>O App é destinado a pessoas com <b>14 anos ou mais</b> (idade de consentimento digital na Espanha, segundo a LOPDGDD), ou com a idade mínima exigida no seu país, se for maior. Se você tiver menos idade, só use o App com autorização e supervisão do seu responsável legal. Para crianças e adolescentes no Brasil, o tratamento segue o melhor interesse do menor (art. 14 da LGPD). Se soubermos que coletamos dados de uma criança sem autorização, vamos apagá-los.</p>
<h2>8. Seus direitos (RGPD / LOPDGDD, Espanha e UE)</h2>
<p>Você tem direito de acesso, retificação, exclusão, oposição, limitação do tratamento e portabilidade, além de não ser objeto de decisões só automatizadas. Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>. Respondemos em até um mês. Você também pode reclamar na <b>Agencia Española de Protección de Datos (AEPD)</b>, em <a href="https://www.aepd.es">www.aepd.es</a>.</p>
<h2>9. Usuários no Brasil (LGPD)</h2>
<p>Você pode pedir confirmação do tratamento, acesso, correção, anonimização, bloqueio ou eliminação, portabilidade, informação sobre compartilhamentos e a revisão de decisões automatizadas (art. 18 da LGPD). Pode também reclamar à <b>ANPD</b> (<a href="https://www.gov.br/anpd">gov.br/anpd</a>). As bases legais usadas são execução de contrato, cumprimento de obrigação legal, legítimo interesse (inclusive para as estatísticas de uso fora da UE/EEE, do Reino Unido e da Suíça, que você pode desligar a qualquer momento) e, para as estatísticas de uso na UE/EEE, no Reino Unido e na Suíça, consentimento, que pode ser retirado.</p>
<h2>10. Usuários na Califórnia (CCPA/CPRA)</h2>
<p>Você pode saber quais dados pessoais coletamos, pedir a exclusão ou a correção deles e não ser discriminado por exercer esses direitos. <b>Não vendemos nem “compartilhamos”</b> (no sentido da CCPA) dados pessoais e não usamos dados sensíveis. Pedidos: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>11. Segurança</h2><p>As conexões usam HTTPS. Cada usuário só acessa os próprios dados (regras de segurança no banco de dados). As senhas são guardadas com hash. Nenhum sistema é 100% seguro: se houver um incidente relevante, avisaremos você e as autoridades, como manda a lei.</p>
<h2>12. Alterações</h2><p>Se fizermos mudanças importantes, avisaremos no App ou nesta página, com a nova data de vigência.</p></main>"""
    page("pt", "privacidade.html", f"Política de Privacidade — {APP}", b, "en/privacy.html")

def privacy_en():
    b = f"""<main class="doc"><h1>Privacy Policy</h1><p class="meta">Effective date: {PRIV_DATE_EN}</p>
<p>This policy explains what data the <b>{APP}</b> app (the “App”) processes, why, who it is shared with, and your rights. It describes what the App actually does today. If that changes, we will update this page. The Portuguese version is the primary one.</p>
<h2>1. Controller</h2><p>{OWNER}, NIF/NIE {NIF}, {ADDR}, Spain. Privacy contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>2. Summary</h2><ul><li>You can use the App <b>without an account</b>. Your progress then stays only on your device.</li>
<li>An account is optional and saves your progress to the cloud. You can sign in with email and password, an email sign-in link, Google or Apple when available on the platform. Social sign-in providers may send your email and, if available, your name.</li>
<li>We do not use advertising, ad tracking or crash-reporting tools, and we do not sell data. The App (iOS and Android) uses <b>anonymous usage statistics</b>, with no name, email or answers, to improve the course. In the European Union, the European Economic Area, the United Kingdom and Switzerland (or if the device region cannot be determined), they are collected only if you agree. In other countries, such as Brazil, they are on by default, with a notice in the App. Wherever you are, you can turn them off at any time in <b>Configurações › Privacidade</b> (Settings › Privacy).</li>
<li>Purchases and subscriptions are processed by Apple or Google, with technical support from RevenueCat. <b>We never receive your card details.</b></li></ul>
<h2>3. Data we process</h2>
<table><tr><th>Data</th><th>When</th><th>Purpose and legal basis</th><th>Where</th></tr>
<tr><td><b>Learning progress</b>: the goal and daily minutes you chose at the start, XP, streak, last practice day, hearts, completed lessons, seals and stamps, interrupted lesson attempts, and the items you got wrong (for review).</td><td>Whenever you use the App</td><td>Providing the service (contract).</td><td>On your device (app or browser local storage). If you have an account, also in the cloud (Supabase).</td></tr>
<tr><td><b>Account data</b>: email, user ID, created and last sign-in dates; password as a hash only for email sign-in and, if provided by Google or Apple, your name.</td><td>Only if you create or access an account</td><td>Authentication and progress sync (contract).</td><td>Supabase (EU, Ireland); Google or Apple provide social sign-in data.</td></tr>
<tr><td><b>Technical security data</b>: IP address and browser or device information in the provider's authentication and access logs.</td><td>When you sign in, sign up or sync</td><td>Security and abuse prevention (legitimate interest).</td><td>Supabase, for a limited time.</td></tr>
<tr><td><b>Purchase data</b>: the pseudonymous purchases SDK identifier, products bought, transaction data and functional purchase or subscription status.</td><td>When you open the App and when you check, make or restore a purchase, or use purchased access</td><td>Processing, restoring and verifying course access (contract), and producing aggregated purchase and revenue metrics in the RevenueCat dashboard.</td><td>RevenueCat (USA) and Apple / Google.</td></tr>
<tr><td><b>Usage statistics</b>: study goal, event and outcome, source, offer set and plan, lesson identifier where applicable, date/time, platform, app version and a random pseudonymous UUID. Events do not include email, account ID, exercise answers or IP address.</td><td>In the iOS and Android App. In the EU/EEA, UK, Switzerland or an unknown region: only after you agree. Elsewhere: on by default until you turn them off.</td><td>Measuring product usage and guiding improvements. In the EU/EEA, UK and Switzerland: consent (GDPR art. 6(1)(a) and ePrivacy rules on device access). Elsewhere: legitimate interest (LGPD art. 7, IX, or GDPR art. 6(1)(f), as applicable), with the right to object by turning them off.</td><td>Local device queue and Supabase for processing.</td></tr>
<tr><td><b>Device region</b> (country code from the language and region settings)</td><td>On the purchase screen and when the App opens</td><td>Showing store information and deciding whether usage statistics need prior consent. Read on the device only, never sent to us and not included in the statistics.</td><td>Device only.</td></tr></table>
<p>We do <b>not</b> collect your phone number, location (GPS), contacts, photos, microphone, advertising ID or sensitive data. Sentence audio is recorded and bundled with the App. If a sentence has no recording, the App may request Spanish speech from the operating system's text-to-speech engine; its operation and any processing depend on the system and that engine's provider. The App also downloads a public configuration (for example, which lessons are free). This request does not include account or progress data, but like any internet connection it may generate technical metadata such as an IP address that may appear in server logs.</p>
<h2>4. Processors</h2><ul>
<li><b>Supabase</b>: database and authentication, hosted in the EU region (Ireland, eu-west-1). It also sends the confirmation and sign-in emails.</li>
<li><b>Google</b> and <b>Apple</b>: optional social sign-in providers when available on the platform and if you choose to use those services.</li>
<li><b>RevenueCat, Inc.</b> (USA): technical processing of purchases and subscriptions.</li>
<li><b>Apple</b> (App Store) and <b>Google</b> (Google Play): payment, billing, renewals and refunds, under their own privacy policies.</li>
<li><b>GitHub Pages</b>: hosts this website and the web demo, and may log IP addresses in technical logs.</li></ul>
<p>Transfers outside the European Economic Area (for example, to the USA) rely on appropriate safeguards, such as the European Commission's Standard Contractual Clauses or the EU-US Data Privacy Framework where applicable. We do not sell data or share it for advertising.</p>
<h2>5. Retention</h2><ul>
<li>Local data: until you delete the App or clear your browser data.</li>
<li>Cloud account and progress: while the account exists. Deletion in the App is immediate. Email requests are handled within 30 days.</li>
<li>Purchase records: as long as tax and accounting law requires.</li>
<li>Usage statistics: 90 days in Supabase, with a daily deletion routine. If you turn them off (or withdraw consent), collection stops immediately and the local queue is cleared; removal of events already sent is requested from Supabase on the next connection. To prevent resending, a pseudonymous record containing the random installation UUID and a hash of the deletion secret, with no account link, is kept for 90 days.</li>
<li>Technical logs: for the provider's retention period.</li></ul>
<h2>6. Deleting your data</h2><p>Without an account: uninstall the App (or clear the site data in your browser) and local progress is removed from the device. With an account: in the App, open <b>Configurações → Sua conta → Apagar conta</b> (Settings → Account → Delete account). The account and its cloud progress are deleted immediately. To delete usage statistics, turn off <b>Compartilhar estatísticas de uso</b> (Share usage statistics) in the Privacy section of Settings. This stops collection, clears the local queue and requests removal of events already sent on the next connection; the deletion request stays pending until it can be sent. If you can no longer use the App, email <a href="mailto:{EMAIL}">{EMAIL}</a>. See <a href="delete-account.html">How to delete your account</a>. Deleting the account <b>does not cancel</b> a subscription: cancel it in the App Store or Google Play.</p>
<h2>7. Minimum age</h2><p>The App is meant for people <b>aged 14 or over</b> (the digital-consent age in Spain under the LOPDGDD), or the minimum age required in your country if that is higher. If you are younger, use the App only with your parent's or guardian's permission and supervision. If we learn that we collected a child's data without that permission, we will delete it.</p>
<h2>8. Your rights (GDPR / LOPDGDD)</h2><p>You have the right of access, rectification, erasure, objection, restriction and portability, and the right not to be subject to solely automated decisions. Email <a href="mailto:{EMAIL}">{EMAIL}</a>; we reply within one month. You may also complain to the <b>Spanish Data Protection Agency (AEPD)</b> at <a href="https://www.aepd.es">www.aepd.es</a>.</p>
<h2>9. Brazil (LGPD)</h2><p>You may request confirmation of processing, access, correction, anonymisation, blocking or deletion, portability, information about sharing, and review of automated decisions (LGPD art. 18). You may also complain to the <b>ANPD</b>. The legal bases we use are contract, legal obligation, legitimate interest (including for usage statistics outside the EU/EEA, UK and Switzerland, which you can turn off at any time) and, for usage statistics in the EU/EEA, UK and Switzerland, consent, which you may withdraw.</p>
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
<h2>3. Conta</h2><p>A conta é opcional (e-mail e senha, link enviado por e-mail, Google ou Apple quando disponíveis na plataforma) e serve para salvar o progresso na nuvem. Você é responsável por manter sua senha em segredo nos logins por e-mail. O progresso de quem usa sem conta fica só no aparelho e pode se perder se o App for apagado.</p>
<h2>4. Amostra e acesso ao curso</h2><ul>
<li>O App oferece <b>sete lições gratuitas</b>, que podem ser repetidas: seis lições do início do percurso e uma amostra de Papelada.</li>
<li>A <b>compra única</b> dá acesso sem vencimento ao curso atual: 117 lições, incluindo 21 lições em Papelada, e as correções e melhorias desse curso. Novos cursos, se lançados, podem ser vendidos separadamente.</li>
<li>A <b>assinatura mensal</b> dá acesso ao curso atual enquanto estiver ativa. Ela renova automaticamente ao fim de cada período, conforme as condições exibidas pela loja.</li>
<li><b>Pagamento</b>: é feito pela sua conta da Apple (App Store) ou do Google (Google Play). A loja mostra o preço, a moeda e os impostos antes da compra.</li>
<li><b>Cancelamento</b>: cancele a assinatura nas configurações de assinaturas da App Store ou do Google Play. O acesso mensal continua até o fim do período já pago. Desinstalar o App ou apagar a conta não cancela a assinatura.</li>
<li>Se você já assina e fizer a compra única do curso, a compra <b>não cancela nem abate</b> a assinatura ativa. Para parar futuras cobranças mensais, cancele-a separadamente na loja. A compra única não exige uma assinatura mensal.</li>
<li>Cada tentativa de lição tem <b>cinco corações</b>, em qualquer modalidade. Se eles acabarem, o App conduz uma revisão gratuita dos erros, recupera os corações e permite retomar a tentativa. Revisões, XP, ofensiva e proteções de sequência não são vendidos.</li>
<li><b>Reembolsos</b>: são decididos pela Apple ou pelo Google, de acordo com as políticas de cada loja. Não conseguimos fazer reembolsos diretamente.</li>
<li><b>Direito de desistência (UE)</b>: para conteúdo digital não fornecido em suporte material, a legislação prevê uma exceção ao direito de desistência quando a execução começa durante o prazo de desistência após seu consentimento expresso prévio, o reconhecimento de que perderá esse direito e a confirmação do contrato exigida por lei. A aplicação dessa exceção depende de esses requisitos legais serem cumpridos; nada nesta cláusula elimina direitos que a lei preserve. Consulte as informações e confirmações apresentadas pela loja antes da compra. As políticas de reembolso da loja também se aplicam.</li>
<li>Alterações de preço da assinatura seguem as regras das lojas e são informadas por elas. As condições vigentes aparecem antes da compra.</li></ul>
<h2>5. Uso permitido</h2><p>O App é para uso pessoal e não comercial. Não é permitido copiar, revender ou redistribuir o conteúdo (textos, áudios, ilustrações, personagens), fazer engenharia reversa, burlar travas ou pagamentos, nem usar o App de forma que prejudique o serviço ou outras pessoas.</p>
<h2>6. Propriedade intelectual</h2><p>O App, o conteúdo das lições, os áudios, as ilustrações e os personagens (como a Lu e o Lino) pertencem a {OWNER} ou aos seus licenciantes. Você recebe uma licença limitada, pessoal, intransferível e revogável para usar o App.</p>
<h2>7. Disponibilidade e mudanças</h2><p>Trabalhamos para manter o App funcionando, mas ele pode ter interrupções, erros ou mudanças de conteúdo. Podemos alterar, suspender ou encerrar funções. Se o Premium for encerrado, avisaremos e você poderá pedir reembolso à loja de acordo com as regras dela.</p>
<h2>8. Responsabilidade</h2><p>O App é fornecido “no estado em que se encontra”. Na medida permitida por lei, não respondemos por danos indiretos nem por perda de progresso guardado só no aparelho. Nada nestes termos limita direitos que você tem como consumidor pela lei aplicável (incluindo o Código de Defesa do Consumidor, para consumidores no Brasil, e a legislação espanhola e europeia de consumo), nem nossa responsabilidade por dolo ou culpa grave.</p>
<h2>9. Encerramento</h2><p>Você pode parar de usar o App e pedir a exclusão da conta a qualquer momento (veja a Política de Privacidade). Podemos suspender contas que violem estes termos.</p>
<h2>10. Lei aplicável e foro</h2><p>Estes termos são regidos pela lei da <b>Espanha</b>. Se você for consumidor, continua tendo a proteção das normas obrigatórias do país onde mora e pode recorrer aos tribunais do seu domicílio. Consumidores podem procurar os meios de resolução extrajudicial de conflitos disponíveis no seu país. A Comissão Europeia mantém uma <a href="https://consumer-redress.ec.europa.eu/list-alternative-dispute-resolution-adr-bodies_en">lista de entidades de resolução alternativa de litígios (ADR)</a> reconhecidas nos países da UE.</p>
<h2>11. Contato</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · {ADDR}</p>
<h2>12. Alterações</h2><p>Podemos atualizar estes termos. Mudanças importantes serão avisadas no App ou nesta página, com nova data de vigência.</p></main>"""
    page("pt", "termos.html", f"Termos e Condições — {APP}", b, "en/terms.html")

def terms_en():
    b = f"""<main class="doc"><h1>Terms &amp; Conditions</h1><p class="meta">Effective date: {DATE_EN}</p>
<p>These terms govern your use of the <b>{APP}</b> app (the “App”), provided by {OWNER}, NIF/NIE {NIF}, {ADDR}, Spain (“we”). By using the App you agree to these terms and to the <a href="privacy.html">Privacy Policy</a>. The Portuguese version is the primary one; if the two versions conflict, the Portuguese one prevails to the extent the law allows.</p>
<h2>1. The service</h2><p>The App teaches the Spanish of Spain to Portuguese speakers, with lessons, audio, exercises and progress tracking. It is educational content, not legal or immigration advice: information about procedures (NIE, TIE, empadronamiento, etc.) is general and may change. Always check the official sources.</p>
<h2>2. Age</h2><p>You must be at least 14, or the minimum age in your country if that is higher. Younger users may use the App only with the permission and supervision of a parent or guardian, who accepts these terms on their behalf.</p>
<h2>3. Account</h2><p>An account is optional (email and password, an email sign-in link, Google or Apple when available on the platform) and saves your progress to the cloud. Keep your password secret when using email sign-in. Progress of users without an account stays only on the device and may be lost if the App is deleted.</p>
<h2>4. Sample and course access</h2><ul>
<li>The App offers <b>seven free lessons</b> that you can repeat: six lessons at the start of the journey and one Papelada sample.</li>
<li>The <b>one-time course purchase</b> gives you access without expiry to the current course: 117 lessons, including 21 Papelada lessons, and corrections and improvements to that course. New courses, if released, may be sold separately.</li>
<li>The <b>monthly subscription</b> gives access to the current course while active. It renews automatically at the end of each period under the terms shown by the store.</li>
<li><b>Payment</b> is made through your Apple (App Store) or Google (Google Play) account. The store shows the price, currency and taxes before you buy.</li>
<li><b>Cancellation</b>: cancel the subscription in the App Store or Google Play subscription settings. Monthly access continues until the end of the paid period. Uninstalling the App or deleting your account does not cancel the subscription.</li>
<li>If you already subscribe and buy the one-time course, the purchase <b>does not cancel or offset</b> the active subscription. Cancel it separately in the store to stop future monthly charges. The one-time purchase does not require a monthly subscription.</li>
<li>Each lesson attempt has <b>five hearts</b>, on every plan. If they run out, the App guides you through a free review of your mistakes, restores the hearts, and lets you resume the attempt. Reviews, XP, streaks and streak freezes are not sold.</li>
<li><b>Refunds</b> are decided by Apple or Google under their own store policies. We cannot issue refunds directly.</li>
<li><b>EU right of withdrawal</b>: for digital content not supplied on a tangible medium, the law provides an exception to the right of withdrawal where performance begins during the withdrawal period after your prior express consent, acknowledgement that you will lose that right, and the legally required contract confirmation. Whether the exception applies depends on those legal requirements being met; nothing in this clause removes rights the law preserves. Review the information and confirmations shown by the store before purchase. The store's refund policies also apply.</li>
<li>Subscription price changes follow store rules and are notified by the store. The current terms appear before purchase.</li></ul>
<h2>5. Acceptable use</h2><p>The App is for personal, non-commercial use. You may not copy, resell or redistribute its content (texts, audio, illustrations, characters), reverse-engineer it, bypass locks or payments, or use it in ways that harm the service or other people.</p>
<h2>6. Intellectual property</h2><p>The App, the lesson content, audio, illustrations and characters (such as Lu and Lino) belong to {OWNER} or its licensors. You receive a limited, personal, non-transferable and revocable licence to use the App.</p>
<h2>7. Availability and changes</h2><p>We work to keep the App running, but it may have outages, bugs or content changes. We may change, suspend or discontinue features. If Premium is discontinued, we will let you know, and you may ask the store for a refund under its rules.</p>
<h2>8. Liability</h2><p>The App is provided “as is”. To the extent the law allows, we are not liable for indirect damages or for the loss of progress stored only on a device. Nothing in these terms limits your statutory consumer rights (including Spanish and EU consumer law, and the Brazilian Consumer Defence Code for consumers in Brazil), or our liability for wilful misconduct or gross negligence.</p>
<h2>9. Termination</h2><p>You may stop using the App and request deletion of your account at any time (see the Privacy Policy). We may suspend accounts that breach these terms.</p>
<h2>10. Governing law and jurisdiction</h2><p>These terms are governed by the laws of <b>Spain</b>. If you are a consumer, you keep the protection of the mandatory rules of your country of residence and may bring claims before the courts where you live. Consumers may seek out-of-court dispute resolution options available in their country. The European Commission maintains a <a href="https://consumer-redress.ec.europa.eu/list-alternative-dispute-resolution-adr-bodies_en">list of alternative dispute resolution (ADR) bodies</a> recognised in EU countries.</p>
<h2>11. Contact</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · {ADDR}</p>
<h2>12. Changes</h2><p>We may update these terms. Material changes will be announced in the App or on this page, with a new effective date.</p></main>"""
    page("en", "en/terms.html", f"Terms & Conditions — {APP}", b, "../termos.html")

def delete_pages():
    pt = f"""<main class="doc"><h1>Como apagar sua conta do {APP}</h1><p class="meta">Atualizado em {PRIV_DATE_PT}</p>
<h2>No App (recomendado)</h2><ol><li>Abra o {APP} e toque na engrenagem de <b>Configurações</b>, depois em <b>Sua conta</b>.</li><li>Toque em <b>Apagar conta</b>.</li><li>Confirme em <b>Apagar para sempre</b>.</li></ol>
<p>A exclusão é imediata e permanente: apagamos sua conta (e-mail e senha), seu perfil e todo o progresso salvo na nuvem. Neste aparelho, o App volta para o modo visitante.</p>
<h2>Por e-mail</h2><p>Se você não consegue usar o App, escreva para <a href="mailto:{EMAIL}?subject=Apagar%20conta">{EMAIL}</a> a partir do e-mail da conta, com o assunto “Apagar conta”. Apagamos em até 30 dias e confirmamos por e-mail.</p>
<h2>O que é apagado e o que fica</h2><ul><li><b>Apagado</b>: conta, perfil, lições concluídas, XP, ofensiva, carimbos, revisões.</li>
<li><b>Fica</b>: registros de compra que a lei fiscal obriga a guardar, mantidos pela Apple/Google e pela RevenueCat, e logs técnicos de segurança até expirarem.</li>
<li>Progresso de visitante no seu aparelho: apague desinstalando o App.</li></ul>
<h2>Estatísticas de uso</h2><p>As estatísticas de uso são anônimas e identificadas por um UUID aleatório do aparelho, não pelo seu e-mail. Na UE/EEE, no Reino Unido e na Suíça, só são coletadas se você aceitar; nos demais países, ficam ligadas por padrão. Você pode desligá-las a qualquer momento: desative <b>Compartilhar estatísticas de uso</b> em <b>Configurações → Privacidade</b>. A coleta para na hora, a fila local é apagada e a remoção dos eventos enviados é solicitada ao Supabase na próxima conexão. Para impedir reenvios, um registro pseudônimo com o UUID aleatório da instalação e o hash do segredo de exclusão, sem vínculo com sua conta, fica por 90 dias.</p>
<h2>Compras e assinatura</h2><p>A compra única do curso não gera cobranças recorrentes. Se você tiver uma assinatura mensal ativa, comprar o curso não cancela nem abate essa assinatura. <b>Apagar a conta não cancela a assinatura.</b> Para parar cobranças mensais futuras, cancele na loja: <a href="https://support.apple.com/pt-br/118428">App Store (Apple)</a> ou <a href="https://support.google.com/googleplay/answer/7018481?hl=pt-BR">Google Play</a>. Reembolsos seguem as regras da loja.</p>
<p>Mais detalhes na <a href="privacidade.html">Política de Privacidade</a>.</p></main>"""
    page("pt", "apagar-conta.html", f"Apagar conta — {APP}", pt, "en/delete-account.html")
    en = f"""<main class="doc"><h1>How to delete your {APP} account</h1><p class="meta">Updated {PRIV_DATE_EN}</p>
<h2>In the App (recommended)</h2><ol><li>Open {APP} and tap the <b>Configurações</b> (Settings) gear, then <b>Sua conta</b> (Account).</li><li>Tap <b>Apagar conta</b> (Delete account).</li><li>Confirm with <b>Apagar para sempre</b> (Delete forever).</li></ol>
<p>Deletion is immediate and permanent: we delete your account (email and password), your profile and all progress saved in the cloud. On this device, the App goes back to guest mode.</p>
<h2>By email</h2><p>If you can't use the App, email <a href="mailto:{EMAIL}?subject=Delete%20account">{EMAIL}</a> from your account address with the subject “Delete account”. We delete within 30 days and confirm by email.</p>
<h2>What is deleted and what is kept</h2><ul><li><b>Deleted</b>: account, profile, completed lessons, XP, streak, stamps, review items.</li>
<li><b>Kept</b>: purchase records that tax law requires (held by Apple/Google and RevenueCat) and technical security logs until they expire.</li>
<li>Guest progress on your device: remove it by uninstalling the App.</li></ul>
<h2>Usage statistics</h2><p>Usage statistics are anonymous and identified by a random device UUID, not your email. In the EU/EEA, UK and Switzerland they are collected only if you agree; elsewhere they are on by default. You can turn them off at any time: turn off <b>Compartilhar estatísticas de uso</b> (Share usage statistics) under <b>Configurações → Privacidade</b> (Settings → Privacy). Collection stops immediately, the local queue is cleared, and removal of sent events is requested from Supabase on the next connection. To prevent resending, a pseudonymous record containing the random installation UUID and a hash of the deletion secret, with no account link, is kept for 90 days.</p>
<h2>Purchases and subscription</h2><p>The one-time course purchase creates no recurring charges. If you have an active monthly subscription, buying the course does not cancel or offset it. <b>Deleting your account does not cancel your subscription.</b> To stop future monthly charges, cancel it in the store: <a href="https://support.apple.com/en-us/118428">App Store (Apple)</a> or <a href="https://support.google.com/googleplay/answer/7018481?hl=en">Google Play</a>. Refunds follow the store's rules.</p>
<p>More in the <a href="privacy.html">Privacy Policy</a>.</p></main>"""
    page("en", "en/delete-account.html", f"Delete account — {APP}", en, "../apagar-conta.html")

def support_page():
    name = "Vamos Espanha!"
    pt = f"""<main class="doc"><h1>Suporte do {name}</h1><p class="meta">Atualizado em 17 de outubro de 2026</p>
<p>Precisa de ajuda com o {name}? Escreva para <a href="mailto:{EMAIL}?subject=Suporte%20Vamos%20Espanha">{EMAIL}</a>. Respondemos normalmente em até 2 dias úteis. Se puder, conte o modelo do aparelho, a versão do iOS e o que aconteceu.</p>
<h2>Perguntas frequentes</h2>
<h3>Como restauro uma compra?</h3><p>No App, abra a engrenagem de <b>Configurações</b> e toque em <b>Restaurar compras</b>. Você também encontra <b>Restaurar compras</b> na tela do Premium. Use a mesma conta Apple (Apple ID) com que fez a compra.</p>
<h3>Como cancelo a assinatura?</h3><p>A assinatura é gerenciada pela Apple. No iPhone, abra <b>Ajustes</b> → toque no seu nome (<b>Apple ID</b>) → <b>Assinaturas</b> → {name} → <b>Cancelar assinatura</b>. O Premium continua até o fim do período já pago. Apagar o App ou a conta não cancela a assinatura. <a href="https://support.apple.com/pt-br/118428">Ajuda da Apple</a>.</p>
<h3>Como excluo minha conta?</h3><p>No App, abra <b>Configurações</b> → <b>Sua conta</b> → <b>Apagar conta</b> e confirme em <b>Apagar para sempre</b>. Se não conseguir usar o App, escreva para <a href="mailto:{EMAIL}?subject=Apagar%20conta">{EMAIL}</a>. Veja <a href="apagar-conta.html">Como apagar sua conta</a>.</p>
<h3>Não estou ouvindo o áudio</h3><p>Confira se o iPhone não está no <b>modo silencioso</b> (chave ou botão de ação na lateral) e se o volume está alto. Se estiver usando fones Bluetooth, verifique se estão conectados. Se continuar sem som, feche e abra o App de novo.</p>
<h3>Meu progresso fica salvo?</h3><p>Sem conta, o progresso fica salvo só neste aparelho e se perde se você apagar o App. Com uma conta (em <b>Configurações</b> → <b>Sua conta</b>), o progresso é salvo na nuvem e você o recupera ao entrar em outro aparelho ou reinstalar o App.</p>
<h2>Contato</h2><p><a href="mailto:{EMAIL}">{EMAIL}</a> · {OWNER} · {ADDR}, Espanha</p>
<p>Veja também a <a href="privacidade.html">Política de Privacidade</a> e os <a href="termos.html">Termos e Condições</a>.</p></main>"""
    page("pt", "suporte.html", f"Suporte — {name}", pt, "en/index.html")

open(os.path.join(ROOT, "style.css"), "w").write(CSS)
delete_pages()
support_page(); landing("pt"); landing("en"); privacy_pt(); privacy_en(); terms_pt(); terms_en()
open(os.path.join(ROOT, ".nojekyll"), "w").write("")
# aliases so /privacy and /terms also work in PT root and /en/privacidade etc.
print("built")
