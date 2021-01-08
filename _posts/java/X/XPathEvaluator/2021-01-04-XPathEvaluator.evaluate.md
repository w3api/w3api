---
title: XPathEvaluator.evaluate()
permalink: Java/XPathEvaluator/evaluate
date: 2021-01-04
key: JavaJava.X.XPathEvaluator
category: java
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
* **Node contextNode**,  {% include w3api/param_description.html metodo=_data parametro="Node contextNode" %}
* **String expression**,  {% include w3api/param_description.html metodo=_data parametro="String expression" %}
* **Object result**,  {% include w3api/param_description.html metodo=_data parametro="Object result" %}
* **XPathNSResolver resolver**,  {% include w3api/param_description.html metodo=_data parametro="XPathNSResolver resolver" %}
* **short type**,  {% include w3api/param_description.html metodo=_data parametro="short type" %}

## Excepciones
[XPathException](/Java/XPathException/), [DOMException](/Java/DOMException/)

## Clase Padre
[XPathEvaluator](/Java/XPathEvaluator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XPathEvaluator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
