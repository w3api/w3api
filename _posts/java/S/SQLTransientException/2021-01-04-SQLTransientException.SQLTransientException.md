---
title: SQLTransientException.SQLTransientException()
permalink: Java/SQLTransientException/SQLTransientException
date: 2021-01-04
key: JavaJava.S.SQLTransientException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLTransientException.constructores valor="SQLTransientException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLTransientException()
public SQLTransientException(String reason)
public SQLTransientException(String reason, String SQLState)
public SQLTransientException(String reason, String SQLState, int vendorCode)
public SQLTransientException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLTransientException(String reason, String SQLState, Throwable cause)
public SQLTransientException(String reason, Throwable cause)
public SQLTransientException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLTransientException](/Java/SQLTransientException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLTransientException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
