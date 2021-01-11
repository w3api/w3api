---
title: JScrollBar.setUI()
permalink: Java/JScrollBar/setUI
date: 2021-01-11
key: JavaJava.J.JScrollBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.metodos valor="setUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(hidden=true, visualUpdate=true, description="The UI object that implements the Component\'s LookAndFeel") public void setUI(ScrollBarUI ui)
~~~

## Parámetros
* **ScrollBarUI ui**,  {% include w3api/param_description.html metodo=_dato parametro="ScrollBarUI ui" %}

## Clase Padre
[JScrollBar](/Java/JScrollBar/)

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
