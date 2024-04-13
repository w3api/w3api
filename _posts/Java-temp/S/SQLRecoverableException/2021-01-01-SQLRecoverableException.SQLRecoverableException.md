---
title: SQLRecoverableException.SQLRecoverableException()
permalink: /Java/SQLRecoverableException/SQLRecoverableException/
date: 2021-01-11
key: Java.S.SQLRecoverableException
category: Java
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
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLRecoverableException](/Java/SQLRecoverableException/)

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
