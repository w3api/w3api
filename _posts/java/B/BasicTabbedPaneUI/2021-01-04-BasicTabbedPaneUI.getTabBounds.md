---
title: BasicTabbedPaneUI.getTabBounds()
permalink: Java/BasicTabbedPaneUI/getTabBounds
date: 2021-01-04
key: JavaJava.B.BasicTabbedPaneUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTabbedPaneUI.metodos valor="getTabBounds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Rectangle getTabBounds(int tabIndex, Rectangle dest)
public Rectangle getTabBounds(JTabbedPane pane, int i)
~~~

## Parámetros
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **JTabbedPane pane**,  {% include w3api/param_description.html metodo=_data parametro="JTabbedPane pane" %}
* **Rectangle dest**,  {% include w3api/param_description.html metodo=_data parametro="Rectangle dest" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_data parametro="int tabIndex" %}

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
