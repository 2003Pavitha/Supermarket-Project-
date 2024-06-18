import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Product data

products = {
    'kids': {'gown': 400, 'shirt': 300},
    'women': {'leggings': 500, 'top': 350},
    'men': {'shirt': 600, 'jeans': 700}
}

# Discounts and GST

offers = {'kids': 0.1, 'women': 0.15, 'men': 0.2}
GST_RATE = 0.18

# Function to calculate the price after discount and GST

def calculate_price(category, product, quantity):
    base_price = products[category][product] * quantity
    discount = base_price * offers[category]
    discounted_price = base_price - discount
    gst = discounted_price * GST_RATE
    total_price = discounted_price + gst
    return total_price

# Function to send an email

def send_email(subject, body, to='pavithauma@gmail.com'):

    msg = MIMEMultipart()
    msg['From'] = 'pavithauma@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as s:
            s.starttls()
            s.login('pavithavaranam2003@gmail.com', 'putz gdiw cajk wiru')
            s.send_message(msg)
        print(f"Email sent to {to}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to process a purchase

def process_purchase(category, product, quantity):
    total_price = calculate_price(category, product, quantity)
    print(f"Total price for {quantity} {product}(s) in {category}: {total_price:.2f}")
    subject = "Purchase Receipt"
    body = (f"Thank you for your purchase of {quantity} {product}(s) in {category}.\n"
            f"Total price (including GST): {total_price:.2f}\n"
            f"Date and Time: {datetime.datetime.now()}\n")
    send_email(subject, body)

# Function to display products

def display_products():
    for category in products:
        print(f"\nCategory: {category}")
        for product, price in products[category].items():
            print(f"  {product}: {price}")

# Main function to run the supermarket system

def main():
    print("Welcome to the Supermarket System!")
    display_products()
    while True:
        print("\nAvailable Categories: kids, women, men")
        category = input("Enter category (or 'exit' to quit): ").strip().lower()
        if category == 'exit':
            print("Thank you for visiting our supermarket!")
            break
        if category not in products:
            print("Invalid category. Please try again.")
            continue
        
        print(f"Products in {category}: {', '.join(products[category].keys())}")
        product = input("Enter product: ").strip().lower()
        if product not in products[category]:
            print("Invalid product. Please try again.")
            continue
        
        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                raise ValueError("Quantity must be greater than 0.")
        except ValueError as e:
            print(e)
            continue
        
        process_purchase(category, product, quantity)

if __name__ == "__main__":
    main()
