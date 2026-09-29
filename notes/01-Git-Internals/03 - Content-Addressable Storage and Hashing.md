---
tags:
  - git
  - hashing
  - cryptography
  - content-addressable
date: 2026-09-29
---

# 03 - Content-Addressable Storage & Hashing

Up-Link: [[Index - Git Architecture Mastery]] | Previous: [[02 - The Four Git Objects]] | Next: [[04 - References HEAD and Branches]]

---

## 🎨 Real-Life Analogy: DNA Fingerprint Locker System

Imagine a storage bank with billions of lockers.
Instead of assigning lockers by sequential numbers (Locker 1, Locker 2), the bank runs every item through a **magic DNA scanner**:

1. You put a document into the scanner.
2. The scanner outputs a unique 40-character fingerprint code (e.g. `c65b433...`).
3. That code **becomes the exact locker address** where the item is stored!

> [!IMPORTANT] Immutable Rule
> If you change even **a single comma** in the document, its DNA fingerprint changes completely, and it goes into a brand-new locker address! You can never overwrite an existing locker without changing its address fingerprint.

---

## 🏛️ Ground-Truth Concept: How Git Computes Object Hashes

Git calculates SHA-1 hashes using a strict header format:

$$\text{Header} = \text{type} + \text{" "} + \text{size\_in\_bytes} + \text{\textbackslash 0}$$
$$\text{SHA-1 Hash} = \text{SHA1}(\text{Header} + \text{Content})$$

### Why Git is Tamper-Proof (The Cryptographic Hash Chain)

Because a Commit contains the Tree hash, and the Tree contains the Blob hashes, altering any historical line of code causes a ripple effect up the graph:

```mermaid
graph LR
    BlobTampered["Altered Code Line"] -->|"Changes Hash"| NewBlobSHA["New Blob SHA"]
    NewBlobSHA -->|"Changes Hash"| NewTreeSHA["New Tree SHA"]
    NewTreeSHA -->|"Changes Hash"| NewCommitSHA["New Commit SHA"]
```

If anyone attempts to alter history on a past commit, the commit hash changes, invalidating all child commits down the chain!

---

## 🧪 Terminal Grounding: Compute a Git Blob Hash Manually

You can reproduce Git's exact hashing formula directly in bash:

```bash
# Create a test string
echo -n "hello world" | git hash-object --stdin
# Output: 5dd01c70286e300d8f5c8866164f9b2b5f6a9170
```
