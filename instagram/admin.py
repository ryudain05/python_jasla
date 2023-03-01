from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

# 장고 어드민
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'created_at', 'updated_at'] #어드민 페이지 컬럼
    list_display_links = ['message'] #링크를 어느 컬럼에 놓을지
    search_fields = ['message'] # 검색

    def photo_tag(self,post): #어드민이 알아서 호출
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width:72px"/>')
        return None

    def message_length(self,post):
        return f"{len(post.message)} 글자"
#admin.site.register(Post, PostAdmin)