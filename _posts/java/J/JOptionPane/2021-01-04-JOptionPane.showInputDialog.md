---
title: JOptionPane.showInputDialog()
permalink: Java/JOptionPane/showInputDialog
date: 2021-01-04
key: JavaJava.J.JOptionPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="showInputDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String showInputDialog(Component parentComponent, Object message) throws HeadlessException
public static String showInputDialog(Component parentComponent, Object message, Object initialSelectionValue)
public static String showInputDialog(Component parentComponent, Object message, String title, int messageType) throws HeadlessException
public static Object showInputDialog(Component parentComponent, Object message, String title, int messageType, Icon icon, Object[] selectionValues, Object initialSelectionValue) throws HeadlessException
public static String showInputDialog(Object message) throws HeadlessException
public static String showInputDialog(Object message, Object initialSelectionValue)
~~~

## Parámetros
* **Object[] selectionValues**,  {% include w3api/param_description.html metodo=_data parametro="Object[] selectionValues" %}
* **String title**,  {% include w3api/param_description.html metodo=_data parametro="String title" %}
* **Object message**,  {% include w3api/param_description.html metodo=_data parametro="Object message" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_data parametro="int messageType" %}
* **Object initialSelectionValue**,  {% include w3api/param_description.html metodo=_data parametro="Object initialSelectionValue" %}
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_data parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JOptionPane.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
