# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('what\'s your name? ').strip().capitalize()
theEmail = input('what\'s your email?').strip()

theUserName = theEmail[:theEmail.index('@')]
theDomain = theEmail[theEmail.index('@') + 1:]

print(f"Hello {theName} Your User Name Is {theUserName} And Your Domain Is {theDomain}")