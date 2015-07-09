# -*- coding: utf-8 -*-


from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from modulhandbuch.models import *

import re

# Option with easy_select2:
from easy_select2 import select2_modelform

## a basic admin to add ownership

class OwnedAdmin(admin.ModelAdmin):

    def __init__(self, *args, **kwargs):
        res = super(OwnedAdmin, self).__init__(*args, **kwargs)

        # self.realInlines = self.inlines

        # construct the field names to show:
        tmp = [f.name for f in self.model._meta.fields]
        try:
            tmp.remove('id')
            tmp.remove('owner')
            tmp.remove('namedentity_ptr')
            tmp.remove('slug')
        except:
            # not all fields might be in all modules,
            # but that is not a problem
            pass
        self.fields = tmp

        return res

    def get_queryset(self, request):
        qs = super(OwnedAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        self.message_user(request,
                          u"EDIT wird nur bei Einträgen angezeigt, die Sie editieren dürfen!")

        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        # print "--------------"
        # print "in save_model: ", obj, obj.owner, change, request.user

        if (change is False) or (obj.owner is None):
            obj.owner = request.user
        obj.save()

    # TODO:
    # die folgenden Funktionen werden eigentlich nicht gebraucht,
    # wenn über get_queryset auf owner eingeschröänkt wird.
    # Es kann trotzdem nicht schaden, falls jemand direkt die URL manipuliert
    # es fehlt hier noch die has_change_permission!

    def has_delete_permission(self, request, obj=None):
        print "has delete: ", obj, request.user, request.user.is_superuser
        if obj:
            if ((request.user.is_superuser) or
                (obj.owner == request.user)):
                return True

        return False

    def get_readonly_fields(self, request, obj=None):
        print "grof: ", request, request.user, obj, obj.owner if obj else "N/A"

        tmp = self.readonly_fields
        print "readonly: ", tmp

        if (obj
            and not (obj.owner == request.user)
            and not request.user.is_superuser):
            print "setting fields readonly"
            # then add further read-only fields, actually, all of them
            # tmp = tmp + self.not_owner_readonly_fields
            tmp = list(tmp) + [f.name for f in self.model._meta.fields]

            # show a message here?
            self.message_user(request,
                              u"Sie dürfen diesen Eintrag nicht editieren!",
                              )

        print "readonly_fields: ", tmp
        return tmp

    # attempt to get the inlines as read-only as well:

    # def get_formsets_with_inlines(self, request, obj=None):
    #     for inline in self.get_inline_instances(request, obj):
    #         yield inline.get_formset(request, obj), inline

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     obj = self.model.objects.get(pk=object_id)
    #     print "in change_veiw ", obj

    #     # if obj and not (obj.owner == request.user):
    #     #     print "disable editing of inlines"
    #     #     self.inlines = []

    #     return super(OwnedAdmin, self).change_view(request,
    #                                                object_id,
    #                                                form_url, extra_context)

    # override the HttpResponse hooks:
    def my_response_url(self, request, obj):
        # redirect back to the survey page for this model
        try:
            urlname = obj.__class__.__name__.lower() + "List"
            url = reverse(urlname)
        except:
            # this exception should only happen if the url names
            # dont match the expected patterns
            url = reverse("modulhandbuchansehen")

        return url

    def response_change(self, request, obj):
        if '_continue' not in request.POST:
            return HttpResponseRedirect(self.my_response_url(request, obj))
        else:
            return super(OwnedAdmin, self).response_change(request, obj)

    def response_delete(self, request, obj_display, obj_id):

        if '_continue' not in request.POST:
            # since no object exists, it is harder to find out the class
            # let's detour via the URL 
            r = re.match('.*/modulhandbuch/([^/]*)/.*', request.path)
            urlname = r.group(1) + 'List'
            return HttpResponseRedirect(reverse(urlname))
        else:
            return super(OwnedAdmin, self).response_delete(request,
                                                       obj_display, obj_id) 

    def response_add(self, request, obj, post_url_continue=None):
        if '_continue' not in request.POST:
            return HttpResponseRedirect(self.my_response_url(request, obj))
        else:
            return super(OwnedAdmin, self).response_add(request,
                                                        obj, post_url_continue)

ModulForm = select2_modelform(Modul, attrs={'width': '250px'})



#########################################################
# inlines that understand whether they should be editable

class OwnedInline(admin.TabularInline):

    pass


class ModulLVInline(OwnedInline):
    model = VeranstaltungsLps
    # TODO: select2_modelform zeigt alle möglichen keys an,
    # in einem ersten select field, das gart nicht angezeigt
    # werden sollte. Das ist ein killer bug :-(

    # form = select2_modelform(VeranstaltungsLps, attrs={'width': '250px'})
    fk_name = "modul"
    fields = ['veranstaltung', 'lp', ]
    readonly_fields = ['modul']
    verbose_name = "Lehrveranstaltung (und LP) in diesem Modul"
    verbose_name_plural = "Lehrveranstaltungen (und LPs) in diesem Modul"

    # def has_delete_permission(self, request, obj=None):
    #     if obj:
    #         print "Modul inlinline: ", request.user, obj, type(obj)
    #         if ((request.user == obj.owner) or
    #             (request.user.is_superuser)):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return True
    #     pass



###############################
# patch the classes together


class ModulAdmin(OwnedAdmin):
    form = ModulForm
    inlines = [ModulLVInline]

    pass


class FocusAreaModulInline(admin.TabularInline):
    model = FocusArea.module.through


class FocusAreaAdmin(admin.ModelAdmin):
    # inlines = [FocusAreaModulInline]
    form = select2_modelform(FocusArea, attrs={'width': '250px'})
    fields = [ 'url', 'nameDe', 'nameEn',
               'module',
               'beschreibungDe', 'beschreibungEn',
               'verantwortlicher']
    pass


class StudiengangFocusAreaInline(admin.TabularInline):
    model = Studiengang.focusareas.through
    verbose_name = "Focus Area dieses Studiengangs"
    verbose_name_plural = "Focus Areas dieses Studiengangs"

class StudiengangModuleInline(admin.TabularInline):
    model = Studiengang.module.through
    verbose_name = "Modul dieses Studiengangs"
    verbose_name_plural = "Module dieses Studiengangs"


class StudiengangAdmin(OwnedAdmin):
    model = Studiengang
    fields = ['nameDe', 'nameEn',
              'url',
              'beschreibungDe', 'beschreibungEn',
              'verantwortlicher',
              'startdateien',
             ]
    inlines = [StudiengangFocusAreaInline,
               StudiengangModuleInline]
    pass


class LehrenderAdmin(OwnedAdmin):
    model = Lehrender


class FachgebietAdmin(OwnedAdmin):
    model = Fachgebiet


class LehreinheitAdmin(OwnedAdmin):
    model = Lehreinheit


class PruefungsformAdmin(OwnedAdmin):
    model = Pruefungsform


class OrganisationsformAdmin(OwnedAdmin):
    model = Organisationsform


class LehrveranstaltungAdmin(OwnedAdmin):
    model = Lehrveranstaltung

admin.site.register(Lehreinheit, LehreinheitAdmin)
admin.site.register(Fachgebiet, FachgebietAdmin)
admin.site.register(Lehrender, LehrenderAdmin)
admin.site.register(Pruefungsform, PruefungsformAdmin)
admin.site.register(Organisationsform, OrganisationsformAdmin)
admin.site.register(Lehrveranstaltung, LehrveranstaltungAdmin)
admin.site.register(Modul, ModulAdmin)
admin.site.register(FocusArea, FocusAreaAdmin)
admin.site.register(Studiengang, StudiengangAdmin)
admin.site.register(TexDateien)
admin.site.register(VeranstaltungsLps)
