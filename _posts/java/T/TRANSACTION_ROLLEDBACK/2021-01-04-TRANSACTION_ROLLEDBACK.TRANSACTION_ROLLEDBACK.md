---
title: TRANSACTION_ROLLEDBACK.TRANSACTION_ROLLEDBACK()
permalink: Java/TRANSACTION_ROLLEDBACK/TRANSACTION_ROLLEDBACK
date: 2021-01-04
key: JavaJava.T.TRANSACTION_ROLLEDBACK
category: java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TRANSACTION_ROLLEDBACK.constructores valor="TRANSACTION_ROLLEDBACK" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TRANSACTION_ROLLEDBACK()
public TRANSACTION_ROLLEDBACK(int minor, CompletionStatus completed)
public TRANSACTION_ROLLEDBACK(String s)
public TRANSACTION_ROLLEDBACK(String s, int minor, CompletionStatus completed)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int minor**,  {% include w3api/param_description.html metodo=_data parametro="int minor" %}
* **CompletionStatus completed**,  {% include w3api/param_description.html metodo=_data parametro="CompletionStatus completed" %}

## Clase Padre
[TRANSACTION_ROLLEDBACK](/Java/TRANSACTION_ROLLEDBACK/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TRANSACTION_ROLLEDBACK.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
