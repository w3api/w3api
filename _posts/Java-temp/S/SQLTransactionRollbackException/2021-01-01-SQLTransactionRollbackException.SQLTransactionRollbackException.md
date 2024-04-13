---
title: SQLTransactionRollbackException.SQLTransactionRollbackException()
permalink: /Java/SQLTransactionRollbackException/SQLTransactionRollbackException/
date: 2021-01-11
key: Java.S.SQLTransactionRollbackException
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLTransactionRollbackException.constructores valor="SQLTransactionRollbackException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLTransactionRollbackException()
public SQLTransactionRollbackException(String reason)
public SQLTransactionRollbackException(String reason, String SQLState)
public SQLTransactionRollbackException(String reason, String SQLState, int vendorCode)
public SQLTransactionRollbackException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLTransactionRollbackException(String reason, String SQLState, Throwable cause)
public SQLTransactionRollbackException(String reason, Throwable cause)
public SQLTransactionRollbackException(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLTransactionRollbackException](/Java/SQLTransactionRollbackException/)

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
