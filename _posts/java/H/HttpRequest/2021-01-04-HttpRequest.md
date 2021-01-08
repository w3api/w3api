---
title: HttpRequest
permalink: Java/HttpRequest
date: 2021-01-04
key: JavaJava.H.HttpRequest
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpRequest.description }}

## Sintaxis
~~~java
public abstract class HttpRequest extends Object
~~~

## Constructores
* [HttpRequest()](/Java/HttpRequest/HttpRequest/)

## Métodos
* [bodyPublisher()](/Java/HttpRequest/bodyPublisher)
* [equals()](/Java/HttpRequest/equals)
* [expectContinue()](/Java/HttpRequest/expectContinue)
* [hashCode()](/Java/HttpRequest/hashCode)
* [headers()](/Java/HttpRequest/headers)
* [method()](/Java/HttpRequest/method)
* [newBuilder()](/Java/HttpRequest/newBuilder)
* [timeout()](/Java/HttpRequest/timeout)
* [uri()](/Java/HttpRequest/uri)
* [version()](/Java/HttpRequest/version)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpRequest.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
