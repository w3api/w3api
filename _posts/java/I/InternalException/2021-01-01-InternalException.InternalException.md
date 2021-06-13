---
title: InternalException.InternalException()
permalink: /Java/InternalException/InternalException/
date: 2021-01-11
key: Java.I.InternalException
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InternalException.constructores valor="InternalException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InternalException()
public InternalException(int errorCode)
public InternalException(String s)
public InternalException(String s, int errorCode)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **int errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int errorCode" %}

## Clase Padre
[InternalException](/Java/InternalException/)

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
