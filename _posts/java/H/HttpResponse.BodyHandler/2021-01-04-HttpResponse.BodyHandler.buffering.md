---
title: HttpResponse.BodyHandler.buffering()
permalink: Java/HttpResponse/BodyHandler/buffering
date: 2021-01-04
key: JavaJava.H.HttpResponse.BodyHandler
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodyHandler.metodos valor="buffering" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> HttpResponse.BodyHandler<T> buffering(HttpResponse.BodyHandler<T> downstreamHandler, int bufferSize)
~~~

## Parámetros
* **int bufferSize**,  {% include w3api/param_description.html metodo=_data parametro="int bufferSize" %}
* **HttpResponse.BodyHandler&lt;T&gt; downstreamHandler**,  {% include w3api/param_description.html metodo=_data parametro="HttpResponse.BodyHandler<T> downstreamHandler" %}

## Clase Padre
[HttpResponse.BodyHandler](/Java/HttpResponse/BodyHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpResponse.BodyHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
