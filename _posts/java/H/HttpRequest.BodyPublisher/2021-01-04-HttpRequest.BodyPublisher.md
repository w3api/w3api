---
title: HttpRequest.BodyPublisher
permalink: Java/HttpRequest/BodyPublisher
date: 2021-01-04
key: JavaJava.H.HttpRequest.BodyPublisher
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpRequest.BodyPublisher.description }}

## Sintaxis
~~~java
public static interface HttpRequest.BodyPublisher extends Flow.Publisher<ByteBuffer>
~~~

## Métodos
* [contentLength()](/Java/HttpRequest/BodyPublisher/contentLength)
* [fromByteArray()](/Java/HttpRequest/BodyPublisher/fromByteArray)
* [fromByteArrays()](/Java/HttpRequest/BodyPublisher/fromByteArrays)
* [fromFile()](/Java/HttpRequest/BodyPublisher/fromFile)
* [fromInputStream()](/Java/HttpRequest/BodyPublisher/fromInputStream)
* [fromPublisher()](/Java/HttpRequest/BodyPublisher/fromPublisher)
* [fromString()](/Java/HttpRequest/BodyPublisher/fromString)
* [noBody()](/Java/HttpRequest/BodyPublisher/noBody)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpRequest.BodyPublisher.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpRequest.BodyPublisher.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
