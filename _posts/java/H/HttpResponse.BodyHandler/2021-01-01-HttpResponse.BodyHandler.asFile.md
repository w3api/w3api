---
title: HttpResponse.BodyHandler.asFile()
permalink: Java/HttpResponse/BodyHandler/asFile
date: 2021-01-11
key: JavaJava.H.HttpResponse.BodyHandler
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodyHandler.metodos valor="asFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpResponse.BodyHandler<Path> asFile(Path file)
static HttpResponse.BodyHandler<Path> asFile(Path file, OpenOption... openOptions)
~~~

## Parámetros
* **Path file**,  {% include w3api/param_description.html metodo=_dato parametro="Path file" %}
* **OpenOption... openOptions**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... openOptions" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[HttpResponse.BodyHandler](/Java/HttpResponse/BodyHandler/)

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
