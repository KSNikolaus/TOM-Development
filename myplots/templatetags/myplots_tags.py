from plotly import offline
import plotly.graph_objs as go
from django import template

from tom_targets.models import Target

register = template.Library()


@register.inclusion_tag('myplots/targets_reduceddata.html')
def targets_reduceddata(targets=Target.objects.all()):
# order targets by creation date
    targets = targets.order_by('-created')
    # x axis: target names. y axis: datum count
    data = [go.Bar(
        x=[target.name for target in targets],
        y=[target.reduceddatum_set.count() for target in targets]
    )]
    # Create the plot
    figure = offline.plot(go.Figure(data=data), output_type='div', show_link=False)
    # Add plot to the template context
    return {'figure': figure}
