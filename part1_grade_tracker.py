# ============================================
# BITSOM Assignment 3  Part-1
# Grade Tracker
# ============================================

print("\n" + "=" * 60)
print("TASK 1 - DATA PARSING & PROFILE CLEANING")
print("=" * 60)

# data raw
intake = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

roster = []

for rec in intake:
    nm  = rec["name"].strip().title()
    rno = int(rec["roll"])

    score_list = []
    for val in rec["marks_str"].split(", "):
        score_list.append(int(val))

    # name check - rejecting anything with digits or symbols
    valid = True
    for chunk in nm.split():
        if not chunk.isalpha():
            valid = False
            break

    print(f"{nm} -> {'✓ Valid' if valid else '✗ Invalid - check for special characters'}")

    roster.append({"name": nm, "roll": rno, "marks": score_list})

    print("=" * 32)
    print(f"Student : {nm}")
    print(f"Roll No : {rno}")
    print(f"Marks   : {score_list}")
    print("=" * 32)

# upper/lower output for roll 103
for rec in roster:
    if rec["roll"] == 103:
        print(f"\nRoll 103 - {rec['name']}")
        print("  Upper :", rec["name"].upper())
        print("  Lower :", rec["name"].lower())


print("\n" + "=" * 60)
print("TASK 2 - MARKS ANALYSIS USING LOOPS & CONDITIONALS")
print("=" * 60)

sname   = "Ayesha Sharma"
subs    = ["Math", "Physics", "CS", "English", "Chemistry"]
scores  = [88, 72, 95, 60, 78]

print(f"\nAnalysing: {sname}")
print("\nSubject Breakdown:")

for i in range(len(subs)):
    sc = scores[i]

    # grading scale from the assignment brief
    if sc >= 90:   g = "A+"
    elif sc >= 80: g = "A"
    elif sc >= 70: g = "B"
    elif sc >= 60: g = "C"
    else:          g = "F"

    print(f"  {subs[i]:12} {sc:>3}   {g}")

ttl = sum(scores)
avg = ttl / len(scores)
print(f"\n  Total   : {ttl}")
print(f"  Average : {avg:.2f}")

hi = max(scores); hi_sub = subs[scores.index(hi)]
lo = min(scores); lo_sub = subs[scores.index(lo)]

print(f"  Best    : {hi_sub} ({hi})")
print(f"  Weakest : {lo_sub} ({lo})")

# add extra subjects - useful if electives were added later
n_added = 0
print("\nAdd extra subjects below. Enter 'done' to exit.\n")

while True:
    inp = input("Subject: ").strip()
    if inp.lower() == "done":
        break

    raw = input(f"Marks for {inp} (0-100): ").strip()
    try:
        sc = int(raw)
        if 0 <= sc <= 100:
            subs.append(inp)
            scores.append(sc)
            n_added += 1
            print(f"  Added {inp}.\n")
        else:
            print("  Out of range - must be 0 to 100.\n")
    except ValueError:
        print("  Could not parse that. Enter a number.\n")

print(f"\n  {n_added} subject(s) added")
print(f"  Revised Average : {sum(scores)/len(scores):.2f}")


print("\n" + "=" * 60)
print("TASK 3 - CLASS PERFORMANCE SUMMARY")
print("=" * 60)

# students from task 1 - averages computed
batch = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",    [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85]),
]

clears   = 0
drops    = 0
sum_avgs = 0
top_nm   = ""
top_avg  = 0

print(f"\n  {'Name':<18}  {'Avg':>6}   Result")
print("  " + "-" * 34)

for nm, mks in batch:
    a = round(sum(mks) / len(mks), 2)

    # 60 is the pass cutoff per grading policy
    if a >= 60:
        result = "Pass"
        clears += 1
    else:
        result = "Fail"
        drops += 1

    print(f"  {nm:<18}  {a:>6.2f}   {result}")
    sum_avgs += a

    if a > top_avg:
        top_avg = a
        top_nm  = nm

c_avg = sum_avgs / len(batch)

print(f"\n  Passed        : {clears}")
print(f"  Failed        : {drops}")
print(f"  Topper        : {top_nm} ({top_avg:.2f})")
print(f"  Class Average : {c_avg:.2f}")


print("\n" + "=" * 60)
print("TASK 4 - STRING MANIPULATION UTILITY")
print("=" * 60)

raw_text = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

t1 = raw_text.strip()
print("\n1. After strip():")
print(t1)

t2 = t1.title()
print("\n2. Title case:")
print(t2)

# counting before replacement so the number reflects original text
cnt = t1.count("python")
print(f"\n3. 'python' appears {cnt} time(s)")

t3 = t1.replace("python", "Python 🐍")
print("\n4. With replacements:")
print(t3)

# splitting by ". " to get individual sentences
parts = t1.split(". ")
print("\n5. Split into sentences:")
print(parts)

print("\n6. Numbered output:")
for idx in range(len(parts)):
    line = parts[idx]
    if not line.endswith("."):
        line += "."
    print(f"  {idx+1}. {line}")