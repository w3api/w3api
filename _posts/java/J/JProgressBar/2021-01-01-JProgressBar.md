---
title: JProgressBar
permalink: /Java/JProgressBar/
date: 2021-01-11
key: Java.J.JProgressBar
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.J.JProgressBar.description }}

## Sintaxis
~~~java
@JavaBean(defaultProperty="UI", description="A component that displays an integer value.") public class JProgressBar extends JComponent implements SwingConstants, Accessible
~~~

## Constructores
* [JProgressBar()](/Java/JProgressBar/JProgressBar/)

## Campos
* [changeEvent](/Java/JProgressBar/changeEvent)
* [changeListener](/Java/JProgressBar/changeListener)
* [model](/Java/JProgressBar/model)
* [orientation](/Java/JProgressBar/orientation)
* [paintBorder](/Java/JProgressBar/paintBorder)
* [paintString](/Java/JProgressBar/paintString)
* [progressString](/Java/JProgressBar/progressString)

## Métodos
* [addChangeListener()](/Java/JProgressBar/addChangeListener)
* [createChangeListener()](/Java/JProgressBar/createChangeListener)
* [fireStateChanged()](/Java/JProgressBar/fireStateChanged)
* [getAccessibleContext()](/Java/JProgressBar/getAccessibleContext)
* [getChangeListeners()](/Java/JProgressBar/getChangeListeners)
* [getMaximum()](/Java/JProgressBar/getMaximum)
* [getMinimum()](/Java/JProgressBar/getMinimum)
* [getModel()](/Java/JProgressBar/getModel)
* [getOrientation()](/Java/JProgressBar/getOrientation)
* [getPercentComplete()](/Java/JProgressBar/getPercentComplete)
* [getString()](/Java/JProgressBar/getString)
* [getUI()](/Java/JProgressBar/getUI)
* [getUIClassID()](/Java/JProgressBar/getUIClassID)
* [getValue()](/Java/JProgressBar/getValue)
* [isBorderPainted()](/Java/JProgressBar/isBorderPainted)
* [isIndeterminate()](/Java/JProgressBar/isIndeterminate)
* [isStringPainted()](/Java/JProgressBar/isStringPainted)
* [paintBorder()](/Java/JProgressBar/paintBorder)
* [paramString()](/Java/JProgressBar/paramString)
* [removeChangeListener()](/Java/JProgressBar/removeChangeListener)
* [setBorderPainted()](/Java/JProgressBar/setBorderPainted)
* [setIndeterminate()](/Java/JProgressBar/setIndeterminate)
* [setMaximum()](/Java/JProgressBar/setMaximum)
* [setMinimum()](/Java/JProgressBar/setMinimum)
* [setModel()](/Java/JProgressBar/setModel)
* [setOrientation()](/Java/JProgressBar/setOrientation)
* [setString()](/Java/JProgressBar/setString)
* [setStringPainted()](/Java/JProgressBar/setStringPainted)
* [setUI()](/Java/JProgressBar/setUI)
* [setValue()](/Java/JProgressBar/setValue)
* [updateUI()](/Java/JProgressBar/updateUI)

## Ejemplo
~~~java
{{ site.data.Java.J.JProgressBar.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.J.JProgressBar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
