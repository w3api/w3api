---
title: BasicTabbedPaneUI.getBaseline()
permalink: Java/BasicTabbedPaneUI/getBaseline
date: 2021-01-04
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="getBaseline" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected int getBaseline(int tab)
public int getBaseline(JComponent c, int width, int height)
~~~

## Parámetros
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **JComponent c**,  {% include w3api/param_description.html metodo=_data parametro="JComponent c" %}
* **int tab**,  {% include w3api/param_description.html metodo=_data parametro="int tab" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicTabbedPaneUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
