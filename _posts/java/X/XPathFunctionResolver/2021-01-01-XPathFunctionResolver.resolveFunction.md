---
title: XPathFunctionResolver.resolveFunction()
permalink: Java/XPathFunctionResolver/resolveFunction
date: 2021-01-11
key: JavaJava.X.XPathFunctionResolver
category: java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathFunctionResolver.metodos valor="resolveFunction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
XPathFunction resolveFunction(QName functionName, int arity)
~~~

## Parámetros
* **int arity**,  {% include w3api/param_description.html metodo=_dato parametro="int arity" %}
* **QName functionName**,  {% include w3api/param_description.html metodo=_dato parametro="QName functionName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XPathFunctionResolver](/Java/XPathFunctionResolver/)

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
