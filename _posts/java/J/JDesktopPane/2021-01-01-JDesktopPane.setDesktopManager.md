---
title: JDesktopPane.setDesktopManager()
permalink: /Java/JDesktopPane/setDesktopManager/
date: 2021-01-11
key: Java.J.JDesktopPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JDesktopPane.metodos valor="setDesktopManager" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="Desktop manager to handle the internal frames in the desktop pane.") public void setDesktopManager(DesktopManager d)
~~~

## Parámetros
* **DesktopManager d**,  {% include w3api/param_description.html metodo=_dato parametro="DesktopManager d" %}

## Clase Padre
[JDesktopPane](/Java/JDesktopPane/)

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
