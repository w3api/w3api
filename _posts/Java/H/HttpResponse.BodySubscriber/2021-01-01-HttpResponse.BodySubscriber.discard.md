---
title: HttpResponse.BodySubscriber.discard()
permalink: /Java/HttpResponse/BodySubscriber/discard/
date: 2021-01-11
key: Java.H.HttpResponse.BodySubscriber
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodySubscriber.metodos valor="discard" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <U> HttpResponse.BodySubscriber<U> discard(U value)
~~~

## Parámetros
* **U value**,  {% include w3api/param_description.html metodo=_dato parametro="U value" %}

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
