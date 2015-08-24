(function () {
    'use strict';

    /*jslint unparam: true*/
    function fileUploadDirective() {
        return {
            restrict: 'A',
            scope: {
                fileBind : '@'
            },
            link: function (scope, el, attrs) {
                var files;
                el.bind('change', function (event) {
                    files = event.target.files;
                    files.forEach(function (element) {
                        scope.$emit(scope.fileBind, {file: element});
                    });
                });
            }
        };
    }
    /*jslint unparam: false*/

    angular.module('mozArtApp')
        .directive('fileUpload', fileUploadDirective);
}());