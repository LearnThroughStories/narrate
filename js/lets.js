var Page = (function () {
  var oldau = null;
  var aualerted = false;
  var playAudio = function (old, page, isLimit) {
    if (isLimit) {
      return false;
    }
    url = page <= 9 ? "0" + page : "" + page;
    url = "audio/clever_kalyani/" + url + ".mp3";
    var au = new Audio(url);
    au.addEventListener("canplaythrough", (event) => {
      try {
        if (oldau) {
          oldau.pause();
        }
        au.play();
        oldau = au;
      } catch (e) {
        if (!aualerted) {
          alert("Please enable automatic audio play");
          aualerted = true;
        }
      }
    });
  };
  playAudio(0, 0, false); // Cover page
  var config = {
      $bookBlock: $("#bb-bookblock"),
      // $navNext : $( '#bb-nav-next' ),
      // $navPrev : $( '#bb-nav-prev' ),
      // $navFirst : $( '#bb-nav-first' ),
      // $navLast : $( '#bb-nav-last' )
    },
    init = function () {
      config.$bookBlock.bookblock({
        speed: 500,
        shadowSides: 0.8,
        shadowFlip: 0.7,
        onEndFlip: playAudio,
      });
      initEvents();
    },
    initEvents = function () {
      var $slides = config.$bookBlock.children();
      $slides.each(function (i) {
        var img = this;
        this.onclick = function (e) {
          if (e.offsetX > e.target.width / 2) {
            config.$bookBlock.bookblock("next");
          } else {
            config.$bookBlock.bookblock("prev");
          }
        };
      });

      // add keyboard events
      $(document).keydown(function (e) {
        var keyCode = e.keyCode || e.which,
          arrow = {
            left: 37,
            up: 38,
            right: 39,
            down: 40,
          };

        switch (keyCode) {
          case arrow.left:
            config.$bookBlock.bookblock("prev");
            break;
          case arrow.right:
            config.$bookBlock.bookblock("next");
            break;
        }
      });
    };

  return { init: init };
})();
