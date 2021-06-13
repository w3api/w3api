---
title: DocumentTraversal.createTreeWalker()
permalink: /Java/DocumentTraversal/createTreeWalker/
date: 2021-01-11
key: Java.D.DocumentTraversal
category: Java
tags: ['java se', 'org.w3c.dom.traversal', 'java.xml', 'metodo java', 'Java 9', 'DOM Level 2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentTraversal.metodos valor="createTreeWalker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
TreeWalker createTreeWalker(Node root, int whatToShow, NodeFilter filter, boolean entityReferenceExpansion) throws DOMException
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
