---
title: HttpRequest.BodyPublisher.fromString()
permalink: /Java/HttpRequest/BodyPublisher/fromString/
date: 2021-01-11
key: Java.H.HttpRequest.BodyPublisher
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.BodyPublisher.metodos valor="fromString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpRequest.BodyPublisher fromString(String body)
static HttpRequest.BodyPublisher fromString(String s, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **String body**,  {% include w3api/param_description.html metodo=_dato parametro="String body" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

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
