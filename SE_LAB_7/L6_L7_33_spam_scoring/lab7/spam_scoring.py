def sender_domain(email):
    if not isinstance(email, str) or "@" not in email:
        return None
    parts = email.split("@")
    domain = parts[1].strip().lower()
    return domain if domain else None


def first_link(text):
    if not isinstance(text, str):
        return None
    start = text.find("http")
    if start == -1:
        return None
    end = text.find(" ", start)
    if end == -1:
        end = len(text)
    link = text[start:end]
    return link if link else None


def shout_ratio(text):
    if not isinstance(text, str):
        return 0.0
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    upper = [c for c in letters if c.isupper()]
    return len(upper) / len(letters)


def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)


if __name__ == "__main__":
    main()