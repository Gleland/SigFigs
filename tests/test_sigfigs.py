from sigfigs import sigfigs


def test_sigfigs_add():
    sf = sigfigs.SigFigs()
    assert(sf.add("0.01", "1") == '1')


def test_sigfigs_subtract():
    sf = sigfigs.SigFigs()
    assert(sf.subtract("0.01", "1") == '-1')


def test_sigfigs_multiply():
    sf = sigfigs.SigFigs()
    test_cases = [
        {"inputs": ["10.0", "1"], "answer": "1e+01"},
        {"inputs": ["0.00203", "0.8888"], "answer": "1.80e-03"},
        {"inputs": ["6.154", "3.14"], "answer": "1.93e+01"}
    ]
    for case in test_cases:
        assert(sf.multiply(*case["inputs"]) == case["answer"])


def test_sigfigs_divide():
    sf = sigfigs.SigFigs()
    test_cases = [
        {"inputs": ["20.0", "4"], "answer": "5e+00"},
        {"inputs": ["01000.", "-0.006700"], "answer": "-1.493e+05"},
        {"inputs": ["90090.", "5420"], "answer": "1.66e+01"},
    ]
    for case in test_cases:
        assert(sf.divide(*case["inputs"]) == case["answer"])


def test_sigfigs_count():
    sf = sigfigs.SigFigs()
    test_cases = {
        "100.0": 4,
        "0.00203": 3,
        "-100.0": 4,
        "1203450": 6,
        "1000": 1,
        "5420": 3,
        "01000.": 4,
        "-0.006700": 4,
        "01000.0": 5,
        "0.06540": 4,
        "0.002": 1,
        "009009.": 4,
        "0.0020": 2,
        "90090.": 5
    }
    for case, count in test_cases.items():
        assert(sf.count(case) == count)


def test_sigfigs_round():
    sf = sigfigs.SigFigs()
    test_cases = [
        {"inputs": ["20.0", 4], "answer": "2.000e+01"},
        {"inputs": ["-012.83", 6], "answer": "-1.28300e+01"},
        {"inputs": ["90090.", 3], "answer": "9.01e+04"},
    ]
    for case in test_cases:
        assert(sf.round(*case["inputs"]) == case["answer"])
