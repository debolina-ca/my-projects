# Digits of Pi

!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi -o digits_of_pi.txt
digits_of_pi_text = open('digits_of_pi.txt', 'r')
pi_digits = digits_of_pi_text.read(4)
print(pi_digits)
pi_digits += digits_of_pi_text.read(4)
print(pi_digits)