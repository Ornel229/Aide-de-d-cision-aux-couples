"""Assistant de lecture des résultats de porteur (drépanocytose) - prototype Hack2Skill.

Lancer :  streamlit run app.py
Aucune donnée n'est enregistrée sur disque : tout vit dans la session du navigateur.
"""
import csv
import io
import json
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

from genetique import (CATEGORIES, GENOTYPES, category_of, category_probabilities,
                       needs_counselling, punnett_grid)
from textes import QUIZ, TEXTS

st.set_page_config(page_title="Résultats de porteur", page_icon="🧬", layout="centered")

OPTIONS = ["?"] + GENOTYPES
COLORS = {"non_porteur": "#d9f2d9", "porteur": "#fff3c4", "drepano": "#ffd9b3", "autre": "#e3dcf5"}


# ---------- état de session ----------
def init_state():
    defaults = {"shares": [], "audit": [], "events": [], "steps": {}, "quiz_score": None}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M")


def log(event, detail=""):
    """Événement anonyme (jamais de nom ni de résultat)."""
    st.session_state.events.append(
        {"ts": now(), "event": event, "lang": st.session_state.get("lang", "fr"), "detail": detail}
    )


def on_step(i):
    done = st.session_state[f"step_{i}"]
    st.session_state.steps[i] = now() if done else None
    log("step", f"{i}:{'done' if done else 'undone'}")


def disp(genotype):
    return genotype.replace("T", "β")


# ---------- composants ----------
def speak_button(text, label, lang):
    code = {"fr": "fr-FR", "en": "en-US"}[lang]
    html = f"""
    <button id="b" style="padding:8px 14px;border-radius:8px;border:1px solid #888;background:#f4f4f4;font-size:15px;cursor:pointer">🔊 {label}</button>
    <script>
      document.getElementById("b").onclick = function() {{
        var u = new SpeechSynthesisUtterance({json.dumps(text, ensure_ascii=False)});
        u.lang = "{code}";
        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(u);
      }};
    </script>"""
    components.html(html, height=52)


def punnett_html(g1, g2, t):
    grid = punnett_grid(g1, g2)
    rows = ["<table style='border-collapse:collapse;width:100%;text-align:center;color:#111'>"]
    rows.append("<tr><th></th>" + "".join(f"<th style='padding:6px'>{disp(b)}</th>" for b in g2) + "</tr>")
    for a, line in zip(g1, grid):
        cells = ""
        for g in line:
            cat = category_of(g)
            cells += (
                f"<td style='background:{COLORS[cat]};border:3px solid #fff;padding:10px'>"
                f"<b>{disp(g)}</b><br><span style='font-size:0.8em'>{t['cat_short'][cat]}</span></td>"
            )
        rows.append(f"<tr><th style='padding:6px'>{disp(a)}</th>{cells}</tr>")
    rows.append("</table>")
    return "".join(rows)


def events_csv():
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=["ts", "event", "lang", "detail"])
    writer.writeheader()
    writer.writerows(st.session_state.events)
    return buf.getvalue()


# ---------- application ----------
init_state()

lang = st.radio("Langue / Language", ["fr", "en"], horizontal=True, key="lang",
                format_func=lambda k: TEXTS[k]["lang_name"])
t = TEXTS[lang]

g1 = st.session_state.get("sel1", "?")
g2 = st.session_state.get("sel2", "?")
both_known = g1 != "?" and g2 != "?"

tab_home, tab_res, tab_exp, tab_share, tab_next = st.tabs(t["tabs"])

# 1. Accueil
with tab_home:
    st.title(t["title"])
    st.caption(t["subtitle"])
    st.info(t["disclaimer"])
    st.markdown(t["welcome_body"])

# 2. Résultats
with tab_res:
    st.header(t["res_title"])
    st.caption(t["res_help"])
    col_a, col_b = st.columns(2)
    with col_a:
        st.selectbox(t["partner_a"], OPTIONS, key="sel1", format_func=lambda g: t["geno"][g])
    with col_b:
        st.selectbox(t["partner_b"], OPTIONS, key="sel2", format_func=lambda g: t["geno"][g])

