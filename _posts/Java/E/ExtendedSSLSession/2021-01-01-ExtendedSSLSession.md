---
title: ExtendedSSLSession
permalink: /Java/ExtendedSSLSession/
date: 2021-01-11
key: Java.E.ExtendedSSLSession
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExtendedSSLSession.description }}

## Sintaxis
~~~java
public abstract class ExtendedSSLSession extends Object implements SSLSession
~~~

## Constructores
* [ExtendedSSLSession()](/Java/ExtendedSSLSession/ExtendedSSLSession/)

## Métodos
* [getLocalSupportedSignatureAlgorithms()](/Java/ExtendedSSLSession/getLocalSupportedSignatureAlgorithms)
* [getPeerSupportedSignatureAlgorithms()](/Java/ExtendedSSLSession/getPeerSupportedSignatureAlgorithms)
* [getRequestedServerNames()](/Java/ExtendedSSLSession/getRequestedServerNames)
* [getStatusResponses()](/Java/ExtendedSSLSession/getStatusResponses)

## Ejemplo
~~~java
{{ site.data.Java.E.ExtendedSSLSession.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExtendedSSLSession.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
