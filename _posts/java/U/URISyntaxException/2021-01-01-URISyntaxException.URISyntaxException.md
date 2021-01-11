---
title: URISyntaxException.URISyntaxException()
permalink: Java/URISyntaxException/URISyntaxException
date: 2021-01-11
key: JavaJava.U.URISyntaxException
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URISyntaxException.constructores valor="URISyntaxException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URISyntaxException(String input, String reason)
public URISyntaxException(String input, String reason, int index)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **String input**,  {% include w3api/param_description.html metodo=_dato parametro="String input" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URISyntaxException](/Java/URISyntaxException/)

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