# 3. Explication
with tab_exp:
    st.header(t["exp_title"])
    for label, g in ((t["partner_a"], g1), (t["partner_b"], g2)):
        if g != "?":
            st.info(f"**{label}** : {t['status'][g]}")
    if not both_known:
        st.warning(t["exp_unknown"])
    else:
        probs = category_probabilities(g1, g2)
        st.subheader(t["punnett_title"])
        st.caption(t["punnett_caption"])
        st.markdown(punnett_html(g1, g2, t), unsafe_allow_html=True)

        lines = [t["each_pregnancy"]]
        for cat in CATEGORIES:
            if probs[cat] > 0:
                lines.append(f"{t['cat'][cat]} : {int(probs[cat] * 100)} %")
        st.markdown("**" + lines[0] + "**\n\n" + "\n".join(f"- {line}" for line in lines[1:]))

        st.subheader(t["key_title"])
        for message in t["key_messages"]:
            st.markdown(f"- {message}")
        st.caption(t["uncertainty"])

        speech = " ".join(lines) + ". " + " ".join(t["key_messages"][:3]) + " " + t["uncertainty"]
        speak_button(speech, t["listen"], lang)

        st.divider()
        st.subheader(t["quiz_title"])
        questions = QUIZ[lang]
        answers = []
        for i, q in enumerate(questions):
            answers.append(st.radio(q["q"], q["options"], index=None, key=f"quiz_{lang}_{i}"))
        if st.button(t["quiz_check"]):
            if any(a is None for a in answers):
                st.warning(t["quiz_answer_all"])
            else:
                score = sum(1 for a, q in zip(answers, questions) if q["options"].index(a) == q["answer"])
                st.session_state.quiz_score = score
                log("quiz", f"{score}/3")
                st.success(t["quiz_result"].format(score=score))

# 4. Partage
with tab_share:
    st.header(t["share_title"])
    st.write(t["share_intro"])
    with st.form("share_form", clear_on_submit=True):
        name = st.text_input(t["share_name"], help=t["share_name_help"])
        role = st.selectbox(t["share_role"], list(t["roles"]), format_func=lambda k: t["roles"][k])
        scope = st.multiselect(t["share_scope"], list(t["scopes"]), format_func=lambda k: t["scopes"][k])
        consent = st.checkbox(t["share_consent"])
        submitted = st.form_submit_button(t["share_add"])
    if submitted:
        if not (name.strip() and scope and consent):
            st.error(t["share_missing"])
        else:
            scope_txt = ", ".join(t["scopes"][s] for s in scope)
            st.session_state.shares.append(
                {"who": name.strip(), "role": role, "scope": scope_txt, "active": True})
            st.session_state.audit.append(
                {"ts": now(), "action": "granted", "who": name.strip(), "role": role, "scope": scope_txt})
            log("share_granted", role)
            st.rerun()

    st.subheader(t["share_active"])
    active = [(i, s) for i, s in enumerate(st.session_state.shares) if s["active"]]
    if not active:
        st.caption(t["share_none"])
    for i, s in active:
        c1, c2 = st.columns([3, 2])
        c1.markdown(f"**{s['who']}** ({t['roles'][s['role']]})  \n{s['scope']}")
        if c2.button(t["share_revoke"], key=f"revoke_{i}"):
            s["active"] = False
            st.session_state.audit.append(
                {"ts": now(), "action": "revoked", "who": s["who"], "role": s["role"], "scope": s["scope"]})
            log("share_revoked", s["role"])
            st.rerun()

    if st.session_state.audit:
        st.subheader(t["audit_title"])
        cols = t["audit_cols"]
        rows = [
            {cols["ts"]: a["ts"], cols["action"]: t["audit_actions"][a["action"]], cols["who"]: a["who"],
             cols["role"]: t["roles"][a["role"]], cols["scope"]: a["scope"]}
            for a in st.session_state.audit
        ]
        st.dataframe(rows, use_container_width=True, hide_index=True)

# 5. Suite
with tab_next:
    st.header(t["next_title"])
    if not both_known:
        st.info(t["counsel_wait"])
        counselling = False
    else:
        counselling = needs_counselling(g1, g2)
        (st.warning if counselling else st.success)(t["counsel_yes"] if counselling else t["counsel_no"])

    for i, label in enumerate(t["steps"]):
        if i == 0:
            st.checkbox(label, value=both_known, disabled=True, key="step_view_0")
        elif i == 2:
            st.checkbox(label, value=counselling, disabled=True, key="step_view_2")
        else:
            st.checkbox(label, key=f"step_{i}", on_change=on_step, args=(i,))
            ts = st.session_state.steps.get(i)
            if ts:
                st.caption(t["step_done_on"].format(ts=ts))

    st.divider()
    st.subheader(t["indicators_title"])
    steps_done = sum(1 for v in st.session_state.steps.values() if v) + int(both_known) + int(counselling)
    shares_active = sum(1 for s in st.session_state.shares if s["active"])
    quiz = st.session_state.quiz_score
    m1, m2, m3 = st.columns(3)
    m1.metric(t["ind_quiz"], f"{quiz}/3" if quiz is not None else "-")
    m2.metric(t["ind_steps"], f"{steps_done}/{len(t['steps'])}")
    m3.metric(t["ind_shares"], shares_active)
    st.download_button(t["ind_export"], events_csv(), file_name="indicateurs_anonymes.csv", mime="text/csv")
    st.caption(t["ind_note"])
