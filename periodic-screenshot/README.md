# Periodic Screenshot

This plugin enables to set a fixed time interval in which a screenshot of the current scene in Catana will be taken and downloaded.
Thus, it can be used to easily document the work, backup what was seen in the scene, or to record performed actions later used as an image input for simple animations or movies.

## How to Use
1. Install/load this plugin
2. Open plugin's properties window (Plugins – Periodic Screenshot Properties) and set your desired settings
3. Go to Plugin Management and find script *periodic-screenshot.jspy* belonging to this plugin.
4. Attach this script to the update call.
5. Done :)
    - If you want to stop the screenshots from being generated, detach the script above
    - To change the plugin properties, use again the modal window mentioned above

## Additional information
The plugin creates two important shared variables in the background:  
1. scr_interval – defines the number of seconds to wait between taking the screenshots  
2. scr_transparent – sets if the screenshot should be taken with the transparent background ("true") or not ("false")  
