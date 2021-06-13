---
title: Expression.Expression()
permalink: /Java/Expression/Expression/
date: 2021-01-11
key: Java.E.Expression
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Expression.constructores valor="Expression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Expression(Object value, Object target, String methodName, Object[] arguments)
@ConstructorProperties({"target","methodName","arguments"}) public Expression(Object target, String methodName, Object[] arguments)
~~~

## Parámetros
* **Object[] arguments**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] arguments" %}
* **Object target**,  {% include w3api/param_description.html metodo=_dato parametro="Object target" %}
* **String methodName**,  {% include w3api/param_description.html metodo=_dato parametro="String methodName" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Clase Padre
[Expression](/Java/Expression/)

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
