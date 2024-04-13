---
title: CellSkinBase
permalink: /Java/CellSkinBase/
date: 2021-01-11
key: Java.C.CellSkinBase
category: Java
tags: ['java se', 'javafx.scene.control.skin', 'javafx.controls', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CellSkinBase.description }}

## Sintaxis
~~~java
public class CellSkinBase<C extends Cell> extends LabeledSkinBase<C>
~~~

## Constructores
* [CellSkinBase()](/Java/CellSkinBase/CellSkinBase/)

## Métodos
* [cellSizeProperty()](/Java/CellSkinBase/cellSizeProperty)
* [getCellSize()](/Java/CellSkinBase/getCellSize)
* [getClassCssMetaData()](/Java/CellSkinBase/getClassCssMetaData)

## Ejemplo
~~~java
{{ site.data.Java.C.CellSkinBase.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CellSkinBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
