---
title: XPathFunction.evaluate()
permalink: /Java/XPathFunction/evaluate/
date: 2021-01-11
key: Java.X.XPathFunction
category: Java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathFunction.metodos valor="evaluate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object evaluate(List<?> args) throws XPathFunctionException
~~~

## Parámetros
* **List&lt;?&gt; args**,  {% include w3api/param_description.html metodo=_dato parametro="List<?> args" %}

## Excepciones
[XPathFunctionException](/Java/XPathFunctionException/)

## Clase Padre
[XPathFunction](/Java/XPathFunction/)

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
