<h1 align=center>Motorsport Standings API</h1>

<p> A simple API written in Python that scraps the FIA website for the current year drivers championship standings. The API currently scraps the FIA website for the World Endurance Championship, World Rally Championship and Formula 1 standings.</p>

<br>

<h3 align=center>Avaliable endpoints</h3>
<h5>GET /wrc</h5>
<p>Returns the 10 first competitors in the FIA World Rally Championship</p>
<h5>GET /wec</h5>
<p>Returns the 20 first competitors in the FIA World Endurance Championship</p>
<h5>GET /f1</h5>
<p>Returns the 10 first competitors in the FIA Formula 1 Championship</p>

<mark>Every endpoint has as optional parameter to limit the competitors returned by championship</mark>

<h3 align=center>Instalation</h3>

<h5>Via Docker</h5>
<p>The installation via Docker is pretty easy:</p>
<ol>
<li>Make sure <a href="https://www.docker.com/">Docker</a> is installed;</li>
<li>Download the repository;</li>
<li>Open a terminal on the root folder of the repository;</li>
<li>Run <code>docker compose up --build</code> and the API should be ready to go;</li>
</ol>
<h5>Manually</h5>
<p>The manual installation can be done following the steps below:</p>
<ol>
<li>Make sure <a href="https://pip.pypa.io/en/stable/getting-started/">pip</a> is installed;</li>
<li>Download the repository;</li>
<li>Open a terminal on the root folder of the repository;</li>
<li>Run <code>pip install -r requirements.txt</code> and then <code>python main.py</code> and the API should be working;</li>
</ol>