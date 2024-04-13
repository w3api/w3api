---
title: SQLNonTransientException.SQLNonTransientException()
permalink: /Java/SQLNonTransientException/SQLNonTransientException/
date: 2021-01-11
key: Java.S.SQLNonTransientException
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLNonTransientException.constructores valor="SQLNonTransientException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLNonTransientException()
public SQLNonTransientException(String reason)
public SQLNonTransientException(String reason, String SQLState)
public SQLNonTransientException(String reason, String SQLState, int vendorCode)
public SQLNonTransientException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLNonTransientException(String reason, String SQLState, Throwable cause)
public SQLNonTransientException(String reason, Throwable cause)
public SQLNonTransientException(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLNonTransientException](/Java/SQLNonTransientException/)

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
