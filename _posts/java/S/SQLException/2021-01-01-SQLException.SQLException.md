---
title: SQLException.SQLException()
permalink: /Java/SQLException/SQLException/
date: 2021-01-11
key: Java.S.SQLException
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLException.constructores valor="SQLException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLException()
public SQLException(String reason)
public SQLException(String reason, String SQLState)
public SQLException(String reason, String SQLState, int vendorCode)
public SQLException(String reason, String sqlState, int vendorCode, Throwable cause)
public SQLException(String reason, String sqlState, Throwable cause)
public SQLException(String reason, Throwable cause)
public SQLException(Throwable cause)
~~~

## Parámetros
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}
* **String sqlState**,  {% include w3api/param_description.html metodo=_dato parametro="String sqlState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Clase Padre
[SQLException](/Java/SQLException/)

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
