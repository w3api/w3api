---
title: FindException.FindException()
permalink: /Java/FindException/FindException/
date: 2021-01-11
key: Java.F.FindException
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FindException.constructores valor="FindException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FindException()
public FindException(String msg)
public FindException(String msg, Throwable cause)
public FindException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[FindException](/Java/FindException/)

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
