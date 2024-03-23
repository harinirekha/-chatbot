# Define the chatbot responses
responses = {
    "about campus": "Our campus is located near venkayapalle and is equipped with modern facilities including libraries, labs, sports complexes, and recreational areas.",
    "exam schedule": "The exam schedule for this semester is available on the university website.",
    "class timings": "Class timings are usually from 9:00 AM to 4:00 PM, with breaks in between.",
    "fee structure": "Our fee structure varies based on the program and category of students (e.g., regular, management quota, etc.). Please visit the university website or contact the admissions office for detailed fee information.",
    "course information": "We offer a variety of courses across different disciplines. You can find detailed information about each course on our website.",
    "faculty directory": "Our faculty directory is available on the university website. You can search for faculty members by name, department, or area of expertise.",
    "exam results": "You can check your exam results on the university portal. Please log in with your credentials to view your grades.",
    "hostel facilities": "We provide comfortable hostel accommodation for students with amenities such as Wi-Fi, laundry services, mess facilities, and 24/7 security.",
    "library services": "Our library offers a wide range of resources including books, e-books, journals, and databases. You can access the library catalog and online resources through our website.",
    "tuition payment": "You can make tuition payments online through our secure payment portal. Please log in to your student account to view your fees and make payments.",
    "academic calendar": "The academic calendar for this semester is available on the university website. It includes important dates such as semester start and end dates, registration deadlines, and exam schedules.",
    "admissions information": "For admissions information, please visit the admissions section on our website. You can find details about application procedures, admission requirements, and deadlines.",
    "student support services": "Our student support services include counseling, career advising, academic tutoring, and disability accommodations. Please visit the student services center for assistance.",
    "research opportunities": "We offer various research opportunities for students. You can explore ongoing research projects, funding opportunities, and research resources on our website.",
    "event announcements": "Stay updated with our latest events, workshops, and seminars by checking the events calendar on our website.",
    "placements support": "Our placement cell works tirelessly to connect students with leading companies for internships and job opportunities. We have a strong track record of placements in reputable organizations.",
    "extracurricular activities": "We encourage students to participate in extracurricular activities such as sports, cultural events, clubs, and community service to enhance their overall development.",
    "feedback and suggestions": "We value your feedback! Please feel free to provide your suggestions and feedback to help us improve our services.",
    "default": "I'm sorry, I'm not sure how to help with that. Please contact the university administration for further assistance."
}

# Define function to get response from the chatbot

# Define university website link
university_website = "https://www.example.com"

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]

# Main loop
def main():
    print("Welcome to the Academic Chatbot!")
    print("How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Have a nice day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
