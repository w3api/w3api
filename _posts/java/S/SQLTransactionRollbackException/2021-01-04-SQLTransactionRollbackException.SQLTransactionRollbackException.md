---
title: SQLTransactionRollbackException.SQLTransactionRollbackException()
permalink: Java/SQLTransactionRollbackException/SQLTransactionRollbackException
date: 2021-01-04
key: JavaJava.S.SQLTransactionRollbackException
category: java
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
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLTransactionRollbackException](/Java/SQLTransactionRollbackException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLTransactionRollbackException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
