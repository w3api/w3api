---
title: HttpRequest.BodyPublisher.fromFile()
permalink: Java/HttpRequest/BodyPublisher/fromFile
date: 2021-01-11
key: JavaJava.H.HttpRequest.BodyPublisher
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.BodyPublisher.metodos valor="fromFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpRequest.BodyPublisher fromFile(Path path) throws FileNotFoundException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/)

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
