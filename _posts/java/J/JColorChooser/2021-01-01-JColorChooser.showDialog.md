---
title: JColorChooser.showDialog()
permalink: /Java/JColorChooser/showDialog/
date: 2021-01-11
key: Java.J.JColorChooser
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JColorChooser.metodos valor="showDialog" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Color showDialog(Component component, String title, Color initialColor) throws HeadlessException
public static Color showDialog(Component component, String title, Color initialColor, boolean colorTransparencySelectionEnabled) throws HeadlessException
~~~

## Parámetros
* **Color initialColor**,  {% include w3api/param_description.html metodo=_dato parametro="Color initialColor" %}
* **boolean colorTransparencySelectionEnabled**,  {% include w3api/param_description.html metodo=_dato parametro="boolean colorTransparencySelectionEnabled" %}
* **String title**,  {% include w3api/param_description.html metodo=_dato parametro="String title" %}
* **Component component**,  {% include w3api/param_description.html metodo=_dato parametro="Component component" %}

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
