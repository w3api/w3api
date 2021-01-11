---
title: HttpResponse.BodySubscriber.asFile()
permalink: Java/HttpResponse/BodySubscriber/asFile
date: 2021-01-11
key: JavaJava.H.HttpResponse.BodySubscriber
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodySubscriber.metodos valor="asFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpResponse.BodySubscriber<Path> asFile(Path file)
static HttpResponse.BodySubscriber<Path> asFile(Path file, OpenOption... openOptions)
~~~

## Parámetros
* **Path file**,  {% include w3api/param_description.html metodo=_dato parametro="Path file" %}
* **OpenOption... openOptions**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... openOptions" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

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
