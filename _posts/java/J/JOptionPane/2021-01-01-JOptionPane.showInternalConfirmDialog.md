---
title: JOptionPane.showInternalConfirmDialog()
permalink: /Java/JOptionPane/showInternalConfirmDialog/
date: 2021-01-11
key: Java.J.JOptionPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="showInternalConfirmDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static int showInternalConfirmDialog(Component parentComponent, Object message)
public static int showInternalConfirmDialog(Component parentComponent, Object message, String title, int optionType)
public static int showInternalConfirmDialog(Component parentComponent, Object message, String title, int optionType, int messageType)
public static int showInternalConfirmDialog(Component parentComponent, Object message, String title, int optionType, int messageType, Icon icon)
~~~

## Parámetros
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_dato parametro="int messageType" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Object message**,  {% include w3api/param_description.html metodo=_dato parametro="Object message" %}
* **int optionType**,  {% include w3api/param_description.html metodo=_dato parametro="int optionType" %}

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
