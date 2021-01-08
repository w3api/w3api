---
title: SQLTransientConnectionException.SQLTransientConnectionException()
permalink: Java/SQLTransientConnectionException/SQLTransientConnectionException
date: 2021-01-04
key: JavaJava.S.SQLTransientConnectionException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLTransientConnectionException.constructores valor="SQLTransientConnectionException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLTransientConnectionException()
public SQLTransientConnectionException(String reason)
public SQLTransientConnectionException(String reason, String SQLState)
public SQLTransientConnectionException(String reason, String SQLState, int vendorCode)
public SQLTransientConnectionException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLTransientConnectionException(String reason, String SQLState, Throwable cause)
public SQLTransientConnectionException(String reason, Throwable cause)
public SQLTransientConnectionException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLTransientConnectionException](/Java/SQLTransientConnectionException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLTransientConnectionException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
