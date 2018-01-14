import csv

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from .models import *
from .forms import *


def index(request):
    output = 'my awesome site begins'
    context = {
        'message': output,
    }
    return render(request, 'coreapps/index.html', context)


def places_home(request):
    output = "this is the 'places' to be"
    all_places = Place.objects.all()
    print(all_places)
    context = {
        'message': output,
        'all_places': all_places,
    }
    return render(request, 'coreapps/place.html', context)


def handle_uploaded_file(f):
    with open('upload.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def places_import(request):
    output = "places import page"
    if request.method == 'POST':
        places_import_form_data = places_import_form(request.POST, request.FILES)
        if places_import_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # redirecto to a new URL:
            #return HttpResponseRedirect('/coreapps/places/')
            #try:
            handle_uploaded_file(request.FILES["file_path"])
            with open('upload.csv', 'r') as f:
                reader = csv.reader(f)
                first_row = True
                for row in reader:
                    if first_row == True:
                        these_keys = row
                        first_row = False
                    else:
                        print("Importing {}".format(row[1]))
                        this_place = dict(zip(these_keys, row))
                        found_it = Place.objects.filter(number=this_place['Store #'])
                        print(found_it)
                        if len(found_it) == 1:
                            this_place_model = found_it[0]
                        else:
                            this_place_model = Place()
                        if '-' in this_place['Zip']:
                            the_zip = (this_place['Zip'].split("-"))[0]
                        this_place_model.name = this_place['Store Name']
                        this_place_model.number = str(this_place['Store #'])
                        this_place_model.address_line1 = this_place['Address']
                        this_place_model.city = this_place['City']
                        this_place_model.state = this_place['St/Prov']
                        this_place_model.zip = the_zip
                        this_place_model.save()
                    print(row)
            #     if not csv_file.name.endswith('.csv'):
            #         messages.error(request,'File is not CSV type')
            #         return HttpResponseRedirect(reverse("myapp:upload_csv"))
            #     # if file is to large, return
            #     if csv_file.multiple_chunks():
            #         messages.error(request,"Uploaded file is to big (%.2f MB)." % (csv_file.size/(1000*1000),))
            #         return HttpResponseRedirect(reverse("myapp:upload_csv"))
            #     file_data = csv_file.read().decode("utf-8")
            #     lines = file_data.split("\n")
            #     # loop over the lines and save them in the db. If error, store as string and then display
            #     for line in lines:
            #         fields = line.split(",")
            #         data_dict = {}
            #         data_dict["name"] = fields[0]
            #         data_dict["start_date_time"] = fields[1]
            #         data_dict["end_date_time"] = fields[1]
            #         data_dict["notes"] = fields[1]
            #         try:
            #             form = EventsForm(data_dict)
            #             if form.is_valid():
            #                 form.save()
            #             else:
            #                 logging.getLogger("error_logger").error(form.errors.as_json())
            #         except Exception as e:
            #             logging.getLogger("error_logger").error(form.errors.as_json())
            #             pass
            # except Exception as e:
            #     logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
            #     messages.error(request, "Unable to upload file. "+repr(e))
            # return HttpResponseRedirect(reverse("myapp:upload_csv"))
    else:
        places_import_form_data = places_import_form()
    context = {
        'message': output,
        'places_import_form_data': places_import_form_data,
    }
    return render(request, 'coreapps/place_import.html', context)


def place_form(request):
    output = "new place page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        place_form_data = place_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if place_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            place_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/places/')
    else:
        place_form_data = place_model_form()
    context = {
        'message': output,
        'place_form_data': place_form_data,
    }
    return render(request, 'coreapps/place_form.html', context)


def place_detail(request, place_id):
    try:
        this_place = Place.objects.get(pk=place_id)
    except Place.DoesNotExist:
        raise Http404("Place does not exist")
    return render(request, 'coreapps/place_detail.html', {'place': this_place})


def lifecycle_home(request):
    output = "this is the 'lifecycle' to live"
    context = {
        'message': output,
    }
    return render(request, 'coreapps/lifecycle.html', context)


def departments_home(request):
    output = "these are the 'departments' to know"
    all_departments = Department.objects.all()
    print(all_departments)
    context = {
        'message': output,
        'all_departments': all_departments,
    }
    return render(request, 'coreapps/department.html', context)


def department_form(request):
    output = "new department page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        department_form_data = department_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if department_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            department_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/department/')
    else:
        department_form_data = department_model_form()
    context = {
        'message': output,
        'department_form_data': department_form_data,
    }
    return render(request, 'coreapps/department_form.html', context)


def department_detail(request, department_id):
    try:
        this_department = Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        raise Http404("Department does not exist")
    return render(request, 'coreapps/department_detail.html', {'department': this_department})


def companies_home(request):
    output = "these are the 'companies' to know"
    all_companies = Company.objects.all()
    print(all_companies)
    context = {
        'message': output,
        'all_companies': all_companies,
    }
    return render(request, 'coreapps/company.html', context)


def company_form(request):
    output = "new company page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        company_form_data = company_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if company_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            company_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/company/')
    else:
        company_form_data = company_model_form()
    context = {
        'message': output,
        'company_form_data': company_form_data,
    }
    return render(request, 'coreapps/company_form.html', context)


def company_detail(request, company_id):
    try:
        this_company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")
    return render(request, 'coreapps/company_detail.html', {'company': this_company})


def things_home(request):
    output = "these are the 'things' to have"
    all_things = Thing.objects.all()
    print(all_things)
    context = {
        'message': output,
        'all_things': all_things,
    }
    return render(request, 'coreapps/thing.html', context)


def thing_form(request):
    output = "new thing page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        thing_form_data = thing_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if thing_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            thing_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/things/')
    else:
        thing_form_data = thing_model_form()
    context = {
        'message': output,
        'thing_form_data': thing_form_data,
    }
    return render(request, 'coreapps/thing_form.html', context)


def thing_detail(request, thing_id):
    try:
        this_thing = Thing.objects.get(pk=thing_id)
    except Thing.DoesNotExist:
        raise Http404("Thing does not exist")
    return render(request, 'coreapps/thing_detail.html', {'thing': this_thing})


def kbs_home(request):
    output = "this is the 'kb' to know"
    all_kbs = KbArticle.objects.all()
    print(all_kbs)
    context = {
        'message': output,
        'all_kbs': all_kbs,
    }
    return render(request, 'coreapps/kb.html', context)


def kb_form(request):
    output = "new kb page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        kb_form_data = kb_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if kb_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            kb_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/kb/')
    else:
        kb_form_data = kb_model_form()
    context = {
        'message': output,
        'kb_form_data': kb_form_data,
    }
    return render(request, 'coreapps/kb_form.html', context)


def kb_detail(request, kb_id):
    try:
        this_kb = KbArticle.objects.get(pk=kb_id)
    except KbArticle.DoesNotExist:
        raise Http404("KbArticle does not exist")
    return render(request, 'coreapps/kb_detail.html', {'kb': this_kb})


def notes_home(request):
    output = "these are the 'notes' to read"
    all_notes = Note.objects.all()
    print(all_notes)
    context = {
        'message': output,
        'all_notes': all_notes,
    }
    return render(request, 'coreapps/note.html', context)


def note_form(request):
    output = "new note page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        note_form_data = note_model_form(request.POST, request.FILES)
        # check whether it's valid:
        if note_form_data.is_valid():
            # process the data in the form.cleaned_data as required.
            # ...
            note_form_data.save()
            # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
            # redirect to a new URL:
            return HttpResponseRedirect('/coreapps/notes/')
    else:
        note_form_data = note_model_form()
    context = {
        'message': output,
        'note_form_data': note_form_data,
    }
    return render(request, 'coreapps/note_form.html', context)


def note_detail(request, note_id):
    try:
        this_note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'coreapps/note_detail.html', {'note': this_note})


