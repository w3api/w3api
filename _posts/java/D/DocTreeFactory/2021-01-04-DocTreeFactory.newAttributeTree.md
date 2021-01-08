---
title: DocTreeFactory.newAttributeTree()
permalink: Java/DocTreeFactory/newAttributeTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newAttributeTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
AttributeTree newAttributeTree(Name name, AttributeTree.ValueKind vkind, List<? extends DocTree> value)
~~~

## Parámetros
* **List&lt;? extends DocTree&gt; value**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends DocTree> value" %}
* **AttributeTree.ValueKind vkind**,  {% include w3api/param_description.html metodo=_data parametro="AttributeTree.ValueKind vkind" %}
* **Name name**,  {% include w3api/param_description.html metodo=_data parametro="Name name" %}

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
