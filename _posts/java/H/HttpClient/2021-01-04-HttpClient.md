---
title: HttpClient
permalink: Java/HttpClient
date: 2021-01-04
key: JavaJava.H.HttpClient
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpClient.description }}

## Sintaxis
~~~java
public abstract class HttpClient extends Object
~~~

## Constructores
* [HttpClient()](/Java/HttpClient/HttpClient/)

## Métodos
* [authenticator()](/Java/HttpClient/authenticator)
* [cookieHandler()](/Java/HttpClient/cookieHandler)
* [executor()](/Java/HttpClient/executor)
* [followRedirects()](/Java/HttpClient/followRedirects)
* [newBuilder()](/Java/HttpClient/newBuilder)
* [newHttpClient()](/Java/HttpClient/newHttpClient)
* [newWebSocketBuilder()](/Java/HttpClient/newWebSocketBuilder)
* [proxy()](/Java/HttpClient/proxy)
* [send()](/Java/HttpClient/send)
* [sendAsync()](/Java/HttpClient/sendAsync)
* [sslContext()](/Java/HttpClient/sslContext)
* [sslParameters()](/Java/HttpClient/sslParameters)
* [version()](/Java/HttpClient/version)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpClient.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpClient.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
