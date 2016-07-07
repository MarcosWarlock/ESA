/*
 
O script deve ser executado na pagina http://concurso.esa.ensino.eb.br/site/ProvasAnteriores.aspx

*/

var links = document.querySelectorAll('a[href*="pdf"]');
var i;
for (i in links) 
{
	window.open(links[i].href);
}
