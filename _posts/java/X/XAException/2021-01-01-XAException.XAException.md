---
title: XAException.XAException()
permalink: /Java/XAException/XAException/
date: 2021-01-11
key: Java.X.XAException
category: Java
tags: ['java se', 'javax.transaction.xa', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAException.constructores valor="XAException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XAException()
public XAException(int errcode)
public XAException(String s)
~~~

## Parámetros
* **int errcode**,  {% include w3api/param_description.html metodo=_dato parametro="int errcode" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Clase Padre
[XAException](/Java/XAException/)

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
