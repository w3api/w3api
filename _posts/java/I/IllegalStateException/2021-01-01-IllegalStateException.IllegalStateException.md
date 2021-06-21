---
title: IllegalStateException.IllegalStateException()
permalink: /Java/IllegalStateException/IllegalStateException/
date: 2021-01-11
key: Java.I.IllegalStateException
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IllegalStateException.constructores valor="IllegalStateException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IllegalStateException()
public IllegalStateException(String s)
public IllegalStateException(String message, Throwable cause)
public IllegalStateException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Clase Padre
[IllegalStateException](/Java/IllegalStateException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
