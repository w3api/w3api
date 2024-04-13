---
title: JMenuItem.setAccelerator()
permalink: /Java/JMenuItem/setAccelerator/
date: 2021-01-11
key: Java.J.JMenuItem
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.metodos valor="setAccelerator" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, description="The keystroke combination which will invoke the JMenuItem\'s actionlisteners without navigating the menu hierarchy") public void setAccelerator(KeyStroke keyStroke)
~~~

## Parámetros
* **KeyStroke keyStroke**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStroke keyStroke" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

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
