from deep_translator import GoogleTranslator

print(
    GoogleTranslator(
        source="auto",
        target="ta"
    ).translate("Hello")
)