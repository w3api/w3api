---
title: SQLNonTransientException.SQLNonTransientException()
permalink: Java/SQLNonTransientException/SQLNonTransientException
date: 2021-01-04
key: JavaJava.S.SQLNonTransientException
category: java
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
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLNonTransientException](/Java/SQLNonTransientException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLNonTransientException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
