---
title: SSLSocketFactory
permalink: Java/SSLSocketFactory
date: 2021-01-11
key: JavaJava.S.SSLSocketFactory
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SSLSocketFactory.description }}

## Sintaxis
~~~java
public abstract class SSLSocketFactory extends SocketFactory
~~~

## Constructores
* [SSLSocketFactory()](/Java/SSLSocketFactory/SSLSocketFactory/)

## Métodos
* [createSocket()](/Java/SSLSocketFactory/createSocket)
* [getDefault()](/Java/SSLSocketFactory/getDefault)
* [getDefaultCipherSuites()](/Java/SSLSocketFactory/getDefaultCipherSuites)
* [getSupportedCipherSuites()](/Java/SSLSocketFactory/getSupportedCipherSuites)

## Ejemplo
~~~java
{{ site.data.Java.S.SSLSocketFactory.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLSocketFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
