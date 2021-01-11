---
title: HttpCookie.parse()
permalink: Java/HttpCookie/parse
date: 2021-01-11
key: JavaJava.H.HttpCookie
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpCookie.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static List<HttpCookie> parse(String header)
~~~

## Parámetros
* **String header**,  {% include w3api/param_description.html metodo=_dato parametro="String header" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[HttpCookie](/Java/HttpCookie/)

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