def links_home(request):
    output = "these are the 'links' to click click clickity"
    all_links = Linker.objects.all()
    context = {
        'message': output,
        'all_links': all_links,
    }
    return render(request, 'coreapps/link.html', context)


def link_form(request):
    output = "new link page"
    all_links = Linker.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with the data from the request:
        print(request.POST)
        if request.POST['task'] == 'delete':
            this_link = Linker.objects.get(pk = request.POST['link_id'])
            this_link.delete()
        elif request.POST['task'] == 'edit':
            this_link = Linker.objects.get(pk = request.POST['link_id'])
            link_id = request.POST['link_id']
            link_form_data = link_model_form(instance=this_link)
            context = {
                'message': output,
                'link_form_data': link_form_data,
                'link_id': link_id,
                'all_links': all_links,
            }
            return render(request, 'coreapps/link_form.html', context)
        else:
            link_form_data = link_model_form(request.POST, request.FILES)
            # check whether it's valid:
            if link_form_data.is_valid():
                # process the data in the form.cleaned_data as required.
                # ...
                link_form_data.save()
                # examples are fun
                # subject = form.cleaned_data['subject']
                # message = form.cleaned_data['message']
                # sender = form.cleaned_data['sender']
                # cc_myself = form.cleaned_data['cc_myself']
                #
                # recipients = ['info@example.com']
                # if cc_myself:
                #     recipients.append(sender)
                #
                # send_mail(subject, message, sender, recipients)
                # redirect to a new URL:
        return HttpResponseRedirect('/coreapps/links/')
    else:
        link_form_data = link_model_form()
    context = {
        'message': output,
        'link_form_data': link_form_data,
        'all_links': all_links,
    }
    return render(request, 'coreapps/link_form.html', context)


