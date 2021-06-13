---
title: BAD_OPERATION.BAD_OPERATION()
permalink: /Java/BAD_OPERATION/BAD_OPERATION/
date: 2021-01-11
key: Java.B.BAD_OPERATION
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BAD_OPERATION.constructores valor="BAD_OPERATION" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BAD_OPERATION()
public BAD_OPERATION(int minor, CompletionStatus completed)
public BAD_OPERATION(String s)
public BAD_OPERATION(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[BAD_OPERATION](/Java/BAD_OPERATION/)

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
