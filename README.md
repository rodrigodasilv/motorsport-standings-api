<h1 align=center>Motorsport Standings API</h1>

<p> A simple API written in Python that scraps the FIA website for the current year drivers championship standings. The API currently scraps the FIA website for the World Endurance Championship, World Rally Championship and Formula 1 standings.</p>

<br>

<h3 align=center>Avaliable endpoints</h3>
<h5>GET /wrc</h5>
<p>Returns the 10 first competitors in the FIA World Rally Championship for the current year</p>
<p>Example:</p>
<p align="center"><img src="https://github.com/rodrigodasilv/motorsport-standings-api/assets/55567123/c300d27b-c0d8-4081-820d-3c83fea26e7b" alt="GET /f1 return" style="width:50%;"/></p>

<h5>GET /wec</h5>
<p>Returns the 20 first competitors in the FIA World Endurance Championship for the current year</p>
<p>Example:</p>
<p align="center"><img src="https://github.com/rodrigodasilv/motorsport-standings-api/assets/55567123/ec217bdc-4792-4986-8eb6-91640a0481c2" alt="GET /f1 return" style="width:50%;"/></p>

<h5>GET /f1</h5>
<p>Returns the 10 first competitors in the FIA Formula 1 Championship for the current year</p>
<p>Example:</p>
<p align="center"><img src="https://github.com/rodrigodasilv/motorsport-standings-api/assets/55567123/d503bd37-637d-4821-b3a6-e5d7eebeee7a" alt="GET /f1 return" style="width:50%;"/></p>

<h4 align=center>PS: Every endpoint has as optional parameter to limit the competitors returned by championship</h4>

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
