---
title: INVALID_TRANSACTION.INVALID_TRANSACTION()
permalink: Java/INVALID_TRANSACTION/INVALID_TRANSACTION
date: 2021-01-11
key: JavaJava.I.INVALID_TRANSACTION
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'JDKJava 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.INVALID_TRANSACTION.constructores valor="INVALID_TRANSACTION" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public INVALID_TRANSACTION()
public INVALID_TRANSACTION(int minor, CompletionStatus completed)
public INVALID_TRANSACTION(String s)
public INVALID_TRANSACTION(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_dato parametro="CompletionStatus completed" %}
* **int minor**,  {% include w3api/param_description.html metodo=_dato parametro="int minor" %}

## Clase Padre
[INVALID_TRANSACTION](/Java/INVALID_TRANSACTION/)

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
