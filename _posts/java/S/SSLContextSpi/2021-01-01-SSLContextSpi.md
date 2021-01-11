---
title: SSLContextSpi
permalink: Java/SSLContextSpi
date: 2021-01-11
key: JavaJava.S.SSLContextSpi
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLContextSpi.description }}

## Sintaxis
~~~java
public abstract class SSLContextSpi extends Object
~~~

## Constructores
* [SSLContextSpi()](/Java/SSLContextSpi/SSLContextSpi/)

## Métodos
* [engineCreateSSLEngine()](/Java/SSLContextSpi/engineCreateSSLEngine)
* [engineGetClientSessionContext()](/Java/SSLContextSpi/engineGetClientSessionContext)
* [engineGetDefaultSSLParameters()](/Java/SSLContextSpi/engineGetDefaultSSLParameters)
* [engineGetServerSessionContext()](/Java/SSLContextSpi/engineGetServerSessionContext)
* [engineGetServerSocketFactory()](/Java/SSLContextSpi/engineGetServerSocketFactory)
* [engineGetSocketFactory()](/Java/SSLContextSpi/engineGetSocketFactory)
* [engineGetSupportedSSLParameters()](/Java/SSLContextSpi/engineGetSupportedSSLParameters)
* [engineInit()](/Java/SSLContextSpi/engineInit)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLContextSpi.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLContextSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
