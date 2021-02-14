header = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <script type="text/javascript" src="js/jquery-3.5.1.min.js"></script>
    <script type="text/javascript" src="js/modernizr.custom.js"></script>
    <link rel="preconnect" href="https://fonts.gstatic.com"> 
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/bookblock.css" />
    <link rel="stylesheet" href="css/style.css" />
   
  </head>
  <body>
    <div class="gridbody">
      <div class="logo">
        <a href="" >
          <img src="images/logo.png" class="rounded" alt="">
        </a>
      </div>
      <div class="library">
        <a href="index.html" >
          <img src="images/library.jpg" class="rounded" alt="">
        </a>
      </div>
"""

      <div id="bb-bookblock" class="bb-bookblock">
        <div class="bb-item"> <img src="images/clever_kalyani/00.png"/></div>
  
    </div>
      
    <script type="text/javascript" src="js/jquerypp.custom.js"></script>
    <script type="text/javascript" src="js/jquery.bookblock.js"></script>
    
    <script>
      var Page = (function() {
        var oldau = null;
        var aualerted = false;
        var playAudio = function(old, page, isLimit) {
          if (isLimit) {return false;}
          url = page <= 9 ? "0" + page : "" + page;
          url = "audio/clever_kalyani/" + url + ".mp3";
          var au = new Audio(url);
          au.addEventListener("canplaythrough", event => {
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
        }
        playAudio(0, 0, false); // Cover page
        var config = {
            $bookBlock : $( '#bb-bookblock' ),
            // $navNext : $( '#bb-nav-next' ),
            // $navPrev : $( '#bb-nav-prev' ),
            // $navFirst : $( '#bb-nav-first' ),
            // $navLast : $( '#bb-nav-last' )
          },
          init = function() {
            config.$bookBlock.bookblock( {
              speed : 500,
              shadowSides : 0.8,
              shadowFlip : 0.7,
              onEndFlip: playAudio
            } );
            initEvents();
          },
          initEvents = function() {
            var $slides = config.$bookBlock.children();
            $slides.each( function(i) {
              var img = this;
              this.onclick = function(e) {
                if (e.offsetX > e.target.width/2) {
                  config.$bookBlock.bookblock( 'next' );
                } else {
                  config.$bookBlock.bookblock( 'prev' );
                }
              }
            });
            
                          
            // add keyboard events
            $( document ).keydown( function(e) {
              var keyCode = e.keyCode || e.which,
                arrow = {
                  left : 37,
                  up : 38,
                  right : 39,
                  down : 40
                };

              switch (keyCode) {
                case arrow.left:
                  config.$bookBlock.bookblock( 'prev' );
                  break;
                case arrow.right:
                  config.$bookBlock.bookblock( 'next' );
                  break;
              }
            } );
          };

          return { init : init };
  
        })();
      </script>
      <script>
          Page.init();
      </script>
      
  </body>
</html>
