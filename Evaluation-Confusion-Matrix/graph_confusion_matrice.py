# -*- coding: utf-8 -*-

#M1 = interest on arrears rate propositon ONE
#M2= interest on arrears rate propositon TWO
#M3= imprescritibility
#M4 = lovering the import tax exception

"""Temperature of zero Gemma 27b"""

import matplotlib.pyplot as plt
import numpy as np



# --- Confusion matrices ---
M1 = np.array([
    [0, 0, 13],
    [0, 2, 0],
    [24, 0, 0]
])

M2 = np.array([
    [0, 0, 3],
    [7, 2, 1],
    [25, 1, 0]
])

M3 = np.array([
    [0, 0, 11],
    [1, 6, 0],
    [27, 0, 0]
])

M4 = np.array([
    [4, 0, 33],
    [1, 0, 0],
    [30, 0, 3]
])

matrices = [M1, M2, M3, M4]
base_titles = [
    "Adjustment of Interest on Arrears — Proposition One",
    "Adjustment of Interest on Arrears — Proposition Two",
    "Imprescriptibility of Murder",
    "Lowering Import Tax Exemption"
]

x_labels = ["Negative", "Neutral", "Positive"]
y_labels = ["Positive", "Neutral", "Negative"]

fig, axes = plt.subplots(2, 2, figsize=(13, 12))
fig.suptitle(
    "Confusion Matrices for Sentiment Classification\n across Policy Cases (Gemma3:27b temp=0)",
    fontsize=20,
    y=0.98
)


vmax = 40
cmap = "OrRd"

for ax, M, base_title in zip(axes.flatten(), matrices, base_titles):
    im = ax.imshow(M, cmap=cmap, vmin=0, vmax=vmax)

    # Calculate accuracy (anti-diagonal sum due to reversed axes labels)
    # y: Pos, Neu, Neg vs x: Neg, Neu, Pos
    correct_preds = M[0, 2] + M[1, 1] + M[2, 0]
    accuracy = correct_preds / np.sum(M)

    title = f"{base_title}\n(Overall Accuracy = {accuracy:.3f})"

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(
                j, i, str(M[i, j]),
                ha='center', va='center', fontsize=11
            )

    ax.set_title(title, fontsize=12, pad=14)

    ax.set_xticks(np.arange(3))
    ax.set_xticklabels(x_labels, fontsize=11)

    ax.set_yticks(np.arange(3))
    ax.set_yticklabels(y_labels, fontsize=11)

    ax.set_xlabel("Prediction", labelpad=8)
    ax.set_ylabel("Reference", labelpad=18)


plt.tight_layout(rect=[0, 0, 1, 0.95], pad=2)


cbar = fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75, pad=0.02)
cbar.set_label("Count")

plt.show()

"""Gemma High temperature"""

import matplotlib.pyplot as plt
import numpy as np

# --- Confusion matrices ---
M1 = np.array([
    [0, 0, 13],
    [0, 2, 0],
    [24, 0, 0]
])

M2 = np.array([
    [0, 0, 3],
    [5, 2, 1],
    [27, 0, 1]
])

M3 = np.array([
    [0, 0, 11],
    [1, 6, 0],
    [27, 0, 0]
])

M4 = np.array([
    [4, 0, 33],
    [1, 0, 0],
    [30, 0, 3]
])

matrices = [M1, M2, M3, M4]
base_titles = [
    "Adjustment of Interest on Arrears — Proposition One",
    "Adjustment of Interest on Arrears — Proposition Two",
    "Imprescriptibility of Murder",
    "Lowering Import Tax Exemption"
]

x_labels = ["Negative", "Neutral", "Positive"]
y_labels = ["Positive", "Neutral", "Negative"]

fig, axes = plt.subplots(2, 2, figsize=(13, 12))
fig.suptitle(
    "Confusion Matrices for Sentiment Classification\n across Policy Cases (Gemma3:27b temp=0.9)",
    fontsize=20,
    y=0.98
)


