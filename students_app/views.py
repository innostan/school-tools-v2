from django.shortcuts import render, redirect
from .models import Student
from .form import StudentForm
from django.http import HttpResponse

# Homepage view: display all students
def home(request):
    students = Student.objects.all()  # get all students from database
    html = """
    <html>
    <head>
        <title>School App Dashboard</title>
        <style>
            body { background-color: #f0f8ff; font-family: Arial, sans-serif; text-align: center; }
            table { width: 80%; margin: 20px auto; border-collapse: collapse; background-color: #ffffff; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: center; }
            th { background-color: #4CAF50; color: white; }
        </style>
    </head>
    <body>
        <h1>School App Dashboard</h1>
        <table>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Email</th>
                <th>Date of Birth</th>
            </tr>
    """
    for s in students:
        html += f"""
            <tr>
                <td>{s.first_name}</td>
                <td>{s.last_name}</td>
                <td>{s.email}</td>
                <td>{s.date_of_birth}</td>
            </tr>
        """
    if not students:
        html += "<tr><td colspan='4'>No students found.</td></tr>"
    html += "</table></body></html>"
    return HttpResponse(html)

# Student registration view
def register_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to homepage
    else:
        form = StudentForm()
    return render(request, 'students_app/register.html', {'form': form})