#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.0.1'
__author__ = 'James Swineson'

class debugString:

    pingResult=[
        # Samlpe results for command "ping -c 10 itunes.apple.com"
        # Debian
        '''PING apple.https.tel.ccgslb.com.cn (122.228.85.199) 56(84) bytes of data.
64 bytes from 122.228.85.199: icmp_req=1 ttl=56 time=201 ms
64 bytes from 122.228.85.199: icmp_req=2 ttl=56 time=3233 ms
64 bytes from 122.228.85.199: icmp_req=3 ttl=56 time=2611 ms
64 bytes from 122.228.85.199: icmp_req=4 ttl=56 time=1796 ms
64 bytes from 122.228.85.199: icmp_req=5 ttl=56 time=839 ms
64 bytes from 122.228.85.199: icmp_req=6 ttl=56 time=434 ms
64 bytes from 122.228.85.199: icmp_req=7 ttl=56 time=1738 ms
64 bytes from 122.228.85.199: icmp_req=8 ttl=56 time=760 ms
64 bytes from 122.228.85.199: icmp_req=9 ttl=56 time=533 ms
64 bytes from 122.228.85.199: icmp_req=10 ttl=56 time=3281 ms

--- apple.https.tel.ccgslb.com.cn ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 61000ms
rtt min/avg/max/mdev = 201.836/1543.078/3281.754/1108.149 ms, pipe 4''',

        # Windows 8.1, Chinese
        '''
正在 Ping apple.https.tel.ccgslb.com.cn [122.228.85.199] 具有 32 字节的数据:
来自 122.228.85.199 的回复: 字节=32 时间=37ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=37ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=22ms TTL=56
来自 122.228.85.199 的回复: 字节=32 时间=77ms TTL=56

122.228.85.199 的 Ping 统计信息:
    数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
往返行程的估计时间(以毫秒为单位):
    最短 = 22ms，最长 = 77ms，平均 = 43ms
''',
        # Mac OS X 10.9.2
        '''PING apple.https.tel.ccgslb.com.cn (115.239.253.43): 56 data bytes
Request timeout for icmp_seq 0
64 bytes from 115.239.253.43: icmp_seq=1 ttl=56 time=41.724 ms
Request timeout for icmp_seq 2
64 bytes from 115.239.253.43: icmp_seq=3 ttl=56 time=176.227 ms
Request timeout for icmp_seq 4
64 bytes from 115.239.253.43: icmp_seq=5 ttl=56 time=138.641 ms
Request timeout for icmp_seq 6
64 bytes from 115.239.253.43: icmp_seq=7 ttl=56 time=27.647 ms
64 bytes from 115.239.253.43: icmp_seq=8 ttl=56 time=36.250 ms

--- apple.https.tel.ccgslb.com.cn ping statistics ---
10 packets transmitted, 5 packets received, 50.0% packet loss
round-trip min/avg/max/stddev = 27.647/84.098/176.227/61.212 ms'''
    ]

    speedtestResult = [
        # Normal result
        '''Ping: 244.141 ms
Download: 0.94 Mbit/s
Upload: 0.82 Mbit/s''',
        # Empty result
        '''


'''       
        ]
    netindexResult = [
        # Normal result
        '''<!doctype html>

<html class="no-js">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="description" content="Explore broadband and mobile performance statistics from around the world. Compiled from billions of tests run on Ookla’s websites and apps like Ookla Speedtest" />
	<meta name="keywords" lang="en" content="download speed, upload speed, r-factor, mos, voip, quality, internet, connection, broadband, dsl, cable, residential, household, statistics" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Download Speed in Ningbo, Zhejiang, China | Net Index from Ookla</title>
	<link rel="stylesheet" type="text/css" href="//cloud.typography.com/7800252/634742/css/fonts.css" />
	<link rel="stylesheet" type="text/css" href="http://cdn.netindex.com/global/dist/styles/main.css?v=1.8" media="screen" />
	<link rel="stylesheet" href="//api.tiles.mapbox.com/mapbox.js/v1.6.0/mapbox.css">
	<link rel="shortcut icon" href="http://cdn.netindex.com/images/favicon.ico?v=1.2" type="image/x-icon" />
	<script src="//api.tiles.mapbox.com/mapbox.js/v1.6.0/mapbox.js"></script>
	<script src="http://cdn.netindex.com/global/lib/modernizr-2.7.1.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/lib/grunticon-loader.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/lib/jquery-1.9.1.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/lib/underscore-1.4.4.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/lib/d3.v3.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/lib/topojson.v1.min.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/main.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/map.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/map-controller.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/graph.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/graph-controller.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/bar-chart-controller.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/fixie.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/dropdown.js?v=1.0"></script>
	<script src="http://cdn.netindex.com/global/js/modal.js?v=1.0"></script>
	
</head>
<body>
<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5PLCZL"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-5PLCZL');</script>
<!-- End Google Tag Manager -->

    <header class="header clearfix" role="banner">
      <div class="container">
        <a href="/" class="logo"><b class="text-hide icon-logo">Ookla</b> Net Index</a>

        <ul class="user-menu">

          <li class="user-menu-centered">
            <a id="my_loc_href" href="#" onClick="getMyLocation()"><i class="icon-location"></i> Go to my Location</a>
            <script type="text/javascript">  
	
	  function goMyLocation(loc) {
		if (loc.address) {
			var zip = loc.address.postalCode;
		} else {
			var zip = '';
		}
		
	    window.location = "/my_location.php?index=download&lat=" + loc.coords.latitude + "&lon=" + loc.coords.longitude + "&accuracy=" + loc.coords.accuracy +
	        "&zip=" + zip;
	  }

      function errorHandler(err) {
		if (err.code == 1) {
			// user said no!
		} else if (err.code == 2) {
			// position unavailable
		} else if (err.code == 3) {
			// timeout
		} else {
			// unknown
		}
		
		window.location = "/my_location.php?index=download";
      }

	  function getMyLocation() {
		if (navigator.geolocation) {
	      navigator.geolocation.getCurrentPosition(goMyLocation, errorHandler, {enableHighAccuracy: false, timeout: 5000, maximumAge: 24*60*60*1000});  // cache for 24 hours
	      var href = document.getElementById("my_loc_href"); 
	    } else {
			window.location = "/my_location.php?index=download";
	    }
	  }
</script>
          </li>

          <li>
            <a class="icon-uservoice" id="feedback" href="#">Feedback</a>
          </li>

          <li class="dropdown-container">
            <button class="text-hide icon-menu dropdown-toggle" type="button">Menu</button>

            <div class="dropdown">
              <section class="dropdown-section">
                <ul class="dropdown-list dropdown-list-primary">
                  <li>
                    <a href="http://explorer.netindex.com"><i class="icon-globe icon-inline"></i> Net Index Explorer</a>
                  </li>
                  <li>
                    <a href="/#source"><i class="icon-source-data icon-inline"></i> Source Data</a>
                  </li>
                  <li>
                    <a href="http://www.ookla.com/netmetrics"><i class="icon-net-metrics icon-inline"></i> Net Metrics  <i class="icon-external-link"></i></a>
                  </li>
                  <li>
                    <a href="http://www.ookla.com/about"><i class="icon-info icon-info-alt icon-inline"></i> About Ookla <i class="icon-external-link"></i></a>
                  </li>
                  <li>
                    <a href="http://www.speedtest.net"><i class="icon-speedtest icon-inline"></i> Speedtest <i class="icon-external-link"></i></a>
                  </li>
                </ul>
              </section>

              <section class="dropdown-section">
                <ul class="dropdown-list dropdown-list-horizontal">
                  <li>
                    <a class="text-hide icon-facebook" href="http://go.ookla.com/facebook">Facebook</a>
                  </li>
                  <li>
                    <a class="text-hide icon-twitter" href="http://go.ookla.com/twitter">Twitter</a>
                  </li>
                  <li>
                    <a class="text-hide icon-google-plus" href="http://go.ookla.com/google+">Google +</a>
                  </li>
                </ul>
              </section>
            </div>
          </li>
        </ul>

        <nav class="nav clearfix" role="navigation">
          <section class="nav-section">
            <h2 class="nav-heading">Global Broadband</h2>

            <ul>
              <li>
                <a class="nav-item highlight active" href="/download/">
                  Download
                  <div class="figure">
                    <b class="figure-content">17.4</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>
              <li>
                <a class="nav-item highlight " href="/upload/">
                  Upload
                  <div class="figure">
                    <b class="figure-content">7.9</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>
              <li>
                <a class="nav-item " href="/quality/">
                  Quality
                  <div class="figure">
                    <b class="figure-content">85.0</b>
                    <span class="figure-unit">R-Factor</span>
                  </div>
                </a>
              </li>
              <li>
                <a class="nav-item " href="/value/">
                  Value
                  <div class="figure">
                    <b class="figure-content">$6.37</b>
                    <span class="figure-unit">USD</span>
                  </div>
                </a>
              </li>
              <li>
                <a class="nav-item " href="/promise/">
                  Promise
                  <div class="figure">
                    <b class="figure-content">87.6 %</b>
                  </div>
                </a>
              </li>
            </ul>
          </section>

          <section class="nav-section">
            <h2 class="nav-heading">Global Mobile</h2>

            <ul>
              <li>
                <a class="nav-item highlight-alt " href="/mdownload/">
                  Download
                  <div class="figure">
                    <b class="figure-content">7.8</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>
              <li>
                <a class="nav-item highlight-alt " href="/mupload/">
                  Upload
                  <div class="figure">
                    <b class="figure-content">2.8</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>
            </ul>
          </section>
        </nav>
      </div>
    </header>
<main>

  <section class="overview-wrapper overview-wrapper-padded">
    <div class="container container-constrained">
      <div class="overview">
        <nav class="breadcrumb">
          <ul><li><a href="/download/2,88/China/">China</a></li></ul>
        </nav>

        <header class="overview-header pure-g-r">
          <div class="pure-u-3-5">
            <p class="overview-type">Broadband download</p>
            <h1 class="overview-heading">Ningbo, China</h1>&nbsp;<div class="tooltip-container">
              <button class="icon-info tooltip-toggle text-hide">Info</button>
              <div class="tooltip">Results were obtained by analyzing test data between Mar 5, 2014 and Apr 3, 2014. Tests from 30,243 unique IPs have been taken in this city and of 45,389 total tests, 3,467 are being used for the current Index.</div>
            </div>
          </div>

          <div class="pure-u-2-5">
            <div class="figure figure-large">
              <b class="figure-content">17.5</b>
              <span class="figure-unit">Mbps</span>
            </div>
          </div>
        </header>

        <nav class="overview-nav clearfix">
          <section class="nav-section overview-nav-section overview-nav-section-alpha">
            <h4 class="nav-heading overview-nav-heading">Broadband</h4>

            <ul><li><a class='nav-item overview-nav-item active' href='/download/4,860/Ningbo,-CN/'>Download <div class='figure'><b class='figure-content'>17.5</b><span class='figure-unit'>Mbps</span></div></a></li><li><a class='nav-item overview-nav-item ' href='/upload/4,860/Ningbo,-CN/'>Upload <div class='figure'><b class='figure-content'>8.7</b><span class='figure-unit'>Mbps</span></div></a></li><li><span class='nav-item overview-nav-item active' >Quality <div class='figure'><b class='figure-content'>-</b><span class='figure-unit'>R-Factor</span></div></span><div class="tooltip-container overview-nav-item-tooltip">
 <button class="tooltip-toggle icon-info-mini text-hide">Why is this empty?</button>
	<div class="tooltip tooltip-mini">
		There is not enough data to display information about this index.
	</div>
</div>
</li><li><span class='nav-item overview-nav-item active' >Value <div class='figure'><b class='figure-content'>-</b><span class='figure-unit'>Dollars</span></div></span><div class="tooltip-container overview-nav-item-tooltip">
 <button class="tooltip-toggle icon-info-mini text-hide">Why is this empty?</button>
	<div class="tooltip tooltip-mini">
		There is not enough data to display information about this index.
	</div>
</div>
</li><li><span class='nav-item overview-nav-item active' >Promise <div class='figure'><b class='figure-content'>-</b><span class='figure-unit'>Percent</span></div></span><div class="tooltip-container overview-nav-item-tooltip">
 <button class="tooltip-toggle icon-info-mini text-hide">Why is this empty?</button>
	<div class="tooltip tooltip-mini">
		There is not enough data to display information about this index.
	</div>
</div>
</li></ul>
          </section>

          <section class="nav-section overview-nav-section overview-nav-section-omega">
            <h4 class="nav-heading overview-nav-heading">Mobile</h4>

            <ul>
              <li>
                <a class="nav-item overview-nav-item " href="/mdownload/4,860/Ningbo,-CN/">
                  Download
                  <div class="figure">
                    <b class="figure-content">16.0</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>

              <li>
                <a class="nav-item overview-nav-item " href="/mupload/4,860/Ningbo,-CN/">
                  Upload
                  <div class="figure">
                    <b class="figure-content">2.8</b>
                    <span class="figure-unit">Mbps</span>
                  </div>
                </a>
              </li>
            </ul>
          </section>
        </nav>
      </div>
    </div>

    <div class="full-map-container map overview-map"></div>
    <script>
  App.incomingMaps.push({
    containerSelector: ".map",
    dataUrl: "http://cdn.netindex.com/ammap-data.php?level=4&id=860&index=download&lastupdate=Apr 3, 2014"
  });
</script>

  </section>

  <div class="banner">
    <div class="container">
      <a class="btn btn-inverse" href="http://explorer.netindex.com/maps?country=China&state=Zhejiang&city=860" target="_blank"><i class="icon-globe-btn icon-inline"></i> View in Net Index Explorer</a>
    </div>
  </div>

  <section>
    <div class="container">
      <h2 class="heading heading-padded graph-heading">Ningbo, China Historical Trend</h2>

      <div class="graph-key-container">
        <ul class="graph-key"></ul>
      </div>
    </div>

    <div class="graph"></div>
    <script>
  App.incomingGraphs.push({
    containerSelector: ".graph",
    index: "download",
    index_level: "4",
    id: "860"
  });
</script>

  </section>

  <section class="ranking-group container">
    
  </section>

  <section class="ranking-group container">
    <div class="more-cities"></div>

    <div class="top-20-cities"></div>

    <div class="brick brick-centered">
      <a href="#" data-level="4" data-count="50" data-index="download" data-id="860" class="btn btn-more-cities">Show More</a>
    </div>
  </section>

  <section class="ranking-group container">
    <header class="brick">
	<h2 class="heading">
    ISPS

    <div class="tooltip-container heading-tooltip">
      <button class="icon-info-mini text-hide tooltip-toggle"></button>
      <div class="tooltip tooltip-mini">
        <p>Graph Period: Oct 3, 2011 - Apr 3, 2014</p>
        <p>ISP ranking requires at least 100 unique IP addresses for a given ISP.</p>
        <p>ISP ratings (up to 5 stars) are based on over 13 million results collected at Speedtest.net. They tell how happy customers are with the ISP.</p>
      </div>
    </div>
  </h2>
</header>

<div class="bar-chart-container brick">
	<div class="bar">
	<div class="bar-content">
	  <div class="bar-heading">China Unicom Zhejiang</div>
	  <div class="rating">
	    <span class="visuallyhidden">3.7</span>
	    <i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star'></i>
	  </div>
	 </div>

	<div class="bar-chart">
		<div class="bar-chart-inner">
		  <div class="figure">
		    <b class="figure-content">27.84</b>
		    <span class="figure-unit">Mbps</span>
		  </div>
		</div>
	</div>
</div>
<div class="bar">
	<div class="bar-content">
	  <div class="bar-heading">China Mobile</div>
	  <div class="rating">
	    <span class="visuallyhidden">3.3</span>
	    <i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star'></i><i class='rating-star icon-star'></i>
	  </div>
	 </div>

	<div class="bar-chart">
		<div class="bar-chart-inner">
		  <div class="figure">
		    <b class="figure-content">18.29</b>
		    <span class="figure-unit">Mbps</span>
		  </div>
		</div>
	</div>
</div>
<div class="bar">
	<div class="bar-content">
	  <div class="bar-heading">China Telecom Zhejiang</div>
	  <div class="rating">
	    <span class="visuallyhidden">3.4</span>
	    <i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star'></i><i class='rating-star icon-star'></i>
	  </div>
	 </div>

	<div class="bar-chart">
		<div class="bar-chart-inner">
		  <div class="figure">
		    <b class="figure-content">17.29</b>
		    <span class="figure-unit">Mbps</span>
		  </div>
		</div>
	</div>
</div>
<div class="bar">
	<div class="bar-content">
	  <div class="bar-heading">China Telecom</div>
	  <div class="rating">
	    <span class="visuallyhidden">3.1</span>
	    <i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star'></i><i class='rating-star icon-star'></i>
	  </div>
	 </div>

	<div class="bar-chart">
		<div class="bar-chart-inner">
		  <div class="figure">
		    <b class="figure-content">16.77</b>
		    <span class="figure-unit">Mbps</span>
		  </div>
		</div>
	</div>
</div>
<div class="bar">
	<div class="bar-content">
	  <div class="bar-heading">NBIP TongLian(Ningbo)info-Port co.,Ltd</div>
	  <div class="rating">
	    <span class="visuallyhidden">3</span>
	    <i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star active'></i><i class='rating-star icon-star'></i><i class='rating-star icon-star'></i>
	  </div>
	 </div>

	<div class="bar-chart">
		<div class="bar-chart-inner">
		  <div class="figure">
		    <b class="figure-content">10.25</b>
		    <span class="figure-unit">Mbps</span>
		  </div>
		</div>
	</div>
</div>

</div>

  </section>
</main>
  <footer class="footer">
    <div class="container pure-g">
      <section class="pure-u footer-column">
        <h6 class="footer-heading">Net Index</h6>
        <ul class="footer-menu">
          <li><a href="http://explorer.netindex.com">Net Index Explorer</a></li>
          <li><a href="/#source">Source Data</a></li>
        </ul>
      </section>

      <section class="pure-u footer-column">
        <h6 class="footer-heading">Apps</h6>
        <ul class="footer-menu">
          <li><a href="http://www.speedtest.net">Ookla Speedtest</a></li>
          <li><a href="http://www.speedtest.net/mini.php">Speedtest Mini</a></li>
          <li><a href="http://www.pingtest.net">Pingtest.net</a></li>
        </ul>
      </section>

      <section class="pure-u footer-column">
        <h6 class="footer-heading">Company</h6>
        <ul class="footer-menu">
          <li><a href="http://www.ookla.com/about">About Ookla</a></li>
          <li><a href="http://www.ookla.com/netgauge">NetGauge</a></li>
          <li><a href="http://www.ookla.com/netmetrics">NetMetrics</a></li>
        </ul>
      </section>

      <section class="pure-u footer-column footer-column-offset">
        <a class="text-hide footer-logo icon-logo-footer" href="http://www.ookla.com">Ookla</a>
        <ul class="footer-menu">
          <li>Copyright 2014 Ookla</li>
          <li><a href="">Privacy Policy</a></li>
          <li class="footer-item-horizontal">
            <a class="text-hide icon-facebook" href="http://go.ookla.com/facebook">Facebook</a>
          </li>
          <li class="footer-item-horizontal">
            <a class="text-hide icon-twitter" href="http://go.ookla.com/twitter">Twitter</a>
          </li>
          <li class="footer-item-horizontal">
            <a class="text-hide icon-google-plus" href="http://go.ookla.com/google+">Google +</a>
          </li>
        </ul>
      </section>
    </div>
  </footer>
</body>
</html>
'''
        ]
