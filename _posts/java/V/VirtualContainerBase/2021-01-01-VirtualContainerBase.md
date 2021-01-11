---
title: VirtualContainerBase
permalink: Java/VirtualContainerBase
date: 2021-01-11
key: JavaJava.V.VirtualContainerBase
category: java
tags: ['java se', 'javafx.scene.control.skin', 'javafx.controls', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VirtualContainerBase.description }}

## Sintaxis
~~~java
public abstract class VirtualContainerBase<C extends Control,I extends IndexedCell> extends SkinBase<C>
~~~

## Constructores
* [VirtualContainerBase()](/Java/VirtualContainerBase/VirtualContainerBase/)

## Métodos
* [createVirtualFlow()](/Java/VirtualContainerBase/createVirtualFlow)
* [getItemCount()](/Java/VirtualContainerBase/getItemCount)
* [getVirtualFlow()](/Java/VirtualContainerBase/getVirtualFlow)
* [markItemCountDirty()](/Java/VirtualContainerBase/markItemCountDirty)
* [updateItemCount()](/Java/VirtualContainerBase/updateItemCount)

## Ejemplo
~~~java
{{ site.data.Java.V.VirtualContainerBase.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VirtualContainerBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
