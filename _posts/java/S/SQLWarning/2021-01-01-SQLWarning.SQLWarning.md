---
title: SQLWarning.SQLWarning()
permalink: /Java/SQLWarning/SQLWarning/
date: 2021-01-11
key: Java.S.SQLWarning
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLWarning.constructores valor="SQLWarning" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SQLWarning()
public SQLWarning(String reason)
public SQLWarning(String reason, String SQLState)
public SQLWarning(String reason, String SQLState, int vendorCode)
public SQLWarning(String reason, String SQLState, int vendorCode, Throwable cause)
public SQLWarning(String reason, String SQLState, Throwable cause)
public SQLWarning(String reason, Throwable cause)
public SQLWarning(Throwable cause)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[SQLWarning](/Java/SQLWarning/)

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
