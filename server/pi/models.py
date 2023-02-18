from django.db import models
from django.utils import timezone
import humanize
from django.utils.safestring import mark_safe
import os


# from pi.storage import OverwriteStorage
# Create your models here.
def image_path(instance, filename):
    return os.path.join('last_images', str(instance.id), 'image.jpg')


class PiDevice(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    # remote_status = models.CharField(max_length=100, default='offline')
    # remote_status_updated = models.DateTimeField(null=True)
    # remote_last_image_url = models.CharField(max_length=100, blank=True, null=True)
    # I added blank True and null True
    remote_last_image = models.ImageField(upload_to=image_path, blank=True, null=True)  # , storage=OverwriteStorage())

    remote_last_image_updated = models.DateTimeField(null=True)
    # is_socket_connected = models.BooleanField(default=False)
    socket_status_updated = models.DateTimeField(null=True)
    cec_hdmi_status = models.CharField(max_length=100, default='unknown')
    group_channel_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name or self.device_id

    def is_socket_connected_live(self):
        return self.group_channel_name

    is_socket_connected_live.short_description = 'socket connected'

    # is_socket_connected_live.boolean = True

    def send_reboot(self):
        try:
            channel_name = 'chat_' + self.device_id
            from .consumers import send_reboot_to_channel
            send_reboot_to_channel(channel_name)
            return True
        except Exception as e:
            print(e)
            return False

    def tv_admin_link(self):
        # /admin/tv/tv/1/change/
        if self.tv:
            return mark_safe(u'<a href="/admin/tv/tv/%s/change/">%s</a>' % (self.tv.id, self.tv))
        else:
            return ''

    # def save(self, *args, **kwargs):
    #     try:
    #         this = TvDevice.objects.get(id=self.id)
    #         if this.remote_last_image != self.remote_last_image:
    #             this.remote_last_image.delete()
    #     except: pass
    #     super(TvDevice, self).save(*args, **kwargs)

    def humanize_remote_status_updated_ago(self):
        return humanize.naturaltime(timezone.now() - self.remote_status_updated)

    humanize_remote_status_updated_ago.short_description = 'status updated'

    def humanize_socket_status_updated_ago(self):
        return humanize.naturaltime(timezone.now() - self.socket_status_updated)

    humanize_socket_status_updated_ago.short_description = 'socket connection updated'

    def image_tag(self):
        return mark_safe(u'<img src="%s" width="150px" height="150px" />' % self.remote_last_image.url)

# class OpenSocketConnections(models.Model):
#     device = models.OneToOneField(PiDevice, on_delete=models.CASCADE, primary_key=True, related_name='open_socket_connection')
#     channel_name = models.CharField(max_length=100, null=True)
#     def __str__(self):
#         return self.device.name or self.device.device_id

#     def get_device_uid(self):
#         return self.device.device_id
