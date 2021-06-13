---
title: JDesktopPane.setDragMode()
permalink: /Java/JDesktopPane/setDragMode/
date: 2021-01-11
key: Java.J.JDesktopPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JDesktopPane.metodos valor="setDragMode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(enumerationValues={"JDesktopPane.LIVE_DRAG_MODE","JDesktopPane.OUTLINE_DRAG_MODE"}, description="Dragging style for internal frame children.") public void setDragMode(int dragMode)
~~~

## Parámetros
* **int dragMode**,  {% include w3api/param_description.html metodo=_dato parametro="int dragMode" %}

## Clase Padre
[JDesktopPane](/Java/JDesktopPane/)

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
