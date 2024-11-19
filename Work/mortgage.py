# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
# extra_payment_duration = 12
extra_payment_start_month = 61
extra_payment_end_month = 108
month = 0

while principal > 0:
    month += 1
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        total_payment = payment + extra_payment
    else:
        if principal <= payment:
            total_payment = principal + (principal * rate / 12)
        else:
            total_payment = payment

    principal = principal * (1 + rate / 12) - total_payment
    total_paid += total_payment
    print(month, round(total_paid, 2), round(principal, 2))

print(f"Total paid: ${total_paid:,.1f}")
print(f"Number of months: {month}")
