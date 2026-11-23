# Gera todas as páginas. Para adicionar um transtorno, inclua um item em D e rode: python build.py
import html
D=[
dict(f="tdah",n="TDAH",full="Transtorno de Déficit de Atenção e Hiperatividade",
 r="Condição do neurodesenvolvimento que afeta atenção, controle de impulsos e nível de atividade. Começa na infância e pode seguir na vida adulta.",
 o="O TDAH envolve diferenças no funcionamento de circuitos cerebrais ligados à autorregulação. Existem três apresentações: desatenta, hiperativa/impulsiva e combinada. Atinge cerca de 5% das crianças e 2,5% dos adultos.",
 s=["Dificuldade de manter foco em tarefas longas ou monótonas","Esquecimentos frequentes, perda de objetos, atrasos","Inquietação, fala excessiva, dificuldade de esperar a vez","Impulsividade em decisões e conversas","Desorganização crônica e procrastinação"],
 c="Forte componente genético (hereditariedade de cerca de 70–80%). Prematuridade, baixo peso ao nascer e exposição pré-natal a álcool e tabaco aumentam o risco. Não é causado por má educação, excesso de telas ou falta de disciplina.",
 d="Clínico: feito por psiquiatra, neurologista ou psicólogo a partir de entrevista detalhada, histórico escolar e escalas. Os sintomas precisam começar antes dos 12 anos e aparecer em mais de um ambiente. Não existe exame de sangue ou imagem que confirme.",
 t="Combinação de medicação (metilfenidato, lisdexanfetamina, atomoxetina, entre outras), terapia cognitivo-comportamental, orientação a pais e adaptações na escola ou no trabalho.",
 cura="Não há cura, mas há controle muito eficaz. Os sintomas podem diminuir ou mudar de forma com a idade, e o tratamento melhora desempenho, relações e qualidade de vida.",
 p=["Não há como prevenir a origem genética","Diagnóstico e intervenção precoces reduzem prejuízos acadêmicos e emocionais","Rotina de sono regular, exercício físico e redução de distrações","Listas, alarmes e divisão de tarefas em etapas curtas"]),
dict(f="ansiedade",n="Ansiedade",full="Transtornos de Ansiedade",
 r="Grupo de condições em que medo e preocupação são intensos, persistentes e desproporcionais, a ponto de atrapalhar a vida.",
 o="Ansiedade normal é uma resposta de alerta. Vira transtorno quando é excessiva e duradoura. Inclui transtorno de ansiedade generalizada, transtorno de pânico, fobia social, fobias específicas e agorafobia.",
 s=["Preocupação difícil de controlar na maior parte dos dias","Palpitações, falta de ar, tremores, sudorese, tensão muscular","Crises de pânico com medo intenso e repentino","Evitação de lugares ou situações","Insônia, irritabilidade, fadiga e dificuldade de concentração"],
 c="Mistura de genética, características de temperamento, experiências estressantes ou traumáticas, desequilíbrios em sistemas de neurotransmissores (como serotonina e GABA) e fatores como excesso de cafeína, álcool e privação de sono.",
 d="Clínico, por psiquiatra ou psicólogo. É preciso descartar causas físicas, como problemas de tireoide, arritmias e uso de substâncias. Escalas como GAD-7 ajudam a medir a intensidade.",
 t="Psicoterapia (terapia cognitivo-comportamental é a de maior evidência), medicação (ISRS e IRSN como primeira linha; benzodiazepínicos só por curto prazo e com cautela) e técnicas de regulação como respiração e relaxamento.",
 cura="É um dos transtornos que mais respondem ao tratamento. Muitas pessoas chegam à remissão completa, embora algumas precisem de acompanhamento prolongado ou tenham recaídas em fases de estresse.",
 p=["Exercício físico regular","Sono adequado e redução de cafeína e álcool","Práticas como respiração diafragmática, meditação e mindfulness","Enfrentar gradualmente situações temidas em vez de evitá-las","Buscar ajuda cedo, antes de o quadro se cronificar"]),
dict(f="depressao",n="Depressão",full="Transtorno Depressivo Maior",
 r="Alteração persistente do humor, com tristeza profunda ou perda de interesse, que afeta pensamentos, corpo e rotina. Não é fraqueza nem falta de vontade.",
 o="É uma das principais causas de incapacidade no mundo. Para o diagnóstico, os sintomas duram pelo menos duas semanas e causam prejuízo importante. Existem também a distimia (forma crônica), a depressão pós-parto e a depressão sazonal.",
 s=["Tristeza, vazio ou desesperança na maior parte do dia","Perda de prazer em atividades antes prazerosas","Alterações de sono e apetite, cansaço intenso","Sentimento de culpa ou inutilidade, dificuldade de concentração","Pensamentos de morte ou suicídio (exigem atenção imediata)"],
 c="Fatores biológicos (genética, neurotransmissores, inflamação, hormônios), psicológicos (traços de personalidade, padrões de pensamento) e sociais (perdas, violência, isolamento, estresse crônico, desemprego).",
 d="Clínico, por psiquiatra ou psicólogo. Exames de sangue podem ser pedidos para excluir causas como anemia, hipotireoidismo e deficiência de vitamina B12. Escalas como PHQ-9 apoiam a avaliação.",
 t="Psicoterapia (TCC, terapia interpessoal), antidepressivos (ISRS, IRSN e outros), atividade física e, em casos resistentes, estimulação magnética transcraniana, eletroconvulsoterapia ou cetamina/escetamina sob supervisão especializada.",
 cura="É tratável e a remissão é possível. A maioria melhora com tratamento adequado. O risco de recaída existe, por isso muitas vezes o acompanhamento continua após a melhora.",
 p=["Manter vínculos sociais e pedir apoio","Atividade física regular, sono e alimentação equilibrada","Reduzir álcool e outras substâncias","Aprender a lidar com estresse e perdas, com apoio psicológico se preciso","Atenção a sinais precoces e histórico familiar"]),
dict(f="bipolaridade",n="Bipolaridade",full="Transtorno Bipolar",
 r="Condição marcada por alternância entre episódios de euforia ou irritabilidade intensa (mania ou hipomania) e episódios depressivos.",
 o="Os tipos principais são o tipo I (com episódios de mania completos), o tipo II (hipomania e depressão) e a ciclotimia. Costuma começar no fim da adolescência ou início da vida adulta.",
 s=["Mania: energia exagerada, pouca necessidade de sono, fala acelerada, grandiosidade, gastos e decisões impulsivas","Depressão: tristeza, lentidão, desesperança, perda de interesse","Mudanças bruscas de humor e de nível de atividade","Em casos graves, sintomas psicóticos (delírios, alucinações)"],
 c="É altamente hereditário. Alterações em circuitos cerebrais e ritmo circadiano contribuem. Estresse, privação de sono, uso de drogas e antidepressivos sem estabilizador podem desencadear episódios.",
 d="Clínico, com psiquiatra. É comum ser confundido com depressão por anos, porque a pessoa procura ajuda na fase depressiva. Por isso o histórico de episódios de euforia, inclusive relatado por familiares, é essencial.",
 t="Estabilizadores de humor (lítio, valproato, lamotrigina), antipsicóticos atípicos, psicoeducação, psicoterapia e regulação rigorosa de rotina e sono. Antidepressivos isolados podem induzir mania e devem ser evitados.",
 cura="Não há cura definitiva, é uma condição crônica, mas é controlável. Com tratamento contínuo, muitas pessoas levam uma vida estável e produtiva. Interromper a medicação por conta própria é a principal causa de recaída.",
 p=["Não é possível prevenir a condição, mas dá para prevenir crises","Rotina fixa de sono, alimentação e atividades","Evitar álcool e drogas","Reconhecer os sinais de alerta precoces com família e equipe de saúde","Manter o tratamento e as consultas regulares"]),
dict(f="borderline",n="Borderline",full="Transtorno de Personalidade Borderline (TPB)",
 r="Padrão de instabilidade nas emoções, na autoimagem e nos relacionamentos, com impulsividade e medo intenso de abandono.",
 o="Também chamado de transtorno de personalidade limítrofe. As emoções são vividas com muita intensidade e demoram a se acalmar. Não é sinônimo de manipulação ou de drama: é sofrimento real, e a pessoa tem alto risco de autolesão.",
 s=["Medo intenso de abandono, real ou imaginado","Relações instáveis, alternando idealização e desvalorização","Imagem de si instável e sensação crônica de vazio","Impulsividade (gastos, sexo de risco, drogas, compulsão alimentar)","Raiva intensa, autolesão e ameaças ou tentativas de suicídio"],
 c="Combinação de predisposição genética e temperamento sensível com ambientes invalidantes na infância, como negligência, abuso e instabilidade familiar.",
 d="Clínico, por psiquiatra ou psicólogo, a partir de entrevista estruturada. É preciso diferenciar de transtorno bipolar, depressão, TEPT e uso de substâncias, que podem coexistir.",
 t="A psicoterapia é o tratamento central: terapia comportamental dialética (DBT), terapia baseada em mentalização (MBT), terapia do esquema e terapia focada na transferência. Medicação trata sintomas associados (humor, ansiedade, impulsividade), mas não o transtorno em si.",
 cura="O prognóstico é melhor do que se acreditava. Estudos de seguimento mostram que a maioria das pessoas deixa de preencher critérios para o diagnóstico ao longo dos anos, sobretudo com terapia especializada.",
 p=["Apoio psicológico cedo para quem viveu trauma ou instabilidade na infância","Aprender habilidades de regulação emocional e tolerância ao mal-estar","Evitar álcool e drogas","Rede de apoio estável e plano de segurança para momentos de crise"]),
dict(f="toc",n="TOC",full="Transtorno Obsessivo-Compulsivo",
 r="Pensamentos intrusivos e angustiantes (obsessões) que levam a comportamentos ou rituais repetitivos (compulsões) para aliviar o desconforto.",
 o="As obsessões são involuntárias e a pessoa costuma saber que são exageradas. Temas comuns: contaminação, simetria, dúvida, medo de causar dano e pensamentos proibidos. Os rituais consomem tempo e prejudicam a vida.",
 s=["Obsessões: medo de contaminação, dúvida constante, necessidade de ordem","Compulsões: lavar as mãos, verificar, contar, repetir, organizar","Mais de uma hora por dia gasta com obsessões e rituais","Evitação de situações que desencadeiam as obsessões"],
 c="Genética, alterações em circuitos entre córtex frontal e gânglios da base, desequilíbrio de serotonina e glutamato. Estresse e eventos de vida podem agravar. Em crianças, infecções por estreptococo podem estar associadas em alguns casos.",
 d="Clínico, com psiquiatra ou psicólogo, usando escalas como a Y-BOCS. É importante diferenciar de ansiedade generalizada, tiques e traços obsessivos de personalidade.",
 t="Terapia cognitivo-comportamental com exposição e prevenção de resposta (EPR), que é o padrão-ouro, e medicação com ISRS em doses mais altas. Casos resistentes podem usar estimulação cerebral profunda ou outras técnicas.",
 cura="Não há cura no sentido de eliminar a predisposição, mas a maioria melhora de forma significativa, e muitos têm remissão dos sintomas com EPR e medicação.",
 p=["Procurar tratamento cedo evita a cronificação","Resistir a rituais, com orientação profissional","Família não deve participar das compulsões nem dar reasseguramento excessivo","Manejo de estresse e sono regular"]),
dict(f="tept",n="TEPT",full="Transtorno de Estresse Pós-Traumático",
 r="Reação persistente após viver ou testemunhar um evento traumático, com revivências, evitação e estado constante de alerta.",
 o="Pode surgir após violência, acidente, abuso, guerra, desastres ou perda súbita. Nem todos que passam por trauma desenvolvem TEPT. Se os sintomas duram mais de um mês e causam prejuízo, é preciso investigar.",
 s=["Lembranças invasivas, flashbacks e pesadelos","Evitação de lugares, pessoas e conversas ligados ao trauma","Pensamentos negativos, culpa, distanciamento emocional","Hipervigilância, sobressalto, irritabilidade e insônia"],
 c="Exposição a trauma combinada com fatores de risco, como trauma anterior, falta de apoio social, predisposição genética e transtornos prévios. O cérebro permanece em modo de ameaça, com amígdala hiperativa e alterações no hipocampo.",
 d="Clínico, por psiquiatra ou psicólogo, a partir do relato do evento e dos sintomas. Escalas como a PCL-5 ajudam. Coexiste com frequência com depressão e uso de substâncias.",
 t="Psicoterapias focadas no trauma (TCC focada no trauma, terapia de processamento cognitivo, exposição prolongada, EMDR) e medicação (sertralina, paroxetina, venlafaxina). Apoio psicossocial e atenção à segurança são fundamentais.",
 cura="É tratável e muitas pessoas se recuperam bem, em especial com terapia focada no trauma. A recuperação pode levar tempo e ser feita por etapas.",
 p=["Apoio social e acolhimento logo após o evento","Primeiros cuidados psicológicos e acompanhamento de quem vive situação de risco","Evitar o isolamento e o uso de álcool para lidar com a dor","Procurar ajuda profissional quando os sintomas persistem além de algumas semanas"]),
dict(f="esquizofrenia",n="Esquizofrenia",full="Esquizofrenia",
 r="Transtorno mental grave que afeta o pensamento, a percepção e o comportamento, com perda parcial de contato com a realidade (psicose).",
 o="Costuma iniciar entre o fim da adolescência e os 30 anos. Atinge cerca de 1% da população. Não significa múltiplas personalidades, e a maioria das pessoas com esquizofrenia não é violenta.",
 s=["Sintomas positivos: delírios, alucinações (como ouvir vozes), pensamento desorganizado","Sintomas negativos: apatia, embotamento emocional, isolamento, pobreza de fala","Sintomas cognitivos: dificuldade de atenção, memória e planejamento","Perda de insight: a pessoa pode não perceber que está doente"],
 c="Forte componente genético e alterações no neurodesenvolvimento (dopamina e glutamato). Complicações na gestação, uso intenso de cannabis na adolescência, urbanização e estresse social são fatores de risco.",
 d="Clínico, por psiquiatra, com seguimento dos sintomas por pelo menos seis meses e exclusão de causas orgânicas e de substâncias. Exames ajudam a descartar outras condições.",
 t="Antipsicóticos (incluindo injetáveis de longa duração), reabilitação psicossocial, psicoeducação da família, terapia cognitivo-comportamental para psicose e acompanhamento em serviços como o CAPS. Clozapina é indicada em casos resistentes.",
 cura="É uma condição crônica sem cura definitiva, mas controlável. Muitas pessoas alcançam estabilidade, estudam, trabalham e mantêm relações com tratamento contínuo.",
 p=["Reconhecer e tratar cedo o primeiro episódio melhora o prognóstico","Evitar cannabis e outras drogas, sobretudo na adolescência","Manter a medicação e o acompanhamento regular","Apoio da família e rotina estável reduzem recaídas"]),
]
# ---------------------------------------------------------------
# Interface (layout, ícones, cores). Os textos ficam todos em D acima.
# ---------------------------------------------------------------
def ico(p, s=24):
    return f'<svg class="i" width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

