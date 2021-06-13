---
title: HttpsURLConnection
permalink: /Java/HttpsURLConnection/
date: 2021-01-11
key: Java.H.HttpsURLConnection
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpsURLConnection.description }}

## Sintaxis
~~~java
public abstract class HttpsURLConnection extends HttpURLConnection
~~~

## Constructores
* [HttpsURLConnection()](/Java/HttpsURLConnection/HttpsURLConnection/)

## Campos
* [hostnameVerifier](/Java/HttpsURLConnection/hostnameVerifier)

## Métodos
* [getCipherSuite()](/Java/HttpsURLConnection/getCipherSuite)
* [getDefaultHostnameVerifier()](/Java/HttpsURLConnection/getDefaultHostnameVerifier)
* [getDefaultSSLSocketFactory()](/Java/HttpsURLConnection/getDefaultSSLSocketFactory)
* [getHostnameVerifier()](/Java/HttpsURLConnection/getHostnameVerifier)
* [getLocalCertificates()](/Java/HttpsURLConnection/getLocalCertificates)
* [getLocalPrincipal()](/Java/HttpsURLConnection/getLocalPrincipal)
* [getPeerPrincipal()](/Java/HttpsURLConnection/getPeerPrincipal)
* [getServerCertificates()](/Java/HttpsURLConnection/getServerCertificates)
* [getSSLSocketFactory()](/Java/HttpsURLConnection/getSSLSocketFactory)
* [setDefaultHostnameVerifier()](/Java/HttpsURLConnection/setDefaultHostnameVerifier)
* [setDefaultSSLSocketFactory()](/Java/HttpsURLConnection/setDefaultSSLSocketFactory)
* [setHostnameVerifier()](/Java/HttpsURLConnection/setHostnameVerifier)
* [setSSLSocketFactory()](/Java/HttpsURLConnection/setSSLSocketFactory)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpsURLConnection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpsURLConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
