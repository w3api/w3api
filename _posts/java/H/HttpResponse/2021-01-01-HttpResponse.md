---
title: HttpResponse
permalink: /Java/HttpResponse/
date: 2021-01-11
key: Java.H.HttpResponse
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpResponse.description }}

## Sintaxis
~~~java
public abstract class HttpResponse<T> extends Object
~~~

## Constructores
* [HttpResponse()](/Java/HttpResponse/HttpResponse/)

## Métodos
* [body()](/Java/HttpResponse/body)
* [headers()](/Java/HttpResponse/headers)
* [previousResponse()](/Java/HttpResponse/previousResponse)
* [request()](/Java/HttpResponse/request)
* [sslParameters()](/Java/HttpResponse/sslParameters)
* [statusCode()](/Java/HttpResponse/statusCode)
* [uri()](/Java/HttpResponse/uri)
* [version()](/Java/HttpResponse/version)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpResponse.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
