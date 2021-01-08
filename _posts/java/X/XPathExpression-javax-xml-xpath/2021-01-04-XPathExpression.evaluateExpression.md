---
title: XPathExpression.evaluateExpression()
permalink: Java/XPathExpression-javax-xml-xpath/evaluateExpression
date: 2021-01-04
key: JavaJava.X.XPathExpression-javax-xml-xpath
category: java
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
* **Class&lt;T&gt; type**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> type" %}
* **InputSource source**,  {% include w3api/param_description.html metodo=_data parametro="InputSource source" %}
* **Object item**,  {% include w3api/param_description.html metodo=_data parametro="Object item" %}

## Excepciones
[XPathExpressionException](/Java/XPathExpressionException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XPathExpression](/Java/XPathExpression-javax-xml-xpath/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XPathExpression-javax-xml-xpath.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
