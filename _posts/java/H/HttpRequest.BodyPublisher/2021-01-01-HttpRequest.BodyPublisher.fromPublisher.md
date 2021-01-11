---
title: HttpRequest.BodyPublisher.fromPublisher()
permalink: Java/HttpRequest/BodyPublisher/fromPublisher
date: 2021-01-11
key: JavaJava.H.HttpRequest.BodyPublisher
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.BodyPublisher.metodos valor="fromPublisher" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpRequest.BodyPublisher fromPublisher(Flow.Publisher<? extends ByteBuffer> publisher)
static HttpRequest.BodyPublisher fromPublisher(Flow.Publisher<? extends ByteBuffer> publisher, long contentLength)
~~~

## Parámetros
* **Flow.Publisher&lt;? extends ByteBuffer&gt; publisher**,  {% include w3api/param_description.html metodo=_dato parametro="Flow.Publisher<? extends ByteBuffer> publisher" %}
* **long contentLength**,  {% include w3api/param_description.html metodo=_dato parametro="long contentLength" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpRequest.BodyPublisher](/Java/HttpRequest/BodyPublisher/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
