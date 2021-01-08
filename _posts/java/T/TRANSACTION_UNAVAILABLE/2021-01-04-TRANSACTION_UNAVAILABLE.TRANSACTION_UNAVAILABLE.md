---
title: TRANSACTION_UNAVAILABLE.TRANSACTION_UNAVAILABLE()
permalink: Java/TRANSACTION_UNAVAILABLE/TRANSACTION_UNAVAILABLE
date: 2021-01-04
key: JavaJava.T.TRANSACTION_UNAVAILABLE
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TRANSACTION_UNAVAILABLE.constructores valor="TRANSACTION_UNAVAILABLE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TRANSACTION_UNAVAILABLE()
public TRANSACTION_UNAVAILABLE(int minor, CompletionStatus completed)
public TRANSACTION_UNAVAILABLE(String s)
public TRANSACTION_UNAVAILABLE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[TRANSACTION_UNAVAILABLE](/Java/TRANSACTION_UNAVAILABLE/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TRANSACTION_UNAVAILABLE.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
