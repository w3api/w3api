---
title: BAD_TYPECODE.BAD_TYPECODE()
permalink: /Java/BAD_TYPECODE/BAD_TYPECODE/
date: 2021-01-11
key: Java.B.BAD_TYPECODE
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BAD_TYPECODE.constructores valor="BAD_TYPECODE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BAD_TYPECODE()
public BAD_TYPECODE(int minor, CompletionStatus completed)
public BAD_TYPECODE(String s)
public BAD_TYPECODE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[BAD_TYPECODE](/Java/BAD_TYPECODE/)

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
