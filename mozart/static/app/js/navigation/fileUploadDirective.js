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
                var files, counter;
                el.bind('change', function (event) {
                    files = event.target.files;
                    console.log(files);
                    for (counter = 0; counter < files.length; counter += 1) {
                        scope.$emit(scope.fileBind, {file: files[counter]});
                    }
                });
            }
        };
    }
    /*jslint unparam: false*/

    angular.module('mozArtApp')
        .directive('fileUpload', fileUploadDirective);
}());