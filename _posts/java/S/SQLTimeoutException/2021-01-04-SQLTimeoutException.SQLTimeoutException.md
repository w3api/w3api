---
title: SQLTimeoutException.SQLTimeoutException()
permalink: Java/SQLTimeoutException/SQLTimeoutException
date: 2021-01-04
key: JavaJava.S.SQLTimeoutException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLTimeoutException.constructores valor="SQLTimeoutException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLTimeoutException()
public SQLTimeoutException(String reason)
public SQLTimeoutException(String reason, String SQLState)
public SQLTimeoutException(String reason, String SQLState, int vendorCode)
public SQLTimeoutException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLTimeoutException(String reason, String SQLState, Throwable cause)
public SQLTimeoutException(String reason, Throwable cause)
public SQLTimeoutException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLTimeoutException](/Java/SQLTimeoutException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLTimeoutException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
