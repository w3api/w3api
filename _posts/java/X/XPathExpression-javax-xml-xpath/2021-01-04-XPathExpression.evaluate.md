---
title: XPathExpression.evaluate()
permalink: Java/XPathExpression-javax-xml-xpath/evaluate
date: 2021-01-04
key: JavaJava.X.XPathExpression-javax-xml-xpath
category: java
tags: ['java se', 'javax.xml.xpath', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathExpression-javax-xml-xpath.metodos valor="evaluate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String evaluate(Object item) throws XPathExpressionException
Object evaluate(Object item, QName returnType) throws XPathExpressionException
String evaluate(InputSource source) throws XPathExpressionException
Object evaluate(InputSource source, QName returnType) throws XPathExpressionException
~~~

## Parámetros
* **QName returnType**,  {% include w3api/param_description.html metodo=_data parametro="QName returnType" %}
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
