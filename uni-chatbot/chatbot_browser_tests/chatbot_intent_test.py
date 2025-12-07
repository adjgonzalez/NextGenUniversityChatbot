import os

from playwright.sync_api import sync_playwright

DJANGO_URL = "http://127.0.0.1:8000/"


def take_screenshot(page, filename, description=""):
    os.makedirs("test_results", exist_ok=True)
    page.screenshot(path=f"test_results/{filename}")
    print(f"✓ Screenshot saved: {filename} ({description})")


def run_intent_tests(page):
    print("=" * 90)
    print("Chatbot JS Intent Tests")
    print(
        "Covers English, French, Spanish, Italian, Mongolian, German, Chinese, Russian, Arabic"
    )
    print("=" * 90)

    intents = [
        # --- English --
        ("student", True),
        ("register", True),
        ("help", True),
        ("thanks", True),
        ("feedback", True),
        ("thank you very much", True),
        ("I need to register for courses", True),
        # --- French (Français) ---
        ("bonjour", True),  # hello
        ("étudiant", True),  # student
        ("s'inscrire", True),  # register
        ("aide", True),  # help
        ("merci", True),  # thanks
        ("retour", False),  # Return on the chatbot is not supported
        ("je veux m'inscrire", True),
        ("pouvez-vous m'aider ?", True),  # can you help me?, should return true
        ("feedback", True),  # Universal
        # --- Spanish (Español) ---
        ("estudiante", True),
        ("registrarse", True),
        ("ayuda", True),
        ("gracias", True),
        ("quiero registrarme", True),
        ("¿puedes ayudarme?", True),
        # --- Italian (Italiano) ---
        ("studente", True),
        ("registrare", True),
        ("aiuto", True),
        ("grazie", True),
        ("vorrei registrarmi", True),
        ("puoi aiutarmi?", True),
        ("feedback", True),
        # --- Mongolian (Монгол) ---
        ("оюутан", True),  # student
        ("бүртгүүлэх", True),  # register
        ("тусламж", True),  # help
        ("баярлалаа", True),  # thanks
        # --- German (Deutsch) ---
        ("student", True),
        ("registrieren", True),
        ("hilfe", True),
        ("danke", True),
        ("können Sie mir helfen?", True),
        ("ich möchte mich registrieren", True),
        ("feedback", True),
        # --- Chinese (中文) ---
        ("学生", True),  # student
        ("注册", True),  # register
        ("帮助", True),  # help
        ("谢谢", True),  # thanks
        ("请帮我注册", True),
        ("我要反馈", True),  # I want to feedback
        # --- Russian (Русский) ---
        ("студент", True),
        ("зарегистрироваться", True),  # register
        ("помощь", True),
        ("спасибо", True),
        ("мне нужна помощь", True),  # I need help
        ("Обратная связь", True),  # Feedback
        # --- Arabic (العربية) ---
        ("طالب", True),  # student
        ("تسجيل", True),  # register
        ("مساعدة", True),  # help
        ("شكرا", True),  # thanks
        ("اريد التسجيل", True),  # I want to register
        ("اريد المساعدة", True),  # I want help
        ("ملاحظات", True),  # feedback
        # === Variants, substrings, casing, extra ===
        ("I am an undergraduate student", True),
        ("can you help me?", True),
        ("PLEASE REGISTER ME", True),
        ("registering now", True),
        ("feedback form", True),
        ("please help", True),
        ("could you register me?", True),
        ("I want to feedback about your service", True),
        # === Punctuation, emoji, spaces, typoes ===
        (" help!  ", True),
        ("register!!!", True),
        ("help 😊", True),
        ("\tstudent\n", True),
        ("    ", False),  # Empty/only whitespace
        ("studnt", False),  # misspelling
        ("regster", False),
        ("hlep", False),
        ("merciii", True),  # We can tell it's merci
        ("graziee", True),  # We can tell it's graziee
        # === Gibberish, numerics, unrelated ===
        ("asldkfjasldkfj", False),
        ("newuser123", False),
        ("123", False),
        ("🚀", False),
        ("what's the meaning of life?", False),
        ("exit", False),
        # === Partial/fragmented/combined/no delimiter ===
        ("stud", False),
        ("registration", True),
        ("studenteaiuto", True),  # Partial matches should return the first matched word
        ("studentregisterhelp", True),
        # === Mixed/multi-lingual input ===
        ("can you help تسجيل me?", True),
        ("merci help", True),
        ("请帮我帮助", True),  # Combination
        ("quiero aiuto", True),  # Spanish/Italian
        # === Multi-intent, repeated words ===
        ("student register help", True),
        ("help!help!help!", True),
        # === Greetings ===
        ("hello", True),
        ("hola", True),
        ("ciao", True),
    ]
    passed = 0
    failed = 0

    for msg, expected in intents:
        print(f"Testing intent: '{msg}' ... ", end="")
        try:
            result = page.evaluate(
                "msg => Boolean(window.checkIntentAndHandle(msg))", msg
            )
        except Exception as e:
            print(f"X ERROR: Could not call checkIntentAndHandle: {e}")
            failed += 1
            continue

        print(f"got: {result}, expected: {expected}", end=" ")
        if bool(result) == bool(expected):
            print("✓ PASS")
            passed += 1
        else:
            print("X FAIL")
            failed += 1

    print("=" * 90)
    print(f"Total passed: {passed}, failed: {failed}")
    take_screenshot(page, "intent_tests_complete.png", "After intent tests")
    return passed, failed


def main():
    print("\nINSTRUCTIONS:")
    print("◼ Make sure your Django server is running at http://127.0.0.1:8000/")
    print("◼ Example: python manage.py runserver\n")
    print("◼ Then run this script in another terminal.\n")
    print(
        "◼ Tests: ENGLISH  |  FRANÇAIS  |  ESPAÑOL  |  ITALIANO  |  МОНГОЛ  |  DEUTSCH  |  中文  |  РУССКИЙ  |  العربية\n"
    )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        print(f"Navigating to {DJANGO_URL}...")
        page.goto(DJANGO_URL)
        page.wait_for_selector("body")
        take_screenshot(page, "chatbot_page_loaded.png", "Landing page loaded")

        passed, failed = run_intent_tests(page)

        browser.close()

        if failed == 0:
            print("\n✓ ALL INTENT TESTS PASSED")
        else:
            print("\nX Some intent tests failed; check above for details.")


if __name__ == "__main__":
    main()
