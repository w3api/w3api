---
title: InvalidPathException.InvalidPathException()
permalink: Java/InvalidPathException/InvalidPathException
date: 2021-01-04
key: JavaJava.I.InvalidPathException
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvalidPathException.constructores valor="InvalidPathException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InvalidPathException(String input, String reason)
public InvalidPathException(String input, String reason, int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **String input**,  {% include w3api/param_description.html metodo=_data parametro="String input" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InvalidPathException](/Java/InvalidPathException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InvalidPathException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
