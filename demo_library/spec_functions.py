from matplotlib import colors

# matplotlib
import matplotlib.pyplot as plt


def background_gradient_(s, m, M, cmap="PuBu", low=0, high=0):
    rng = M - m
    norm = colors.Normalize(m - (rng * low), M + (rng * high))
    normed = norm(s.values)
    c = [colors.rgb2hex(x) for x in plt.cm.get_cmap(cmap)(normed)]
    return ["background-color: %s" % color for color in c]


# highlight_pxx: to highlight certain p-values in the following overview.
# Input s = p-value threshold
def highlight_p99(s):
    p99 = s < 0.01
    return ["background-color: red" if v else "" for v in p99]


def highlight_p95(s):
    p95 = s < 0.05
    return ["background-color: orange" if v else "" for v in p95]


def highlight_p90(s):
    p90 = s < 0.10
    return ["background-color: yellow" if v else "" for v in p90]


def highlight_p00(s):
    p00 = s < 1.01
    return ["background-color: #5fba7d" if v else "" for v in p00]


def highlight_p99_2(s):
    p99 = s < 0.01
    return ["background-color: #5fba7d" if v else "" for v in p99]


def highlight_p95_2(s):
    p95 = s < 0.05
    return ["background-color: yellow" if v else "" for v in p95]


def highlight_p90_2(s):
    p90 = s < 0.10
    return ["background-color: orange" if v else "" for v in p90]


def highlight_p00_2(s):
    p00 = s < 1.01
    return ["background-color: red" if v else "" for v in p00]


def highlight_c00(s):
    c00 = s > -0.01
    return ["background-color: #5fba7d" if v else "" for v in c00]


def highlight_c02(s):
    c02 = s > 0.2
    return ["background-color: #D1D81E" if v else "" for v in c02]


def highlight_c05(s):
    c05 = s > 0.5
    return ["background-color: yellow" if v else "" for v in c05]


def highlight_c08(s):
    c08 = s > 0.8
    return ["background-color: orange" if v else "" for v in c08]


def highlight_c13(s):
    c13 = s > 1.3
    return ["background-color: red" if v else "" for v in c13]


def highlight_HI25(s):
    hi25 = s == "Red"
    return ["background-color: red" if v else "" for v in hi25]


def highlight_HI10(s):
    hi10 = s == "Orange"
    return ["background-color: orange" if v else "" for v in hi10]


def highlight_HI00(s):
    hi00 = s == "Green"
    return ["background-color: #5fba7d" if v else "" for v in hi00]
