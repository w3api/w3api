---
title: ImportEntryTree
permalink: /Java/ImportEntryTree/
date: 2021-01-11
key: Java.I.ImportEntryTree
category: Java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.ImportEntryTree.description }}

## Sintaxis
~~~java
public interface ImportEntryTree extends Tree
~~~

## Métodos
* [getImportName()](/Java/ImportEntryTree/getImportName/)
* [getLocalName()](/Java/ImportEntryTree/getLocalName/)
* [getModuleRequest()](/Java/ImportEntryTree/getModuleRequest/)

## Ejemplo
~~~java
{{ site.data.Java.I.ImportEntryTree.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.ImportEntryTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
