---
title: JColorChooser.createDialog()
permalink: Java/JColorChooser/createDialog
date: 2021-01-11
key: JavaJava.J.JColorChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JColorChooser.metodos valor="createDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static JDialog createDialog(Component c, String title, boolean modal, JColorChooser chooserPane, ActionListener okListener, ActionListener cancelListener) throws HeadlessException
~~~

## Parámetros
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **ActionListener cancelListener**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener cancelListener" %}
* **ActionListener okListener**,  {% include w3api/param_description.html metodo=_dato parametro="ActionListener okListener" %}
* **JColorChooser chooserPane**,  {% include w3api/param_description.html metodo=_dato parametro="JColorChooser chooserPane" %}
* **boolean modal**,  {% include w3api/param_description.html metodo=_dato parametro="boolean modal" %}
* **Component c**,  {% include w3api/param_description.html metodo=_dato parametro="Component c" %}

## Excepciones
[HeadlessException](/Java/HeadlessException/)

## Clase Padre
[JColorChooser](/Java/JColorChooser/)

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