P = dict(
 tdah='<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 ansiedade='<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 12h16a3 3 0 1 1-3 3"/><path d="M3 16h8"/>',
 depressao='<path d="M7 18a4 4 0 0 1-.5-8A6 6 0 0 1 18 9a4.5 4.5 0 0 1 0 9z"/>',
 bipolaridade='<path d="M2 12c2-8 4-8 6 0s4 8 6 0 4-8 6 0"/>',
 borderline='<circle cx="9" cy="12" r="6"/><circle cx="15" cy="12" r="6"/>',
 toc='<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
 tept='<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',
 esquizofrenia='<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 arrow='<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
 chev='<path d="M6 9l6 6 6-6"/>',
 menu='<path d="M4 7h16M4 12h16M4 17h16"/>',
 close='<path d="M6 6l12 12M18 6 6 18"/>',
 book='<path d="M2 5h6a4 4 0 0 1 4 4v11a3 3 0 0 0-3-3H2z"/><path d="M22 5h-6a4 4 0 0 0-4 4v11a3 3 0 0 1 3-3h7z"/>',
 heart='<path d="M12 20s-8-5-8-11a4.5 4.5 0 0 1 8-2.5A4.5 4.5 0 0 1 20 9c0 6-8 11-8 11z"/>',
 shieldok='<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 buoy='<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="M5.6 5.6l3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"/>',
 route='<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/>',
)
# cor principal e cor de fundo de cada transtorno
COL = dict(
 tdah=("#b45309", "#fef3dc"), ansiedade=("#0369a1", "#e1f1fb"), depressao=("#4338ca", "#e6e8fd"),
 bipolaridade=("#7e22ce", "#f4e9fd"), borderline=("#be185d", "#fde8f1"), toc=("#0f766e", "#dcf5f0"),
 tept=("#c2410c", "#ffeadb"), esquizofrenia=("#4d7c0f", "#edf6d8"),
)
def cv(f):
    c, b = COL[f]
    return f'--c:{c};--cb:{b}'

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&display=swap" rel="stylesheet">'

