---
title: SQLInvalidAuthorizationSpecException.SQLInvalidAuthorizationSpecException()
permalink: Java/SQLInvalidAuthorizationSpecException/SQLInvalidAuthorizationSpecException
date: 2021-01-04
key: JavaJava.S.SQLInvalidAuthorizationSpecException
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLInvalidAuthorizationSpecException.constructores valor="SQLInvalidAuthorizationSpecException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLInvalidAuthorizationSpecException()
public SQLInvalidAuthorizationSpecException(String reason)
public SQLInvalidAuthorizationSpecException(String reason, String SQLState)
public SQLInvalidAuthorizationSpecException(String reason, String SQLState, int vendorCode)
public SQLInvalidAuthorizationSpecException(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLInvalidAuthorizationSpecException(String reason, String SQLState, Throwable cause)
public SQLInvalidAuthorizationSpecException(String reason, Throwable cause)
public SQLInvalidAuthorizationSpecException(Throwable cause)
~~~

## Parámetros
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}

## Clase Padre
[SQLInvalidAuthorizationSpecException](/Java/SQLInvalidAuthorizationSpecException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SQLInvalidAuthorizationSpecException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
