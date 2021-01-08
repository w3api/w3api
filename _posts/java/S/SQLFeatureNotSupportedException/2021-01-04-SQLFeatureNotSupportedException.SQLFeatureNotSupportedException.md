---
title: SQLFeatureNotSupportedException.SQLFeatureNotSupportedException()
permalink: Java/SQLFeatureNotSupportedException/SQLFeatureNotSupportedException
date: 2021-01-04
key: JavaJava.S.SQLFeatureNotSupportedException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLFeatureNotSupportedException.constructores valor="SQLFeatureNotSupportedException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLFeatureNotSupportedException()
public SQLFeatureNotSupportedException(String reason)
public SQLFeatureNotSupportedException(String reason, String SQLState)
public SQLFeatureNotSupportedException(String reason, String SQLState, int vendorCode)
public SQLFeatureNotSupportedException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLFeatureNotSupportedException(String reason, String SQLState, Throwable cause)
public SQLFeatureNotSupportedException(String reason, Throwable cause)
public SQLFeatureNotSupportedException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLFeatureNotSupportedException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
