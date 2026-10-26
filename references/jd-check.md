# Checking a resume against a job posting

Be strict and factual. Use only the resume, the case library and what the user told you.

## Step 1: Hard constraints

Check each one. For each, record what the posting asks, what the user has, and a status: `pass`, `fail`, `unknown`, or `skipped` (user didn't say).

| Constraint | How to judge |
|---|---|
| Degree level / enrollment | Compare levels: undergraduate < Master's < PhD. `pass` if the user's level meets or exceeds the posting's. `fail` only if the posting requires a higher level (e.g. PhD only). Many internships require being enrolled during or after the internship; check that too. |
| Graduation timing | Posting often states a graduation window (e.g. "graduating Dec 2027 - Jun 2028"). Compare with the user's expected date. |
| Availability | Internship dates and length vs when the user can start and must return to school. |
| Location | Office location and in-office days vs the user's preference. Mark `unknown` if the user hasn't said. |
| Work authorization | If the user is on an F-1 or J-1 student visa, call this "Work authorization (CPT)". CPT is authorized by the school and doesn't need employer sponsorship. `pass` if it's an internship and the posting doesn't exclude students who need CPT. `unknown` if the posting says it won't sponsor or requires authorization "without restriction"; tell the user to confirm CPT with the recruiter. `fail` only if the posting requires U.S. citizenship or permanent residency (e.g. security clearance). |

Don't ask about visa status unless the user brings it up or the posting has an authorization requirement; then ask once.

## Step 2: Label each qualification

- List the posting's qualifications other than the hard constraints, one requirement per item, up to 8, in the posting's order.
- Mark each `required` (minimum / basic) or preferred.
- Label the match:
  - `strong`: the resume or a case clearly shows it
  - `partial`: related but not the same experience
  - `none`: not shown
- Name the evidence ("Resume: Product Analyst, Brightline" or a case title).
- Past job titles and dates count as evidence (a past PM role counts as hands-on PM experience; years count toward experience requirements).
- Judge product type as its own item when the posting stresses it (consumer vs business-facing, social, AI, hardware).

## Step 3: Score and verdict

Write the labels to a JSON file and run `scripts/fit_score.py`. Report its score and verdict as-is; don't adjust them by hand.

- `skip`: a hard constraint fails
- `stretch`: 2 or more required items are `none`
- `worth_applying`: otherwise

## Step 4: Advice

Give 2-3 specific, honest suggestions based on the partial and missing items:
- Say plainly where experience is limited.
- Point to true, related experience that could be shown better (then tailor with writing-guide.md).
- Suggest what to add if there's time (a project, a course, a line in the cover letter).
- Never suggest claiming experience the user doesn't have.

## Output format

```
Verdict: Worth applying — fit 78/100
<one-sentence summary>

Hard constraints
✓ Degree level — posting: BS/MS; you: MS in progress
? Work authorization (CPT) — posting says "no sponsorship"; confirm CPT with the recruiter

Qualifications
● Strong   [required] SQL — Resume: Data Analyst, Acme
◐ Partial  [required] Consumer product experience — your PM work was for business users
○ Missing  [preferred] iOS experience

Suggestions
1. ...
```
