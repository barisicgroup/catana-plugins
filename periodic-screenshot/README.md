# Periodic Screenshot

This plugin enables to set a fixed time interval in which a screenshot of the current scene in Catana will be taken and downloaded.
Thus, it can be used to easily document the work, backup what was seen in the scene or record performed actions to be used as an image input for simple animations or movies.

## How to Use
1. Install/load this plugin
2. Create two global variables:  
  a. scr_interval – defines the number of seconds to wait between taking the screenshots  
  b. scr_transparent – sets if the screenshot should be taken with the transparent background ("true") or not ("false")  
  *Note: if the variables are not created, plugin fallbacks to 60-second interval and transparent background.*   
3. Attach the plugin to the update call
4. Done :)
