---
title: HttpRequest.BodyPublisher.fromString()
permalink: Java/HttpRequest/BodyPublisher/fromString
date: 2021-01-04
key: JavaJava.H.HttpRequest.BodyPublisher
category: java
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
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **String body**,  {% include w3api/param_description.html metodo=_data parametro="String body" %}

## Clase Padre
[HttpRequest.BodyPublisher](/Java/HttpRequest/BodyPublisher/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpRequest.BodyPublisher.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
