import justpy as jp

alert_dialog_html = """
<div class="q-pa-md q-gutter-sm">
    <q-btn label="Alert" color="primary" name="alert_button" />
    <q-dialog name="alert_dialog" persistent>
      <q-card>
        <q-card-section>
          <div class="text-h6">Alert</div>
        </q-card-section>

        <q-card-section>
          Please enter your name
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="OK" color="primary" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
</div>
"""

seamless_dialog_html = """
<div class="q-pa-md q-gutter-sm">
    <q-btn label="Open seamless Dialog" color="primary" name="seamless_button" />

    <q-dialog seamless position="bottom" name="seamless_dialog">
      <q-card style="width: 350px">
        <q-linear-progress :value="0.6" color="pink" />

        <q-card-section class="row items-center no-wrap">
          <div>
            <div class="text-weight-bold">The Walker</div>
            <div class="text-grey">Fitz & The Tantrums</div>
          </div>

          <q-space />

          <q-btn flat round icon="play_arrow" />
          <q-btn flat round icon="pause" />
          <q-btn flat round icon="close" v-close-popup />
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
"""


def open_dialog(self, msg):
    self.dialog.value = True

def dialog_test():
    wp = jp.QuasarPage()

    c = jp.parse_html(alert_dialog_html, a=wp)
    c.name_dict["alert_button"].dialog = c.name_dict["alert_dialog"]
    c.name_dict["alert_button"].on('click', open_dialog)

    c = jp.parse_html(seamless_dialog_html, a=wp)
    c.name_dict["seamless_button"].dialog = c.name_dict["seamless_dialog"]
    c.name_dict["seamless_button"].on('click', open_dialog)

    return wp

jp.justpy(dialog_test)