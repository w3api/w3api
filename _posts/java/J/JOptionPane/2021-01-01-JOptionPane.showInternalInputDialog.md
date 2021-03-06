---
title: JOptionPane.showInternalInputDialog()
permalink: /Java/JOptionPane/showInternalInputDialog/
date: 2021-01-11
key: Java.J.JOptionPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="showInternalInputDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String showInternalInputDialog(Component parentComponent, Object message)
public static String showInternalInputDialog(Component parentComponent, Object message, String title, int messageType)
public static Object showInternalInputDialog(Component parentComponent, Object message, String title, int messageType, Icon icon, Object[] selectionValues, Object initialSelectionValue)
~~~

## Parámetros
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_dato parametro="int messageType" %}
* **Object initialSelectionValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object initialSelectionValue" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Object message**,  {% include w3api/param_description.html metodo=_dato parametro="Object message" %}
* **Object[] selectionValues**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] selectionValues" %}

## Clase Padre
[JOptionPane](/Java/JOptionPane/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