SOS = 'Em crise ou pensando em se machucar? Ligue <b>188 (CVV, 24h, gratuito)</b> ou <b>192 (SAMU)</b>.'

def head(t, d):
    return (f'<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(t)} | Mente Clara</title><meta name="description" content="{html.escape(d)}">{FONTS}'
            f'<link rel="stylesheet" href="style.css"></head><body><div class="strip">{SOS}</div>')

LOGO = ('<svg class="mark" width="30" height="30" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="none" stroke="currentColor" stroke-width="2"/>'
        '<path d="M16 2a14 14 0 0 0 0 28z" fill="currentColor"/></svg>')

def nav(cur):
    main = D[:5]; more = D[5:]
    a = ''.join(f'<a href="{x["f"]}.html"{" class=on" if x["f"]==cur else ""}>{x["n"]}</a>' for x in main)
    m = ''.join(f'<a href="{x["f"]}.html"{" class=on" if x["f"]==cur else ""}>{x["n"]}</a>' for x in more)
    return ('<header class="top"><div class="bar">'
            f'<a class="logo" href="index.html">{LOGO}<span>Mente Clara</span></a>'
            f'<nav class="links" id="menu">{a}<div class="more"><button type="button" aria-haspopup="true">Mais {ico(P["chev"],16)}</button><div class="drop">{m}</div></div></nav>'
            '<a class="cta" href="ajuda.html">Preciso de ajuda</a>'
            f'<button class="burger" aria-label="Abrir menu" aria-expanded="false" aria-controls="menu" onclick="var o=document.body.classList.toggle(\'menu\');this.setAttribute(\'aria-expanded\',o)">{ico(P["menu"],26)}{ico(P["close"],26)}</button>'
            '</div></header>')

