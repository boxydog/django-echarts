"""
The file is generated by django-echarts {{ version }}.
Now you can add site urls to the entry urlpatterns in project urls.py.
Example:
    urlpatterns = [
        # Other urlpatterns
        path('', site_obj.urls),
    ]

"""
from django_echarts.starter.widgets import Copyright
from django_echarts.starter.sites import DJESite{% if view_type == 'cbv' %}, DJESiteDetailView{% endif %}

__all__ = ['site_obj']

site_obj = DJESite(
    site_title='{{ site_title }}'
)

site_obj.add_widgets(
    copyright_=Copyright(start_year={{ start_year }}, powered_by='{{ powered_by }}')
)

@site_obj.register_chart
def mychart():
    # Write your pyecharts here.
    # This method must return an object of pycharts.charts.Chart
    pass