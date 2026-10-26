# Tech resume playbooks (distilled)

Distilled from public university career-center guides, plus a set of real internship job postings for the TPM section (sources at the end; each rule cites its source by tag, e.g. [CMU]).
These are patterns, not copied text. All example bullets are fictional and written for this skill.
Rules marked [house] are this skill's own choices, not taken from a source.

---

## 1. Bullet checklist (use the IDs in feedback, e.g. "bullet 3 fails R4")

| ID | Rule | Source |
|---|---|---|
| R1 | Starts with a strong, specific action verb. No "I", "we", "responsible for", "helped with", "worked on". | [CMU] [Yale] |
| R2 | Past tense for finished work, present tense only for a current role. One tense per entry. | [CMU] |
| R3 | Shows **your** part, not the team's. If it was a team project, say what you owned. | [Yale] |
| R4 | Has a result or a concrete scale (see Section 2 when there is no metric). | [CMU] [Yale] [MIT] |
| R5 | Gives context for the result: a baseline ("from X to Y"), a comparison, or the size of the base. | [Yale] |
| R6 | Names the tool or method when it is a skill the job asks for. | [MIT] [Duke] |
| R7 | One line, two at most. | [CMU] |
| R8 | Punctuation is consistent: no period at the end of bullets, same date format everywhere. | [CMU] |
| R9 | Recent and relevant entries get more bullets; old or unrelated ones get fewer. | [CMU] |
| R10 | Soft skills appear through what happened ("aligned 3 teams on…"), never as a bare claim. | [CMU] [MIT] |

**Bullet shapes** (pick whichever reads most naturally):
- Action + project + result [Yale] (also: action verb + context + result [CMU])
- "Accomplished X, as measured by Y, by doing Z" [Yale]

---

## 2. When there is no number

Many student bullets have no metric. Use these, in order:

1. **Range** when the exact figure is unknown: "mentored 7-12 new members each semester" [UMKC]
2. **Frequency** to show volume: "reviewed 40-50 support tickets per week" [UMKC]
3. **People served or reached**: team size, audience size, number of users or participants [UMKC] [Yale]
4. **Selection rate** for awards and programs: "one of 230 participants selected nationally" [Yale]
5. **Qualitative result** when nothing is countable: shipped, adopted by another team, replaced the old process, cited in a paper, chosen for the final product [Yale] [MIT]

**Never invent a number.** If a range or estimate would help, ask the user for it and write it only after they confirm. Mark estimates with "~" or a range. [house]

---

## 3. Section order [house, confirmed by user]

| Situation | Order |
|---|---|
| **Current student** (any level) | Education → Experience → Projects (optional) → Skills |
| **Current student, little relevant work** | Education → Projects → Experience → Skills |
| **Graduated / not in school, with work experience** | Experience → Education → Skills (Projects only if they show a skill the job needs) |
| **Career switcher, not in school** | Summary → Projects in the new field → Experience → Education → Skills |

Graduate students put Education first [CMU]. Students who worked full-time for years before returning to school still lead with Education by default, because internship recruiters check degree and graduation date first. [house]

**Summary:** include it only if it adds focus: a career switch, several years of experience, or a story that needs explaining (e.g., returning to school after working). 2-3 lines, one target role, no generic claims. Skip it for most students. [CMU]

**Projects:** include when paid experience doesn't prove a required skill, or the role values a portfolio (SWE, ML, UX). Format a project like a job: name, context, date, 2-4 bullets, link. [CMU] [MIT]

**Optional sections:** Activities (with dates), Honors (recent, strong, no high school), Publications (own section if several, otherwise under the related role). [CMU]
Also: Certifications (name, issuer, date) and course projects done with a real company, formatted like Projects. [house]

---

## 4. Layout and format

### Rules from sources
- One page for students and anyone under ~10 years of experience. [CMU] [MIT] [CSU]
- One body font, 10-12 pt; only the name is larger. Margins at least 0.5 in, consistent. [CMU]
- Organization and title on the left; dates and location on the right. Location as "City, ST" (US) or "City, Country". Remote roles: "Remote". [CMU]
- Contact line: name, phone, professional email, LinkedIn. Optional: GitHub, portfolio, personal site. [CMU] [UMD]
- Education: school in full, location, degree and major as on the transcript, graduation (or expected) month and year. Optional: GPA with scale, relevant courses (never future courses), thesis. [CMU]
- Skills: hard skills only, grouped by type, strongest first. No soft skills. [CMU]
- ATS: single column, no tables, text boxes, icons, skill bars or photos; submit a text-based PDF named with your name. [Western] [CSU] [MIT]

