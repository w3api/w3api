---
title: XPathEvaluator.evaluate()
permalink: /Java/XPathEvaluator/evaluate/
date: 2021-01-11
key: Java.X.XPathEvaluator
category: Java
tags: ['java se', 'org.w3c.dom.xpath', 'jdk.xml.dom', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XPathEvaluator.metodos valor="evaluate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object evaluate(String expression, Node contextNode, XPathNSResolver resolver, short type, Object result) throws XPathException, DOMException
~~~

## Parámetros
* **String expression**,  {% include w3api/param_description.html metodo=_dato parametro="String expression" %}
* **XPathNSResolver resolver**,  {% include w3api/param_description.html metodo=_dato parametro="XPathNSResolver resolver" %}
* **Object result**,  {% include w3api/param_description.html metodo=_dato parametro="Object result" %}
* **short type**,  {% include w3api/param_description.html metodo=_dato parametro="short type" %}
* **Node contextNode**,  {% include w3api/param_description.html metodo=_dato parametro="Node contextNode" %}

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
