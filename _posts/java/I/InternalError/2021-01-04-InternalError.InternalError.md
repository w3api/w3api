---
title: InternalError.InternalError()
permalink: Java/InternalError/InternalError
date: 2021-01-04
key: JavaJava.I.InternalError
category: java
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
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[InternalError](/Java/InternalError/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InternalError.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