def link_detail(request, link_id):
    try:
        this_link = Linker.objects.get(pk=link_id)
        all_links = Linker.objects.all()
        context = {
            'all_links': all_links,
            'link': this_link,
        }
    except Linker.DoesNotExist:
        raise Http404("Linker does not exist")
    return render(request, 'coreapps/link_detail.html', context)


def groups_home(request):
    output = "these are the 'groups' to be in"
    all_groups = Group.objects.all()
    print(all_groups)
    context = {
        'message': output,
        'all_groups': all_groups,
    }
    return render(request, 'coreapps/group.html', context)


def group_form(request, group_id=None):
    output = "new group page"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if not group_id == None:
            question = get_object_or_404(Question, pk=question_id)
            group_form_data = group_model_form(instance=question)
            # check whether it's valid:
            if group_form_data.is_valid():
                # process the data in the form.cleaned_data as required.
                # ...
                question.name = request.POST['name']
                question.save()
                # examples are fun
                    # subject = form.cleaned_data['subject']
                    # message = form.cleaned_data['message']
                    # sender = form.cleaned_data['sender']
                    # cc_myself = form.cleaned_data['cc_myself']
                    #
                    # recipients = ['info@example.com']
                    # if cc_myself:
                    #     recipients.append(sender)
                    #
                    # send_mail(subject, message, sender, recipients)
                    # redirect to a new URL:
                return HttpResponseRedirect('/coreapps/groups/')
        else:
            # create a form instance and populate it with the data from the request:
            group_form_data = group_model_form(request.POST, request.FILES)
            # check whether it's valid:
            if group_form_data.is_valid():
                # process the data in the form.cleaned_data as required.
                # ...
                group_form_data.save()
                # examples are fun
                    # subject = form.cleaned_data['subject']
                    # message = form.cleaned_data['message']
                    # sender = form.cleaned_data['sender']
                    # cc_myself = form.cleaned_data['cc_myself']
                    #
                    # recipients = ['info@example.com']
                    # if cc_myself:
                    #     recipients.append(sender)
                    #
                    # send_mail(subject, message, sender, recipients)
                    # redirect to a new URL:
                return HttpResponseRedirect('/coreapps/groups/')
    else:
        if not group_id == None:
            this_group = Group.objects.get(pk=group_id)
            group_form_data = group_model_form(instance=this_group)
        else :
            group_form_data = group_model_form()
    context = {
        'message': output,
        'group_form_data': group_form_data,
    }
    return render(request, 'coreapps/group_form.html', context)


def group_detail(request, group_id):
    try:
        this_group = Group.objects.get(pk=group_id)
    except Group.DoesNotExist:
        raise Http404("Group does not exist")
    return render(request, 'coreapps/group_detail.html', {'group': this_group})
