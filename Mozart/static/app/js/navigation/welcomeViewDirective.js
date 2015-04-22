(function() {
  'use strict';
 
  function mozartWelcomeDirective($window, $log) {
    return {
      restrict: 'A',
      scope: {
        baseDir : "@"
      },
      transclude: false,
      link: function(scope, elem, attrs){
        var images = [scope.baseDir + 'img/fondo1.jpg', 
                      scope.baseDir + 'img/fondo2.jpg', 
                      scope.baseDir + 'img/fondo3.jpg', 
                      scope.baseDir + 'img/fondo4.jpg', 
                      scope.baseDir + 'img/fondo5.jpg'];
        elem.css({'background-image':'url(' + images[0] + ')'});
        elem
          .scroll(function (event){
            var sectionHeight = elem.innerHeight();
            var height = angular.element(event.target).scrollTop();
            $log.log(height + ':' + sectionHeight);
            if(height < sectionHeight) {
              elem.css({'background-image':'url(' + images[0] + ')'});
              $log.log('aa');
            }
            else if(height < 2*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[1] + ')'});
              $log.log('bb');
            }
            else if(height < 3*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[2] + ')'});
              $log.log('cc');
            }
            else if(height < 4*(sectionHeight)) {
              elem.css({'background-image':'url(' + images[3] + ')'});
              $log.log('cc');
            }
            else {
              elem.css({'background-image':'url(' + images[4] + ')'});
              $log.log('cc');
            }
          });
      }
    };
  }

  mozartWelcomeDirective.$inject = ['$window', '$log'];

  angular.module('mozArtApp')
    .directive('mzWelcome', mozartWelcomeDirective);
})();