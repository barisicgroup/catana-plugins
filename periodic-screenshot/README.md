# Periodic Screenshot

This plugin enables to set a fixed time interval in which a screenshot of the current scene in Catana will be taken and downloaded.
Thus, it can be used to easily document the work, backup what was seen in the scene or record performed actions to be used as an image input for simple animations or movies.

## How to Use
1. Install/load this plugin
2. Attach the plugin to the update call  
The first time the plugin is run, you will be prompted to provide your input regarding the time interval and usage of transparency.
3. Done :)

## Additional information
The plugin creates two important global variables in the background:  
1. scr_interval – defines the number of seconds to wait between taking the screenshots  
2. scr_transparent – sets if the screenshot should be taken with the transparent background ("true") or not ("false")  
If you want to run plugin repeatedly but change these properties, modify the values of these variables directly.