### House template [house, chosen by user]
The skill outputs one layout: the plain one-column style most common on US tech resumes (often built from the "Jake's Resume" LaTeX template). This skill uses its own implementation of that layout.

```
                    FIRST LAST                         ← centered, bold, ~22 pt
  555-123-4567 | email@example.com | linkedin.com/in/x | github.com/x   ← centered, linked
EDUCATION ─────────────────────────────────────────────  ← heading + full-width rule
**School Name**                                   City, ST
*Degree in Major*                       Expected May 2027
  • Relevant Coursework: …
EXPERIENCE ────────────────────────────────────────────
**Company**                                       City, ST
*Job Title*                           Jun 2026 – Aug 2026
  • Bullet without a final period
```

- Font: serif. LaTeX: Computer Modern (default). Word: a standard serif such as Times New Roman or Georgia. Body 10.5-11 pt.
- Margins 0.5-0.6 in. Round bullets. Dates written as "Jun 2026 – Aug 2026" everywhere.
- No bold inside bullets by default (it competes with the company names); allow it only if the user asks.
- Show links without "https://". Add GitHub only if it has real, relevant content. Add a portfolio link for UX, and for PM if one exists.

---

## 5. Common mistakes (all roles)

| Mistake | Fix |
|---|---|
| Duty list ("Responsible for weekly reports") | Rewrite as action + result (R1, R4) |
| Tool dump: a bullet that is just a list of technologies | Say what was built with them and why it mattered (R6) |
| Team result written as personal ("Increased revenue 20%") | Name your part (R3) |
| Buzzwords with no evidence ("passionate", "results-driven", "synergy") | Delete, or replace with an example (R10) |
| Vague verbs ("assisted", "participated", "involved in") | Use the verb for what you actually did (R1) |
| Number with no baseline ("improved by 40%") | Add from-to or base size (R5) |
| Listing skills that can't be defended in an interview | Remove them |

---

## 6. Role playbooks

Each role has two fictional examples: one for a student or intern, one for someone with full-time experience. Use the one closer to the user.

### Product manager / APM
- **Show:** a product decision you drove, the user insight behind it, cross-functional work (eng, design, data), prioritization, and the result. [MIT] [Yale]
- **Metrics:** adoption, activation, retention, conversion, satisfaction; or scope (users, teams, markets).
- **Without PM titles:** class projects, hackathons, clubs and research that show user research → decision → result.
- **Example, student (fictional):**
  - Weak: Worked on a campus app project with a team.
  - Strong: Led user interviews with 25 students and cut the app's sign-up flow from 5 steps to 2, raising completed sign-ups from 40% to 65% in a semester pilot
- **Example, experienced (fictional):**
  - Weak: Worked with engineers on the onboarding flow.
  - Strong: Led a 3-step onboarding redesign with design and engineering, raising day-7 activation from 22% to 29% across 40K new users

### Software engineer
- **Show:** what you built, the stack, ownership, and a scale or performance result. [CMU] [MIT]
- **Metrics:** latency, throughput, cost, build or test time, bugs reduced, users or requests served.
- **Projects:** essential when experience is thin; link the repo.
- **Example, student (fictional):**
  - Weak: Used React, Node.js, and MongoDB for a web app.
  - Strong: Built a course-planning web app in React and Node.js used by 300+ students, and added server-side caching that cut page load from 3.1 s to 0.9 s
- **Example, experienced (fictional):**
  - Weak: Worked on backend APIs.
  - Strong: Built a caching layer for the search API in Go and Redis, cutting p95 latency from 480 ms to 120 ms at 2K requests per second

### Data analyst / data scientist
- **Show:** the question, the method or tool, and the decision it informed. [Duke] [OSU]
- **Metrics:** time saved, accuracy, size of the dataset, decision or budget influenced.
- **Skills to name if true:** SQL, Python/R, Excel, Tableau/Power BI/Looker, A/B testing, regression.
- **Example, student (fictional):**
  - Weak: Analyzed data for a student organization.
  - Strong: Analyzed 3 years of event sign-up data in Python and found that weekday-evening events drew twice the turnout, which the board used to plan the next semester's schedule
- **Example, experienced (fictional):**
  - Weak: Made dashboards for the sales team.
  - Strong: Built a Looker pipeline-health dashboard in SQL that replaced 6 weekly spreadsheets and cut reporting time by 5 hours per week

### Machine learning / AI engineer
- **Show:** the problem, the model or system, the offline metric, and what happened when it was used (deployed, adopted, published). [Buffalo]
- **Be explicit** about offline vs real-world results; don't present an offline gain as a business result.
- **Example, student (fictional):**
  - Weak: Trained a deep learning model for image classification.
  - Strong: Fine-tuned a vision model to flag damaged parcels in warehouse photos (F1 0.72 → 0.86 on a 5K-image test set) as part of a 3-person capstone with a logistics partner