def foot():
    l = ''.join(f'<a href="{x["f"]}.html">{x["n"]}</a>' for x in D)
    return ('<footer><div class="wrap fgrid"><div class="fbrand"><strong>' + LOGO + '<span>Mente Clara</span></strong>'
            '<p>Informação educativa sobre saúde mental. Não substitui avaliação, diagnóstico ou tratamento por profissional de saúde.</p></div>'
            f'<div class="fl">{l}<a href="ajuda.html">Onde buscar ajuda</a></div></div><div class="sos">{SOS}</div></footer>'
            '<script>(function(){var l=document.querySelectorAll(".toc a");if(!l.length||!("IntersectionObserver"in window))return;var m={};l.forEach(function(a){m[a.getAttribute("href").slice(1)]=a});'
            'var o=new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){l.forEach(function(a){a.classList.remove("active")});m[x.target.id].classList.add("active")}})},{rootMargin:"-15% 0px -75% 0px"});'
            'document.querySelectorAll("article section[id]").forEach(function(s){o.observe(s)})})();</script></body></html>')

def page(x):
    secs = [("o", "O que é", f'<p>{x["o"]}</p>', ""),
            ("s", "Sintomas", "<ul>" + "".join(f"<li>{i}</li>" for i in x["s"]) + "</ul>", ""),
            ("c", "Causas e fatores de risco", f'<p>{x["c"]}</p>', ""),
            ("d", "Diagnóstico", f'<p>{x["d"]}</p>', ""),
            ("t", "Tratamento", f'<p>{x["t"]}</p>', ""),
            ("u", "Tem cura?", f'<p class="callout">{x["cura"]}</p>', ""),
            ("p", "Prevenção e autocuidado", "<ul>" + "".join(f"<li>{i}</li>" for i in x["p"]) + "</ul>", ""),
            ("h", "Quando buscar ajuda", '<p>Procure um psiquiatra ou psicólogo quando os sintomas durarem semanas, atrapalharem estudo, trabalho ou relações, ou causarem sofrimento. No SUS, comece pela unidade básica de saúde ou pelo CAPS da sua cidade. Se houver risco de vida, ligue 192 ou 188.</p>', "help")]
    toc = ''.join(f'<a href="#{i}">{t}</a>' for i, t, _, _ in secs)
    body = ''.join(f'<section id="{i}"{" class=%s" % k if k else ""}><h2>{t}</h2>{c}</section>' for i, t, c, k in secs)
    return (head(x["full"], x["r"]) + nav(x["f"]) +
            f'<main style="{cv(x["f"])}"><div class="hero"><div class="wrap herorow"><div><p class="crumb"><a href="index.html">Início</a> / Transtornos / {x["n"]}</p>'
            f'<h1>{x["full"]}</h1><p class="lead">{x["r"]}</p></div><div class="bubble">{ico(P[x["f"]],44)}</div></div></div>'
            f'<div class="wrap doc"><aside class="toc"><strong>Nesta página</strong>{toc}</aside>'
            f'<article>{body}<p class="note">Conteúdo educativo, baseado em consensos clínicos gerais. Cada caso é único e exige avaliação profissional.</p></article></div></main>' + foot())

