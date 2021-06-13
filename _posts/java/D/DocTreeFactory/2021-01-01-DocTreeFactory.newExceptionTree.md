---
title: DocTreeFactory.newExceptionTree()
permalink: /Java/DocTreeFactory/newExceptionTree/
date: 2021-01-11
key: Java.D.DocTreeFactory
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newExceptionTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ThrowsTree newExceptionTree(ReferenceTree name, List<? extends DocTree> description)
~~~

## Parámetros
* **ReferenceTree name**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceTree name" %}
* **List&lt;? extends DocTree&gt; description**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> description" %}

## Clase Padre
[DocTreeFactory](/Java/DocTreeFactory/)

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
