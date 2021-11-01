      var pageName;
      var aboutNumber;

      var sketchNames = ["wolfStudy", "horseStudy", "orchid", "nighttime", "pants", "streamArt", "owlHead", "ftcBot", "talons"];
      var minorNames = ["flower", "rhino", "succulent", "quote", "crayonFlower", "tuershen", "polarbear", "blm", "kimpa", "majorFlower", "banff", "aRhino"];
      var majorNames = ["gamutClash"];

      var darkenButton = function(id) {
        document.getElementById(id).style.filter = "brightness(82%)";
      };

      var returnButton = function(id) {
          if (id != pageName) {
            document.getElementById(id).style.filter = "brightness(100%)";
          } else {
            document.getElementById(id).style.filter = "brightness(82%)";
          }
      };
      
      function refreshButton(id) {
        darkenButton(id);
        returnButton(id);
      };

      function switchMain(id) {
        aboutNumber = 0;
        var buttonNames = ["about", "links", "works", "contact"];
        buttonNames = buttonNames.filter(e => e !== id);
        function buttonHideButton() {
          var i = 2;
          while (i > -1) {
            document.getElementById(buttonNames[i]).style.filter = "brightness(100%)";
            i--;
          }
        }
        switch(id) {
          case "about":
            buttonHideButton();
            document.getElementById("back").hidden = false;
            document.getElementById("back").style.marginTop = "0.5rem";
            document.getElementById("forward").hidden = false;
            document.getElementById("email").hidden = true;
            document.getElementById("discord").hidden = true;
            pageName = "about";
            document.getElementById("storm").src = "https://user-images.githubusercontent.com/57303754/134820289-8af52caa-b8b1-49ee-b28b-bdaca4043c0f.png";
            document.getElementById("storm").alt = "(blank space which text is displayed over)";
            document.getElementById("theText").hidden = false;
            document.getElementById("theText").innerHTML = "&emsp;Hi! I'm Gray, a high school student into drawing, coding, and mathematics. My artwork often features various flora and fauna as well as machines and tech.";
            document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/102863112-f9f42c00-43e6-11eb-8b9b-423d3f3df709.png";
            document.getElementById("myName").alt = "gray zhuang";
          break;

          case "links":

            var hideForWorks = ["about", "links", "works", "contact", "storm", "forward", "email", "discord", "theText"];
            var i = 0;
            while (i < hideForWorks.length) {
              document.getElementById(hideForWorks[i]).hidden = true;
              i++;
            }

            document.getElementById("scratch").hidden = false;
            document.getElementById("twitter").hidden = false;
            document.getElementById("instagram").hidden = false;
            document.getElementById("github").hidden = false;

            document.getElementById("back").hidden = false;
            document.getElementById("back").style.marginTop = "1.25rem";
            document.getElementById("linkedPlay").hidden = false;
            document.getElementById("play").hidden = true;

            buttonHideButton();
            pageName = "links";

             document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/103330303-b9fbfd00-4a15-11eb-8510-978c88ee616a.png";
             document.getElementById("myName").alt = "gray zhuang links (level select)";
          break;

          case "works":
            buttonHideButton();
            selectedGallery = 0;

            var hideForWorks = ["about", "links", "works", "contact", "storm", "forward", "email", "discord", "theText"];
            var i = 0;
            while (i < hideForWorks.length) {
              document.getElementById(hideForWorks[i]).hidden = true;
              i++;
            }
            document.getElementById("back").hidden = false;
            document.getElementById("back").style.marginTop = "1.25rem";
            document.getElementById("play").hidden = false;

            document.getElementById("sketchIcon").hidden = false;
            document.getElementById("minorIcon").hidden = false;
            document.getElementById("majorIcon").hidden = false;
            pageName = "works";
            document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/134959636-af53f099-040d-4e83-a9e7-4dea5f97a820.png";
            document.getElementById("myName").alt = "gray zhuang works (level select)";
          break;
                
          case "contact":
            buttonHideButton();
            document.getElementById("theText").hidden = true;
            document.getElementById("back").hidden = false;
            document.getElementById("back").style.marginTop = "0.5rem";
            document.getElementById("forward").hidden = true;
            document.getElementById("email").hidden = false;
            document.getElementById("discord").hidden = false;
            pageName = "contact";
            document.getElementById("storm").src = "https://user-images.githubusercontent.com/57303754/134799044-d0696ad6-0dc2-41c1-868c-51d061f2c698.png";
            document.getElementById("storm").alt = "my email is c190draws@gmail.com and my discord tag is 小王子#0164";
            document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/102863112-f9f42c00-43e6-11eb-8b9b-423d3f3df709.png";
            document.getElementById("myName").alt = "gray zhuang";
          break;
        }
      };

      var levelButtons = ["sketchIcon", "minorIcon", "majorIcon", "scratch", "twitter", "instagram", "github"];

      function returnMain(id) {
        document.getElementById("theLink").href = "#";
        document.getElementById("theLink").target = "";
        var i = 0;
        while (i < levelButtons.length) {
          document.getElementById(levelButtons[i]).style.filter = "brightness(100%)";
              i++;
        }
        if (aboutNumber == 0) {
          document.getElementById("theText").hidden = true;
          document.getElementById("storm").src = "https://user-images.githubusercontent.com/57303754/100564216-3f548c00-3275-11eb-976b-fca49ff1f360.png";
          document.getElementById("storm").alt = "storm pagedoll";
          document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/102863112-f9f42c00-43e6-11eb-8b9b-423d3f3df709.png";
          document.getElementById("myName").alt = "gray zhuang";
          document.getElementById(pageName).style.filter = "brightness(100%)";
          document.getElementById("back").hidden = true;
          document.getElementById("forward").hidden = true;
          document.getElementById("email").hidden = true;
          document.getElementById("discord").hidden = true;
          document.getElementById("sketchIcon").hidden = true;
          document.getElementById("minorIcon").hidden = true;
          document.getElementById("majorIcon").hidden = true;
          document.getElementById("scratch").hidden = true;
          document.getElementById("twitter").hidden = true;
          document.getElementById("instagram").hidden = true;
          document.getElementById("github").hidden = true;
          document.getElementById("play").hidden = true;
          document.getElementById("linkedPlay").hidden = true;
          var showAgain = ["about", "links", "works", "contact", "storm"];
          var i = 0;
          while (i < showAgain.length) {
            document.getElementById(showAgain[i]).hidden = false;
            i++;
          }
          pageName = "index";
        } else if (pageName == "works") {
            var returnElements = ["about", "links", "works", "contact", "storm"];
            var i = 4;
            while (i > -1) {
              document.getElementById(returnElements[i]).hidden = false;
              i--;
            }
            document.getElementById("storm").src = "https://user-images.githubusercontent.com/57303754/100564216-3f548c00-3275-11eb-976b-fca49ff1f360.png";
            document.getElementById("storm").alt = "storm pagedoll";
            document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/102863112-f9f42c00-43e6-11eb-8b9b-423d3f3df709.png";
            document.getElementById("myName").alt = "gray zhuang";
            document.getElementById("works").style.filter = "brightness(100%)";
            pageName = "index";
        } else {
          slideNumbers(id);
        }
      };

      function slideNumbers(id) {
        if (id == "back") {
          aboutNumber--;
          slideChange();
        } else if (id == "forward") {
          if (aboutNumber != 2) {
            aboutNumber++;
            slideChange();
          } else {
              aboutNumber = 0;
              returnMain();
          }
        }
      };

      function slideChange() {
      document.getElementById("storm").src = "https://user-images.githubusercontent.com/57303754/134820289-8af52caa-b8b1-49ee-b28b-bdaca4043c0f.png";
      if (aboutNumber == 0) { 
          document.getElementById("theText").innerHTML = "&emsp;Hi! I'm Gray, a high school student into drawing, coding, and mathematics. My artwork often features various flora and fauna as well as machines and tech.";
          //EDIT HERE
          //document.getElementById("aboutText").style.marginTop = "5.2rem";
        } else if (aboutNumber == 1) {
          document.getElementById("theText").innerHTML = "&emsp;This website was coded without frameworks or templates, but with a substantial amount of coffee. It features graphics drawn with a mouse in Scratch Bitmap and animated with the JS DOM.";
        } else if (aboutNumber == 2) {
          document.getElementById("theText").innerHTML = "&emsp;A major goal of mine is to expand my drawing and coding endeavours to the professional level. But in the meantime, enjoy this project (best viewed on PC!).";
        }
      };

