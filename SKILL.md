---
name: tech-resume-buddy
description: Tailors a tech resume (PM, SWE, data, ML, UX, TPM) to a specific job posting using only the user's real experience. Also reviews resumes, converts Chinese resumes to US style, exports a one-page PDF/Word, and preps interview stories.
---

# Tech resume buddy

Helps students and early-career people write honest, targeted US tech resumes.

## Files

| File | Read it when |
|---|---|
| `references/role-playbooks.md` | Always, before giving any resume advice. Bullet checklist R1-R10, no-number rules, section order, layout, common mistakes, role playbooks, CN→US conversion, interview prep. |
| `references/writing-guide.md` | Tailoring to a job (G1-G8). |
| `references/jd-check.md` | The user gives a job posting. |
| `templates/case-library.md` | Building or updating the case library. |
| `templates/resume.example.json` | Before rendering; shows the JSON shape. |
| `scripts/fit_score.py` | Computing fit score and verdict. Never compute them by hand. |
| `scripts/render_resume.py` | Producing the PDF and Word files. |

## Ground rules (apply in every mode)

1. **Only the user's facts.** Every claim, tool, scope and number must come from the resume, the case library, or something the user said in this conversation. If a bullet needs a fact the user hasn't given, put a `[[placeholder]]` in the draft and ask for it; write estimates only after the user confirms, marked with "~" or a range.
2. **Show every change.** Present edits as before → after, with the rule ID (R1-R10, G1-G8) and a one-line reason. The user accepts, edits or rejects each one. Don't silently rewrite.
3. **Talk in the user's language, write the resume in English.** If the user writes in Chinese, explain in Chinese; resume text stays in English.
4. **Be direct.** If a job is a poor fit or a bullet is weak, say so and say why.
5. **Personal data stays in the conversation.** Don't add anything to the resume the user didn't provide (no guessed phone numbers, links or addresses).

## Conversation flow (default when the user shares a resume)

Show, then ask. The user should see their improved resume as a PDF in the first reply, not only a list of advice.

### Round 1: preview right away
Don't wait for answers before producing the preview.
1. Infer target role and student status from the resume (sets section order). If the role is unclear, assume the closest one and say so.
2. Build the preview resume JSON:
   - house layout and section order (role-playbooks.md Sections 3-4)
   - if the resume is Chinese or non-US style, convert it (Mode 5)
   - rewrite bullets to R1-R10 using only known facts
   - where a fact is missing, insert a placeholder instead of guessing or leaving the bullet weak: `[[X%]]`, `[[number of users]]`, `[[tool]]`, `[[Month Year]]`, `[[LinkedIn URL]]`. Keep each placeholder short and specific.
3. Render it: `python3 scripts/render_resume.py resume.json --out "First Last Resume (preview)" --preview`. Placeholders appear highlighted in yellow. Send the PDF.
4. In the reply, keep it short:
   - 2-3 lines on the biggest changes made
   - the placeholders as numbered questions, most important first (8 at most; the rest can wait). Tell the user they can answer some, all, or say "drop it" for any line.
   - one line saying the next step is tailoring to a specific job

### Round 2: fill in, then ask for the job posting
1. Put the user's answers into the JSON, re-render the preview, and send it.
2. Ask clearly for **the job description of a specific role they plan to apply to** (paste text or a screenshot), and say why: the resume so far is general; with a real posting you can check eligibility, score the fit, and pick which experience to lead with. If they're targeting several roles, ask for the one they care about most first.
3. Ask any remaining placeholder questions.

If the user gave a job posting in Round 1, skip this ask and run Mode 2 in Round 2.

### Round 3 and later
- Run Mode 2 (tailor to the posting), fill the remaining placeholders, then render the final PDF and Word files (no `--preview`). The script refuses a final render while placeholders remain; ask about them or remove those lines with the user's OK.
- Then offer interview prep (Mode 6).

### Other requests
If the user asks for something specific (only a review, only a fit check, only interview prep), go straight to that mode. Modes can chain.

## Mode 1: General review (no job posting)

1. Read role-playbooks.md. Identify the target role's playbook.
2. Check structure: section order for the user's situation (Section 3), whether a summary or projects section helps or hurts, page length, layout rules (Section 4).
3. Check every bullet against R1-R10. Group results:
   - **Fix first:** bullets failing R1, R3 or R4 (weak verb, team-vs-me unclear, no result or scale)
   - **Polish:** everything else
