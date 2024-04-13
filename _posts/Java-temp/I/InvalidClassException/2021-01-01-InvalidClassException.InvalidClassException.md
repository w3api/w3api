---
title: InvalidClassException.InvalidClassException()
permalink: /Java/InvalidClassException/InvalidClassException/
date: 2021-01-11
key: Java.I.InvalidClassException
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvalidClassException.constructores valor="InvalidClassException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InvalidClassException(String reason)
public InvalidClassException(String cname, String reason)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **String cname**,  {% include w3api/param_description.html metodo=_dato parametro="String cname" %}

## Clase Padre
[InvalidClassException](/Java/InvalidClassException/)

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
