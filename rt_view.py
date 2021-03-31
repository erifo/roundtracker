from dearpygui import core, simple
from rt_model import RTModel

class RTView:
    def __init__(self):
        self.model = RTModel()
        self.timefactors = {
            "Hours" : 600,
            "Minutes" : 10,
            "Rounds" : 1
        }

    def __add_effect(self):
        name = core.get_value("##new_effect_name")
        #---
        duration_string = core.get_value("##new_effect_duration")
        if (name == "" or duration_string == ""):
            return
        duration = int(duration_string)
        #---
        timefactor_string = core.get_value("##new_effect_timefactor")
        timefactor = self.timefactors[timefactor_string]
        #---
        self.model.add_effect(name, int(duration)*timefactor)
        self.model.save()

    def __remove_effect(self):
        index = core.get_value("##effect_list")
        try:
            self.model.remove_effect(index)
            self.model.save()
        except:
            return

    def __tick(self):
        duration_string = core.get_value("##tick_duration")
        if (duration_string == ""):
            return
        duration = int(duration_string)
        #---
        timefactor_string = core.get_value("##tick_timefactor")
        timefactor = self.timefactors[timefactor_string]
        #---
        mode_string = core.get_value("##tick_mode")
        mode = -1
        if (mode_string == "Up"):
            mode = 1
        #---
        self.model.tick_effects(mode*timefactor*duration)
        self.model.save()
        

    def __render(self):
        core.configure_item("##effect_list", items=self.model.effects_to_strings())

    def show(self):
        with simple.window("Main Window"):
            core.set_main_window_size(480, 350)
            core.set_main_window_resizable(False)
            core.set_main_window_title("Roundtracker")
            #---
            core.add_group("##group_new_effect", horizontal=True)
            core.add_input_text("##new_effect_duration", decimal=True, hint="Duration", width=75)
            core.add_combo("##new_effect_timefactor", items=['Hours', 'Minutes', 'Rounds'], default_value="Rounds", width=75)
            core.add_input_text("##new_effect_name", hint="New effect name", width=200)
            core.end()
            #---
            core.add_group("##group_addremove", horizontal=True)
            core.add_button("Add effect", callback=self.__add_effect)
            core.add_button("Remove selected", callback=self.__remove_effect)
            core.end()
            #---
            core.add_separator()
            core.add_text("Hrs".ljust(10) + "Min".ljust(10) + "Rnd".ljust(10) + "Effect")
            core.add_listbox('##effect_list', width=425, num_items=11)
            #core.add_table('Effects', ['Hours','Minutes','Rounds','Names'], height=200, width=500)
            core.add_separator()
            #---
            core.add_group("##group_bottom", horizontal=True)
            core.add_input_text("##tick_duration", decimal=True, hint="Duration", width=75, default_value="1")
            core.add_combo("##tick_timefactor", items=['Hours', 'Minutes', 'Rounds'], default_value="Rounds", width=75)
            core.add_combo("##tick_mode", items=['Up', 'Down'], default_value="Down", width=75)
            core.add_button("Tick", callback=self.__tick)
            core.end()

            # Render Callback and Start gui
            core.set_render_callback(self.__render)
        core.start_dearpygui(primary_window="Main Window")