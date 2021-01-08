---
title: DefaultComboBoxModel
permalink: Java/DefaultComboBoxModel
date: 2021-01-04
key: JavaJava.D.DefaultComboBoxModel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DefaultComboBoxModel.description }}

## Sintaxis
~~~java
public class DefaultComboBoxModel<E> extends AbstractListModel<E> implements MutableComboBoxModel<E>, Serializable
~~~

## Constructores
* [DefaultComboBoxModel()](/Java/DefaultComboBoxModel/DefaultComboBoxModel/)

## Métodos
* [getIndexOf()](/Java/DefaultComboBoxModel/getIndexOf)
* [removeAllElements()](/Java/DefaultComboBoxModel/removeAllElements)
* [setSelectedItem()](/Java/DefaultComboBoxModel/setSelectedItem)

## Ejemplo
~~~java
{{ site.data.Java.D.DefaultComboBoxModel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultComboBoxModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
