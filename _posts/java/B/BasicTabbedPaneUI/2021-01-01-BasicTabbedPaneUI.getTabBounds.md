---
title: BasicTabbedPaneUI.getTabBounds()
permalink: /Java/BasicTabbedPaneUI/getTabBounds/
date: 2021-01-11
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
* **JTabbedPane pane**,  {% include w3api/param_description.html metodo=_dato parametro="JTabbedPane pane" %}
* **Rectangle dest**,  {% include w3api/param_description.html metodo=_dato parametro="Rectangle dest" %}
* **int tabIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int tabIndex" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[BasicTabbedPaneUI](/Java/BasicTabbedPaneUI/)

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
