(function() {
	'use strict';
	
	function fileUploadDirective() {
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
	}

	angular.module('mozArtApp')
		.directive('fileUpload', fileUploadDirective);
})();