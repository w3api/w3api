---
title: JMenuItem.setUI()
permalink: /Java/JMenuItem/setUI/
date: 2021-01-11
key: Java.J.JMenuItem
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the LookAndFeel.") public void setUI(MenuItemUI ui)
~~~

## Parámetros
* **MenuItemUI ui**,  {% include w3api/param_description.html metodo=_dato parametro="MenuItemUI ui" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

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
