from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views import View

def person_data_validation(request, person):
    name = request.POST.get("name")
    surname = request.POST.get("surname")
    description = request.POST.get("description")
    person.name = name
    person.surname = surname
    person.description = description
    if name and surname:
        person.save()

class AddPerson(View):

    def get(self, request):
        return render(request, "phonebook/add_person.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")
        newPerson = Person.objects.create(name=name, surname=surname, description=description)
        return redirect("/show/%s" % newPerson.id)


class PersonDetails(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)

        context = {
            'person' : person
        }
        return render(request, "phonebook/person_details.html", context)


class AllPersonsDisplay(View):

    def get(self, request):
        persons = Person.objects.all().order_by('surname') #alfabetycznie

        context = {

            'persons' : persons
        }
        return render(request, "phonebook/all_persons_display.html", context)


class PersonDelete(View):

    def get(self, request, id):
        context = { 'person' : Person.objects.get(pk=id)}
        return render(request, "phonebook/person_delete.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            Person.objects.filter(pk=id).first().delete()
            return HttpResponse("Contact has been deleted")
        else:
            return redirect('/')

class PersonModify(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phone_numbers = person.phone_set.all()
        context = {
            'person' : person,
            'phone_numbers' : phone_numbers,
        }
        return render(request, "phonebook/person_modify.html", context)

    def post(self, request, id):
        person_data_validation(request, Person.objects.get(pk=id))
        return HttpResponse("Changes have been applied")

class AddAddress(View):

    def get(self, request, id):
        person = Person.objects.get(pk=id)
        context = {
            'person': person
        }
        return render(request, "phonebook/add_address.html", context)

    def post(self, request, id):
        person_address = Person.objects.filter(pk=id).first()
        city = request.POST.get('city')
        street = request.POST.get('street')
        house_number = request.POST.get('house_number')
        apartment_number = request.POST.get('apartment_number')
        Address.objects.create(city=city, street=street, house_number=house_number,
                                            apartment_number=apartment_number, person_address=person_address)
        return HttpResponse("New address has been added")


class AddPhone(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        context = {
            'person': person
        }
        return render(request, "phonebook/add_phone.html", context)
    def post(self, request, id):
        person_number = Person.objects.filter(pk=id).first()
        number = request.POST.get('number')
        number_type = request.POST.get('number_type')
        Phone.objects.create(number=number, number_type=number_type, person_number=person_number)
        return HttpResponse("Number has been added")

class AddEmail(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        context = {
            'person': person
        }
        return render(request, "phonebook/add_email.html", context)
    def post(self, request, id):
        person_mail = Person.objects.filter(pk=id).first()
        email = request.POST.get('email')
        email_type = request.POST.get('email_type')
        Email.objects.create(email=email, email_type=email_type, person_mail=person_mail)
        return HttpResponse("Email address has been added")

class AddressDelete(View):

    def get(self, request, id):
        context = { 'person' : Person.objects.get(pk=id)}
        return render(request, "phonebook/delete_address.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            Address.objects.filter(pk=id).first().delete()
            return HttpResponse("Address has been deleted")
        else:
            return redirect('/')


class PhoneDelete(View):

    def get(self, request, id):
        context = { 'person' : Person.objects.get(pk=id)}
        return render(request, "phonebook/delete_phone.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            Phone.objects.filter(pk=id).first().delete()
            return HttpResponse("Phone number has been deleted")
        else:
            return redirect('/')


class EmailDelete(View):
    def get(self, request, id):
        context = { 'person' : Person.objects.get(pk=id)}
        return render(request, "phonebook/delete_email.html", context)

    def post(self, request, id):
        if request.POST.get('decision') == 'yes':
            Email.objects.filter(pk=id).first().delete()
            return HttpResponse("Email address has been deleted")
        else:
            return redirect('/')

class CreateGroup(View):

    def get(self, request):
        return render(request, "phonebook/create_group.html")
    def post(self, request):
        name = request.POST.get("name")
        group = Group.objects.create(name=name)
        # group_id = group.id
        return HttpResponse("New group has been created") #redirect("/AddMembers/%s" % group_id)



class ShowGroup(View):
    def get(self, group_id):
        group = Group.objects.get(pk=group_id)
        context = {
            'group' : group,
            'members' : group.person.all()
        }
        return render(request, "phonebook/show_group.html", context)

class AddGroupMember(View):
    def get(self, request, group_id):
        group = Group.objects.get(pk=group_id)
        context = {
            'group': group,
            'members' : group.person.all(),
            'contacts': Person.objects.all(),
        }
        return render(request, "phonebook/members_add.html", context)

    def post(self, request, group_id):
        group = Group.objects.get(pk=group_id)
        context = {
            'contacts': Person.objects.all(),
            'group': group,
            'members': group.person.all()
        }
        member = str(request.POST.get('person'))
        group.person.add(member)
        return HttpResponse("New contact has been added to your group")






