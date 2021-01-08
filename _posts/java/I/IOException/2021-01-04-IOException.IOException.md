---
title: IOException.IOException()
permalink: Java/IOException/IOException
date: 2021-01-04
key: JavaJava.I.IOException
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IOException.constructores valor="IOException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public IOException()
public IOException(String message)
public IOException(String message, Throwable cause)
public IOException(Throwable cause)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[IOException](/Java/IOException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IOException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
