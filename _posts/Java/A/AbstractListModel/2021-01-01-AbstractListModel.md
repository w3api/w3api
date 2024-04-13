---
title: AbstractListModel
permalink: /Java/AbstractListModel/
date: 2021-01-11
key: Java.A.AbstractListModel
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractListModel.description }}

## Sintaxis
~~~java
public abstract class AbstractListModel<E> extends Object implements ListModel<E>, Serializable
~~~

## Constructores
* [AbstractListModel()](/Java/AbstractListModel/AbstractListModel/)

## Campos
* [listenerList](/Java/AbstractListModel/listenerList)

## Métodos
* [addListDataListener()](/Java/AbstractListModel/addListDataListener)
* [fireContentsChanged()](/Java/AbstractListModel/fireContentsChanged)
* [fireIntervalAdded()](/Java/AbstractListModel/fireIntervalAdded)
* [fireIntervalRemoved()](/Java/AbstractListModel/fireIntervalRemoved)
* [getListDataListeners()](/Java/AbstractListModel/getListDataListeners)
* [getListeners()](/Java/AbstractListModel/getListeners)
* [removeListDataListener()](/Java/AbstractListModel/removeListDataListener)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractListModel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractListModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
