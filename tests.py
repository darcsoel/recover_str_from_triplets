from main import recoverSecret

secret = "whatisup"
triplets = [
    ["t", "u", "p"],
    ["w", "h", "i"],
    ["t", "s", "u"],
    ["a", "t", "s"],
    ["h", "a", "p"],
    ["t", "i", "s"],
    ["w", "h", "s"],
]


def test1():
    assert recoverSecret(triplets) == secret
