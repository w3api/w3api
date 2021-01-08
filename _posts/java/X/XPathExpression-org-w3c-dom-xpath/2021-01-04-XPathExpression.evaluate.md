---
title: XPathExpression.evaluate()
permalink: Java/XPathExpression-org-w3c-dom-xpath/evaluate
date: 2021-01-04
key: JavaJava.X.XPathExpression-org-w3c-dom-xpath
category: java
tags: ['java se', 'org.w3c.dom.xpath', 'jdk.xml.dom', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathExpression-org-w3c-dom-xpath.metodos valor="evaluate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object evaluate(Node contextNode, short type, Object result) throws XPathException, DOMException
~~~

## Parámetros
* **Object result**,  {% include w3api/param_description.html metodo=_data parametro="Object result" %}
* **Node contextNode**,  {% include w3api/param_description.html metodo=_data parametro="Node contextNode" %}
* **short type**,  {% include w3api/param_description.html metodo=_data parametro="short type" %}

## Excepciones
[XPathException](/Java/XPathException/), [DOMException](/Java/DOMException/)

## Clase Padre
[XPathExpression](/Java/XPathExpression-org-w3c-dom-xpath/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XPathExpression-org-w3c-dom-xpath.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