- **Example, experienced (fictional):**
  - Weak: Trained a model to classify support tickets.
  - Strong: Fine-tuned a text classifier to route support tickets (F1 0.71 → 0.84) and deployed it to production, cutting median first-response time by 30%

### UX researcher / UX designer
- **Show:** the research method, what it found, the design decision it changed, and the outcome. Portfolio link in the header; the resume points to case studies, the portfolio shows them. [Pitt] [Binghamton]
- **Metrics:** task success, time on task, participants, issues found, conversion.
- **Example, student (fictional):**
  - Weak: Did user research and made wireframes for a library app.
  - Strong: Ran 10 usability tests on the library app's room-booking flow, found 3 points where users gave up, and redesigned the flow in Figma, raising task success from 60% to 90% in retesting
- **Example, experienced (fictional):**
  - Weak: Conducted user research for the mobile app.
  - Strong: Ran 14 usability sessions on the checkout flow, found 3 blocking issues, and redesigned the payment step, raising task success from 68% to 91%

### Technical program manager (distilled from 6 internship postings)
What postings repeatedly ask for [JD]:
- Delivering a project end to end against a plan (timelines, milestones, critical path)
- Finding risks and blockers early and resolving trade-offs (scope, schedule, cost)
- Coordinating several teams and keeping them aligned with regular updates
- Technical fluency: enough to discuss design and dependencies with engineers; some postings require coding in one language or an engineering/CS degree
- Using data to report status and support decisions
- Proposing process improvements

- **Show:** a project you ran end to end, how many teams or people, the risk or blocker you caught, and the delivery result. Add one line of technical depth.
- **Metrics:** on-time delivery, number of teams or workstreams, dependencies tracked, cycle time, issues reduced.
- **Example, student (fictional):**
  - Weak: Managed the timeline for a senior design project.
  - Strong: Ran the schedule for a 12-person, 3-subteam robotics capstone, tracked 20+ hardware and software dependencies, and moved integration testing two weeks earlier after catching a parts delay, delivering on time
- **Example, experienced (fictional):**
  - Weak: Managed the data migration project.
  - Strong: Ran a 5-team migration of billing data to a new warehouse, mapped 30+ dependencies and cut-over risks, and delivered two weeks early with zero data loss

---

## 7. Converting a non-US (e.g. Chinese) resume to US style

**Remove** [UMD] [UConn] [CSU] [Pomona]
- Photo, age/birth date, gender, marital status, ethnicity, religion, hometown/hukou, political status, height/weight
- Immigration or visa status, home-country permanent address
- Test scores (TOEFL, IELTS, SAT, GRE); "English" as a language skill
- References (give them separately on request); self-evaluation paragraphs (自我评价)

**Name** [UMD]
- Legal name; an English name goes in parentheses: "Wei (David) Zhang". Keep it the same on LinkedIn.
- Optional: if the name is hard for US readers to pronounce, add a simple phonetic line under it, e.g. "(way-jahng)". [UMD]

**Schools and titles** [house]
- Schools: use the official English name.
- Titles: keep the real title; let bullets show scope. If the title has no US equivalent, use the closest plain description and confirm with the user.
- Don't add descriptors to company or school names (user's choice).

**GPA** [UMD] [UConn]
- Convert to the 4.0 scale and show the original: "GPA 88/100 (3.7/4.0 equivalent)". Use the school's official conversion or a credential evaluator's, and ask the user which one; if neither exists, keep the original scale only. [house for the last part]

**Awards** [Yale]
- Translate the name, then show how selective it was: "National Scholarship (awarded to top 2% of undergraduates nationally)" or "Valedictorian, class of 3,000". Ask the user for the rate or class size; don't guess.
- Drop high-school awards. [CMU]

**Group projects (项目经历)** [Yale]
- Chinese resumes often describe the whole team's project. Rewrite each bullet around what the user did (R3); move team context into one short clause.

**Many short internships** [CMU] [house]
- Keep the ones most relevant to the target role with full bullets; reduce older or unrelated ones to one line, or drop them if the page is full.

**Add** [UConn] [UMD]
- Languages with level ("Mandarin: native"), cross-market or cross-cultural work, and US experience (work, volunteering, student organizations) if any.

**Then apply the house template (Section 4).**

---

## 8. Interview prep from a resume

