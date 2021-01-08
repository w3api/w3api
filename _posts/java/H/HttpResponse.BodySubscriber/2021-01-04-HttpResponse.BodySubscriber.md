---
title: HttpResponse.BodySubscriber
permalink: Java/HttpResponse/BodySubscriber
date: 2021-01-04
key: JavaJava.H.HttpResponse.BodySubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.H.HttpResponse.BodySubscriber.description }}

## Sintaxis
~~~java
public static interface HttpResponse.BodySubscriber<T> extends Flow.Subscriber<List<ByteBuffer>>
~~~

## Métodos
* [asByteArray()](/Java/HttpResponse/BodySubscriber/asByteArray)
* [asByteArrayConsumer()](/Java/HttpResponse/BodySubscriber/asByteArrayConsumer)
* [asFile()](/Java/HttpResponse/BodySubscriber/asFile)
* [asInputStream()](/Java/HttpResponse/BodySubscriber/asInputStream)
* [asString()](/Java/HttpResponse/BodySubscriber/asString)
* [buffering()](/Java/HttpResponse/BodySubscriber/buffering)
* [discard()](/Java/HttpResponse/BodySubscriber/discard)
* [fromSubscriber()](/Java/HttpResponse/BodySubscriber/fromSubscriber)
* [getBody()](/Java/HttpResponse/BodySubscriber/getBody)

## Ejemplo
~~~java
{{ site.data.Java.H.HttpResponse.BodySubscriber.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.BodySubscriber.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
