---
title: XPathEvaluator.createExpression()
permalink: Java/XPathEvaluator/createExpression
date: 2021-01-11
key: JavaJava.X.XPathEvaluator
category: java
tags: ['java se', 'org.w3c.dom.xpath', 'jdk.xml.dom', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathEvaluator.metodos valor="createExpression" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
XPathExpression createExpression(String expression, XPathNSResolver resolver) throws XPathException, DOMException
~~~

## Parámetros
* **String expression**,  {% include w3api/param_description.html metodo=_dato parametro="String expression" %}
* **XPathNSResolver resolver**,  {% include w3api/param_description.html metodo=_dato parametro="XPathNSResolver resolver" %}

## Excepciones
[DOMException](/Java/DOMException/), [XPathException](/Java/XPathException/)

## Clase Padre
[XPathEvaluator](/Java/XPathEvaluator/)

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
