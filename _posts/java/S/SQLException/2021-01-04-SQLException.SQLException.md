---
title: SQLException.SQLException()
permalink: Java/SQLException/SQLException
date: 2021-01-04
key: JavaJava.S.SQLException
category: java
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
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String sqlState**,  {% include w3api/param_description.html metodo=_data parametro="String sqlState" %}

## Clase Padre
[SQLException](/Java/SQLException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