var selectedGallery = 0;

function gallerySelection(id) {
  selectedGallery = id;
  var galleryOptions = ["sketchIcon", "minorIcon", "majorIcon"];
  galleryOptions = galleryOptions.filter(e => e !== id);
  var i = 1;
  while (i > -1) {
    document.getElementById(galleryOptions[i]).style.filter = "brightness(100%)";
    i--;
  }
  document.getElementById(id).style.filter = "brightness(72%)";
};

function linksSelection(id) {
  var linksOptions = ["scratch", "twitter", "instagram", "github"];
  linksOptions = linksOptions.filter(e => e !== id);
  var i = 2;
  while (i > -1) {
    document.getElementById(linksOptions[i]).style.filter = "brightness(100%)";
    i--;
  }
  document.getElementById(id).style.filter = "brightness(72%)";
  document.getElementById("theLink").target = "_blank";
      
  switch(id) {
    case "scratch":
      document.getElementById("theLink").href = "https://scratch.mit.edu/users/Crafty190";
    break;
    case "twitter":
      document.getElementById("theLink").href = "https://twitter.com/c190draws";
    break;
    case "instagram":
      document.getElementById("theLink").href = "https://www.instagram.com/c190draws";
    break;
    case "github":
      document.getElementById("theLink").href = "https://github.com/wangzi190";
    break;
  }
};

