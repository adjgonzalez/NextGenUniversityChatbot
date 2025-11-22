import json
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from users.services import enroll_user_in_program
from pages.models import Program
from django.shortcuts import get_object_or_404
# Home page
def index(request):
    return render(request, "pages/home.html")


# Admissions full page view (reload-safe, works with dynamic sidebar)
def admissions_page(request, page_name="undergraduate"):
    allowed_pages = ["undergraduate", "graduate", "online_course", "funding"]
    if page_name not in allowed_pages:
        page_name = "undergraduate"

    context = {
        "current_page": page_name,
        "page_title": page_name.replace("_", " ").title(),  # e.g., "Undergraduate"
    }
    return render(request, "admissions/admission.html", context)


# Load sidebar content dynamically via AJAX
def load_sidebar_content(request, page_name):
    template_map = {
        "undergraduate": "admissions/undergraduate.html",
        "graduate": "admissions/graduate.html",
        "online_course": "admissions/online_course.html",
        "funding": "admissions/funding.html",
    }

    template_name = template_map.get(page_name)
    if template_name:
        html = render_to_string(template_name, request=request)
        return JsonResponse({"html": html})
    return JsonResponse({"html": "<p>Page not found</p>"}, status=404)


# Contact page
def contact(request):
    return render(request, "base/contact.html")


# Faculty page
def faculty(request):
    return render(request, "base/faculty.html")


def programs(request):
    """Displays all programs with categories"""
    programs = Program.objects.all()
    categories = set(program.program_type.name for program in programs)

    return render(request, "base/programs.html", {"programs": programs, "categories": categories })


