app.service('peticionObras', ['$http',  function($http){
	this.get=function(fnOK,fnError, modo, categoria, autor, cantidad) {
		$http({
			method: 'GET',
			url: 'static/data/obras' + cantidad + '.json'
		})
		.success(function(data, status, headers, config) {
			fnOK(data);
		})
		.error(function(data, status, headers, config) {
			fnError(data,status);
		});
	};
}]);
/*
app.service('peticionNickname', ['$http',  function($http){
	this.get=function(fnOK,fnError, nick) {
		$http({
			method: 'GET',
			url: 'static/data/obras' + cantidad + '.json'
		})
		.success(function(data, status, headers, config) {
			fnOK(data);
		})
		.error(function(data, status, headers, config) {
			fnError(data,status);
		});
	};
}]);
*/
// Los otros dos servicios aun no estan completos

app.service('peticionPromotores', ['$http',  function($http){
	this.get=function(fnOK,fnError, modo, inicial, cantidad) {
		$http({
			method: 'GET',
			url: 'static/data/promotores' + cantidad + '.json'
		})
		.success(function(data, status, headers, config) {
			fnOK(data);
		})
		.error(function(data, status, headers, config) {
			fnError(data,status);
		});
	};
}]);
/*
app.service('peticionBusqueda', ['$http',  function($http){
	this.get=function(fnOK,fnError, tipos, palabras, cantidad) {
		$http({
			method: 'GET',
			url: 'static/data/obras' + cantidad + '.json'
		})
		.success(function(data, status, headers, config) {
			fnOK(data);
		})
		.error(function(data, status, headers, config) {
			fnError(data,status);
		});
	};
}]);
*/
