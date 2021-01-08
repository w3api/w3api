---
title: SQLIntegrityConstraintViolationException.SQLIntegrityConstraintViolationException()
permalink: Java/SQLIntegrityConstraintViolationException/SQLIntegrityConstraintViolationException
date: 2021-01-04
key: JavaJava.S.SQLIntegrityConstraintViolationException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLIntegrityConstraintViolationException.constructores valor="SQLIntegrityConstraintViolationException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLIntegrityConstraintViolationException()
public SQLIntegrityConstraintViolationException(String reason)
public SQLIntegrityConstraintViolationException(String reason, String SQLState)
public SQLIntegrityConstraintViolationException(String reason, String SQLState, int vendorCode)
public SQLIntegrityConstraintViolationException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLIntegrityConstraintViolationException(String reason, String SQLState, Throwable cause)
public SQLIntegrityConstraintViolationException(String reason, Throwable cause)
public SQLIntegrityConstraintViolationException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLIntegrityConstraintViolationException](/Java/SQLIntegrityConstraintViolationException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLIntegrityConstraintViolationException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
