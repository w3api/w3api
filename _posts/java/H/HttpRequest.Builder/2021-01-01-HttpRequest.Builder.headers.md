---
title: HttpRequest.Builder.headers()
permalink: /Java/HttpRequest/Builder/headers/
date: 2021-01-11
key: Java.H.HttpRequest.Builder
category: Java
tags: ['java se', 'jdk.incubator.http', 'jdk.incubator.httpclient', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpRequest.Builder.metodos valor="headers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract HttpRequest.Builder headers(String... headers)
~~~

## Parámetros
* **String... headers**,  {% include w3api/param_description.html metodo=_dato parametro="String... headers" %}

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