PROGRAMS = {
    "Undergraduate": [
        {
            "id": "55204d2b-3dfa-4d92-873a-9b6ec8ae49ff",
            "name": "BSc in Computer Science",
            "slug": "bsc-in-computer-science",
            "degree": "BSc",
            "duration": "4 years",
            "routes": "Course-based",
            "enrollment_status": "Full-time",
            "campus": "St. John's",
            "description": (
                "Learn programming, algorithms, AI, and software development. "
                "Computer science deals with the theoretical foundations of information and computation, and with practical techniques for their implementation and application. "
                "Virtually every discipline – practical, theoretical or creative – is experiencing the influence of computers. The ever-increasing dependence on computer technology "
                "in our daily lives presents rich opportunities for those interested in the design of new applications and systems. Every career can benefit from a deeper understanding of computing. "
                "The technology skills a major in computer science helps develop will make you indispensable and relevant no matter your position. "
                "We offer individual courses and full programs so any student can develop their computer skills and interest regardless of their career trajectory. "
                "Memorial’s Co-operative Internship in Computer Science (CICS) provides an opportunity for you to obtain rewarding placements in computer industries. "
                "The internship program includes a paid placement of eight to 16 months so you can explore career options and develop workplace skills at the same time. "
                "We offer major, minor and honours programs leading to either a bachelor of arts (BA) or bachelor of science (B.Sc.) in Computer Science. "
                "Joint programs are available in: "
            ),
            "joint_programs": [
                "Applied Mathematics and Computer Science (B.Sc. major)",
                "Computer Science and Economics (B.Sc. major)",
                "Computer Science and Physics (B.Sc. major and honours)",
                "Computer Science and Pure Mathematics (B.Sc. major and honours)",
                "Computer Science and Statistics (B.Sc. major and honours)",
            ],
        },
        {
            "id": "7d523468-684f-4d44-b904-bfca5251d511",
            "name": "BA in Economics",
            "slug": "ba-in-economics",
            "degree": "BA",
            "duration": "3 years",
            "description": "Study economics, finance, and market theory. "
            "Economics is a versatile field that deals with the analysis and management of production, "
            "distribution and consumption of goods and services. Economics gives us the analytical tools to understand questions "
            "such as how prices are determined, why some people are unemployed, why interest rates rise and fall, "
            "and why product is traded between nations.",
        },
    ],
    "Graduate": [
        {
            "id": "1ff1babe-54aa-46a5-bee4-1112964ba0d8",
            "name": "MBA",
            "slug": "mba",
            "degree": "MBA",
            "duration": "2 years",
            "description": "Advanced business management, leadership, and strategy. The MBA program is made up of 20 courses to be "
            "completed on a part-time or full-time basis. Our MBA program is offered on campus in St. John’s and is not available online. "
            "Required courses include business ethics, leadership skills and international business as well as business fundamentals "
            "such as economics, finance, accounting, organizational behaviour, operations management, statistics, marketing, information "
            "systems, human resources and strategic management. "
            "Students can focus their studies through electives, including up to two graduate courses from other faculties, "
            "and self-directed, faculty supervised research projects. One elective must be a designated course in any area of "
            "international business.",
        },
        {
            "id": "71669288-a256-466a-8eb4-7113eac249c0",
            "name": "MDSc in Data Science",
            "slug": "mdsc-in-data-science",
            "degree": "MDSc",
            "duration": "2 years",
            "description": "Master data analytics, machine learning, and AI. Data science is one of the most sought-after professions of "
            "the 21st century. With lives increasingly being lived online, nearly every individual leaves behind a data trail that is as "
            "valuable as gold in this digital age. With this increasing generation of data, there is also an ever-increasing demand for "
            "specialists who are able to structure, analyse and process it. This work is done by data scientists. Given the continuing "
            "demand for data scientists, and the expected accelerated growth of this profession over the next few decades, Memorial has "
            "developed the Master of Data Science (MDSc). Jointly offered by the Departments of Mathematics and Statistics and Computer "
            "Science, it is a one-year program aiming to equip students with the foundations of data science and provide them with "
            "practical techniques needed to effectively translate data into knowledge, communicate the findings, and help in the "
            "decision-making process.",
        },
    ],
    "Online Courses": [
        {
            "id": "ed404c78-959e-42fe-9bb8-14a238ebfcd0",
            "name": "Web Development Bootcamp",
            "slug": "web-development-bootcamp",
            "degree": "Web development",
            "duration": "6 months",
            "description": "Learn full stack web development with hands-on projects. The Web Development Bootcamp is an intensive, "
            "hands-on program designed to help learners master the essential skills required to build modern, responsive websites "
            "and web applications. Through a practical, project-based approach, students gain experience in front-end technologies "
            "such as HTML, CSS, JavaScript, and React, as well as back-end development using Node.js, Express, and databases like "
            "MongoDB. Whether you’re a complete beginner or looking to enhance your existing skills, this bootcamp prepares you "
            "for a successful career as a Full-Stack Web Developer. By the end of the course, participants will have built multiple "
            "real-world projects, developed a professional portfolio, and gained the confidence to pursue freelance work or entry-level "
            "developer roles.",
        },
        {
            "id": "dfee4da8-cf6d-4955-90b8-4a8c3ba0d851",
            "name": "Introduction to AI",
            "slug": "introduction-to-ai",
            "degree": "AI",
            "duration": "3 months",
            "description": "Beginner-friendly AI concepts and tools. The Introduction to Artificial Intelligence course provides a "
            "comprehensive foundation in the core principles and applications of AI. Designed for beginners and aspiring professionals, "
            "this program explores how machines can simulate human intelligence through problem-solving, learning, and decision-making. "
            "Students will gain hands-on experience with key AI techniques such as machine learning, natural language processing, and "
            "computer vision. The course also covers the ethical implications of AI and its growing impact across industries including "
            "healthcare, finance, and technology. By the end of the course, learners will understand fundamental AI concepts, develop "
            "basic models using Python-based tools, and be prepared to pursue advanced studies or careers in AI-driven fields.",
        },
    ],
}


def programs_detail(request, program_slug):
    """Loads program information based on slug
    
        Input: 
            program_slug: slug to search program from
    """
    program = get_object_or_404(Program, slug=program_slug)
    category = program.program_type.name
    
    #Create dictionary of program to handle JSON serialization
    program_dict = {
        "id": str(program.id),
        "name": program.name,
        "slug": program.slug,
        "degree": program.degree,
        "duration": program.duration,
        "description": program.description,
        "routes": program.routes,
        "enrollment_status": program.enrollment_status,
        "campus": program.campus,
        "joint_programs": program.joint_programs,
    }
    # Create JSON object from dictionary
    program_json = json.dumps(program_dict, ensure_ascii=False)

    return render(
                    request,
                    "base/programs_detail1.html",
                    {"program": program
                     , "program_json": program_json   
                     , "category": category},
                )

def apply_now(request):        
    if not request.user.is_authenticated:
        return JsonResponse({"message": "You must be logged in"}, status=401)

    try:
        # Get program that user wants to apply for
        data = json.loads(request.body)
        program = data.get("program")        
        enroll_user_in_program(request.user, program)
        return JsonResponse({"message": "Application successful"})                      

    except Exception as e:        
        return JsonResponse({"message": "Something went wrong. Application Cancelled"}, status=500)

    
    