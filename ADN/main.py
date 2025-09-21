import matplotlib.pyplot as plt


def count_pairs(dna: str):
    # Counters
    cg_count = 0
    at_count = 0
    total_pairs = 0

    i = 0
    while i < len(dna) - 1:
        c1, c2 = dna[i], dna[i + 1]
        pair = c1 + c2

        # If either character is invalid, skip one step
        if c1 not in "ATGC" or c2 not in "ATGC":
            i += 1

        # Check for CG or GC
        elif pair in ("CG", "GC"):
            cg_count += 1
            total_pairs += 1
            i += 2

        # Check for AT or TA
        elif pair in ("AT", "TA"):
            at_count += 1
            total_pairs += 1
            i += 2

        # We never know
        else:
            i += 1

    return cg_count, at_count


# Example usage
with open("ADN/DNAFile.txt", "r") as f:
    inputs = [line.strip() for line in f if line.strip()]

results = []
for dna in inputs:
    cg_count, at_count = count_pairs(dna)
    total = cg_count + at_count

    # Avoid dividing by 0
    if total == 0:
        cg_percent = at_percent = 0
    else:
        cg_percent = cg_count / total * 100
        at_percent = at_count / total * 100

    results.append((cg_count, at_count))

    # Print final results
    print(f"DNA: {dna}")
    print(f"  CG/GC count: {cg_count}, AT/TA count: {at_count}, total pairs: {total}")
    print(f"  CG/GC %: {cg_percent:.2f}%, AT/TA %: {at_percent:.2f}%\n")


# --------- Plotting ---------
labels = [f"DNA {i+1}" for i in range(len(inputs))]
cg_counts = [r[0] for r in results]
at_counts = [r[1] for r in results]

x = range(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar([i - width / 2 for i in x], cg_counts, width, label="CG/GC")
ax.bar([i + width / 2 for i in x], at_counts, width, label="AT/TA")

ax.set_ylabel("Counts")
ax.set_title("Pair counts in DNA sequences")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
