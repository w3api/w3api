---
title: IllegalArgumentException.IllegalArgumentException()
permalink: /Java/IllegalArgumentException/IllegalArgumentException/
date: 2021-01-11
key: Java.I.IllegalArgumentException
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IllegalArgumentException.constructores valor="IllegalArgumentException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IllegalArgumentException()
public IllegalArgumentException(String s)
public IllegalArgumentException(String message, Throwable cause)
public IllegalArgumentException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Clase Padre
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
