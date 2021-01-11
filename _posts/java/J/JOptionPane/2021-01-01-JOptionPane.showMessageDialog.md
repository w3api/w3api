---
title: JOptionPane.showMessageDialog()
permalink: Java/JOptionPane/showMessageDialog
date: 2021-01-11
key: JavaJava.J.JOptionPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JOptionPane.metodos valor="showMessageDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void showMessageDialog(Component parentComponent, Object message) throws HeadlessException
public static void showMessageDialog(Component parentComponent, Object message, String title, int messageType) throws HeadlessException
public static void showMessageDialog(Component parentComponent, Object message, String title, int messageType, Icon icon) throws HeadlessException
~~~

## Parámetros
* **Component parentComponent**,  {% include w3api/param_description.html metodo=_dato parametro="Component parentComponent" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_dato parametro="Icon icon" %}
* **int messageType**,  {% include w3api/param_description.html metodo=_dato parametro="int messageType" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Object message**,  {% include w3api/param_description.html metodo=_dato parametro="Object message" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