ART = ('<svg class="art" viewBox="0 0 420 420" aria-hidden="true"><circle cx="210" cy="210" r="196" fill="none" stroke="#c9dcd8" stroke-dasharray="3 9" stroke-width="2"/>'
       '<circle cx="210" cy="210" r="150" fill="#e4f1ee"/><path d="M210 60a150 150 0 0 0 0 300z" fill="#0b5d5b"/>'
       '<circle cx="210" cy="210" r="150" fill="none" stroke="#0b5d5b" stroke-width="2"/>'
       '<circle cx="338" cy="98" r="26" fill="#fef3dc"/><circle cx="82" cy="112" r="20" fill="#e1f1fb"/><circle cx="352" cy="318" r="22" fill="#fde8f1"/>'
       '<circle cx="76" cy="312" r="28" fill="#e6e8fd"/><circle cx="210" cy="14" r="12" fill="#dcf5f0"/></svg>')

def index():
    cards = ''.join(f'<a class="card" style="{cv(x["f"])}" href="{x["f"]}.html"><span class="cico">{ico(P[x["f"]],24)}</span><h3>{x["n"]}</h3><p>{x["r"]}</p><span class="more-l">Ler mais {ico(P["arrow"],18)}</span></a>' for x in D)
    return (head("Saúde mental: transtornos, tratamento e prevenção", "Guia completo sobre transtornos mentais.") + nav("") +
            '<main><div class="hero big"><div class="wrap herorow"><div><h1>Entender a mente é o primeiro passo para cuidar dela</h1>'
            '<p class="lead">Guia em português sobre transtornos mentais: o que são, sintomas, causas, tratamentos, se há cura e como prevenir.</p>'
            f'<a class="cta lg" href="#transtornos">Explorar transtornos {ico(P["chev"],20)}</a></div>{ART}</div></div>'
            f'<div class="wrap"><section id="transtornos" class="grid-sec"><h2>Transtornos mentais</h2><div class="grid">{cards}</div></section></div>'
            '<section class="band"><div class="wrap"><h2>Cada página responde</h2><div class="grid three">'
            f'<div class="mini">{ico(P["book"],26)}<h3>O que é e quais os sinais</h3><p>Definição, tipos e sintomas explicados em linguagem simples.</p></div>'
            f'<div class="mini">{ico(P["heart"],26)}<h3>Como tratar e se há cura</h3><p>Terapias, medicação e o que a ciência diz sobre recuperação.</p></div>'
            f'<div class="mini">{ico(P["shieldok"],26)}<h3>Como prevenir</h3><p>Hábitos, sinais de alerta e quando procurar um profissional.</p></div>'
            '</div></div></section></main>' + foot())

