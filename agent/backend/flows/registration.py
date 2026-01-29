import re
from agent.google_sheets import save_student_to_google_sheet
def handle_registration(message: str, state):
    """
    Registration flow handler.
    Uses `state` to track steps: ask_name → ask_phone → ask_email → ask_course
    """
    # Step 0: Initialize registration
    if not state.has("reg_step"):
        state.set("intent", "registration")
        state.set("reg_step", "ask_name")
        return "Please enter your full name 👤"

    # Step 1: Full Name
    if state.get("reg_step") == "ask_name":
        if len(message.strip()) < 3:
            return "Name must be at least 3 characters. Please re-enter 👤"
        state.set("name", message.strip())
        state.set("reg_step", "ask_phone")
        return "Please enter your 10-digit mobile number 📞"

    # Step 2: Phone
    if state.get("reg_step") == "ask_phone":
        if not re.match(r"^[6-9]\d{9}$", message):
            return "Invalid mobile number. It should start with 6-9 and be 10 digits."
        state.set("phone", message)
        state.set("reg_step", "ask_email")
        return "Please enter your email address 📧"

    # Step 3: Email
    if state.get("reg_step") == "ask_email":
        if not re.match(r"[^@]+@[^@]+\.[^@]+", message):
            return "Invalid email format. Please enter a valid email."
        state.set("email", message)
        state.set("reg_step", "ask_course")
        return "Which course would you like to register for? 🎓"

    # Step 4: Course
    if state.get("reg_step") == "ask_course":
        state.set("course", message)

        # Save to Google Sheet
        save_student_to_google_sheet({
            "name": state.get("name"),
            "email": state.get("email"),
            "phone": state.get("phone"),
            "course": state.get("course")
        })

        # Clear registration state
        state.clear("intent")
        state.clear("reg_step")
        state.clear("name")
        state.clear("email")
        state.clear("phone")
        state.clear("course")

        return (
            "🎉 Registration successful!\n"
            "Our team will contact you shortly.\n"
            "You can now ask me anything about Blismos Academy."
        )
