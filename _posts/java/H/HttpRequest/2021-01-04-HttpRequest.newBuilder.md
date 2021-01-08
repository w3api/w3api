---
title: HttpRequest.newBuilder()
permalink: Java/HttpRequest/newBuilder
date: 2021-01-04
key: JavaJava.H.HttpRequest
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.metodos valor="newBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static HttpRequest.Builder newBuilder()
public static HttpRequest.Builder newBuilder(URI uri)
~~~

## Parámetros
* **URI uri**,  {% include w3api/param_description.html metodo=_data parametro="URI uri" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpRequest](/Java/HttpRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HttpRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
