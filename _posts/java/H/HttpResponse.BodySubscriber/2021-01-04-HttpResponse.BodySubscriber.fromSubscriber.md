---
title: HttpResponse.BodySubscriber.fromSubscriber()
permalink: Java/HttpResponse/BodySubscriber/fromSubscriber
date: 2021-01-04
key: JavaJava.H.HttpResponse.BodySubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodySubscriber.metodos valor="fromSubscriber" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S extends Flow.Subscriber<? super List<ByteBuffer>>>HttpResponse.BodySubscriber<Void> fromSubscriber(S subscriber)
static <S extends Flow.Subscriber<? super List<ByteBuffer>>,T>HttpResponse.BodySubscriber<T> fromSubscriber(S subscriber, Function<S,T> finisher)
~~~

## Parámetros
* **Function&lt;S**,  {% include w3api/param_description.html metodo=_data parametro="Function<S" %}
* **T&gt; finisher**,  {% include w3api/param_description.html metodo=_data parametro="T> finisher" %}
* **S subscriber**,  {% include w3api/param_description.html metodo=_data parametro="S subscriber" %}

## Clase Padre
[HttpResponse.BodySubscriber](/Java/HttpResponse/BodySubscriber/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.BodySubscriber.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
