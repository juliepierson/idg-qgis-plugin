from idg.toolbelt.tree_node_factory import download_default_idg_list, download_all_config_files
from idg.toolbelt import PlgOptionsManager, PluginGlobals

import json
import os.path

class RemotePlatforms:
    def __init__(self):
        with open(os.path.join(PluginGlobals.instance().config_dir_path,'default_idg.json')) as f : #Télécharger si non existant ?
            self.stock_idgs = json.load(f)
        self.custom_idg = PlgOptionsManager().get_plg_settings().custom_idgs.split(',')
        #TOFIX supprimer empty string de custom_idg
        pass

    def url_all(self):
        return self.url_stock() + self.url_custom()

    def url_custom(self):
        return self.custom_idg

    def url_stock(self):
        return list(self.stock_idgs.values())

    def reset(self):
        rep = PluginGlobals.instance().config_dir_path
        for fichier in os.listdir(rep):
            chemin_fichier = os.path.join(rep, fichier)
            if fichier != 'default_idg.json':
                if os.path.isfile(chemin_fichier):
                    os.remove(chemin_fichier)

        download_default_idg_list()
        download_all_config_files(RemotePlatforms().url_all())
        #TODO remove all local files (projects & images)