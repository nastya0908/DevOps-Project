from Calculator.src.greeting import greeting


def test_greeting(capsys):
    greeting("Nastya")
    out, _ = capsys.readouterr()
    assert out == "Hello, Nastya!\nOkey. Let me try to calculate example you enter!\n\n"
