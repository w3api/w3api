---
title: COMM_FAILURE.COMM_FAILURE()
permalink: /Java/COMM_FAILURE/COMM_FAILURE/
date: 2021-01-11
key: Java.C.COMM_FAILURE
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.COMM_FAILURE.constructores valor="COMM_FAILURE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public COMM_FAILURE()
public COMM_FAILURE(int minor, CompletionStatus completed)
public COMM_FAILURE(String s)
public COMM_FAILURE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[COMM_FAILURE](/Java/COMM_FAILURE/)

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
