---
title: DocTreeFactory.newAttributeTree()
permalink: /Java/DocTreeFactory/newAttributeTree/
date: 2021-01-11
key: Java.D.DocTreeFactory
category: Java
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
* **List&lt;? extends DocTree&gt; value**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> value" %}
* **Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Name name" %}
* **AttributeTree.ValueKind vkind**,  {% include w3api/param_description.html metodo=_dato parametro="AttributeTree.ValueKind vkind" %}

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
