---
title: SQLRecoverableException.SQLRecoverableException()
permalink: Java/SQLRecoverableException/SQLRecoverableException
date: 2021-01-04
key: JavaJava.S.SQLRecoverableException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLRecoverableException.constructores valor="SQLRecoverableException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLRecoverableException()
public SQLRecoverableException(String reason)
public SQLRecoverableException(String reason, String SQLState)
public SQLRecoverableException(String reason, String SQLState, int vendorCode)
public SQLRecoverableException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLRecoverableException(String reason, String SQLState, Throwable cause)
public SQLRecoverableException(String reason, Throwable cause)
public SQLRecoverableException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLRecoverableException](/Java/SQLRecoverableException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLRecoverableException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
