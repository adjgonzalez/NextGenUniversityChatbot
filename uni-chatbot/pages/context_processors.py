from .models import AdmissionSidebarItem, Logo, Navbar


# Provides navbar items and logo_path to all templates.
def navbar_items(request):
    # Fetch active menu items
    menu_items = Navbar.objects.filter(is_active=True).order_by("order")

    # Fetch logo from Logo model
    logo = Logo.objects.first()
    logo_path = logo.image_path if logo else None

    return {"navbar_items": menu_items, "logo_path": logo_path}


# Admission pages Sidebar
def admissions_sidebar(request):
    items = AdmissionSidebarItem.objects.filter(is_active=True).order_by("order")
    return {"admissions_sidebar_items": items}
