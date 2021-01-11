---
title: HttpResponse.BodyHandler.asFileDownload()
permalink: Java/HttpResponse/BodyHandler/asFileDownload
date: 2021-01-11
key: JavaJava.H.HttpResponse.BodyHandler
category: java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpResponse.BodyHandler.metodos valor="asFileDownload" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static HttpResponse.BodyHandler<Path> asFileDownload(Path directory, OpenOption... openOptions)
~~~

## Parámetros
* **OpenOption... openOptions**,  {% include w3api/param_description.html metodo=_dato parametro="OpenOption... openOptions" %}
* **Path directory**,  {% include w3api/param_description.html metodo=_dato parametro="Path directory" %}

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
