use strict;

my $header = <<'__HEADER';
<!DOCTYPE html>
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
__HEADER

my $bookname = shift(@ARGV);
$bookname =~ s{/$}{};  # Get rid of trailing '/' if any
$bookname =~ s{^.*/}{}; # Get rid of basename. "images/CleverKalyani/" becomes "CleverKalyani"

my $title = `cat "images/$bookname/title.txt"`;
chomp($title);

print ($header);
print ("      <div class = 'title'>$title</div>\n");
print ("      <div id='bb-bookblock' class='bb-bookblock'>\n");
for (my $i= 0; $i < 30; $i++) {
    # prefer png to jpg if same file.
    # quit the loop if neither found
    my $file = sprintf("images/$bookname/%02d.png", $i);

    if (! -e $file) {
      $file = sprintf("images/$bookname/%02d.jpg", $i);
      last if (! -e $file);
    } 
    print("        <div class=\"bb-item\"> <img src=\"$file\"/></div>\n");
}
print ("      </div>\n");

my $footer = <<"__FOOTER";
    <script type="text/javascript" src="js/jquerypp.custom.js"></script>
    <script type="text/javascript" src="js/jquery.bookblock.js"></script>
    <script type="text/javascript" src="js/lets.js"></script>
    <script>
      Page().init("$bookname");
    </script>
  </body>
</html>
__FOOTER

print ($footer);
