---
title: HttpRequest.BodyPublisher.fromByteArray()
permalink: Java/HttpRequest/BodyPublisher/fromByteArray
date: 2021-01-11
key: JavaJava.H.HttpRequest.BodyPublisher
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.BodyPublisher.metodos valor="fromByteArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpRequest.BodyPublisher fromByteArray(byte[] buf)
static HttpRequest.BodyPublisher fromByteArray(byte[] buf, int offset, int length)
~~~

## Parámetros
* **byte[] buf**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] buf" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
