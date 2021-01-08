---
title: PropertyValueFactory
permalink: Java/PropertyValueFactory
date: 2021-01-04
key: JavaJava.P.PropertyValueFactory
category: java
tags: ['java se', 'javafx.scene.control.cell', 'javafx.controls', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PropertyValueFactory.description }}

## Sintaxis
~~~java
public class PropertyValueFactory<S,T> extends Object implements Callback<TableColumn.CellDataFeatures<S,T>,ObservableValue<T>>
~~~

## Constructores
* [PropertyValueFactory()](/Java/PropertyValueFactory/PropertyValueFactory/)

## Métodos
* [getProperty()](/Java/PropertyValueFactory/getProperty)

## Ejemplo
~~~java
{{ site.data.Java.P.PropertyValueFactory.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyValueFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
