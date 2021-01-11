---
title: Throwable.printStackTrace()
permalink: Java/Throwable/printStackTrace
date: 2021-01-11
key: JavaJava.T.Throwable
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.Throwable.metodos valor="printStackTrace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void printStackTrace()
public void printStackTrace(PrintStream s)
public void printStackTrace(PrintWriter s)
~~~

## Parámetros
* **PrintWriter s**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter s" %}
* **PrintStream s**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream s" %}

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
