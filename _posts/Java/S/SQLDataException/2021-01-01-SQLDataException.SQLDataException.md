---
title: SQLDataException.SQLDataException()
permalink: /Java/SQLDataException/SQLDataException/
date: 2021-01-11
key: Java.S.SQLDataException
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLDataException.constructores valor="SQLDataException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLDataException()
public SQLDataException(String reason)
public SQLDataException(String reason, String SQLState)
public SQLDataException(String reason, String SQLState, int vendorCode)
public SQLDataException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLDataException(String reason, String SQLState, Throwable cause)
public SQLDataException(String reason, Throwable cause)
public SQLDataException(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLDataException](/Java/SQLDataException/)

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
