def reprova_comentarios(modeladmin, request, queryset):
    queryset.update(Aprovado=False)

def aprova_comentarios(modeladmin, request, queryset):
    queryset.update(Aprovado=True)

reprova_comentarios.short_description = 'Reprovar comentarios'
aprova_comentarios.short_description = 'Aprovar comentarios'