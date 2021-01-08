---
title: DocTreeFactory.newParamTree()
permalink: Java/DocTreeFactory/newParamTree
date: 2021-01-04
key: JavaJava.D.DocTreeFactory
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeFactory.metodos valor="newParamTree" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ParamTree newParamTree(boolean isTypeParameter, IdentifierTree name, List<? extends DocTree> description)
~~~

## Parámetros
* **boolean isTypeParameter**,  {% include w3api/param_description.html metodo=_data parametro="boolean isTypeParameter" %}
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
