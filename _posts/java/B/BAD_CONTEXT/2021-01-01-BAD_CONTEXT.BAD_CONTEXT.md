---
title: BAD_CONTEXT.BAD_CONTEXT()
permalink: /Java/BAD_CONTEXT/BAD_CONTEXT/
date: 2021-01-11
key: Java.B.BAD_CONTEXT
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BAD_CONTEXT.constructores valor="BAD_CONTEXT" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BAD_CONTEXT()
public BAD_CONTEXT(int minor, CompletionStatus completed)
public BAD_CONTEXT(String s)
public BAD_CONTEXT(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[BAD_CONTEXT](/Java/BAD_CONTEXT/)

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
