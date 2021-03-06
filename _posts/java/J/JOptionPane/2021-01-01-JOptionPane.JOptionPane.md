---
title: JOptionPane.JOptionPane()
permalink: /Java/JOptionPane/JOptionPane/
date: 2021-01-11
key: Java.J.JOptionPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.constructores valor="JOptionPane" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JOptionPane()
public JOptionPane(Object message)
public JOptionPane(Object message, int messageType)
public JOptionPane(Object message, int messageType, int optionType)
public JOptionPane(Object message, int messageType, int optionType, Icon icon)
public JOptionPane(Object message, int messageType, int optionType, Icon icon, Object[] options)
public JOptionPane(Object message, int messageType, int optionType, Icon icon, Object[] options, Object initialValue)
~~~

## Parámetros
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_dato parametro="int messageType" %}
* **Object[] options**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] options" %}
* **Object initialValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object initialValue" %}
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
