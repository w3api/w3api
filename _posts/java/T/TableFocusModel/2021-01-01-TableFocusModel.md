---
title: TableFocusModel
permalink: Java/TableFocusModel
date: 2021-01-11
key: JavaJava.T.TableFocusModel
category: java
tags: ['java se', 'javafx.scene.control', 'javafx.controls', 'clase java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TableFocusModel.description }}

## Sintaxis
~~~java
public abstract class TableFocusModel<T,TC extends TableColumnBase<T,?>> extends FocusModel<T>
~~~

## Constructores
* [TableFocusModel()](/Java/TableFocusModel/TableFocusModel/)

## Métodos
* [focus()](/Java/TableFocusModel/focus)
* [focusAboveCell()](/Java/TableFocusModel/focusAboveCell)
* [focusBelowCell()](/Java/TableFocusModel/focusBelowCell)
* [focusLeftCell()](/Java/TableFocusModel/focusLeftCell)
* [focusRightCell()](/Java/TableFocusModel/focusRightCell)
* [isFocused()](/Java/TableFocusModel/isFocused)

## Ejemplo
~~~java
{{ site.data.Java.T.TableFocusModel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TableFocusModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
