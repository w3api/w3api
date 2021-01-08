---
title: DocumentTraversal.createTreeWalker()
permalink: Java/DocumentTraversal/createTreeWalker
date: 2021-01-04
key: JavaJava.D.DocumentTraversal
category: java
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
* **boolean entityReferenceExpansion**,  {% include w3api/param_description.html metodo=_data parametro="boolean entityReferenceExpansion" %}
* **Node root**,  {% include w3api/param_description.html metodo=_data parametro="Node root" %}
* **int whatToShow**,  {% include w3api/param_description.html metodo=_data parametro="int whatToShow" %}
* **NodeFilter filter**,  {% include w3api/param_description.html metodo=_data parametro="NodeFilter filter" %}

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
{%- for _ldc in site.data.Java.D.DocumentTraversal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
