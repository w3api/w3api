---
title: HttpResponse.BodyHandler
permalink: Java/HttpResponse/BodyHandler
date: 2021-01-04
key: JavaJava.H.HttpResponse.BodyHandler
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpResponse.BodyHandler.description }}

## Sintaxis
~~~java
@FunctionalInterface public static interface HttpResponse.BodyHandler<T>
~~~

## Métodos
* [apply()](/Java/HttpResponse/BodyHandler/apply)
* [asByteArray()](/Java/HttpResponse/BodyHandler/asByteArray)
* [asByteArrayConsumer()](/Java/HttpResponse/BodyHandler/asByteArrayConsumer)
* [asFile()](/Java/HttpResponse/BodyHandler/asFile)
* [asFileDownload()](/Java/HttpResponse/BodyHandler/asFileDownload)
* [asInputStream()](/Java/HttpResponse/BodyHandler/asInputStream)
* [asString()](/Java/HttpResponse/BodyHandler/asString)
* [buffering()](/Java/HttpResponse/BodyHandler/buffering)
* [discard()](/Java/HttpResponse/BodyHandler/discard)
* [fromSubscriber()](/Java/HttpResponse/BodyHandler/fromSubscriber)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpResponse.BodyHandler.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.BodyHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
