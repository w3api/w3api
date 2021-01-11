---
title: HttpResponse.BodyHandler.fromSubscriber()
permalink: Java/HttpResponse/BodyHandler/fromSubscriber
date: 2021-01-11
key: JavaJava.H.HttpResponse.BodyHandler
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodyHandler.metodos valor="fromSubscriber" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpResponse.BodyHandler<Void> fromSubscriber(Flow.Subscriber<? super List<ByteBuffer>> subscriber)
static <S extends Flow.Subscriber<? super List<ByteBuffer>>,T>HttpResponse.BodyHandler<T> fromSubscriber(S subscriber, Function<S,T> finisher)
~~~

## Parámetros
* **S subscriber**,  {% include w3api/param_description.html metodo=_dato parametro="S subscriber" %}
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_dato parametro="Function<S" %}
* **Flow.Subscriber&lt;? super List&lt;ByteBuffer&gt;&gt; subscriber**,  {% include w3api/param_description.html metodo=_dato parametro="Flow.Subscriber<? super List<ByteBuffer>> subscriber" %}
* **T&gt; finisher**,  {% include w3api/param_description.html metodo=_dato parametro="T> finisher" %}

## Clase Padre
[HttpResponse.BodyHandler](/Java/HttpResponse/BodyHandler/)

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
