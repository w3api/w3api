---
title: HttpRequest.Builder.timeout()
permalink: /Java/HttpRequest/Builder/timeout/
date: 2021-01-11
key: Java.H.HttpRequest.Builder
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.Builder.metodos valor="timeout" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpRequest.Builder timeout(Duration duration)
~~~

## Parámetros
* **Duration duration**,  {% include w3api/param_description.html metodo=_dato parametro="Duration duration" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[HttpRequest.Builder](/Java/HttpRequest/Builder/)

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
