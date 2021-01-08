---
title: JColorChooser.setColor()
permalink: Java/JColorChooser/setColor
date: 2021-01-04
key: JavaJava.J.JColorChooser
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JColorChooser.metodos valor="setColor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setColor(int c)
public void setColor(int r, int g, int b)
@BeanProperty(bound=false, description="The current color the chooser is to display.") public void setColor(Color color)
~~~

## Parámetros
* **int r**,  {% include w3api/param_description.html metodo=_data parametro="int r" %}
* **Color color**,  {% include w3api/param_description.html metodo=_data parametro="Color color" %}
* **int g**,  {% include w3api/param_description.html metodo=_data parametro="int g" %}
* **int c**,  {% include w3api/param_description.html metodo=_data parametro="int c" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
