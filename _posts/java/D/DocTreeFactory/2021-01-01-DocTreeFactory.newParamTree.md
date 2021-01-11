---
title: DocTreeFactory.newParamTree()
permalink: Java/DocTreeFactory/newParamTree
date: 2021-01-11
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
* **boolean isTypeParameter**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isTypeParameter" %}
* **List&lt;? extends DocTree&gt; description**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends DocTree> description" %}
* **IdentifierTree name**,  {% include w3api/param_description.html metodo=_dato parametro="IdentifierTree name" %}

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