vmax = 40
cmap = "OrRd"

for ax, M, base_title in zip(axes.flatten(), matrices, base_titles):
    im = ax.imshow(M, cmap=cmap, vmin=0, vmax=vmax)

    # Calculate accuracy (anti-diagonal sum due to reversed axes labels)
    # y: Pos, Neu, Neg vs x: Neg, Neu, Pos
    correct_preds = M[0, 2] + M[1, 1] + M[2, 0]
    accuracy = correct_preds / np.sum(M)
    title = f"{base_title}\n(Overall Accuracy = {accuracy:.3f})"

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(
                j, i, str(M[i, j]),
                ha='center', va='center', fontsize=11
            )

    ax.set_title(title, fontsize=12, pad=14)

    ax.set_xticks(np.arange(3))
    ax.set_xticklabels(x_labels, fontsize=11)

    ax.set_yticks(np.arange(3))
    ax.set_yticklabels(y_labels, fontsize=11)

    ax.set_xlabel("LLM classification", labelpad=8)
    ax.set_ylabel("Administrative report classification", labelpad=18)


plt.tight_layout(rect=[0, 0, 1, 0.95], pad=2)


cbar = fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75, pad=0.02)
cbar.set_label("Count")

plt.show()

"""GPT-5-mini"""

import matplotlib.pyplot as plt
import numpy as np

# --- Confusion matrices ---
M1 = np.array([
    [0, 0, 11],
    [0, 2, 0],
    [24, 0, 2]
])

M2 = np.array([
    [1, 0, 3],
    [1, 2, 0],
    [31, 0, 1]
])

M3 = np.array([
    [0, 0, 11],
    [1, 6, 0],
    [27, 0, 0]
])

M4 = np.array([
    [4, 0, 39],
    [1, 0, 0],
    [31, 0, 1]
])

matrices = [M1, M2, M3, M4]
base_titles = [
    "Adjustment of Interest on Arrears — Proposition One",
    "Adjustment of Interest on Arrears — Proposition Two",
    "Imprescriptibility of Murder",
    "Lowering Import Tax Exemption"
]

x_labels = ["Negative", "Neutral", "Positive"]
y_labels = ["Positive", "Neutral", "Negative"]

fig, axes = plt.subplots(2, 2, figsize=(13, 12))
fig.suptitle(
    "Confusion Matrices for Sentiment Classification\n across Policy Cases (GPT-5-mini)",
    fontsize=20,
    y=0.98
)


vmax = 40
cmap = "OrRd"

for ax, M, base_title in zip(axes.flatten(), matrices, base_titles):
    im = ax.imshow(M, cmap=cmap, vmin=0, vmax=vmax)

    # Calculate accuracy (anti-diagonal sum due to reversed axes labels)
    # y: Pos, Neu, Neg vs x: Neg, Neu, Pos
    correct_preds = M[0, 2] + M[1, 1] + M[2, 0]
    accuracy = correct_preds / np.sum(M)
    title = f"{base_title}\n(Overall Accuracy = {accuracy:.3f})"

    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(
                j, i, str(M[i, j]),
                ha='center', va='center', fontsize=11
            )

    ax.set_title(title, fontsize=12, pad=14)

    ax.set_xticks(np.arange(3))
    ax.set_xticklabels(x_labels, fontsize=11)

    ax.set_yticks(np.arange(3))
    ax.set_yticklabels(y_labels, fontsize=11)

    ax.set_xlabel("LLM classification", labelpad=8)
    ax.set_ylabel("Administrative report classification", labelpad=18)


plt.tight_layout(rect=[0, 0, 1, 0.95], pad=2)


cbar = fig.colorbar(im, ax=axes.ravel().tolist(), shrink=0.75, pad=0.02)
cbar.set_label("Count")

plt.show()
