---
title: SQLInvalidAuthorizationSpecException.SQLInvalidAuthorizationSpecException()
permalink: /Java/SQLInvalidAuthorizationSpecException/SQLInvalidAuthorizationSpecException/
date: 2021-01-11
key: Java.S.SQLInvalidAuthorizationSpecException
category: Java
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
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLInvalidAuthorizationSpecException](/Java/SQLInvalidAuthorizationSpecException/)

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