**Questions per bullet** (the interviewer may ask):
- What exactly was your part vs the team's?
- How did you measure the number? Baseline, time frame, source?
- Why this approach, and what else did you consider?
- What went wrong, or what would you do differently?
- For skills listed: "Walk me through how you used X."

Flag any bullet the user can't answer in about 30 seconds; it's a risk to keep as written.

**Story bank** [house]
Map the user's case library to common behavioral themes, one or two stories each:

| Theme | Typical question |
|---|---|
| Impact / proudest work | Tell me about a project you're most proud of |
| Conflict | Tell me about a disagreement with a teammate or stakeholder |
| Failure / mistake | Tell me about a time something didn't go as planned |
| Influence without authority | How did you convince people who didn't report to you? |
| Ambiguity | Tell me about a time the goal or data was unclear |
| Prioritization / trade-off | How did you decide what not to do? |
| Learning fast | Tell me about something you had to learn quickly |
| Customer / user focus | Tell me about a time you changed a plan because of users |

For each story, outline Situation, Task, Action, Result, using only facts from the resume or case library. Mark themes with no story so the user can add one.

---

## Sources

University career centers
- [CMU] Carnegie Mellon Career & Professional Development, SCS Resume Guide — https://www.cmu.edu/career/documents/resources-by-college/scs-resume-guide-2020.pdf
- [MIT] MIT CAPD, Crafting an effective resume — https://capd.mit.edu/resources/career-toolkit-crafting-an-effective-resume/
- [Yale] Yale Office of Career Strategy, Writing Impactful Resume Bullets — https://ocs.yale.edu/resources/writing-impactful-resume-bullets/
- [UMKC] UMKC Bloch School Career Services, How to Quantify Your Resume Bullets (When You Don't Work With Numbers) — https://careers.bloch.umkc.edu/blog/2021/11/17/how-to-quantify-your-resume-bullets-when-you-dont-work-with-numbers/
- [Duke] Duke Career Hub, Data Analyst Resume Guide and Templates — https://careerhub.students.duke.edu/blog/2025/04/14/data-analyst-resume-guide-and-templates/
- [Buffalo] University at Buffalo Career Design Studio, ML Engineer Resume Guide — https://careerdesignstudio.buffalo.edu/blog/2025/10/28/ml-engineer-resume-guide-and-templates/
- [OSU] Ohio State Data Analytics, sample resume — https://data-analytics.osu.edu/sites/default/files/2021-11/data_analytics_resume_sample.pdf
- [Western] Western Engineering Careers, Resume Formatting Guidelines — https://www.eng.uwo.ca/careers/resources/Resume Formatting Guidelines.pdf
- [Pitt] University of Pittsburgh Career Central, How to Build a UX Design Portfolio — https://careercentral.pitt.edu/blog/2023/02/08/how-to-build-a-ux-design-portfolio/
- [Binghamton] Binghamton Fleishman Center, UX Design Career Guide for Students — https://careertools.binghamton.edu/resources/ux-design-career-guide-for-students/
- [UMD] University of Maryland Feller Center, International Students: Resumes - US Style — https://fellercenter.umd.edu/career-planning/international-students-resume (page and its sample resume PDF)
- [UConn] UConn Center for Career Readiness, Writing a Compelling U.S.-Style Resume — https://career.uconn.edu/blog/2025/10/14/writing-a-compelling-u-s-style-resume/
- [CSU] Colorado State Career Center, International Students Resume & CV Trends — https://career.colostate.edu/wp-content/uploads/2022/08/International-Students-Resume-CV-Trends.pdf
- [Pomona] Pomona College CDO, U.S. Résumé Tips for International Students — https://cdo.pomona.edu/resources/u-s-resume-tips-for-international-students/

TPM internship postings [JD]
- Intuit, Summer 2027 TPM Intern — https://jobs.anitab.org/companies/intuit/jobs/95499198-ghc-2026-summer-2027-technical-program-manager-intern
- Google, TPM Summer Intern BS/MS — https://prosple.com/graduate-employers/google/jobs-internships/technical-program-manager-summer-intern-bsms
- Amazon, TPM Summer Internship — https://amazon.jobs/en/jobs/2737011/technical-program-manager-summer-internship-2025-us
- Microsoft, Technical Program Management Internship — https://jobs.anitab.org/companies/microsoft/jobs/63964576-technical-program-management-internship-opportunities
- Zipline, TPM Intern — https://jobs.techstars.com/companies/zipline/jobs/63567809-technical-program-manager-intern-summer-2026
- Tesla, TPM Intern — https://simplify.jobs/p/d6f2e134-6d3d-4e88-93bd-4c8794fc745e/Technical-Program-Manager-Intern
