<h1 align="center">Web crawler / Rastreador web</h1>

<p align="center">
  <img src="https://neilpatel.com/wp-content/uploads/2019/10/entenda-o-que-e-web-crawler.jpeg" width="400px">
</p>

<h2 align="center">Resumo</h2>
Função que simula um web crawler e pega palavras (especificas ou não) de um site e de suas paginas, tambem pode ser especificado a quantidade de paginas que serão analisadas do site. No final, cria um arquivo JSON contendo todos os dados que foram analisados.

<h2 align="center">Funcionalidades e demonstração</h2>
<h3>| Como funciona?</h3>
Este código foi feito para procurar palavras em um site e suas páginas. Com o uso dele, você poderá rastrear uma palavra específica ou exibir todas as palavras do site, ver quantas vezes cada uma foi exibida e o endereço onde elas se encontram.

<h3>| Como usar? </h3>
<p>Para usar este programa, basta você baixar o codigo e chamar a função no seu projeto ou direto do codigo.</p><br>

<strong>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ Chamando função ]
</strong>
<p>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images_readme/chamando_funcao.png">
</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A função ira procurar em 100 paginas do site "https://g1.globo.com/" a palavra "tecnologia". Apos feito esta analise, ela ira criar um &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arquivo JSON com o endereço onde cada palavra foi encontrada e quantas vezes a palavra foi mostrada.

<strong>
	<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ Parametros da função ]
</strong>
<p>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images_readme/parametros.png">
</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Se você não informar uma palavra especifica, o programa ira pegar todas as palavras encontradas e colocar quantas vezes estas &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;palavras foram mostradas em cada site<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• Se você não informar quantas paginas o programa deve analisar, o programa so ira analisar 10 paginas do site informado.<br>

<strong>
	<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ Arquivo JSON criado ]
</strong>
<p>
	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="images_readme/palavras_json.png">
</p>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mostrando o endereço onde foi encontrado a palavra e quantas vezes a palavra foi mostrada.

<h2 align="center">Tecnologias usadas</h2>
<p align="center">
	<a href='https://www.python.org/' target='_blank'>
	<img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg' width='40' height='40'>
	</a>
	<a href='https://requests.readthedocs.io/en/latest/' target='_blank'>
	<img src='https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png' width='40' height='40'>
	</a>
	<a href='https://pypi.org/project/beautifulsoup4/' target='_blank'>
	<img src='https://cdn-ak.f.st-hatena.com/images/fotolife/m/mitsu3204/20180824/20180824013430.jpg' width='40' height='40'>
	</a>
	<a href='https://www.w3schools.com/python/python_regex.asp' target='_blank'>
	<img src='https://static.javatpoint.com/tutorial/regex/images/regex-tutorial.png' width='40' height='40'>
	</a>
	<a href='https://docs.python.org/3/library/collections.html' target='_blank'>
	<img src='https://cdn-icons-png.flaticon.com/512/2761/2761077.png' width='40' height='40'>
	</a>
</p>
