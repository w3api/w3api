---
title: FunctionDeclarationTree
permalink: Java/FunctionDeclarationTree
date: 2021-01-11
key: JavaJava.F.FunctionDeclarationTree
category: java
tags: ['java se', 'jdk.nashorn.api.tree', 'jdk.scripting.nashorn', 'interface java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FunctionDeclarationTree.description }}

## Sintaxis
~~~java
public interface FunctionDeclarationTree extends StatementTree
~~~

## Métodos
* [getBody()](/Java/FunctionDeclarationTree/getBody)
* [getName()](/Java/FunctionDeclarationTree/getName)
* [getParameters()](/Java/FunctionDeclarationTree/getParameters)
* [isGenerator()](/Java/FunctionDeclarationTree/isGenerator)
* [isStrict()](/Java/FunctionDeclarationTree/isStrict)

## Ejemplo
~~~java
{{ site.data.Java.F.FunctionDeclarationTree.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FunctionDeclarationTree.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
