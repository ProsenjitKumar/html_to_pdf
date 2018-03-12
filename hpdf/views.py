from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View


# Create your views here.
from hpdf.utils import render_to_pdf


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        context = {
            'invoice_id': 91199,
            'customer_name': 'Prosenjit Kumar',
            'amount': 99.21,
            'today': "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Prosenjit_%s.pdf" % "Kumar"
            content = "inline; filename = '%s' " % filename
            download = request.GET.get("download")
            if download:
                content = "attachment; filename = '%s' " % filename
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")
