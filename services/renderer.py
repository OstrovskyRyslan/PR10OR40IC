class Renderer:
    objects_to_render = [] 
    @classmethod
    def add_object(cls, obj):
        cls.objects_to_render.append(obj)
    @classmethod
    def remove_object(cls, index):
        if 0 <= index < len(cls.objects_to_render):
            cls.objects_to_render.pop(index)
    @classmethod
    def render_all(cls):
        for obj in cls.objects_to_render:
            obj.draw_player()