function hideGallerySelect() {
  var takeElements = ["about", "links", "works", "contact", "storm", "back", "forward", "email", "discord", "sketchIcon", "minorIcon", "majorIcon", "play"];
  var i = 12;
  while (i > -1) {
    document.getElementById(takeElements[i]).hidden = true;
    i--;
  }
  document.getElementById("galleryBack").hidden = false;
};

function openGallery() {
  var i = 0;
  while (i < levelButtons.length) {
    document.getElementById(levelButtons[i]).style.filter = "brightness(100%)";
    i++;
  }

  if (selectedGallery != 0) {
    document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/102863121-feb8e000-43e6-11eb-8fad-87aa1bb07cc0.png";
    document.getElementById("myName").alt = "gray zhuang gallery";

    switch(selectedGallery) {
      case "sketchIcon":
      hideGallerySelect();
        var i = sketchNames.length - 1;
        while (i > -1) {
          document.getElementById(sketchNames[i]).hidden = false;
          i--;
        }
      break;
      case "minorIcon":
      hideGallerySelect();
        var i = minorNames.length - 1;
        while (i > -1) {
          document.getElementById(minorNames[i]).hidden = false;
          i--;
        }
      break;
      case "majorIcon":
      hideGallerySelect();
        var i = majorNames.length - 1;
        while (i > -1) {
          document.getElementById(majorNames[i]).hidden = false;
          i--;
        }
      break;
    }
  }
};

function returnGallery() {
  var i = sketchNames.length - 1;
  while (i > -1) {
  document.getElementById(sketchNames[i]).hidden = true;
  i--;}
  i = minorNames.length - 1;
  while (i > -1) {
  document.getElementById(minorNames[i]).hidden = true;
  i--;}
  i = majorNames.length - 1;
  while (i > -1) {
  document.getElementById(majorNames[i]).hidden = true;
  i--;}
  
  var hideForWorks = ["about", "links", "works", "contact", "storm", "forward", "email", "discord"];
  i = 0;
  while (i < hideForWorks.length) {
    document.getElementById(hideForWorks[i]).hidden = true;
      i++;
  }
  document.getElementById("back").hidden = false;
  document.getElementById("play").hidden = false;
  document.getElementById("sketchIcon").hidden = false;
  document.getElementById("minorIcon").hidden = false;
  document.getElementById("majorIcon").hidden = false;
  document.getElementById("galleryBack").hidden = true;
  pageName = "works";
  document.getElementById("myName").src = "https://user-images.githubusercontent.com/57303754/134959636-af53f099-040d-4e83-a9e7-4dea5f97a820.png";
  document.getElementById("myName").alt = "gray zhuang works (level select)";
  selectedGallery = 0;
};
