---
title: Exception.Exception()
permalink: Java/Exception/Exception
date: 2021-01-11
key: JavaJava.E.Exception
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Exception.constructores valor="Exception" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Exception()
public Exception(String message)
public Exception(String message, Throwable cause)
protected Exception(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace)
public Exception(Throwable cause)
~~~

## Parámetros
* **boolean writableStackTrace**,  {% include w3api/param_description.html metodo=_dato parametro="boolean writableStackTrace" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **boolean enableSuppression**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enableSuppression" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[Exception](/Java/Exception/)

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