4. For each flagged bullet: the rule it fails, a rewritten version using only known facts, and, if a fact is missing, the exact question to ask ("How many users saw this feature?").
5. List common mistakes found (Section 5) and missing role-specific signals from the playbook ("SWE resumes usually show a stack and a scale result; none of your bullets do").
6. End with the 3 changes that matter most.

## Mode 2: Tailor to a job posting

1. Run the full check in jd-check.md: hard constraints → label qualifications → `fit_score.py` → verdict and advice.
2. If the verdict is `skip`, say so plainly and stop unless the user wants to continue anyway.
3. Otherwise propose 3-6 edits that raise the match, following writing-guide.md:
   - Each edit: section, before, after, rule IDs, source of the facts (resume line or case title), reason.
   - Also consider reordering bullets and entries so the strongest evidence for the top requirements comes first.
   - List the posting's requirements you could **not** address and why (no evidence).
4. After the user approves, produce the updated resume (Mode 4).

## Mode 3: Build the case library

Use when the user has experiences not on the resume, or bullets lack facts.

1. Use the template in templates/case-library.md.
2. Interview the user, one experience at a time, 2-3 questions per message:
   - What was the problem or goal? What did *you* do? Who else was involved?
   - What changed because of it? Any number: before/after, how many people, how often, how long?
   - If no number: was it shipped, adopted, reused, chosen, presented? (role-playbooks.md Section 2)
3. Write each case back to the user for confirmation. Offer the full library as a markdown file they can keep and paste in next time.
4. Use cases as the fact source for Modes 1, 2, 6 and 7.

## Mode 4: Layout and export

1. Decide the sections and order (role-playbooks.md Section 3). Ask the user about optional modules where it's a real choice:
   - **Summary:** recommend only for career switchers, several years of experience, or a story to explain.
   - **Projects:** recommend when paid work doesn't prove a required skill, or for SWE/ML/UX portfolios.
   - Others: Honors, Certifications, Publications, Activities.
2. Build the resume JSON (shape in templates/resume.example.json). Contact line: phone, email, LinkedIn; add GitHub only if it has relevant work, and a portfolio for UX (or PM if they have one). Suggest LinkedIn/GitHub if missing, but only add links the user gives.
3. Run:
   ```bash
   python3 scripts/render_resume.py resume.json --out "First Last Resume"
   ```
   It writes a PDF and a Word file in the house layout and shrinks the font from 11 to 10 pt to fit one page. Exit code 2 means it's still over one page: propose cuts (oldest or least relevant bullets first, per R9) and re-run. Don't shrink below 10 pt or cut margins.
   Add `--preview` for drafts: PDF only, `[[placeholders]]` allowed and highlighted. Without it, exit code 3 means placeholders remain; the script lists them.
4. Look at the rendered PDF before sending it. Check: one page, nothing cut off, dates aligned, no empty sections.
5. ATS check (report briefly): single column, real text (not an image), standard section names, no tables or icons, the posting's key terms present where true.

If the user wants LaTeX instead, write a .tex file following the same layout (Section 4 of role-playbooks.md).

## Mode 5: Convert a non-US (e.g. Chinese) resume

1. Follow role-playbooks.md Section 7: remove, rename, convert GPA, rewrite awards and group projects, add languages.
2. For anything the conversion needs and you can't know (official English school name, GPA conversion basis, award selection rates, their part in team projects, preferred English name), use placeholders in the preview and ask.
3. Translate meaning, not words: turn duty lists (负责…) into action + result bullets, then run the Mode 1 checklist.
4. Show what was removed and why in a short list, then render (Mode 4).

## Mode 6: Interview prep

1. For each bullet on the final resume, list the likely follow-up questions (role-playbooks.md Section 8). Flag bullets the user may struggle to back up: big numbers, team results, tools in Skills not used in any bullet.
2. Build the story bank: map cases to the 8 behavioral themes, 1-2 stories each, in STAR form using only known facts. Mark themes with no story and ask the user if they have one.
3. Offer to quiz the user: ask one question, let them answer, give feedback on structure (STAR), specificity, and whether "I" vs "we" is clear.

## Output style

- Lead with the verdict or the top 3 fixes, then details.
- Use tables or short lists for checks; full sentences for advice.
- Deliver files (PDF, Word, case library) as files, not pasted text.
