(function () {
    'use strict';

    /*jslint unparam: true*/
    function mozartWelcomeDirective($window) {
        return {
            restrict: 'A',
            scope: {
                baseDir : "@"
            },
            transclude: false,
            link: function (scope, elem, attrs) {
                var images = [scope.baseDir + 'img/fondo1.jpg',
                          scope.baseDir + 'img/fondo2.jpg',
                          scope.baseDir + 'img/fondo3.jpg',
                          scope.baseDir + 'img/fondo4.jpg',
                          scope.baseDir + 'img/fondo5.jpg'];
                elem.css({'background-image': 'url(' + images[0] + ')'});
                elem.scroll(function (event) {
                    var sectionHeight, height;
                    sectionHeight = elem.innerHeight();
                    height = angular.element(event.target).scrollTop();
                    if (height < sectionHeight) {
                        elem.css({'background-image': 'url(' + images[0] + ')'});
                    } else if (height < 2 * sectionHeight) {
                        elem.css({'background-image': 'url(' + images[1] + ')'});
                    } else if (height < 3 * sectionHeight) {
                        elem.css({'background-image': 'url(' + images[2] + ')'});
                    } else if (height < 4 * sectionHeight) {
                        elem.css({'background-image': 'url(' + images[3] + ')'});
                    } else {
                        elem.css({'background-image': 'url(' + images[4] + ')'});
                    }
                });
            }
        };
    }
    /*jslint unparam: false*/
    mozartWelcomeDirective.$inject = ['$window'];

    angular.module('mozArtApp')
        .directive('mzWelcome', mozartWelcomeDirective);
}());