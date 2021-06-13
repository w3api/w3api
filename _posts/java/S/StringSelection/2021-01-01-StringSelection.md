---
title: StringSelection
permalink: /Java/StringSelection/
date: 2021-01-11
key: Java.S.StringSelection
category: Java
tags: ['java se', 'java.awt.datatransfer', 'java.datatransfer', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StringSelection.description }}

## Sintaxis
~~~java
public class StringSelection extends Object implements Transferable, ClipboardOwner
~~~

## Constructores
* [StringSelection()](/Java/StringSelection/StringSelection/)

## Métodos
* [getTransferData()](/Java/StringSelection/getTransferData)
* [getTransferDataFlavors()](/Java/StringSelection/getTransferDataFlavors)
* [isDataFlavorSupported()](/Java/StringSelection/isDataFlavorSupported)

## Ejemplo
~~~java
{{ site.data.Java.S.StringSelection.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringSelection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
