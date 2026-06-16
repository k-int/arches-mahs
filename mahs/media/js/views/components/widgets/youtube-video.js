define(["knockout", "underscore", "viewmodels/widget", "arches", "templates/views/components/widgets/youtube-video.htm"], function (
  ko,
  _,
  WidgetViewModel,
  arches,
  youTubeWidgetTemplate
) {
  /**
   * registers a text-widget component for use in forms
   * @function external:"ko.components".text-widget
   * @param {object} params
   * @param {string} params.value - the value being managed
   * @param {function} params.config - observable containing config object
   * @param {string} params.config().label - label to use alongside the text input
   * @param {string} params.config().placeholder - default text to show in the text input
   */

    const viewModel = function (params) {
      WidgetViewModel.apply(this, [params]);
      var that = this;

      //Bind YoutubeUrl to entered short url
      that.YoutubeUrl = that.value();

      if (that.YoutubeUrl !== null) {
        // e.g. https://www.youtu.be/ArCLT4ds0Yc --> https://www.youtube.com/embed/ArCLT4ds0Yc
        // multiple types of youtube video URLs https://gist.github.com/rodrigoborgesdeoliveira/987683cfbfcc8d800192da1e73adc486

        startUrl = "https://www.youtube.com/embed/";

        // regex to match most variations of youtube URLs
        // https://gist.github.com/rodrigoborgesdeoliveira/987683cfbfcc8d800192da1e73adc486?permalink_comment_id=4342805#gistcomment-4342805
        const regexpUrlMatch = /(?<=[=\/&])[a-zA-Z0-9_\-]{11}(?=[=\/&?#\n\r]|$)/
        const extractedID = that.YoutubeUrl.match(regexpUrlMatch)

        extractedID ? that.YoutubeUrl = startUrl + extractedID[0] : that.YoutubeUrl = startUrl // Combine embed link with video ID
      }
    };

    return ko.components.register("youtube-video", {
        viewModel: viewModel,
        template: youTubeWidgetTemplate
  });
});