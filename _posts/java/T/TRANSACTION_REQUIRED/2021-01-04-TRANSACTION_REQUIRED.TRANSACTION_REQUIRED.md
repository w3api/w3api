---
title: TRANSACTION_REQUIRED.TRANSACTION_REQUIRED()
permalink: Java/TRANSACTION_REQUIRED/TRANSACTION_REQUIRED
date: 2021-01-04
key: JavaJava.T.TRANSACTION_REQUIRED
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TRANSACTION_REQUIRED.constructores valor="TRANSACTION_REQUIRED" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TRANSACTION_REQUIRED()
public TRANSACTION_REQUIRED(int minor, CompletionStatus completed)
public TRANSACTION_REQUIRED(String s)
public TRANSACTION_REQUIRED(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[TRANSACTION_REQUIRED](/Java/TRANSACTION_REQUIRED/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TRANSACTION_REQUIRED.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
