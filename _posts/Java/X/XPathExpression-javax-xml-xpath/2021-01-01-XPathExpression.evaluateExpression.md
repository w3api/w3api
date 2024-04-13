---
title: XPathExpression.evaluateExpression()
permalink: /Java/XPathExpression-javax-xml-xpath/evaluateExpression/
date: 2021-01-11
key: Java.X.XPathExpression-javax-xml-xpath
category: Java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathExpression-javax-xml-xpath.metodos valor="evaluateExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default XPathEvaluationResult<?> evaluateExpression(Object item) throws XPathExpressionException
default <T> T evaluateExpression(Object item, Class<T> type)
default XPathEvaluationResult<?> evaluateExpression(InputSource source) throws XPathExpressionException
default <T> T evaluateExpression(InputSource source, Class<T> type)
~~~

## Parámetros
* **Object item**,  {% include w3api/param_description.html metodo=_dato parametro="Object item" %}
* **InputSource source**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource source" %}
* **Class&lt;T&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> type" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [XPathExpressionException](/Java/XPathExpressionException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[XPathExpression](/Java/XPathExpression-javax-xml-xpath/)

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
