---
title: HttpResponse.BodySubscriber.buffering()
permalink: /Java/HttpResponse/BodySubscriber/buffering/
date: 2021-01-11
key: Java.H.HttpResponse.BodySubscriber
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodySubscriber.metodos valor="buffering" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> HttpResponse.BodySubscriber<T> buffering(HttpResponse.BodySubscriber<T> downstream, int bufferSize)
~~~

## Parámetros
* **HttpResponse.BodySubscriber&lt;T&gt; downstream**,  {% include w3api/param_description.html metodo=_dato parametro="HttpResponse.BodySubscriber<T> downstream" %}
* **int bufferSize**,  {% include w3api/param_description.html metodo=_dato parametro="int bufferSize" %}

## Clase Padre
[HttpResponse.BodySubscriber](/Java/HttpResponse/BodySubscriber/)

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
