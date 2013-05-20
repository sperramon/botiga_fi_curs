<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
      xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
  <title>${page.name} - Pyramid tutorial wiki (based on
    TurboGears 20-Minute Wiki)</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />
  <link rel="shortcut icon"
        href="${request.static_url('tutorial:static/favicon.ico')}" />
  <link rel="stylesheet"
        href="${request.static_url('tutorial:static/pylons.css')}"
        type="text/css" media="screen" charset="utf-8" />
  <!--[if lte IE 6]>
  <link rel="stylesheet"
        href="${request.static_url('tutorial:static/ie6.css')}"
        type="text/css" media="screen" charset="utf-8" />
  <![endif]-->
</head>
<body>
  <div id="wrap">
    <div id="top-small">
      <div class="top-small align-center">
        <div>
          <img width="220" height="50" alt="pyramid"
        src="${request.static_url('tutorial:static/pyramid-small.png')}" />
        </div>
      </div>
    </div>
    <div id="middle">
      <div class="middle align-right">
        <div id="left" class="app-welcome align-left">
          Viewing <b><span tal:replace="page.name">Page Name
            Goes Here</span></b><br/>
          You can return to the
          <a href="${request.application_url}">FrontPage</a>.<br/>
        </div>
        <div id="right" class="app-welcome align-right">
          <span tal:condition="logged_in">
            <a href="${request.application_url}/logout">Logout</a>
          </span>
        </div>
      </div>
    </div>
    <div id="bottom">
      <div class="bottom">
        <div tal:replace="structure content">
          Page text goes here.
        </div>
        <p>
          <a tal:attributes="href edit_url" href="">
            Edit this page
          </a>
        </p>
      </div>
    </div>
  </div>
  <div id="footer">
    <div class="footer"
         >&copy; Copyright 2008-2011, Agendaless Consulting.</div>
  </div>
</body>
</html>
