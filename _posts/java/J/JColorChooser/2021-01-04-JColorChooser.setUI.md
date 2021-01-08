---
title: JColorChooser.setUI()
permalink: Java/JColorChooser/setUI
date: 2021-01-04
key: JavaJava.J.JColorChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JColorChooser.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, description="The UI object that implements the color chooser\'s LookAndFeel.") public void setUI(ColorChooserUI ui)
~~~

## Parámetros
* **ColorChooserUI ui**,  {% include w3api/param_description.html metodo=_data parametro="ColorChooserUI ui" %}

## Clase Padre
[JColorChooser](/Java/JColorChooser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JColorChooser.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
