'use strict';
/**
* @ngdoc function
* @name mozArtApp.directive:fileUpload
* @description
* # fileUpload
*
* Directive of the mozArtApp.
*/

app.directive('fileUpload', [function () {
	return {
    restrict: 'A',
		scope: {
			fileBind : '@'
		},
		link: function (scope, el, attrs) {
			el.bind('change', function (event) {
				var files = event.target.files;
				for (var i = 0;i<files.length;i++) {
					scope.$emit(scope.fileBind, { file: files[i] });
				}
			});
		}
	};
}]);