def ajuda():
    return (head("Onde buscar ajuda", "Serviços gratuitos de saúde mental no Brasil.") + nav("") +
            '<main><div class="hero"><div class="wrap"><h1>Onde buscar ajuda</h1><p class="lead">Você não precisa passar por isso sozinho. Estes serviços são gratuitos.</p></div></div>'
            '<div class="wrap helpwrap">'
            f'<section class="panel crisis"><h2><span class="hico">{ico(P["buoy"],24)}</span>Em crise agora</h2><ul><li><b>CVV – 188</b>: apoio emocional e prevenção do suicídio, 24 horas, ligação gratuita. Também por chat em cvv.org.br.</li><li><b>SAMU – 192</b>: emergência médica.</li><li><b>Pronto-socorro ou UPA</b> mais próximos em caso de risco imediato.</li></ul></section>'
            '<div class="two">'
            f'<section class="panel"><h2><span class="hico">{ico(P["route"],24)}</span>Acompanhamento contínuo</h2><ul><li><b>UBS (posto de saúde)</b>: porta de entrada do SUS, faz o encaminhamento.</li><li><b>CAPS</b>: Centros de Atenção Psicossocial, para casos moderados a graves.</li><li><b>Clínicas-escola</b> de universidades de Psicologia, com atendimento a baixo custo ou gratuito.</li></ul></section>'
            f'<section class="panel"><h2><span class="hico">{ico(P["heart"],24)}</span>Como ajudar alguém</h2><p>Escute sem julgar, pergunte diretamente como a pessoa está, evite minimizar o sofrimento e incentive a busca por um profissional. Se houver risco, não deixe a pessoa sozinha e ligue 192 ou 188.</p></section>'
            '</div></div></main>' + foot())

open("index.html", "w", encoding="utf-8").write(index()); open("ajuda.html", "w", encoding="utf-8").write(ajuda())
for x in D: open(x["f"] + ".html", "w", encoding="utf-8").write(page(x))