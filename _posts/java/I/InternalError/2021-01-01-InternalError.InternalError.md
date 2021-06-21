---
title: InternalError.InternalError()
permalink: /Java/InternalError/InternalError/
date: 2021-01-11
key: Java.I.InternalError
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InternalError.constructores valor="InternalError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InternalError()
public InternalError(String message)
public InternalError(String message, Throwable cause)
public InternalError(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[InternalError](/Java/InternalError/)

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
