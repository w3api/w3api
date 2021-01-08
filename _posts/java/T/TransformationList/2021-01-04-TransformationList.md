---
title: TransformationList
permalink: Java/TransformationList
date: 2021-01-04
key: JavaJava.T.TransformationList
category: java
tags: ['java se', 'javafx.collections.transformation', 'javafx.base', 'clase java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransformationList.description }}

## Sintaxis
~~~java
public abstract class TransformationList<E,F> extends ObservableListBase<E> implements ObservableList<E>
~~~

## Constructores
* [TransformationList()](/Java/TransformationList/TransformationList/)

## Métodos
* [getSource()](/Java/TransformationList/getSource)
* [getSourceIndex()](/Java/TransformationList/getSourceIndex)
* [getSourceIndexFor()](/Java/TransformationList/getSourceIndexFor)
* [getViewIndex()](/Java/TransformationList/getViewIndex)
* [isInTransformationChain()](/Java/TransformationList/isInTransformationChain)
* [sourceChanged()](/Java/TransformationList/sourceChanged)

## Ejemplo
~~~java
{{ site.data.Java.T.TransformationList.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransformationList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
