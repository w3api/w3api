---
title: TRANSACTION_MODE.TRANSACTION_MODE()
permalink: Java/TRANSACTION_MODE/TRANSACTION_MODE
date: 2021-01-04
key: JavaJava.T.TRANSACTION_MODE
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TRANSACTION_MODE.constructores valor="TRANSACTION_MODE" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TRANSACTION_MODE()
public TRANSACTION_MODE(int minor, CompletionStatus completed)
public TRANSACTION_MODE(String s)
public TRANSACTION_MODE(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[TRANSACTION_MODE](/Java/TRANSACTION_MODE/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TRANSACTION_MODE.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
