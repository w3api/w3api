---
title: DocTreeFactory.newSerialFieldTree()
permalink: Java/DocTreeFactory/newSerialFieldTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newSerialFieldTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
SerialFieldTree newSerialFieldTree(IdentifierTree name, ReferenceTree type, List<? extends DocTree> description)
~~~

## Parámetros
* **ReferenceTree type**,  {% include w3api/param_description.html metodo=_data parametro="ReferenceTree type" %}
* **IdentifierTree name**,  {% include w3api/param_description.html metodo=_data parametro="IdentifierTree name" %}
* **List&lt;? extends DocTree&gt; description**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends DocTree> description" %}

## Clase Padre
[DocTreeFactory](/Java/DocTreeFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreeFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
