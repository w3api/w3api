---
title: JDesktopPane.setUI()
permalink: /Java/JDesktopPane/setUI/
date: 2021-01-11
key: Java.J.JDesktopPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JDesktopPane.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the Component\'s LookAndFeel.") public void setUI(DesktopPaneUI ui)
~~~

## Parámetros
* **DesktopPaneUI ui**,  {% include w3api/param_description.html metodo=_dato parametro="DesktopPaneUI ui" %}

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
