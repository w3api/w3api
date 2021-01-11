---
title: SQLNonTransientConnectionException.SQLNonTransientConnectionException()
permalink: Java/SQLNonTransientConnectionException/SQLNonTransientConnectionException
date: 2021-01-11
key: JavaJava.S.SQLNonTransientConnectionException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLNonTransientConnectionException.constructores valor="SQLNonTransientConnectionException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLNonTransientConnectionException()
public SQLNonTransientConnectionException(String reason)
public SQLNonTransientConnectionException(String reason, String SQLState)
public SQLNonTransientConnectionException(String reason, String SQLState, int vendorCode)
public SQLNonTransientConnectionException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLNonTransientConnectionException(String reason, String SQLState, Throwable cause)
public SQLNonTransientConnectionException(String reason, Throwable cause)
public SQLNonTransientConnectionException(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLNonTransientConnectionException](/Java/SQLNonTransientConnectionException/)

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
