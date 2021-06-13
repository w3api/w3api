---
title: HttpResponse.BodySubscriber.asByteArrayConsumer()
permalink: /Java/HttpResponse/BodySubscriber/asByteArrayConsumer/
date: 2021-01-11
key: Java.H.HttpResponse.BodySubscriber
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodySubscriber.metodos valor="asByteArrayConsumer" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpResponse.BodySubscriber<Void> asByteArrayConsumer(Consumer<Optional<byte[]>> consumer)
~~~

## Parámetros
* **Consumer&lt;Optional&lt;byte[]&gt;&gt; consumer**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<Optional<byte[]>> consumer" %}

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
