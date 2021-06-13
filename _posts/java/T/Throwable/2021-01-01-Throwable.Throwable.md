---
title: Throwable.Throwable()
permalink: /Java/Throwable/Throwable/
date: 2021-01-11
key: Java.T.Throwable
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Throwable.constructores valor="Throwable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Throwable()
public Throwable(String message)
public Throwable(String message, Throwable cause)
protected Throwable(String message, Throwable cause, boolean enableSuppression, boolean writableStackTrace)
public Throwable(Throwable cause)
~~~

## Parámetros
* **boolean writableStackTrace**,  {% include w3api/param_description.html metodo=_dato parametro="boolean writableStackTrace" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **boolean enableSuppression**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enableSuppression" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[Throwable](/Java/Throwable/)

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
