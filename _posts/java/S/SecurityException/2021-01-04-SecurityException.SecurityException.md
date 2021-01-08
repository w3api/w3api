---
title: SecurityException.SecurityException()
permalink: Java/SecurityException/SecurityException
date: 2021-01-04
key: JavaJava.S.SecurityException
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityException.constructores valor="SecurityException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SecurityException()
public SecurityException(String s)
public SecurityException(String message, Throwable cause)
public SecurityException(Throwable cause)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SecurityException](/Java/SecurityException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecurityException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
