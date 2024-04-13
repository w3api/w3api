---
title: DocTreeFactory.newLinkPlainTree()
permalink: /Java/DocTreeFactory/newLinkPlainTree/
date: 2021-01-11
key: Java.D.DocTreeFactory
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newLinkPlainTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LinkTree newLinkPlainTree(ReferenceTree ref, List<? extends DocTree> label)
~~~

## Parámetros
* **List&lt;? extends DocTree&gt; label**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> label" %}
* **ReferenceTree ref**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceTree ref" %}

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
