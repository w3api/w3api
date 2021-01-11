---
title: DocumentTraversal.createNodeIterator()
permalink: Java/DocumentTraversal/createNodeIterator
date: 2021-01-11
key: JavaJava.D.DocumentTraversal
category: java
tags: ['java se', 'org.w3c.dom.traversal', 'java.xml', 'metodo java', 'Java 9', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentTraversal.metodos valor="createNodeIterator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
NodeIterator createNodeIterator(Node root, int whatToShow, NodeFilter filter, boolean entityReferenceExpansion) throws DOMException
~~~

## Parámetros
* **Node root**,  {% include w3api/param_description.html metodo=_dato parametro="Node root" %}
* **NodeFilter filter**,  {% include w3api/param_description.html metodo=_dato parametro="NodeFilter filter" %}
* **int whatToShow**,  {% include w3api/param_description.html metodo=_dato parametro="int whatToShow" %}
* **boolean entityReferenceExpansion**,  {% include w3api/param_description.html metodo=_dato parametro="boolean entityReferenceExpansion" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[DocumentTraversal](/Java/DocumentTraversal/)

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
