---
title: HttpResponse.MultiSubscriber.asMap()
permalink: Java/HttpResponse/MultiSubscriber/asMap
date: 2021-01-11
key: JavaJava.H.HttpResponse.MultiSubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.MultiSubscriber.metodos valor="asMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <V> HttpResponse.MultiSubscriber<MultiMapResult<V>,V> asMap(Function<HttpRequest,Optional<HttpResponse.BodyHandler<V>>> reqHandler)
static <V> HttpResponse.MultiSubscriber<MultiMapResult<V>,V> asMap(Function<HttpRequest,Optional<HttpResponse.BodyHandler<V>>> reqHandler, boolean completion)
~~~

## Parámetros
* **boolean completion**,  {% include w3api/param_description.html metodo=_dato parametro="boolean completion" %}
* **Optional&lt;HttpResponse.BodyHandler&lt;V&gt;&gt;&gt; reqHandler**,  {% include w3api/param_description.html metodo=_dato parametro="Optional<HttpResponse.BodyHandler<V>>> reqHandler" %}
* **Function&lt;HttpRequest**,  {% include w3api/param_description.html metodo=_dato parametro="Function<HttpRequest" %}

## Clase Padre
[HttpResponse.MultiSubscriber](/Java/HttpResponse/MultiSubscriber/)

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
